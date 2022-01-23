
.. tip::

    You can change the theme from light to dark by clicking
    on the Sun/Shaded Sun/Moon icon. --->


.. image:: friendly_logo.png
   :class: sidebar-logo


Bienvenue 환영합니다 Bienvenido - ようこそ Welcome  歡迎光臨
========================================================================

**Friendly** helps users understand what caused a given
exception in their Python program, and how to fix it.

In this documentation, **Friendly**, with an uppercase **F**
refers to two related packages: **friendly_traceback** and **friendly**.

.. tab:: friendly_traceback

    **friendly_traceback** does all the work to figure out what caused
    a particular exception and does some minimal formatting of the
    information it obtains.  In this documentation, I will often use
    **friendly_traceback** to generate the text version
    of the examples' output.


.. tab:: friendly

    **friendly** takes the information obtained by **friendly_traceback**
    and applies some additional formatting (most often, adding colours)
    with the intention to make
    the information easier to understand.
    In this documentation, I will almost always use
    **friendly** to generate the screen capture of the examples.


`Code on Github <https://github.com/friendly-traceback>`_


Introduction
-------------

There exists many Python projects
whose primary goal is to supplement the information
given by Python traceback to make them more useful.
To my knowledge, of all those projects, **Friendly** is
the only one designed with beginners in mind.


To be more specific, while **Friendly**
can be useful for advanced programmers,
it strives to present the information in a way that is easily
understood by beginners and/or by users
who would like to get information about traceback in their own language.
**Friendly** can give more detailed information as to
**where** an exception occurred, **what** a given exception means and
**why** it might have occurred (sometimes adding suggestions as to how to fix it.)

Even though **Friendly** can be used on its own with a specially
designed console, a better option might be to use it together with
GUI-based editors/IDE including JupyterLab and Jupyter notebooks.
I explain how to do so later.
For now, I'll just show one quick example.


A quick look
------------

Consider the following program::

    # example.py
    def get_last(seq):
        last_index = len(seq)
        return seq[last_index]

    print(get_last([1, 2, 3]))

First, here is what happens when I use Python
to run this program.

.. tab:: Screen capture

    .. image:: images/python_indexerror.png
       :scale: 60 %
       :class: only-dark
       :alt: Python IndexError example

    .. image:: images/python_indexerror_light.png
       :scale: 60 %
       :class: only-light
       :alt: Python IndexError example

.. tab:: Text version

  .. code-block:: none

    > python example.py
    Traceback (most recent call last):
      File "C:\Users\andre\friendly-traceback\friendly-traceback\example.py", line 6, in <module>
        print(get_last([1, 2, 3]))
      File "C:\Users\andre\friendly-traceback\friendly-traceback\example.py", line 4, in get_last
        return seq[last_index]
    IndexError: list index out of range



Not exactly the most helpful information for beginners ...

Here's the corresponding version with full explanation from friendly,
making use of
`Rich <https://github.com/willmcgugan/rich>`_ to produce a colourful output.

.. tab:: Screen capture

    .. image:: images/friendly_indexerror_en.png
       :scale: 50 %
       :class: only-dark
       :alt: friendly IndexError example in English

    .. image:: images/friendly_indexerror_en_light.png
       :scale: 50 %
       :class: only-light
       :alt: friendly IndexError example in English


.. tab:: Text version

  .. code-block:: none

    > python -m friendly_traceback example.py

    Traceback (most recent call last):
      File "example.py", line 6, in <module>
        print(get_last([1, 2, 3]))
      File "example.py", line 4, in get_last
        return seq[last_index]
    IndexError: list index out of range

            Remember: the first item of a `list` is not at index 1 but at index 0.

        An `IndexError` occurs when you try to get an item from a list,
        a tuple, or a similar object (sequence), and use an index which
        does not exist; typically, this happens because the index you give
        is greater than the length of the sequence.

        You have tried to get the item with index `3` of `seq`,
        a `list` of length `3`.
        The valid index values of `seq` are integers ranging from
        `-3` to `2`.

        Execution stopped on line 6 of file example.py.

           2: def get_last(seq):
           3:     last_index = len(seq)
           4:     return seq[last_index]
        -->6: print(get_last([1, 2, 3]))
                    ^^^^^^^^^^^^^^^^^^^

                get_last:  <function get_last>
                print:  <builtin function print>

        Exception raised on line 4 of file example.py.

           2: def get_last(seq):
           3:     last_index = len(seq)
        -->4:     return seq[last_index]
                         ^^^^^^^^^^^^^^^

                last_index:  3
                seq:  [1, 2, 3]



One unique feature of friendly is that all the information
it provides can be translated into another language; currently, only
English (by default) and French are available but other languages
could easily be added.

.. tab:: Screen capture

    .. image:: images/friendly_indexerror_fr.png
       :scale: 50 %
       :class: only-dark
       :alt: friendly IndexError in French

    .. image:: images/friendly_indexerror_fr_light.png
       :scale: 50 %
       :class: only-light
       :alt: friendly IndexError in French


.. tab:: Text version

    .. code-block:: none


        > python -m friendly_traceback example.py --lang fr

        Traceback (most recent call last):
          File "example.py", line 6, in <module>
            print(get_last([1, 2, 3]))
          File "example.py", line 4, in get_last
            return seq[last_index]
        IndexError: list index out of range

                N’oubliez pas : le premier élément d'un objet de type `une liste (`list`)` est à l’indice 0
                et non pas à l'indice 1.

            Une exception `IndexError` se produit lorsque vous essayez d’obtenir un élément
            d'une liste, d'un tuple, ou d'un objet similaire (séquence), à l’aide d’un indice qui
            n’existe pas; typiquement, c’est parce que l’indice que vous donnez
            est plus grand que la longueur de la séquence.

            Vous avez essayé d’obtenir l’élément avec l’indice `3` de `seq`,
            une liste (`list`) de longueur `3`.
            Les indices valides de `seq` sont les entiers allant de `-3` à `2`.

            L'exécution s'est arrêtée à la ligne 6 du fichier example.py

               2: def get_last(seq):
               3:     last_index = len(seq)
               4:     return seq[last_index]
            -->6: print(get_last([1, 2, 3]))
                        ^^^^^^^^^^^^^^^^^^^

                    get_last:  <function get_last>
                    print:  <builtin function print>

            Exception levée à la ligne 4 du fichier example.py.

               2: def get_last(seq):
               3:     last_index = len(seq)
            -->4:     return seq[last_index]
                             ^^^^^^^^^^^^^^^

                    last_index:  3
                    seq:  [1, 2, 3]


.. note::

    New: Spanish translation is approximately half done and work
    has started on an Italian translation.


**Keep reading if you want to find out more.**


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Begin here

   beginner
   install
   usage
   usage_adv


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: friendly console

   repl
   why
   what
   where
   explain
   www
   history
   friendly_object
   repl_api
   about_warnings

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Why import *?

   import_all

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: IDLE

   idle
   idle_repl
   idle_run

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Mu

   mu_about
   mu_install
   mu_repl
   mu_run


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Other consoles

   pyrepl
   vs_code_repl
   ipython_repl
   other_repl


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Editors and Notebooks

   install_thonny
   editor
   jupyter
   vs_code
   colab


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Thoughts on design

   design
   themes
   multiple_tracebacks
   friendly_tb
   ipython_tb
   jupyter_tb
   numbered_prompt
   idle_colours

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Use in your project

   api
   formatter
   custom_errors
   plugins

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: All the tracebacks!

   Friendly tracebacks - Python 3.9 <tracebacks_en_3.9>
   SyntaxError - Python 3.9 <syntax_tracebacks_en_3.9>


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: En español

   tracebacks_es
   syntax_tracebacks_es


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: En français

   tracebacks_fr
   syntax_tracebacks_fr


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: בעברית

   tracebacks_he
   syntax_tracebacks_he


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: In italiano

   tracebacks_it
   syntax_tracebacks_it


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: More tracebacks

   known
   Friendly tracebacks - Python 3.6 in English <tracebacks_en_3.6>
   SyntaxError - Python 3.6 in English <syntax_tracebacks_en_3.6>
   Friendly tracebacks - Python 3.7 in English <tracebacks_en_3.7>
   SyntaxError - Python 3.7 in English <syntax_tracebacks_en_3.7>
   Friendly tracebacks - Python 3.8 in English <tracebacks_en_3.8>
   SyntaxError - Python 3.8 in English <syntax_tracebacks_en_3.8>
   Friendly tracebacks - Python 3.10 in English <tracebacks_en_3.10>
   SyntaxError - Python 3.10 in English <syntax_tracebacks_en_3.10>
   Friendly tracebacks - Python 3.11 in English <tracebacks_en_3.11>
   SyntaxError - Python 3.11 in English <syntax_tracebacks_en_3.11>
   compare_exceptions
   compare


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Contribute

   suggest
   translation_notes
