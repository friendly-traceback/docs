Public API
==========

Before getting Sphinx to document the public API automatically,
I need to let you in on a little secret:
occasionally, friendly-traceback will lie to you.
Furthermore, I encourage you to do the same.

Actually, if you have read the section
:ref:`multiple_tracebacks`, you already have seen that the
traceback shown usually does not include modules from friendly
itself.  You can do the same for your own modules
using something like the following::

    import my_module
    friendly_traceback.add_excluded_path(my_module.__file__)


Without further ado, here's the API automatically obtained
by Sphinx from the source code.

``friendly_traceback``
----------------------

.. automodule:: friendly_traceback
   :members:

``friendly_traceback.info_generic``
-----------------------------------

.. automodule:: friendly_traceback.info_generic

   .. autodecorator:: friendly_traceback.info_generic.register

``friendly_traceback.info_specific``
------------------------------------

.. automodule:: friendly_traceback.info_specific

   .. autodecorator:: friendly_traceback.info_specific.register
