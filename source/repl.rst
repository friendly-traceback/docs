.. _using_repl:

Console basics
===============

As a rule, I do not recommend that beginners write their programs
in a console (REPL) but that they use an editor instead or a
notebook environment as it is easier to edit and correct mistakes.
However, using a console is useful to demonstrate various
features of friendly which can be made available
in many editor/IDE environments.
Furthermore, the combination of using an editor and a console
can be quite useful.

The example I will be using is the same as the one shown on the
first page of this documentation: I have a file with the
following content::

    # example.py
    def get_last(seq):
        last_index = len(seq)
        return seq[last_index]

    print(get_last([1, 2, 3]))

However, instead of using::

    python -m friendly example.py

to run this file, I will add an additional ``i`` flag so that ``-m`` become ``-im``;
as a result, a friendly console will be available after the program ends
so that we can execute more Python commands.


.. tab:: Screen capture

    .. image:: images/python_interactive_indexerror.png
       :scale: 50 %
       :class: only-dark
       :alt: Python IndexError example

    .. image:: images/python_interactive_indexerror_light.png
       :scale: 50 %
       :class: only-light
       :alt: Python IndexError example

.. tab:: Text version

  .. code-block:: none

        > python -im friendly_traceback example.py

        Traceback (most recent call last):
          File "example.py", line 6, in <module>
            print(get_last([1, 2, 3]))
          File "example.py", line 4, in get_last
            return seq[last_index]
        IndexError: list index out of range

            Remember: the first item of a `list` is not at index 1 but at index 0.

        Friendly-traceback version 0.4.52. [Python version: 3.9.5]
        Type 'Friendly' for help on special functions/methods.

        [1]:

The output above includes a normal Python traceback followed by a reminder
about list indices, and ends with a numbered prompt ``[1]:`` awaiting for
user input.

In the next pages, we will see various functions that can be
entered at the prompt to give us more information.
