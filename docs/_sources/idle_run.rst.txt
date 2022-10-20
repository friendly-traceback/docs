IDLE: using the editor
========================

.. tip::

    As mentioned before, simply install ``friendly_idle`` and start it from a terminal
    as mentioned previously. If you do so, you **never** have to 
    write something like ::

        from friendly.idle import run
        run("hello.py")
    
    to get the benefit of using **friendly** with IDLE.

    There is however one limitation: if a SyntaxError is raised,
    the information is shown "all at once" and
    is nothing is saved in the recorded ``history()``, so you cannot
    query it further.

    If you change the language used, say from English to French
    by doing ``set_lang('fr')``, **friendly** and **friendly_idle**
    will remember your choice in the future.

The indirect way ...
---------------------


Since IDLE is part of the standard library, it is often the first
editor that is used by beginners learning Python.
Let's have a look at what happens if we run
a program with IDLE using the
"Run -> Run Module" menu item.

.. image:: images/python_idle.png
   :scale: 60 %
   :alt: Screen capture of IDLE


Below, I did something similar, but using friendly
as a program launcher, and using French as the default
language. After the program's execution had been
completed, I entered more code, making a syntax error.


.. image:: images/friendly_idle.png
   :scale: 50 %
   :alt: Screen capture of IDLE using friendly to launch a program


.. admonition:: Summary

    To run a program named ``hello.py`` with only **friendly** and not
    **friendly_idle**, create a second Python
    program saved in the same directory
    and containing the following::

        from friendly.idle import run
        run("hello.py")


.. danger::

    Do not name your own program ``friendly.py``.


If you are using Python 3.10 and do not worry about syntax errors,
you can add the following at the beginning of your
module and run it as is, without needing to add another file::

    from friendly.idle import *
    install()

    # rest of your code


If you do not like to use ``import *``, I suggest instead to use the
following::

    from friendly.idle import Friendly, install
    install()

    # rest of your code

If an exception is raised and you want friendly to tell you "why",
you will then have to use ``Friendly.why()``.

