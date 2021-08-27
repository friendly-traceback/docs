.. _console_api:


Everything about the friendly console
=======================================


.. note::

    The hand-written documentation about the console
    might not reflect the latest version of the code.
    This page documents the relevant API by automatically
    extracting information from the **friendly-traceback** code.

    Note that, in addition to the functions shown below,
    when using **friendly** instead of **friendly-traceback**,
    some additional functions might be included as means to
    change the colour scheme used by **friendly**.


.. automodule:: friendly_traceback.console_helpers
   :members:

.. class:: FriendlyHelpers

    Helper class which can be used in a console as an alternative
    to using the helper functions directly.
    This can be helpful if one of the helper functions gets redefined.

    It is usually instantiated using the name ``Friendly``.

    For example, we can write ``Friendly.why()`` as equivalent to ``why()``.
