Jupyter notebooks and JupyterLab
================================

Friendly supports Jupyter notebooks and variants.
Note that, other than when I specifically do work to improve
friendly's integration with Jupyter, I do not use Jupyter
and may not notice any bugs due to changes in Jupyter and iPython;
please feel free to report any issues.


Suggested usage
----------------

If you are using a Classic notebook, or JupyterLab
with a light theme, I suggest that use the following::

    from friendly.jupyter import Friendly


This should automatically install friendly.

.. image:: images/jupyter_light_install.png
   :scale: 60 %

If you are using JupyterLab with the dark theme
selected, then I suggest the following::


    from friendly.jupyter import Friendly
    Friendly.dark()

.. image:: images/jupyter_light_install.png
   :scale: 60 %

In both these cases, an easy to use interactive mode is selected
where you can have access to the ``what()``, ``why()``, and ``where()``
information when an exception is raised without having to type anything.
Because of this, there is little advantage to use ``from friendly.jupyter import *``
and my use recommendation to do a ``* import`` does not apply.


.. image:: images/jupyter_message_only.png
   :scale: 60 %

.. image:: images/jupyter_more_clicked.png
   :scale: 60 %


.. todo::

    Set width to 60 by default. Add new function to set width
    of traceback separately, and set that to 100 by default.
    For iPython, set both to 60. Keep track of tb width
    so that it is never smaller than general width.

.. image:: images/jupyter_wide_why.png
   :scale: 40 %

.. image:: images/jupyter_narrow_why.png
   :scale: 60 %



.. design_choice::
   :title: automatic installation for Jupyter

   Anyone using friendly in a Jupyter environment does so because
   they want the traceback information to be processed by friendly.
   For this reason, friendly is automatically installed when
   ``friendly.jupyter`` is imported, instead of requiring users
   to call ``install()`` after the ``import`` statement.


.. design_choice::
   :title: buttons instead of function calls for Jupyter
   :prefix: UI


   friendly aims to be as easy to use as possible for beginners.
   Having them clicking on buttons to reveal some additional information
   when needed is more user-friendly than requiring them to
   type in and execute some function calls.


.. design_choice::
   :title: only message shown by default for Jupyter

   Rather than showing the friendly traceback by default,
   only the exception message is shown in addition to the ``More ...``
   button.



Available formatters
---------------------

To be added



Normal Jupyter tracebacks.
--------------------------


By default, tracebacks in JupyterLab notebooks (or Juypter notebooks)
displayed in a browser are given a pink background (1).
The image below shows the "old" style of tracebacks.

.. image:: images/jupyter-lab-error.png
   :scale: 60 %

The "location" of the error (2) includes was of the form
``<ipython-input-A-B>`` where ``A`` is the code block number
and ``B`` is an internal value ("hash_digest") of no particular use
to a end user.

Recently, Jupyter (lab/notebooks) have changed the way they
operate and use temporary files to store code to be
executed; the filenames currently do not have any
relation to the code block number.

Friendly's traceback however indicate clearly what code blocks
were involved in the execution leading to a particular traceback.










This hash_digest is removed by friendly
as shown below.

.. image:: images/jupyter-lab-default.png
   :scale: 60 %

1. To use friendly, we use a special import statement.

2. Tracebacks shown by friendly do not have a pink background. Note how
   the "file" name has been shortened, compared with Jupyter's default.

3. The *formatter* value is changed from the default to ``'bw'``
   which is meant to be short for "black and white" meaning that no
   special colouring is done..

4. This ``'bw'`` choice results in a plain output on pink background.

5. A different syntax colouring (``'light'``)
   is also available.

6. The colour scheme with this formatter is fairly similar to the default
   used for Jupyter notebooks.

After changing to the ``'light'``, I displayed a more complete
content displayed with ``explain()``


.. image:: images/jupyter-lab-default2.png
   :scale: 40 %


When using ``from friendly.jupyter import *``,
the default formatter is known as ``'jupyter'``.

.. image:: images/jupyter-lab-default3.png
   :scale: 60 %



Dark background
----------------

JupyterLab also gives the choice of a dark background theme.
Here's how the previous example look with this dark theme.

.. image:: images/jupyter-lab-dark.png
   :scale: 60 %

As a last step, I changed the formatter to use the ``'dark'`` option,
which is the default for the friendly console when used in a terminal.

.. image:: images/jupyter-lab-dark-rich.png
   :scale: 40 %

Finally, here is the result from changing back to the default
``'jupyter'`` formatter.

.. image:: images/jupyter-lab-dark2.png
   :scale: 60 %

For the dark Jupyter theme, some elements, such as numbers and operators,
are very difficult to read.
For this reason, I much prefer using the ``'dark'`` friendly
formatter in this case.

About the hash_digest
~~~~~~~~~~~~~~~~~~~~~~

The hash_digest is meant to uniquely identify the content of a code block.
However, this does not appear the case when the same code is entered
in different cells for sessions where one uses more than one notebook.
`I suggested what I believe is a better approach <https://github.com/ipython/ipython/issues/12755>`_ using
the kernel number instead of the hash_digest: the combination of
the code-block number and kernel number should be unique.
However, IPython developers are certainly swamped with issues to consider
and would be right not to consider this a high priority item to look at,
although it might prevent some messages one occasionally gets about
the need to restart a kernel.


Developer's notes
------------------

.. design_choice::
   :title: Jupyter font family with Rich

   Instead of using the Jupyter default, Rich specifies a
   set of possible fonts for its output. As a result, the apparent
   size of the fonts, at least on Windows, appears to be
   larger when using Rich than without.  To avoid this,
   I override the default from Rich to give a more consistent
   look and feel.
