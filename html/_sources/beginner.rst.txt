Useful information for beginners
=================================

.. tip::

    If you already know how to run Python programs from a terminal/command line,
    and know what is meant by a "REPL", you should go directly to the
    next page.


Get someone to help you
-----------------------

Learning programming on your own can be extremely challenging.
Having a teacher or an experienced friend helping you can be invaluable.

**Friendly** has been designed to help beginners when they encounter
problems with their code, giving rise to what is known as a **traceback**.
I believe that the information available from **Friendly** is much
more useful that that normally provided by Python. Still, before someone
can use **Friendly**, they have to know many other concepts, including setting
up correctly their programming environment, to using a terminal,
and knowing how to install packages, etc.

In case no one is available to help you, here is some basic information
that can be helpful for some of you, but that is definitely not
intended to take the place of a complete introduction for beginners,
nor can it replace having someone helping you.

.. tip::

    If you find yourself stuck, ask questions on Internet forums intended
    for Python beginners such as `Reddit's LearnPython <https://reddit.com/r/learnpython>`_
    or `Python users <https://discuss.python.org/c/users/>`_.

    - Describe what you wanted to do.
    - Describe **exactly** what you have done.
    - Describe what does not work. If you get an error message,
      include **all the text** that was shown.
    - Do not include images.


What is a REPL?
---------------

A REPL (Read-Eval-Print Loop) is an interactive mode where
we are invited to type in some Python code after
**prompt** (most often written as ``>>>``). Python reads
this code, interprets what it means, and might "print" (show) some
result before showing another prompt waiting for us to enter
more code.

Other words sometimes used instead of the REPL acronym are
"console", "shell", and "interpreter".

.. image:: images/python_terminal.png
   :scale: 50 %
   :alt: Python runing in a terminal

In the image shown above, I have started a python interpreter
using the command ``python``, and entered the code
``print('Hello world!')`` at the prompt.

The ``python`` command refers to whatever you need to type to invoke your
favourite Python interpreter in a terminal on your computer.
It could be ``python``, ``python3``, ``py -3.8``, etc.


How to run a Python program
----------------------------

Instead of using an interpreter to type code when prompted
by Python, you can use an editor, save your program in
a file (named ``hello.py`` in my example) and run
it in a terminal by using the command
``python hello.py``.

.. image:: images/python_terminal2.png
   :scale: 50 %
   :alt: Python runing in a terminal

Another option is to use a program like IDLE which includes
both an editor and a python interpreter.

.. image:: images/python_idle.png
   :scale: 50 %
   :alt: Python runing in IDLE

There exists many other editors designed to be used
by Python programmers.
For example, some of you might be familiar with Mu:

.. image:: images/beginner_mu.png
   :scale: 50 %
   :alt: Python runing in Mu

Summary
-------

You can run Python programs by typing ``python ...`` or ``python3 ...``
in a terminal or by using and editor with a built-in menu
for running Python programs.

In the early part of this documentation, the examples I will use
will be mostly done using ``python ...`` in a Windows terminal.
Even if this is not the way that you normally run Python programs,
it would be most helpful if you tried to follow along by doing
something similar to what I show.
