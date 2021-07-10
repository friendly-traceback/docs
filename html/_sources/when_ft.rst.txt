
.. note::

    This documentation covers two related projects:
    ``friendly`` and ``friendly-traceback``.

    You likely need to install and use ``friendly``.


Differences between friendly and friendly_traceback
===================================================

**friendly_traceback** is the program that does all the required
work to analyze a traceback and present the information
in an helpful way.

**friendly** takes the output of **friendly_traceback**
and formats it for specific environments, **usually** adding colour
to the output.

If you use one of:

- A terminal, ideally with colour support
- Python's IDLE
- Mu
- IPython
- Jupyter Notebooks and Jupyter Lab
- Visual Studio Code
- Google Colab notebooks
- etc.

you will want to install and use **friendly**.

Note that **friendly** has quite a few additional dependencies compared with
**friendly_traceback**.


If you design your own programming environment, such as is done on
`HackInScience <https://HackInScience.org>`_
or `futurecoder <https://futurecoder.io>`_
then you likely only need to install **friendly_traceback**.
