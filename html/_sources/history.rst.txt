history() 
=========

**Friendly** keeps a record of all warnings and exceptions raised during
an interactive session. We can get a list of these at any time
using ``history()``.

.. code-block:: none

   [1]: history()
   0. DeprecationWarning: Indiana, February 6, 1897
   1. IndexError: list index out of range

Note that each recorded item is shown with an index, starting at 0.
If we want **Friendly** to forget about the last recorded item, we can
use ``history.pop()``. If we want Friendly to remove one particular
item, we can use ``history.pop(index)``. Finally, if we want **Friendly**
to forget about all recorded items so far, we can use ``history.clear()``.

