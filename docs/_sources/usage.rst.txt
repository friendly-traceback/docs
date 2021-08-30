Basic usage
============

There are various ways of using **Friendly**.
I only list here the basic scenarios available from a
terminal or from within a Python interpreter.
More options are possible, including running from an editor/IDE
as described later in this documentation.

For those that know how to run programs **from a terminal**,
I recommend using **one of the first three** following options.


1. Execute a Python program, as I have already shown at the beginning:


.. tab:: friendly

    .. code-block::

        $ python -m friendly example.py


.. tab:: friendly_traceback

    .. code-block::

        $ python -m friendly_traceback example.py


2. You can also start a friendly console:

.. tab:: friendly

    .. code-block::

        $ python -m friendly


.. tab:: friendly_traceback

    .. code-block::

        $ python -m friendly_traceback


3. Combining the two options above by using Python's ``-i`` flag
   to start friendly's console after executing
   a program:


.. tab:: friendly

    .. code-block::

        $ python -im friendly example.py


.. tab:: friendly_traceback

    .. code-block::

        $ python -im friendly_traceback example.py


.. sidebar:: Suggestion

    If you are a Windows user I **very strongly suggest** that you use the new
    `Windows Terminal <https://github.com/microsoft/terminal>`_
    that you can get from the Windows Store; this is
    what I have used for various screen captures.


You can also start a friendly console from any Python interactive interpreter.


.. tab:: friendly

    .. code-block::

        >>> import friendly
        >>> friendly.start_console()


.. tab:: friendly_traceback

    .. code-block::

        >>> import friendly_traceback
        >>> friendly_traceback.start_console()


While **friendly_traceback** does not print in colour, **friendly** does.
For **friendly**, all of the above assume that you are using
a terminal with a dark background.
If you are using a terminal with a light background, you might want to
add ``--format light``, which can be abbreviated as ``-f light``,
as a command line option::

    $ python -m friendly --format light


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

In principle, **Friendly** could support languages other than English
and French. Contributions from native speakers of other languages
are welcome.  Note that this is not a small task as
there is a lot of text that needs to be translated.
