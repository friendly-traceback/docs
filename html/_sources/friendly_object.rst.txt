.. _Friendly_object:

Friendly object
================

What happens if someone uses an object with the same name
as a friendly helper function?

.. image:: images/friendly_why.png
   :scale: 50 %
   :alt: why as a static method

As you can see, these functions are also available as static
methods of a ``Friendly`` object.  So, as long as you don't
use ``Friendly`` as the name of an object in your program,
you don't have to worry about not being able to use
any of **friendly**'s interactive functions.

If you simply enter the name of that object, you can see
a summary of each available  method of that object.


.. image:: images/friendly_object1.png
   :scale: 40 %
   :alt: friendly object methods


A somewhat similar short description is available for
each individual functions. These descriptions are
available in both French and English as shown below.


.. image:: images/friendly_object2.png
   :scale: 80 %
   :alt: description in French of explain.


For advanced users
-----------------------

If you use ``set_debug()`` to enter a debugging mode,
you get access to more methods of the ``Friendly``
object. These can be used to explore normally hidden
values related to tracebacks.



.. image:: images/friendly_object_debug.png
   :scale: 60 %
   :alt: debugging methods

These are only available as methods of ``Friendly``
and not as individual functions.

Here is one example illustrating the type of information
that could be available for ``SyntaxError`` cases:

.. image:: images/friendly_object_statement.png
   :scale: 60 %
   :alt: debugging methods: Statement
