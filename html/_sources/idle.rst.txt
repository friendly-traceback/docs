About IDLE
=====================

.. warning::

    This documentation is out of date.
    Using pip, please install ``friendly_idle``
    which you can start from a terminal simply using ``friendly_idle``.
    friendly_idle automatically makes use of friendly-tracaback and
    works even when dealing with syntax errors.

IDLE is often the first program that is used by beginners
learning Python since it is installed with Python.
It includes its own REPL (known as its "shell") and enable
users to write code in editors and run them, with the output
redirected to the shell.

Before Python version 3.10.0a5, IDLE did not allow a user to
define their own "exception hook" to modify the information shown to
a user. Since then, it is possible to have IDLE use a custom
exception hook **except** when dealing with syntax errors.
Furthermore, the changes that made this possible have been
ported to Python 3.9.5 and 3.8.10.
