.. _using_repl:

Interactive mode
================

Python is often run in interactive mode, where a user type
statements one by one, with Python interpreting the result.
This can be done in a terminal, in a Jupyter notebook, and 
various other environments.

In this section, I will demonstrate various features of Friendly
in interactive mode in a terminal.


The example I will be using is essentially the same as the one shown on the
first page of this documentation: I have a file with the
following content::

    # example.py
    def get_last(seq):
        last_index = len(seq)
        return seq[last_index]

    print(get_last([1, 2, 3]))

However, instead of using::

    friendly example.py

to run this file, I will add an additional ``-x`` flag and have the following::

    friendly example.py -x


.. tab:: Screen capture

    .. image:: images/python_interactive_indexerror.png
       :scale: 70 %
       :alt: Python IndexError example


.. tab:: Text version

  .. code-block:: python

        > friendly example.py -x

        Traceback (most recent call last):
          File "HOME:\demos\example.py", line 6, in <module>
            print(get_last([1, 2, 3]))
          File "HOME:\demos\example.py", line 4, in get_last
            return seq[last_index]
        IndexError: list index out of range

        Remember: the first item of a list is not at index 1 but at index 0.

        friendly-traceback: 0.7.45
        friendly: 0.7.19
        Python: 3.10.6
        Use exit() or Ctrl-Z plus Return to exit.
        Type 'Friendly' for help on special functions/methods.


        [1]:


.. sidebar::  Supported languages

    Adding the ``-x`` flag will make **friendly** start a console
    if an exception is raised. If one wants to always start the
    console after a program is run, use ``-i`` as a flag.
    
    ``-x`` is not available for **friendlyl_traceback**.

The output above includes a normal Python traceback followed by a reminder
about list indices, and ends with a numbered prompt ``[1]:`` awaiting for
user input.


In order to keep the documentation shorter, in the following
pages, I will use a slightly modified example, one that raises a warning
as well as an exception::

    # example2.py
    import warnings

    def indiana_pi():
        warnings.warn("Indiana, February 6, 1897", DeprecationWarning,
                      stacklevel = 2)
        return 3.2

    indiana_tau = indiana_pi() * 2

    def get_last(seq):
        last_index = len(seq)
        return seq[last_index]

    print(get_last([1, 2, 3]))


Here's the result::

        > friendly example2.py -x

        DeprecationWarning: Indiana, February 6, 1897

        Traceback (most recent call last):
          File "HOME:\demos\example2.py", line 15, in <module>
            print(get_last([1, 2, 3]))
          File "HOME:\demos\example2.py", line 13, in get_last
            return seq[last_index]
        IndexError: list index out of range

        Remember: the first item of a list is not at index 1 but at index 0.

        friendly-traceback: 0.7.45
        friendly: 0.7.19
        Python: 3.10.6
        Use exit() or Ctrl-Z plus Return to exit.
        Type 'Friendly' for help on special functions/methods.


        [1]:


In terms of the output, the only difference with the first example is that
we see a DeprecationWarning printed before the traceback.
Unlike exceptions, by default warnings do not interrupt the normal
execution of a program.

Using this example, in the next pages, we will see various functions that can be
entered at the prompt to give us more information.
