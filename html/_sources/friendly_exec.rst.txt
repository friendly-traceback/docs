Friendlier exec
================

When using ``exec(code)`` with the standard Python interpreter, the
code is not retrieved when a traceback occurs. This creates problems
for many users, including those interested in projects like **Friendly**
which seek to add improvements to the standard Python tracebacks.
Alex Hall has compiled a good list of such projects and discussed
this
`issue on Python-ideas <https://mail.python.org/archives/list/python-ideas@python.org/message/CMM5ZV7GJPAR7KLEECETZP3SNFLCIKHQ/>`_;
unfortunately, no one (other than me) seemed to be interested
in this topic and the discussion died down.

**Friendly** has a modified version of ``exec`` which makes it possible
to retrieve the content of the code that was executed. Below is
an example, illustrating some differences between the standard ``exec``
and the alternative provided by **Friendly**. This example uses
``friendly_traceback`` but could just as well have used ``friendly``.

* Notice on line 17 how no content is shown from the file ``<string>`` when using ``exec``.

* On line 18, Python (3.10) does offer a suggestion for a fix but ````friendly_traceback`` cannot do the same as the code is not available.

* Using ``friendly_exec`` on line 23 solves this problem.

.. code-block::
   :linenos:

        > python -m friendly_traceback
        Friendly-traceback version 0.7.50
        Python version: 3.10.6
        Use exit() or Ctrl-Z plus Return to exit.
        Type 'Friendly' for help on special functions/methods.

        [1]: from math import pi

        [2]: code = "a = 2 * Pi"

        [3]: exec(code)

        Traceback (most recent call last):
          Code block [3], line 1
            exec(code)
          File "<string>", line 1, in <module>

        NameError: name 'Pi' is not defined. Did you mean: 'pi'?

        [4]: why()
        I have no suggestion to offer.

        [5]: friendly_exec(code)

        Traceback (most recent call last):
          Code block [5], line 1
            friendly_exec(code)
          File "FRIENDLY:\source_cache.py", line 127, in friendly_exec
            return exec(code, globals_, locals_)
          File "<friendly-exec-0>", line 1, in <module>
            a = 2 * Pi
        NameError: name 'Pi' is not defined. Did you mean: 'pi'?

                Did you mean `pi`?


        [6]: why()

            In your program, no object with the name `Pi` exists.
            The similar name `pi` was found in the local scope.


        [7]: where()

            Execution stopped on line `1` of code block [5].

            -->1| friendly_exec(code)
                  ^^^^^^^^^^^^^^^^^^^

                    code:  'a = 2 * Pi'
                    friendly_exec:  <function friendly_exec>

            Exception raised on line `1` of file '<friendly-exec-0>'.

            -->1| a = 2 * Pi
                          ^^

