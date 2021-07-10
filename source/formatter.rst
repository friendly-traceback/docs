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
   At the time this documenation was written, the dict items were the following::

       items = [
            "header",
            "message",
            "original_python_traceback",
            "simulated_python_traceback",
            "shortened_traceback",
            "suggest",
            "generic",
            "parsing_error",
            "parsing_error_source",
            "cause",
            "last_call_header",
            "last_call_source",
            "last_call_variables",
            "exception_raised_header",
            "exception_raised_source",
            "exception_raised_variables",
        ]


.. tip::

    Use ``Friendly._show_info()`` in a friendly console to see all possible items.
    Note that, when an actual exception is recorded, a few items not meant to
    be shown to the end user are stored in ``info``; this is done so as
    to make them available in the console using method calls like
    ``Friendly._get_exception()``, ``Friendly._get_frame()``, etc.


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
