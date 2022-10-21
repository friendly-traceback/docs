Logging and keeping confidential information secret
======================================================

In some situations, it is useful to log exceptions that are raised
and continue the execution. Since the information cannot be queried
interactively, one might want to capture all the required information
to figure out what went wrong. While friendly_traceback was not initially
designed with this purpose in mind, it is perfectly suitable to use
in such cases.


Let's look at a fairly detailed example meant for more advanced programmes.
First, here's the code that we wish to run

.. code-block:: python
    :linenos:

    def compute_fraction(numerator, denominator):
        return numerator / denominator

    a = 4
    b = 2
    c = 1
    # The following will raise an exception

    def fn_1(a, b):
        d, e = 4, 5
        irrelevant = d * e
        return irrelevant + fn_2(c, a - b**2) + irrelevant

    def fn_2(secret_x, secret_y):
        return fn_3 (secret_x, secret_y)

    def fn_3(x, y):
        return compute_fraction(x, y)


    fraction = fn_1(a, b)


At this point, note on line 12 that the ``fn_2`` function call is
part of an expression between two terms that we named ``irrelevant``.
This will be relevant later.

Furthermore, on line 15, we have two variable names beginning with ``secret``.

How to use logging: an example
-------------------------------

Suppose we wish to run this code and log any exception that arise.
Furthermore, we do not want to reveal what the value of any variable
whose name begins by ``secret``, while having as much information as possible
about the state of the program and values of variables when
the exception was raised. Here's how we can do it.



.. code-block:: python
    :linenos:

    import friendly_traceback
    from friendly_traceback.console_helpers import history, where
    import logging

    # Configure as desired before running the code
    logging.basicConfig(filename="ignore.log")
    friendly_traceback.set_stream(redirect="capture")

    # We don't ever want to show the name
    friendly_traceback.hide_secrets(patterns=[r"secret\w*"])

    try:
        import example_logging_source
    except Exception:
        friendly_traceback.explain_traceback()
        log = friendly_traceback.get_output()

        # The following will add some detailed information about variables
        # in each frame, in case it is relevant
        where(more=True)
        where_log = friendly_traceback.get_output()

        history.clear()  # prevent memory leaks

        full_log = (
            " Output from friendly_traceback\n"
            + log
            + "\n------More details--------\n"
            + where_log
            + "\n======Original traceback=======\n"
        )

        # exc_info=True below will append the original traceback
        logging.error(full_log, exc_info=True)



1. On line 7 we set friendly_traceback so that its output is (temporarily) captured
   rather than printed out.

2. On line xxx we add a regular expression pattern identifying variable names whose
   value we wish to keep secret.

3. On line 10, we extract the content that was captured and, in doing so, clear the buffer
   where that content was held. It is possible to pass the argument ``flush=False`` to
   keep that content if needed.

4. By default, friendly_traceback gives a "short" traceback, with more details given
   for the initial and final frame. On line 20, with ``where(more=True)``, we get
   friendly_traceback to output detailed information about each frame involved in
   the traceback.

5. By default, friendly_traceback keeps a copy of each traceback that was generated.
   This is sometimes useful in interactive mode, especially if warnings are emitted
   as they do not cause an interruption to the program. By calling ``history.clear()``
   on line 23, we remove this content, helping to reduce the risk of memory leaks.


Analysing the output
---------------------

The example described previously yields the following result,
to which we add comments afterwords.

.. code-block:: none
    :linenos:

    ERROR:root: Output from friendly_traceback

    Traceback (most recent call last):
      File "HOME:\example_logging.py", line 13, in <module>
        import example_logging_source
           ... More lines not shown. ...
      File "HOME:\example_logging_source.py", line 18, in fn_3
        return compute_fraction(x, y)
      File "HOME:\example_logging_source.py", line 2, in compute_fraction
        return numerator / denominator
    ZeroDivisionError: division by zero

        A `ZeroDivisionError` occurs when you are attempting to divide a value
        by zero either directly or by using some other mathematical operation.
        
        You are dividing by the following term
        
             denominator
        
        which is equal to zero.
        
        Execution stopped on line `13` of file 'HOME:\example_logging.py'.
        
            9| # We don't ever want to show the name
           10| friendly_traceback.hide_secrets(patterns=[r"secret\w*"])
           11| 
           12| try:
        -->13|     import example_logging_source
           14| except Exception:

        Exception raised on line `2` of file 'HOME:\example_logging_source.py'.
        
           1| def compute_fraction(numerator, denominator):
        -->2|     return numerator / denominator
                         ^^^^^^^^^^^^^^^^^^^^^^^

                denominator:  0
                numerator:  1
            

    ------More details--------

        File 'HOME:\example_logging.py', line `13`
            9| # We don't ever want to show the name
           10| friendly_traceback.hide_secrets(patterns=[r"secret\w*"])
           11| 
           12| try:
        -->13|     import example_logging_source
           14| except Exception:

            
        File 'HOME:\example_logging_source.py', line `21`
           15|     return fn_3 (secret_x, secret_y)
           16| 
           17| def fn_3(x, y):
           18|     return compute_fraction(x, y)
            :
        -->21| fraction = fn_1(a, b)
                          ^^^^^^^^^^

                a:  4
                b:  2
                fn_1:  <function fn_1>
            
        File 'HOME:\example_logging_source.py', line `12`
            9| def fn_1(a, b):
           10|     d, e = 4, 5
           11|     irrelevant = d * e
        -->12|     return irrelevant + fn_2(c, a - b**2) + irrelevant
                                       ^^^^^^^^^^^^^^^^^

                a:  4
                b:  2
                global c:  1
                global fn_2:  <function fn_2>
                a - b**2:  0
                b**2:  4
            
        File 'HOME:\example_logging_source.py', line `15`
           14| def fn_2(secret_x, secret_y):
        -->15|     return fn_3 (secret_x, secret_y)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^

                secret_x:  '••••••'
                secret_y:  '••••••'
                global fn_3:  <function fn_3>
            
        File 'HOME:\example_logging_source.py', line `18`
           17| def fn_3(x, y):
        -->18|     return compute_fraction(x, y)
                          ^^^^^^^^^^^^^^^^^^^^^^

                x:  1
                y:  0
                global compute_fraction:  <function compute_fraction>
            
        File 'HOME:\example_logging_source.py', line `2`
           1| def compute_fraction(numerator, denominator):
        -->2|     return numerator / denominator
                         ^^^^^^^^^^^^^^^^^^^^^^^

                denominator:  0
                numerator:  1
            

    ======Original traceback=======
    Traceback (most recent call last):
      File "C:\Users\Andre\example_logging.py", line 13, in <module>
        import example_logging_source
      File "C:\Users\Andre\example_logging_source.py", line 21, in <module>
        fraction = fn_1(a, b)
      File "C:\Users\Andre\example_logging_source.py", line 12, in fn_1
        return irrelevant + fn_2(c, a - b**2) + irrelevant
      File "C:\Users\Andre\example_logging_source.py", line 15, in fn_2
        return fn_3 (secret_x, secret_y)
      File "C:\Users\Andre\example_logging_source.py", line 18, in fn_3
        return compute_fraction(x, y)
      File "C:\Users\Andre\example_logging_source.py", line 2, in compute_fraction
        return numerator / denominator
    ZeroDivisionError: division by zero


1. **friendly-traceback** uses Alex Hall's `executing <https://github.com/alexmojaki/executing>`_
   to narrow down the parts of the code in a traceback to those that are involved in
   generating an exception. For example, look at line 69 above where the part highlighted by
   carets (``^``) does not include the variable name ``irrelevant``.
   Lines 72 to 79 shows the value of various relevant objects in this highlighted
   part.  **Please see the note at the bottom of this page** which includes
   two questions.

   While cPython 3.11 does include such highlighting of relevant code regions in traceback,
   it only shows one line per frame. By contrast, **Friendly** will show relevant parts
   of a statement even it if spans multiple lines. Furthermore, it does so for Python 
   version 3.6 and greater.

2. Lines 84 and 85 shows that two variables, ``secret_1`` and ``secret_2``, were involved
   in the code included in the traceback. However, since their names are included by
   the pattern we declared as being that of confidential variables, their values are
   redacted.



About keeping secrets
----------------------

**Friendly** gives you the possibility of testing your pattern deemed to be
confidential before you deploy your code. To protect against the possibility
of having some confidential information shown in the "value" of a given
variable, for example, if you have a dict containing keys whose values
should be confidential, **Friendly** will also see if the pattern
appears in the "value" (technically, the ``repr``) of the variable
and will redact it if it does. Furthermore, in order to reduce the length
of the display, the "value" will be truncated if it exceeds a certain length.

Here's a concrete example:


.. code-block:: python

    import friendly_traceback as ft

    ft.hide_secrets(["secret\w*"])
    not_secret = "should be public"
    secret1 = "confidential because of the variable name."
    hidden = "contains a secret."
    long_list = list(range(100))
    def fn(): ...

    for name, true_repr in [
        ("not_secret", not_secret),
        ("secret1", secret1),
        ("hidden", hidden),
        ("long_list", long_list),
        ("fn", fn)
    ]:
        print(f"{name}: {true_repr=}")
        result = ft.test_secrets(name)
        print("display by friendly_traceback:\n", result, "\n")



And here's the corresponding result:


.. code-block:: none

    not_secret: true_repr='should be public'
    display by friendly_traceback:
         not_secret:  'should be public'

    secret1: true_repr='confidential because of the variable name.'
    display by friendly_traceback:
         secret1:  '••••••'

    hidden: true_repr='contains a secret.'
    display by friendly_traceback:
         hidden:  '••••••'

    long_list: true_repr=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    display by friendly_traceback:
         long_list:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, ...]
                len(long_list): 100


    fn: true_repr=<function fn at 0x0000026D56C5F160>
    display by friendly_traceback:
         fn:  <function fn>



.. note::

      1. For those that use logging, would it be useful to have the option to show the value **all** the
         variables involved in a given frame, like what is done by ``rich.traceback`` and other
         "traceback enhancers"?

      2. As mentioned, the "value" (``repr``) shown is truncated if it exceeds a certain length.
         Would it be useful for this length to be adjustable?

      If you have any opinion on any or both of these two questions, please feel free to open
      up an issue for discussion.
