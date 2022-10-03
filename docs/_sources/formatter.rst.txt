Custom formatter
================

friendly comes with various formatters which style
the information differently based on the environment.
If the builtin formatters do not meet your need, you can design
your own and set it as a default using either::

    import friendly
    from my_module import my_formatter

    friendly.set_formatter(formatter=my_formatter)

or, from the command line:

.. code-block:: none

    python -m friendly --format path.to.my_module.my_formatter
    

Currently, a formatter must accept two arguments:

1. A dict (``info``) which contains the friendly traceback information.
   At the time this documentation was written, the dict items were the following::

        items_in_order = [
            "header",  # Currently unused by this project; used by HackInScience
            "message",  # The last line of a Python traceback
            "original_python_traceback",  # <-- Friendly._debug_tb()
            "simulated_python_traceback",  # <-- python_tb()
            "shortened_traceback",  # <-- friendly_tb()
            "suggest",  # <-- hint()
            "warning message",
            "generic",  # <-- what()
            "parsing_error",
            "parsing_error_source",
            "cause",  # <-- why()
            "last_call_header",
            "last_call_source",
            "last_call_variables",
            "exception_raised_header",
            "exception_raised_source",
            "exception_raised_variables",
            "warning location header",
            "warning source",
            "warning variables",
            "additional variable warning",
        ]


.. tip::

    Use ``Friendly._show_info()`` in a friendly console to see all possible items.


2. A string (``include``) which specifies which parts of the friendly
   traceback should be shown, and whose value is currently set
   using ``friendly.set_include(...)``.

The second argument _might_ change in the future. If you only plan
on making use of the traceback information compiled by friendly
and determine what to show (and in which order) on your own, to ensure
that future version of friendly will be compatible with
your formatter, we suggest the following definition::

    def my_formatter(info, **ignore):
        ....

.. automodule:: friendly_traceback.base_formatters
   :members:
