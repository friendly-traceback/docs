
where()
=======

Python traceback give information about where an exception was raised and
more. But it does so in a way that's not entirely friendly to users, showing a
single line for each "frame" in which a function call took place::

  > python example2.py
  C:\Users\Andre\demos\example2.py:9: DeprecationWarning: Indiana, February 6, 1897
    indiana_tau = indiana_pi() * 2
  Traceback (most recent call last):
    File "C:\Users\Andre\demos\example2.py", line 15, in <module>
      print(get_last([1, 2, 3]))
    File "C:\Users\Andre\demos\example2.py", line 13, in get_last
      return seq[last_index]
  IndexError: list index out of range


Friendly, can give more information about the location of the error.


.. tab:: Screen capture

    .. image:: images/where.png
       :scale: 70 %
       :alt: Python IndexError example - where()


.. tab:: Text version

  .. code-block:: python


    [10]: where()

        Execution stopped on line `15` of file 'HOME:\demos\example2.py'.

           11| def get_last(seq):
           12|     last_index = len(seq)
           13|     return seq[last_index]
           14|
        -->15| print(get_last([1, 2, 3]))
                     ^^^^^^^^^^^^^^^^^^^

                get_last:  <function get_last>

        Exception raised on line `13` of file 'HOME:\demos\example2.py'.

           11| def get_last(seq):
           12|     last_index = len(seq)
        -->13|     return seq[last_index]
                          ^^^^^^^^^^^^^^^

                last_index:  3
                seq:  [1, 2, 3]

.. note::

    In the text version above, instead of using ``friendly example2.py -x``,
    which highlights the location of the error with a different background
    colour, I have used ``friendlyl example2.py -x -f docs`` to get a text
    version which uses carets (``^``) to indicate the location of the error.

We can do the same for the deprecation warning::

  [11]: where(0)

      Warning issued on line `9` of file 'HOME:\demos\example2.py'.

         5|     warnings.warn("Indiana, February 6, 1897", DeprecationWarning,
         6|                   stacklevel = 2)
         7|     return 3.2
         8|
      -->9| indiana_tau = indiana_pi() * 2
                          ^^^^^^^^^^^^
         10|
         11| def get_last(seq):

              indiana_pi:  <function indiana_pi>


More details
-------------

By default, ``where()`` focuses on the last line where the exception was actually 
raised and, if different, the first line entered by a user which started the
series of call that resulted in a traceback. Sometimes, it might
be useful to get more information about each "frame" which was involved in 
a traceback. This can be done using an optional argument:
``where(more=True)``. 