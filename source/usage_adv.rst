Other details for advanced users
=================================

.. tip::

    Some additional information might be available from the command line:

    .. tab:: friendly

        .. code-block::

            $ python -m friendly -h

    .. tab:: friendly_traceback

        .. code-block::

            $ python -m friendly_traceback -h


Running another script
----------------------

We have already explained how to run a program using **Friendly**.
What if the separate script has its own command line arguments?


.. sidebar:: Included in repository

    A similar program is included in the **demos/** directory of both
    **friendly** and **friendly_traceback** Github repository.

Consider the following program::

    # Demonstration of a program that uses command line arguments
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("numbers", nargs="*",
                         help="List of numbers to add."
                         )
    parser.add_argument("--to_int",
                        help="Converts the sum to integer",
                        action="store_true"
                        )

    total = 0
    args = parser.parse_args()

    for number in args.numbers:
        total += float(number)

    if int(total) == total and args.to_int:
        total = int(total)

    print("The sum is", total)


Using Python, we would normally run this program as follows.

.. code-block::

    $ python demos/adder.py 1 2 3
    The sum is 6

We can do the same using **friendly** (or **friendly_traceback**).

.. code-block::

    $ python -m friendly demos/adder.py 1 2 3
    The sum is 6.0

Note that this works even if you specify command line arguments
that are specific to friendly::

    $ python -m friendly --lang fr demos/adder.py 1 2 3
    The sum is 6.0

However, what if one wants to run a script that uses optional named arguments
similarly to how friendly can use ``--lang`` and other optional
arguments? In this case, use ``--`` to separate the list of arguments
to be used by the script from those written previously and
intended to be used by friendly:

.. code-block::

    $ python -m friendly --lang fr demos/adder.py -- --to_int 1 2 3
    The sum is 6

Finally, let's generate a traceback to see **Friendly** in action, this time
using **friendly_traceback** so that no special formatting is applied.

.. code-block::

    $ python -m friendly_traceback demos/adder.py -- --to_int 1 2 3 a

    Traceback (most recent call last):
      File "demos\adder.py", line 13, in <module>
        total += float(number)
    ValueError: could not convert string to float: 'a'

        A `ValueError` indicates that a function or an operation
        received an argument of the right type, but an inappropriate value.

        I do not recognize this error message.
        I am guessing that the problem is with the function `float`.
        Its docstring is:

        `'''Convert a string or number to a floating point number, if possible.'''`

        Exception raised on line 13 of file demos\adder.py.

            9: total = 0
           10: args = parser.parse_args()
           12: for number in args.numbers:
        -->13:     total += float(number)
                            ^^^^^^^^^^^^^
           15: if int(total) == total and args.to_int:

                number:  'a'
                float:  <class float>


All possible ``ValueError`` cases are not yet explained by **Friendly**
as we can see above.

.. todo::

    Provide an explanation for the error message
    ``ValueError: could not convert string to float: 'a'``.



Where the output is written?
----------------------------

By default, friendly tracebacks are written to ``sys.stderr``.
However, it is possible to override this choice, as follows::

    friendly.set_stream(stream)

Thus, the default amounts to::

    friendly.set_stream(sys.stderr)

A special option exists to capture the output as a string::

    friendly.set_stream("capture")

Later, this captured output can be retrieved using::

    output = friendly.get_output()

    # equivalent to
    output = friendly.get_output(flush=True)


The value shown for the ``flush`` parameter is the default; this means that
the output will be cleared once it has been retrieved. If this is not the
desired behaviour, simply use ``flush=False``.


Language used
-------------

.. sidebar::  Supported languages

    English is the default language. 
    As a rule, French translations is (almost) always at 100%.
    Currently, Spanish, Russian, and Tamil translations are at more
    than 95% done, and Italian is about 10% done.

    A translation to Hebrew is approximately 80% done.
    However, since Hebrew is a right-to-left language, I am not sure that
    the translation appears correctly. 
    
    Additional translations are more than welcome.

The language used can be explicitly set as follows::

    friendly.set_lang("fr")  # two-letter code for French

The language currently used can be obtained using::

    lang = friendly.get_lang()

If the language requested does not exist, no error is raised nor any warning
given, but the choice reverts to the default (English).

As an exception hook
---------------------

When "installing" friendly, one can use various optional
parameters::

    friendly.install(lang="fr", redirect="capture", include="explain")

This is equivalent to writing::

    friendly.install()
    friendly.set_lang("fr")
    friendly.set_stream("capture")
    friendly.set_include("explain")


Using **Friendly** by default
------------------------------

An alterative to installing **Friendly** in each individual
programs is to use either a ``sitecustomize.py``
or a ``usercustomize.py`` file, as described in the
`Python documentation <https://docs.python.org/3/library/site.html>`_.

For example, you can use the following approach.

1. Create a ``usercustomize.py`` file whose content is the following::

    import friendly
    friendly.install()
    # specify other desired options here

2. Set the ``PYTHONPATH`` environment variable to that directory.
   On Windows, this can be done by navigating to that directory
   and writing::

       set PYTHONPATH=%CD%

You can now run your script normally: friendly exception
handling will be used by default on it.


Catching exception locally
--------------------------

As mentioned before, another way to use friendly is to catch
exceptions where they are expected to arise, such as::


    try:
        # Some code
    except Exception:
        friendly.explain_traceback()

This uses the default of writing to ``sys.stderr``.
One can also **temporarily** redirect the output to any stream::

    try:
        # Some code
    except Exception:
        friendly.explain_traceback(redirect=stream)

By default, friendly takes its information from ``sys.exc_info()``.
It may happen that this is not what we want to show.
For example, the `showtraceback method in Python's code.py <https://github.com/python/cpython/blob/3.7/Lib/code.py#L131>`_ replaces one of the items prior to
showing the traceback to the user; we currently also do something similar in
friendly's own console.

Finally, if one wishes to *temporarily* change some other option mentioned above,
it can be done as in the following example::

    try:
        # Some code
    except Exception:
        lang = friendly.get_lang()
        friendly.set_lang("fr")
        friendly.explain_traceback()
        friendly.set_lang(lang)




Logging
--------

You can use friendly_traceback with the logging module.
Here's an example, together with the corresponding
output::

    import friendly_traceback
    import logging

    # Configure as desired before running the code
    logging.basicConfig(filename="ignore.log")
    friendly_traceback.set_lang('fr')  # Just as an example :-)

    try:
        import ignore2
    except Exception:
        friendly_traceback.explain_traceback(redirect="capture")
        # Note: friendly often remove some details from tracebacks
        # to make them more readable. This can be helpful
        # but sometimes we might also need to see the full
        # traceback in log files.
        # For example, compare the path of ignore2.py shown
        # in both tracebacks.
        log = (" Friendly traceback\n" +
                  friendly.get_output() +
                  "\n----Original traceback-----\n")
        # exc_info=True below will append the original traceback
        logging.error(log, exc_info=True)


And here's the output:

.. code-block:: none

    Traceback (most recent call last):
      File "ignore.py", line 9, in <module>
        import ignore2
      File "CWD:\ignore2.py", line 3, in <module>
        c = a / b
    ZeroDivisionError: division by zero

        Une exception de type `ZeroDivisionError` se produit lorsque vous essayez de diviser une valeur
        par zéro soit directement ou en utilisant une autre opération mathématique.

        Vous divisez par le terme suivant

             b

        qui est égal à zéro.

        L'exécution s'est arrêtée à la ligne 9 du fichier ignore.py

            7:
            8: try:
        --> 9:     import ignore2
           10: except Exception:

        Exception levée à la ligne 3 du fichier CWD:\ignore2.py.

           1: a = 1
           2: b = 0
        -->3: c = a / b
                  ^^^^^

                a:  1
                b:  0


    ----Original traceback-----
    Traceback (most recent call last):
      File "ignore.py", line 9, in <module>
        import ignore2
      File "C:\Users\andre\github\friendly\ignore2.py", line 3, in <module>
        c = a / b
    ZeroDivisionError: division by zero
