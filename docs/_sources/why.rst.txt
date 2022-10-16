

why()
======

Let's continue with the previously shown ``IndexError`` case and try
to find what was the cause.

.. code-block:: none

    [2]: why()

    You have tried to get the item with index 3 of seq, a list of length 3.
    The valid index values of seq are integers ranging from -3 to 2.


When you call ``why()``, **Friendly** attempts to analyze the code you
entered and figure out what exactly went wrong, and quite often makes
suggestions as to how to fix it.

What if we wanted to see what was the cause of the ``DeprecationWarning`` we saw.
Since this was a made-up example, we should not expect much in terms
of explanation. Remember that, in the history, the ``DeprecationWarning``
was indicated as the zeroth item::

    [3]: why(0)

    I have no suggestion to offer.

This was not particular helpful. However, it helps to illustrate how we can
get some information about "old" items recorded at any time by **Friendly**,
as long as we have not removed them from the history.

Note that, by default, if ``why()`` is called with no argument, it will
give an explanation for the last recorded item.