

why()
======

Let's continue with the previously shown ``IndexError`` case and try
to find what was the cause.


.. tab:: Screen capture

    .. image:: images/why.png
       :scale: 50 %
       :class: only-dark
       :alt: Python IndexError example: why() gives the cause

    .. image:: images/why_light.png
       :scale: 50 %
       :class: only-light
       :alt: Python IndexError example: why() gives the cause

.. tab:: Text version

  .. code-block:: none

        [1]: why()

        You have tried to get the item with index 3 of seq, a list of length 3.
        The valid index values of seq are integers ranging from -3 to 2.


        [2]:


When you call ``why()``, **Friendly** attempts to analyze the code you
entered and figure out what exactly went wrong, and quite often makes
suggestions as to how to fix it.

