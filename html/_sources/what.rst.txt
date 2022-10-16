what()
======

Perhaps you are a beginner and do not known what ``IndexError`` and ``DeprecationWarning``
mean. Here's how **Friendly** can help you.

.. code-block:: none

   [4]: what()

   An IndexError occurs when you try to get an item from a list, a tuple,
   or a similar object (sequence), and use an index which does not exist;
   typically, this happens because the index you give is greater than the
   length of the sequence.


   [5]: what(0)

   DeprecationWarning indicates that some feature will not be available in
   a future version.

At any time, you can change the language used and **Friendly** will
try to provide some help in that language provided a translation exists::

   [6]: set_lang('fr')

   [7]: what()

   Une exception IndexError se produit lorsque vous essayez d’obtenir un
   élément d'une liste, d'un tuple, ou d'un objet similaire (séquence), à
   l’aide d’un indice qui n’existe pas; typiquement, c’est parce que
   l’indice que vous donnez est plus grand que la longueur de la séquence.

   [8]: set_lang('en')


