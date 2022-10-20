Basic usage
============

There are various ways of using **friendly**.
I only list here the basic scenarios available from a
terminal or from within a Python interpreter.
More options are possible, including running from an editor/IDE
as described later in this documentation.

For those that know how to run programs **from a terminal**,
I recommend using **one of the first five** following options.


1. Execute a Python program, as I have already shown at the beginning:


.. code-block::

    friendly example.py

2. You can also start a friendly console:

.. code-block::

    friendly



3. Combining the two options above by adding ``-i``
   to **always** start friendly's console after executing
   a program:


.. code-block::

    friendly example.py -i
    # or
    friendly -i example.py


4. As an altertive, add ``-x``
   to  start friendly's console after executing
   a program **only if an exception has been raised**:


.. code-block::

    friendly example.py -x
    # or
    friendly -x example.py



.. sidebar:: Suggestion

    If you are a Windows user I **very strongly suggest** that you use the new
    `Windows Terminal <https://github.com/microsoft/terminal>`_
    that you can get from the Windows Store; this is
    what I have used for various screen captures.


5. If you run a program that raises an error and leaves you at an
   interactive prompt, you can import friendly "after the fact".
   Consider the following content of a file named ``ignore.py``::

        from math import *

        def test():
            a = cost(pi)

        test()


Here's a sample session:


.. code-block:: none

        > python -i ignore.py
        Traceback (most recent call last):
          File "C:\Users\andre\friendly-traceback\friendly\ignore.py", line 6, in <module>
            test()
          File "C:\Users\andre\friendly-traceback\friendly\ignore.py", line 4, in test
            a = cost(pi)
        NameError: name 'cost' is not defined
        >>> from friendly import start_console
        An exception occurred before friendly-traceback was imported.
        Some information is available.
        >>> start_console()

        friendly-traceback: 0.4.79
        friendly: 0.4.29
        Python: 3.9.5
        Type 'Friendly' for help on special functions/methods.

        [1]: why()

            In your program, no object with the name `cost` exists.
            Instead of writing `cost`, perhaps you meant one of the following:
            *   Global scope: `cos`, `cosh`, `acos`


.. note::

    This last example is more easily done in environments like Jupyter
    notebooks where the Friendly console does not have to be explicitly
    called to have access to the information from Friendly.



6. You can also start a friendly console from any Python interactive interpreter,
   which is what was done above.


.. code-block::

    >>> import friendly
    >>> friendly.start_console()


For **friendly**, all of the above assume that you are using
a terminal with a dark background.
If you are using a terminal with a light background, you might want to
add ``--format light``, which can be abbreviated as ``-f light``,
as a command line option::

    friendly --format light


Similarly, the ``start_console()`` function
accept various parameters, including ``formatter`` for **friendly**
which can be specified to be either ``dark`` or ``light``.


Using in other environments
---------------------------

If you want to use **Friendly** elsewhere than from a terminal,
you likely will need to use a custom mode designed for that
environment. Currently, as explained elsewhere in this documentation,
**friendly** (but not **friendly-traceback**)
has special options that need to be selected
so that it can work best with the following:

- Python's IDLE
- Mu
- IPython
- Normal programs run from Visual Studio Code
- Jupyter notebooks (in a browser)
- JupyterLab
- Jupyter notebooks inside Visual Studio Code
- Google's Colab notebooks


If you design your own programming environment, such as is done on
`HackInScience <https://HackInScience.org>`_
or `futurecoder <https://futurecoder.io>`_
then you likely only need to install **friendly_traceback**.
Compared with **friendly_traceback**, **friendly** has
quite a few additional dependencies that you would likely not need.


|france| En Français
---------------------

**Friendly** offre la possibilité de présenter l'information en
Français.
Par exemple, si on désire démarrer **Friendly** à partir d'un terminal
tel que décrit ci-dessus, il suffit de rajouter l'argument
``lang fr`` de la façon suivante:

.. tab:: friendly

    .. code-block::

        $ python -m friendly --lang fr


.. tab:: friendly_traceback

    .. code-block::

        $ python -m friendly_traceback --lang fr

Si on désire démarrer la console à partir d'un interprète
Python, on utilise le paramètre
``lang`` de la façon suivante:


.. tab:: friendly

    .. code-block::

        >>> import friendly
        >>> friendly.start_console(lang='fr')


.. tab:: friendly_traceback

    .. code-block::

        >>> import friendly_traceback
        >>> friendly_traceback.start_console(lang='fr')

Other languages
---------------

As mentioned previously, in addition to English and French,
**Friendly** is available in other languages.
