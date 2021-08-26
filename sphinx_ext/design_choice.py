"""
    design_choice
    ~~~~~~~~~~~~~~

    IMPORTANT: This is a straightforward adaptation of sphinx's todo extension
    done by search/replace.


    Allow design_choices to be inserted into your documentation.
    Inclusion of design_choices can be switched of by a configuration variable.
    The design_choice_list directive collects all design_choices of your
    project and lists them along with a backlink to the original location.

    :copyright: Copyright 2007-2021 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""


import warnings
from typing import Any, Dict, Iterable, List, Tuple, cast

from docutils import nodes
from docutils.nodes import Element, Node
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.admonitions import BaseAdmonition

import sphinx
from sphinx import addnodes
from sphinx.application import Sphinx
# from sphinx.deprecation import RemovedInSphinx40Warning
from sphinx.domains import Domain
from sphinx.environment import BuildEnvironment
from sphinx.errors import NoUri
from sphinx.locale import _, __
from sphinx.util import logging, texescape
from sphinx.util.docutils import SphinxDirective, new_document
from sphinx.util.nodes import make_refnode
from sphinx.writers.html import HTMLTranslator
from sphinx.writers.latex import LaTeXTranslator

logger = logging.getLogger(__name__)


class design_choice_node(nodes.Admonition, nodes.Element):
    pass


class design_choice_list(nodes.General, nodes.Element):
    pass


class DesignChoice(BaseAdmonition, SphinxDirective):
    """
    A design_choice entry, displayed (if configured) in the form of an admonition.
    """

    node_class = design_choice_node
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        "class": directives.class_option,
        "name": directives.unchanged,
        "title": directives.unchanged,
        "prefix": directives.unchanged,
    }

    def run(self) -> List[Node]:
        if not self.options.get("class"):
            self.options["class"] = ["admonition-design_choice"]

        (design_choice,) = super().run()  # type: Tuple[Node]
        if isinstance(design_choice, nodes.system_message):
            return [design_choice]
        elif isinstance(design_choice, design_choice_node):
            prefix = ''
            if "prefix" in self.options:
                prefix = self.options["prefix"] + " "
            design_choice.insert(
                0, nodes.title(text=prefix + _("Design Choice: ") + self.options["title"])
            )
            design_choice["docname"] = self.env.docname
            self.add_name(design_choice)
            self.set_source_info(design_choice)
            self.state.document.note_explicit_target(design_choice)
            return [design_choice]
        else:
            raise RuntimeError  # never reached here


class DesignChoiceDomain(Domain):
    name = "design_choice"
    label = "design_choice"

    @property
    def design_choices(self) -> Dict[str, List[design_choice_node]]:
        return self.data.setdefault("design_choices", {})

    def clear_doc(self, docname: str) -> None:
        self.design_choices.pop(docname, None)

    def merge_domaindata(self, docnames: List[str], otherdata: Dict) -> None:
        for docname in docnames:
            self.design_choices[docname] = otherdata["design_choices"][docname]

    def process_doc(
        self, env: BuildEnvironment, docname: str, document: nodes.document
    ) -> None:
        design_choices = self.design_choices.setdefault(docname, [])
        for design_choice in document.traverse(design_choice_node):
            env.app.emit("design_choice-defined", design_choice)
            design_choices.append(design_choice)

            if env.config.design_choice_emit_warnings:
                logger.warning(
                    __("TODO entry found: %s"),
                    design_choice[1].astext(),
                    location=design_choice,
                )


def process_design_choices(app: Sphinx, doctree: nodes.document) -> None:
    # warnings.warn(
    #     "process_design_choices() is deprecated.",
    #     RemovedInSphinx40Warning,
    #     stacklevel=2,
    # )
    # collect all design_choices in the environment
    # this is not done in the directive itself because it some transformations
    # must have already been run, e.g. substitutions
    env = app.builder.env
    if not hasattr(env, "design_choice_all_design_choices"):
        env.design_choice_all_design_choices = []  # type: ignore
    for node in doctree.traverse(design_choice_node):
        app.events.emit("design_choice-defined", node)

        newnode = node.deepcopy()
        newnode["ids"] = []
        env.design_choice_all_design_choices.append(
            {  # type: ignore
                "docname": env.docname,
                "source": node.source or env.doc2path(env.docname),
                "lineno": node.line,
                "design_choice": newnode,
                "target": node["ids"][0],
            }
        )

        if env.config.design_choice_emit_warnings:
            label = cast(nodes.Element, node[1])
            logger.warning(__("TODO entry found: %s"), label.astext(), location=node)


class DesignChoiceList(SphinxDirective):
    """
    A list of all design_choice entries.
    """

    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}  # type: Dict

    def run(self) -> List[Node]:
        # Simply insert an empty design_choice_list node which will be replaced later
        # when process_design_choice_nodes is called
        return [design_choice_list("")]


class DesignChoiceListProcessor:
    def __init__(self, app: Sphinx, doctree: nodes.document, docname: str) -> None:
        self.builder = app.builder
        self.config = app.config
        self.env = app.env
        self.domain = cast(DesignChoiceDomain, app.env.get_domain("design_choice"))
        self.document = new_document("")

        self.process(doctree, docname)

    def process(self, doctree: nodes.document, docname: str) -> None:
        design_choices = sum(
            self.domain.design_choices.values(), []
        )  # type: List[design_choice_node]
        for node in doctree.traverse(design_choice_list):
            if not self.config.design_choice_include_design_choices:
                node.parent.remove(node)
                continue

            if node.get("ids"):
                content = [nodes.target()]  # type: List[Element]
            else:
                content = []

            for design_choice in design_choices:
                # Create a copy of the design_choice node
                new_design_choice = design_choice.deepcopy()
                new_design_choice["ids"].clear()

                self.resolve_reference(new_design_choice, docname)
                content.append(new_design_choice)

                design_choice_ref = self.create_design_choice_reference(
                    design_choice, docname
                )
                content.append(design_choice_ref)

            node.replace_self(content)

    def create_design_choice_reference(
        self, design_choice: design_choice_node, docname: str
    ) -> nodes.paragraph:
        if self.config.design_choice_link_only:
            description = _("<<original entry>>")
        else:
            description = _("(The <<original entry>> is located in %s, line %d.)") % (
                design_choice.source,
                design_choice.line,
            )

        prefix = description[: description.find("<<")]
        suffix = description[description.find(">>") + 2 :]

        para = nodes.paragraph(classes=["design_choice-source"])
        para += nodes.Text(prefix, prefix)

        # Create a reference
        linktext = nodes.emphasis(_("original entry"), _("original entry"))
        reference = nodes.reference("", "", linktext, internal=True)
        try:
            reference["refuri"] = self.builder.get_relative_uri(
                docname, design_choice["docname"]
            )
            reference["refuri"] += "#" + design_choice["ids"][0]
        except NoUri:
            # ignore if no URI can be determined, e.g. for LaTeX output
            pass

        para += reference
        para += nodes.Text(suffix, suffix)

        return para

    def resolve_reference(
        self, design_choice: design_choice_node, docname: str
    ) -> None:
        """Resolve references in the design_choice content."""
        for node in design_choice.traverse(addnodes.pending_xref):
            if "refdoc" in node:
                node["refdoc"] = docname

        # Note: To resolve references, it is needed to wrap it with document node
        self.document += design_choice
        self.env.resolve_references(self.document, docname, self.builder)
        self.document.remove(design_choice)


def process_design_choice_nodes(
    app: Sphinx, doctree: nodes.document, fromdocname: str
) -> None:
    """Replace all design_choice_list nodes with a list of the collected design_choices.
    Augment each design_choice with a backlink to the original location.
    """
    # warnings.warn(
    #     "process_design_choice_nodes() is deprecated.",
    #     RemovedInSphinx40Warning,
    #     stacklevel=2,
    # )

    domain = cast(DesignChoiceDomain, app.env.get_domain("design_choice"))
    design_choices = sum(
        domain.design_choices.values(), []
    )  # type: List[design_choice_node]

    for node in doctree.traverse(design_choice_list):
        if node.get("ids"):
            content = [nodes.target()]  # type: List[Element]
        else:
            content = []

        if not app.config["design_choice_include_design_choices"]:
            node.replace_self(content)
            continue

        for design_choice_info in design_choices:
            para = nodes.paragraph(classes=["design_choice-source"])
            if app.config["design_choice_link_only"]:
                description = _("<<original entry>>")
            else:
                description = _(
                    "(The <<original entry>> is located in %s, line %d.)"
                ) % (design_choice_info.source, design_choice_info.line)
            desc1 = description[: description.find("<<")]
            desc2 = description[description.find(">>") + 2 :]
            para += nodes.Text(desc1, desc1)

            # Create a reference
            innernode = nodes.emphasis(_("original entry"), _("original entry"))
            try:
                para += make_refnode(
                    app.builder,
                    fromdocname,
                    design_choice_info["docname"],
                    design_choice_info["ids"][0],
                    innernode,
                )
            except NoUri:
                # ignore if no URI can be determined, e.g. for LaTeX output
                pass
            para += nodes.Text(desc2, desc2)

            design_choice_entry = design_choice_info.deepcopy()
            design_choice_entry["ids"].clear()

            # (Recursively) resolve references in the design_choice content
            app.env.resolve_references(design_choice_entry, design_choice_info["docname"], app.builder)  # type: ignore  # NOQA

            # Insert into the design_choice_list
            content.append(design_choice_entry)
            content.append(para)

        node.replace_self(content)


def purge_design_choices(app: Sphinx, env: BuildEnvironment, docname: str) -> None:
    # warnings.warn(
    #     "purge_design_choices() is deprecated.", RemovedInSphinx40Warning, stacklevel=2
    # )
    if not hasattr(env, "design_choice_all_design_choices"):
        return
    env.design_choice_all_design_choices = [
        design_choice
        for design_choice in env.design_choice_all_design_choices  # type: ignore
        if design_choice["docname"] != docname
    ]


def merge_info(
    app: Sphinx, env: BuildEnvironment, docnames: Iterable[str], other: BuildEnvironment
) -> None:
    # warnings.warn("merge_info() is deprecated.", RemovedInSphinx40Warning, stacklevel=2)
    if not hasattr(other, "design_choice_all_design_choices"):
        return
    if not hasattr(env, "design_choice_all_design_choices"):
        env.design_choice_all_design_choices = []  # type: ignore
    env.design_choice_all_design_choices.extend(other.design_choice_all_design_choices)  # type: ignore


def visit_design_choice_node(self: HTMLTranslator, node: design_choice_node) -> None:
    if self.config.design_choice_include_design_choices:
        self.visit_admonition(node)
    else:
        raise nodes.SkipNode


def depart_design_choice_node(self: HTMLTranslator, node: design_choice_node) -> None:
    self.depart_admonition(node)


def latex_visit_design_choice_node(
    self: LaTeXTranslator, node: design_choice_node
) -> None:
    if self.config.design_choice_include_design_choices:
        self.body.append("\n\\begin{sphinxadmonition}{note}{")
        self.body.append(self.hypertarget_to(node))

        title_node = cast(nodes.title, node[0])
        title = texescape.escape(title_node.astext(), self.config.latex_engine)
        self.body.append("%s:}" % title)
        node.pop(0)
    else:
        raise nodes.SkipNode


def latex_depart_design_choice_node(
    self: LaTeXTranslator, node: design_choice_node
) -> None:
    self.body.append("\\end{sphinxadmonition}\n")


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_event("design_choice-defined")
    app.add_config_value("design_choice_include_design_choices", False, "html")
    app.add_config_value("design_choice_link_only", False, "html")
    app.add_config_value("design_choice_emit_warnings", False, "html")

    app.add_node(design_choice_list)
    app.add_node(
        design_choice_node,
        html=(visit_design_choice_node, depart_design_choice_node),
        latex=(latex_visit_design_choice_node, latex_depart_design_choice_node),
        text=(visit_design_choice_node, depart_design_choice_node),
        man=(visit_design_choice_node, depart_design_choice_node),
        texinfo=(visit_design_choice_node, depart_design_choice_node),
    )

    app.add_directive("design_choice", DesignChoice)
    app.add_directive("design_choice_list", DesignChoiceList)
    app.add_domain(DesignChoiceDomain)
    app.connect("doctree-resolved", DesignChoiceListProcessor)
    return {
        "version": sphinx.__display_version__,
        "env_version": 2,
        "parallel_read_safe": True,
    }
