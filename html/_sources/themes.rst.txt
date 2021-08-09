.. _themes:

Themes, Styles, and Colours
============================

As mentioned before, friendly uses
`Rich <https://github.com/willmcgugan/rich>`_ to add colours.
Syntax colouring is done by Rich using Pygments.
While Pygments comes with many different styles (colour schemes),
most of them do not define colours for all possible parts of
a Python traceback: depending on the style, we sometimes end up with
some text with the same colour as the background.

Furthermore, depending on the context, using the default
values, Rich might use different colours for the same Python object.

To ensure that all of friendly's output would be styled
consistently, I have created two pygments styles: one suitable for
white or light coloured backgrounds,
and one for black or dark coloured backgrounds.
These are found in the
`friendly_styles <https://github.com/friendly-traceback/friendly_styles>`_
repository.


.. design_choice::
   :title: Red means exception or error
   :prefix: UI

   For both themes, I have chosen to use the colour red only for
   exception names, such as ``SyntaxError``, for traceback headings,
   and for headings showing where an exception occurred.



.. image:: images/friendly_indexerror_en.png
   :scale: 50 %
   :alt: friendly IndexError example in English


This choice of only using red to signal something related to an exception
results in some styles that might be different from the
default style in some environments. For example, Jupyter notebooks
use red as the colour for strings.


friendly default theme using Windows Terminal
----------------------------------------------

When using Windows, only the new Windows Terminal can faithfully
support the full colour gamet provided by Rich as shown in
the above screenshot.


Other OS
--------

Screenshots taken by MacOS or Linux users would be welcome.



Different background colours
----------------------------

Both styles/themes designed for friendly support specifying a
different background colour when highlighting.
See the section on Mu as an example.


Colour consistency
------------------

As mentioned previously, depending on the context, Rich can colour
Python objects differently. The screenshot below illustrates this,
and shows how one can use friendly's styles to achieve consistency.


.. image:: images/rich_vs_friendly.png
   :scale: 50 %
   :alt: Illustrating differences between rich's default and friendly's


Rich partially supported
------------------------

.. sidebar:: Old screenshots

    The screenshots showing partial support for Rich when using ConEmu
    have been taken with an older version of friendly.
    A few changes have been done since, but the conclusion would
    remain the same.


Designing a pygments colour style is one thing; having it faithfully
displayed in a terminal even if it supports escape sequences emitted
by Rich is something else altogether.
Below you will see a few screenshots taken using
`ConEmu <https://conemu.github.io/>`_,
using different colour schemes available from ConEmu's settings.
Much to my surprise, even though the colours I have chosen are not standard
colours, they are much altered by ConEmu depending on the chosen
colour scheme.



ConEmu: base16 theme
~~~~~~~~~~~~~~~~~~~~

.. image:: images/conemu_base16.png
   :scale: 40 %
   :alt: ConEmu: base16 theme


ConEmu: default windows theme
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/conemu_default_windows.png
   :scale: 40 %
   :alt: ConEmu: default windows theme

Rich not supported
-------------------

Rich works by adding escape sequences which are interpreted
by terminals as adding style (colours, font style like bold, italics, or
underlined, etc.). Some environment cannot interpret these escape
sequences. Here is what happens if we attempt to use Rich
together with Python's IDLE for the same code as shown above:

.. image:: images/rich_not_supported.png
   :scale: 40 %
   :alt: Rich not supported in IDLE


However, friendly includes special support for adding colours
when using IDLE.
