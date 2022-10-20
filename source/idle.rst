About IDLE
=====================

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

A better alternative
--------------------

Instead of using IDLE as described in the following pages,
provided that you have a version of IDLE that support
exception hooks already installed on your computer,
simply install ``friendly_idle`` and start it from a 
terminal using either ``friendly_idle`` or ``friendly-idle``:
you will automatically have a version of IDLE that will
incorporate all the features of **friendly** without having
to import it.
