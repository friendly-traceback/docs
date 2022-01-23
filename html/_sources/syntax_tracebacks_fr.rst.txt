
|france| Friendly SyntaxError tracebacks - en Français
======================================================

Le but principal de friendly est de fournir des rétroactions plus
conviviales que les fameux **tracebacks** de Python lorsqu'une exception survient.
Ci-dessous, on peut voir plusieurs exemples, uniquement pour les
exceptions de type SyntaxError et des classes dérivées;
les autres sont couvertes dans une autre page.
Le but est de documenter ici tous les exemples possibles
tels qu'interprétés par friendly_traceback.

.. note::

     Le contenu de cette page a été généré par l'exécution de
     trb_syntax_french.py situé dans le répertoire ``tests/``.
     Ceci a besoin d'être fait de manière explicite lorsqu'on veut
     faire des corrections ou des ajouts, avant de faire la mise
     à jour du reste de la documentation avec Sphinx.
     Sous Windows, si Sphinx est installé sur votre ordinateur, il est
     plutôt suggéré d'exécuter make_trb.bat qui est au premier niveau
     du répertoire de fichier. Si vous faites ceci, la documentation pour
     toutes les langues sera automatiquement mise à jour.

Friendly version: 0.5.13
Python version: 3.9.10



(1) Using 'and' in import statement
-----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\and_in_import_statement.py", line 1
        from math import sin and cos
                             ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\and_in_import_statement.py'
    à l'endroit indiqué.
    
       1: from math import sin and cos
                               ^^^

    Le mot-clé Python `and` ne peut être utilisé que pour les expressions booléennes.
    Vous vouliez peut-être écrire
    
    `from math import sin , cos`
    

(2) Using 'and' after comma in import statement
-----------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\and_in_import_statement_2.py", line 1
        from math import sin, tan, and cos
                                   ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\and_in_import_statement_2.py'
    à l'endroit indiqué.
    
       1: from math import sin, tan, and cos
                                     ^^^

    Le mot-clé Python `and` ne peut être utilisé que pour les expressions booléennes.
    Vous vouliez peut-être écrire
    
    `from math import sin, tan,  cos`
    

(3) Annotated name cannot be global
-----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\annotated_name_global.py", line 4
        var:int = 1
        ^
    SyntaxError: annotated name 'var' can't be global
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\annotated_name_global.py'
    à l'endroit indiqué.
    
       4:     var:int = 1
              ^^^

    L’objet nommé `var` est défini avec une annotation de type
    comme une variable locale. Il ne peut pas être déclaré variable globale.
    

(4) Incorrect use of 'from module import ... as ...
---------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\as_instead_of_comma_in_import.py", line 2
        from math import (sin, cos) as funcs
                                    ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\as_instead_of_comma_in_import.py'
    à l'endroit indiqué.
    
       2: from math import (sin, cos) as funcs
                                      ^^

    Je suppose que vous essayez d’importer au moins un objet
    à partir du module `math` pour le renommer en utilisant le mot clé Python `as`;
    ce mot clé ne peut être utilisé que pour renommer un objet à la fois
    en utilisant une syntaxe bien définie.
    Je vous suggère de diviser une telle déclaration d’importation avec chaque objet
    renommé sur une ligne séparée comme suit:
    
        from math import objet_1 as nom_1
        from math import objet_2 as nom_2 # si nécessaire
    

(5) Assign instead of equal (or walrus).
----------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_instead_of_equal.py", line 1
        a = (b = 2)  # issue #65
               ^
    SyntaxError: invalid syntax
    
        Peut-être que vous aviez besoin de `==` ou `:=` au lieu de `=`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_instead_of_equal.py'
    à l'endroit indiqué.
    
       1: a = (b = 2)  # issue #65
                 ^

    Vous avez utilisé un opérateur d’affectation `=`; vous vouliez peut-être utiliser 
    un opérateur d'égalité, `==`, ou l'opérateur `:=`.
    

(6) Name assigned prior to global declaration
---------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_name_before_global_1.py", line 7
        global aa, bb, cc, dd
        ^
    SyntaxError: name 'cc' is assigned to before global declaration
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_name_before_global_1.py'
    à l'endroit indiqué.
    
       7:     global aa, bb, cc, dd
              ------         ^^

    Vous avez attribué une valeur à la variable `cc`
    avant de la déclarer comme une variable globale.
    

(7) Name used prior to global declaration
-----------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_name_before_global_2.py", line 7
        global var
        ^
    SyntaxError: name 'var' is used prior to global declaration
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_name_before_global_2.py'
    .
    
       7:     global var
              ------ ^^^

    Vous avez utilisé la variable `var`
    avant de la déclarer comme une variable globale.
    

(8) Name used prior to nonlocal declaration
-------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_name_before_nonlocal_1.py", line 11
        nonlocal pp, qq
        ^
    SyntaxError: name 'qq' is used prior to nonlocal declaration
    
        Avez-vous oublié d’ajouter `nonlocal` en premier ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_name_before_nonlocal_1.py'
    à l'endroit indiqué.
    
       11:         nonlocal pp, qq
                   --------     ^^

    Vous avez utilisé la variable `qq`
    avant de la déclarer comme variable non locale.
    

(9) Name assigned prior to nonlocal declaration
-----------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_name_before_nonlocal_2.py", line 9
        nonlocal s
        ^
    SyntaxError: name 's' is assigned to before nonlocal declaration
    
        Avez-vous oublié d’ajouter `nonlocal` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_name_before_nonlocal_2.py'
    .
    
       9:         nonlocal s
                  -------- ^

    Vous avez attribué une valeur à la variable `s`
    avant de la déclarer comme variable non locale.
    

(10) Assign to conditional expression
-------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_to_conditional.py", line 3
        a if 1 else b = 1
        ^
    SyntaxError: cannot assign to conditional expression
    
        Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_to_conditional.py'
    à l'endroit indiqué.
    
       3: a if 1 else b = 1
          ^^^^^^^^^^^^^

    Du côté gauche d'un signe d'égalité, vous avez une
    expression génératrice au lieu du nom d'une variable.
        a if 1 else b = ...
        ^^^^^^^^^^^^^
    Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
    

(11) Assignment to keyword (__debug__)
--------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_to_debug.py", line 4
        __debug__ = 1
        ^
    SyntaxError: cannot assign to __debug__
    
        Vous ne pouvez pas attribuer une valeur à `__debug__`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_to_debug.py'
    à l'endroit indiqué.
    
       4: __debug__ = 1
          ^^^^^^^^^

    `__debug__` est une constante dans python; vous ne pouvez pas lui assigner une valeur différente.
    
    

(12) Assignment to keyword (__debug__)
--------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_to_debug2.py", line 4
        a.__debug__ = 1
        ^
    SyntaxError: cannot assign to __debug__
    
        Vous ne pouvez pas attribuer une valeur à `__debug__`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_to_debug2.py'
    à l'endroit indiqué.
    
       4: a.__debug__ = 1
            ^^^^^^^^^

    `__debug__` est une constante dans python; vous ne pouvez pas lui assigner une valeur différente.
    
    

(13) Assignment to Ellipsis symbol
----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_to_ellipsis.py", line 4
        ... = 1
        ^
    SyntaxError: cannot assign to Ellipsis
    
        Vous ne pouvez pas attribuer une valeur au symbole 'ellipsis' [`...`].
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_to_ellipsis.py'
    à l'endroit indiqué.
    
       4: ... = 1
          ^^^

    Le symbole `...` est une constante dans python; vous ne pouvez pas lui assigner une valeur différente.
    
    

(14) Cannot assign to f-string
------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_to_f_string.py", line 6
        f'{x}' = 42
        ^
    SyntaxError: cannot assign to f-string expression
    
        Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_to_f_string.py'
    à l'endroit indiqué.
    
       6: f'{x}' = 42
          ^^^^^^

    Vous avez écrit une expression qui a la chaine de
    caractères formatés `f'{x}'`
    du côté gauche du signe d'égalité.
    Une telle chaîne ne doit apparaître que du côté droit d'un signe d’égalité.
    Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
    

(15) Cannot assign to function call: single = sign
--------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_to_function_call_1.py", line 6
        len('a') = 3
        ^
    SyntaxError: cannot assign to function call
    
        Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_to_function_call_1.py'
    à l'endroit indiqué.
    
       6: len('a') = 3
          ^^^^^^^^

    Vous avez écrit une expression comme
    
        len('a') = ...
        ^^^^^^^^
    
    où `len('a')`, à la gauche du signe d'égalité est soit l'invocation
    d'une fonction, ou inclus une telle invocation,
    et n'est pas simplement le nom d'une variable.
    Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
    

(16) Cannot assign to function call: two = signs
------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_to_function_call_2.py", line 6
        func(a, b=3) = 4
        ^
    SyntaxError: cannot assign to function call
    
        Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_to_function_call_2.py'
    à l'endroit indiqué.
    
       6: func(a, b=3) = 4
          ^^^^^^^^^^^^

    Vous avez écrit une expression comme
    
        func(a, b=3) = ...
        ^^^^^^^^^^^^
    
    où `func(a, b=3)`, à la gauche du signe d'égalité est soit l'invocation
    d'une fonction, ou inclus une telle invocation,
    et n'est pas simplement le nom d'une variable.
    Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
    

(17) Cannot assign to function call: continues on second line
-------------------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_to_function_call_3.py", line 6
        a = f(1, 2,  # this is a comment
            ^
    SyntaxError: cannot assign to function call
    
        Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_to_function_call_3.py'
    à l'endroit indiqué.
    
    -->6: a = f(1, 2,  # this is a comment
              ^^^^^^^-->
       7:       3, 4) = 5

    Vous avez écrit une expression comme
    
        f(1, 2,...) = ...
        ^^^^^^^-->
    
    où `f(1, 2,...)`, à la gauche du signe d'égalité est soit l'invocation
    d'une fonction, ou inclus une telle invocation,
    et n'est pas simplement le nom d'une variable.
    Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
    

(18) Assign to generator expression
-----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_to_generator.py", line 3
        (x for x in x) = 1
        ^
    SyntaxError: cannot assign to generator expression
    
        Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_to_generator.py'
    à l'endroit indiqué.
    
       3: (x for x in x) = 1
          ^^^^^^^^^^^^^^

    Du côté gauche d'un signe d'égalité, vous avez une
    expression génératrice au lieu du nom d'une variable.
    Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
    

(19) Cannot assign to literal - 4
---------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_to_literal_dict.py", line 7
        {1 : 2, 2 : 4} = 5
        ^
    SyntaxError: cannot assign to dict display
    
        Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_to_literal_dict.py'
    à l'endroit indiqué.
    
       7: {1 : 2, 2 : 4} = 5
          ^^^^^^^^^^^^^^

    Vous avez écrit une expression comme
    
        {1 : 2, 2 : 4} = 5
    où `{1 : 2, 2 : 4}`, du côté gauche du signe d'égalité
    est ou inclut un objet de type `dict`
    et n'est pas simplement le nom d'une variable.
    
    Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
    

(20) Cannot assign to literal int
---------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_to_literal_int.py", line 3
        1 = a
        ^
    SyntaxError: cannot assign to literal
    
        Peut-être que vous vouliez plutôt écrire : `a = 1`
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_to_literal_int.py'
    à l'endroit indiqué.
    
       3: 1 = a
          ^

    Vous avez écrit une expression comme
    
        1 = a
    où `1`, du côté gauche du signe d'égalité
    est ou inclut un objet de type `int`
    et n'est pas simplement le nom d'une variable.
    Peut-être que vous vouliez plutôt écrire :
    
        a = 1
    
    

(21) Cannot assign to literal int - 2
-------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_to_literal_int_2.py", line 3
        1 = 2
        ^
    SyntaxError: cannot assign to literal
    
        Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_to_literal_int_2.py'
    à l'endroit indiqué.
    
       3: 1 = 2
          ^

    Vous avez écrit une expression comme
    
        1 = 2
    où `1`, du côté gauche du signe d'égalité
    est ou inclut un objet de type `int`
    et n'est pas simplement le nom d'une variable.
    
    Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
    

(22) Cannot assign to literal - 5
---------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_to_literal_int_3.py", line 4
        1 = a = b
        ^
    SyntaxError: cannot assign to literal
    
        Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_to_literal_int_3.py'
    à l'endroit indiqué.
    
       4: 1 = a = b
          ^

    Vous avez écrit une expression comme
    
        1 = nom_de_variable
    où `1`, du côté gauche du signe d'égalité
    est ou inclut un objet de type `int`
    et n'est pas simplement le nom d'une variable.
    
    Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
    

(23) Cannot assign to literal - 3
---------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_to_literal_set.py", line 7
        {1, 2, 3} = 4
        ^
    SyntaxError: cannot assign to set display
    
        Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_to_literal_set.py'
    à l'endroit indiqué.
    
       7: {1, 2, 3} = 4
          ^^^^^^^^^

    Vous avez écrit une expression comme
    
        {1, 2, 3} = 4
    où `{1, 2, 3}`, du côté gauche du signe d'égalité
    est ou inclut un objet de type `set`
    et n'est pas simplement le nom d'une variable.
    
    Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
    

(24) Assign to keyword def
--------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_to_keyword_def.py", line 3
        def = 2
            ^
    SyntaxError: invalid syntax
    
        Les mots clés Python ne peuvent pas être utilisés comme identifiants (noms de variables).
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_to_keyword_def.py'
    à l'endroit indiqué.
    
       3: def = 2
          ^^^

    Vous essayiez d’assigner une valeur au mot clé Python `def`.
    Ceci n’est pas permis.
    
    

(25) Assign to keyword else
---------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_to_keyword_else.py", line 3
        else = 1
        ^
    SyntaxError: invalid syntax
    
        Les mots clés Python ne peuvent pas être utilisés comme identifiants (noms de variables).
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_to_keyword_else.py'
    à l'endroit indiqué.
    
       3: else = 1
          ^^^^

    Vous essayiez d’assigner une valeur au mot clé Python `else`.
    Ceci n’est pas permis.
    
    

(26) Assignment to keyword (None)
---------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_to_keyword_none.py", line 4
        None = 1
        ^
    SyntaxError: cannot assign to None
    
        Vous ne pouvez pas attribuer une valeur à `None`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_to_keyword_none.py'
    à l'endroit indiqué.
    
       4: None = 1
          ^^^^

    `None` est une constante dans python; vous ne pouvez pas lui assigner une valeur différente.
    
    

(27) Assign to math operation
-----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_to_operation.py", line 4
        a + 1 = 2
        ^
    SyntaxError: cannot assign to operator
    
        Peut-être que vous aviez besoin de `==` au lieu de `=`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_to_operation.py'
    à l'endroit indiqué.
    
       4: a + 1 = 2
          ^

    Vous avez écrit une expression qui inclut des opérations mathématiques
    du côté gauche du signe d'égalité; ceci devrait être
    utilisé uniquement pour attribuer une valeur à une variable.
    

(28) Assign to yield expression
-------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assign_to_yield_expression.py", line 1
        (yield i) = 3
         ^
    SyntaxError: cannot assign to yield expression
    
        Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assign_to_yield_expression.py'
    à l'endroit indiqué.
    
       1: (yield i) = 3
           ^^^^^

    Vous avez écrit une expression qui inclut le mot-clé `yield`
    du côté gauche du signe égal.
    Vous ne pouvez pas attribuer une valeur à une telle expression.
    Notez que, comme le mot-clé `return`,
    `yield` ne peut être utilisé qu'à l'intérieur d'une fonction.
    

(29) Augmented assignment inside comprehension
----------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assignment_expression_cannot_rebind.py", line 1
        a = [(i := 1) for i in [1]]
             ^
    SyntaxError: assignment expression cannot rebind comprehension iteration variable 'i'
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assignment_expression_cannot_rebind.py'
    à l'endroit indiqué.
    
       1: a = [(i := 1) for i in [1]]
               ^

    Vous utilisez l'opérateur d'affectation augmenté `:=` à l'intérieur d'une
    compréhension pour assigner une valeur à la variable d'itération `i`.
    Cette variable est censée être utilisée uniquement à l'intérieur de la compréhension.
    L'opérateur d'affectation augmenté est normalement utilisé pour affecter une valeur
    à une variable afin que cette dernière puisse être réutilisée ailleurs.
    Ceci n'est pas possible pour la variable `i`.
    

(30) Augmented assignment inside comprehension - inner loop
-----------------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\assignment_expression_cannot_rebind_2.py", line 1
        [i for i in range(5) if (j := 0) for k[j + 1] in range(5)]
        ^
    SyntaxError: comprehension inner loop cannot rebind assignment expression target 'j'
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\assignment_expression_cannot_rebind_2.py'
    à l'endroit indiqué.
    
       1: [i for i in range(5) if (j := 0) for k[j + 1] in range(5)]
          ^

    Vous utilisez l'opérateur d'affectation augmenté `:=` à l'intérieur d'une
    compréhension pour assigner une valeur à la variable d'itération `j`.
    Cette variable est censée être utilisée uniquement à l'intérieur de la compréhension.
    L'opérateur d'affectation augmenté est normalement utilisé pour affecter une valeur
    à une variable afin que cette dernière puisse être réutilisée ailleurs.
    Ceci n'est pas possible pour la variable `j`.
    

(31) def: missing parentheses
-----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\async_def_missing_parens.py", line 1
        async def name:
                      ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié d’ajouter des parenthèses ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\async_def_missing_parens.py'
    à l'endroit indiqué.
    
       1: async def name:
                        ^

    Vous avez peut-être oublié d’inclure des parenthèses.
    Vous avez peut-être voulu écrire 
    
        async def name():
    

(32) Augmented assignment to literal
------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\augmented_assignment_to_literal.py", line 1
        if "word" := True:
           ^
    SyntaxError: cannot use assignment expressions with literal
    
        Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\augmented_assignment_to_literal.py'
    à l'endroit indiqué.
    
       1: if "word" := True:
             ^^^^^^

    Vous ne pouvez pas utiliser l’opérateur d’affectation augmentée `:=`,
    parfois appelé l’opérateur morse, avec des littéraux comme `"word"`.
    Vous ne pouvez attribuer des objets qu’à des identifiants (noms de variables).
    

(33) Walrus/Named assignment depending on Python version
--------------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\augmented_assigment_with_true.py", line 4
        (True := 1)
         ^
    SyntaxError: cannot use assignment expressions with True
    
        Vous ne pouvez pas attribuer une valeur à `True`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\augmented_assigment_with_true.py'
    à l'endroit indiqué.
    
       4: (True := 1)
           ^^^^

    `True` est une constante dans python; vous ne pouvez pas lui assigner une valeur différente.
    
    

(34) Backslash instead of slash
-------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\backslash_instead_of_slash.py", line 1
        a = 3 \ 4.0
               ^
    SyntaxError: unexpected character after line continuation character
    
        Voulez-vous diviser par 4.0 ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\backslash_instead_of_slash.py'
    à l'endroit indiqué.
    
       1: a = 3 \ 4.0
                  ^^^

    Vous utilisez le caractère de continuation `\` en dehors d'une chaîne de caractères,
    et il est suivi par au moins un autre caractère.
    Je suppose que vous vouliez diviser par le nombre 4.0
    et avez écrit \ au lieu de /.

(35) Brackets instead of parentheses
------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\bracket_instead_of_paren.py", line 1
        print(sum[i for i in [1, 2, 3] if i%2==0])
                    ^
    SyntaxError: invalid syntax
    
        Vous avez utilisé des crochets, `[...]` au lieu de parenthèses.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\bracket_instead_of_paren.py'
    à l'endroit indiqué.
    
       1: print(sum[i for i in [1, 2, 3] if i%2==0])
                      ^^^

    Vous avez utilisé des crochets, `[...]` au lieu de parenthèses.
    Écrivez plutôt ce qui suit :
    
        print(sum(i for i in [1, 2, 3] if i%2==0))

(36) break outside loop
-----------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\break_outside_loop.py", line 4
        break
        ^
    SyntaxError: 'break' outside loop
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\break_outside_loop.py'
    à l'endroit indiqué.
    
       4:     break
              ^^^^^

    Le mot-clé Python `break` ne peut être utilisé qu'à l'intérieur d'une boucle `for` ou à l'intérieur d'une boucle `while`.
    

(37) Cannot assign to attribute here.
-------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\cannot_assign_to_attribute_here.py", line 1
        if x.a = 1:
               ^
    SyntaxError: invalid syntax
    
        Peut-être que vous aviez besoin de `==` au lieu de `=`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\cannot_assign_to_attribute_here.py'
    à l'endroit indiqué.
    
       1: if x.a = 1:
                 ^

    Vous avez utilisé un opérateur d’affectation `=` au lieu d’un opérateur d'égalité `==` 
    L'énoncé suivant ne contient pas d'erreur de syntaxe :
    
        if x.a == 1:

(38) Cannot guess the cause
---------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\cannot_guess_the_cause.py", line 1
        SyntaxErrors can be annoying!
                     ^
    SyntaxError: invalid syntax
    
        Friendly-traceback ne connaît pas la cause de cette erreur.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\cannot_guess_the_cause.py'
    à l'endroit indiqué.
    
       1: SyntaxErrors can be annoying!
                       ^^^

    Présentement, je ne peux pas deviner la cause probable de cette erreur.
    Essayez d’examiner attentivement la ligne indiquée ainsi que celle
    immédiatement au dessus pour voir si vous pouvez identifier
    un mot mal orthographié, ou des symboles manquants, comme (,), [,],:, etc.
    
    Si votre code n'utilise pas d'annotations de type,
    et que vous pensez que friendly devrait
    pouvoir l'analyser correctement, SVP rapporter ce cas au site suivant:
    https://github.com/aroberge/friendly/issues
    
    

(39) Cannot use star operator
-----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\cannot_use_star.py", line 3
        *a
        ^
    SyntaxError: can't use starred expression here
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\cannot_use_star.py'
    à l'endroit indiqué.
    
       3: *a
          ^

    L’opérateur astérisque `*` est interprété comme signifiant que
    le déballage itérable doit être utilisé pour attribuer un nom
    à chaque élément d’un itérable, ce qui n’a pas de sens ici.
    

(40) Cannot use double star operator
------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\cannot_use_double_star.py", line 4
        (**k)
         ^
    SyntaxError: f-string: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\cannot_use_double_star.py'
    à l'endroit indiqué.
    
       1: (**k)
           ^-->

    L’opérateur double astérisque, `**` est probablement interprété comme signifiant
    qu'un déballage de `dict` doit être utilisé ce qui n'est soit par permis
    ou n’a pas de sens ici.
    

(41) Missing class name
-----------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\class_missing_name.py", line 1
        class:
             ^
    SyntaxError: invalid syntax
    
        Une classe a besoin d’un nom.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\class_missing_name.py'
    à l'endroit indiqué.
    
       1: class:
               ^

    Un énoncé `class` doit inclure un nom :
    
        class NomQuelconque:
            ...
    
    

(42) Missing () for tuples in comprehension
-------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\comprehension_missing_tuple_paren.py", line 1
        x = [i, i**2 for i in range(10)]
                     ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié d’ajouter des parenthèses ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\comprehension_missing_tuple_paren.py'
    à l'endroit indiqué.
    
       1: x = [i, i**2 for i in range(10)]
                       ^^^

    Je suppose que vous écriviez une compréhension ou une expression génératrice
    et vous avez oublié d’inclure des parenthèses autour des tuples.
    Voici un exemple: au lieu d’écrire
    
        [i, i**2 for i in range(10)]
    
    vous auriez besoin d’écrire
    
        [(i, i**2) for i in range(10)]
    
    

(43) Comprehension with condition (no else)
-------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\comprehension_with_condition_no_else.py", line 1
        a = [f(x) if condition for x in sequence]
                               ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\comprehension_with_condition_no_else.py'
    à l'endroit indiqué.
    
       1: a = [f(x) if condition for x in sequence]
                                 ^^^

    Je suppose que vous écriviez une compréhension ou une expression génératrice
    et avez utiliser le mauvais ordre pour une condition.
    L'ordre correct dépend de la présence ou non d'une clause `else`.
    Par exemple, le bon ordre pour une compréhension de liste avec
    une condition est
    
        [f(x) if condition else autre for x in séquence]  # 'if' avant 'for'
    
    ou, s'il n'y a pas de `else`
    
        [f(x) pour x in séquence si condition]  # 'if' après 'for'
    
    

(44) Comprehension with condition (with else)
---------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\comprehension_with_condition_with_else.py", line 1
        a = [f(x) for x in sequence if condition else other]
                                                 ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\comprehension_with_condition_with_else.py'
    à l'endroit indiqué.
    
       1: a = [f(x) for x in sequence if condition else other]
                                                   ^^^^

    Je suppose que vous écriviez une compréhension ou une expression génératrice
    et avez utiliser le mauvais ordre pour une condition.
    L'ordre correct dépend de la présence ou non d'une clause `else`.
    Par exemple, le bon ordre pour une compréhension de liste avec
    une condition est
    
        [f(x) if condition else autre for x in séquence]  # 'if' avant 'for'
    
    ou, s'il n'y a pas de `else`
    
        [f(x) pour x in séquence si condition]  # 'if' après 'for'
    
    

(45) continue outside loop
--------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\continue_outside_loop.py", line 4
        continue
        ^
    SyntaxError: 'continue' not properly in loop
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\continue_outside_loop.py'
    à l'endroit indiqué.
    
       4:     continue
              ^^^^^^^^

    Le mot-clé Python `continue` ne peut être utilisé qu'à l'intérieur d'une boucle `for` ou à l'intérieur d'une boucle `while`.
    

(46) Copy/paste from interpreter
--------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\copy_pasted_code.py", line 2
        >>> print("Hello World!")
        ^
    SyntaxError: invalid syntax
    
        Avez-vous utilisé le copier-coller ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\copy_pasted_code.py'
    à l'endroit indiqué.
    
       2: >>> print("Hello World!")
          ^^^

    On dirait que vous avez copié-collé le code d’un interprète interactif.
    L’invite Python, `>>>`, ne doit pas être incluse dans votre code.
    

(47) Copy/paste from interpreter - 2
------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\copy_pasted_code_2.py", line 2
        ... print("Hello World!")
            ^
    SyntaxError: invalid syntax
    
        Avez-vous utilisé le copier-coller ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\copy_pasted_code_2.py'
    .
    
       2: ... print("Hello World!")
          ----^^^^^

    On dirait que vous avez copié-collé le code d’un interprète interactif.
    L’invite Python, `...`, ne doit pas être incluse dans votre code.
    

(48) def: positional arg after kwargs
-------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_arg_after_kwarg.py", line 1
        def test(a, **kwargs, b):
                              ^
    SyntaxError: invalid syntax
    
        Les arguments positionnels doivent être avant les arguments nommés.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_arg_after_kwarg.py'
    à l'endroit indiqué.
    
       1: def test(a, **kwargs, b):
                                ^

    Les arguments positionnels doivent être avant les arguments nommés.
    `b` est un argument positionnel qui apparaît après un ou plusieurs
    arguments nommés dans votre définition de fonction.
    

(49) def: named arguments must follow bare *
--------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_bare_star_arg.py", line 4
        def f(*):
               ^
    SyntaxError: named arguments must follow bare *
    
        Avez-vous oublié d’ajouter quelque chose après `*` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_bare_star_arg.py'
    à l'endroit indiqué.
    
       4: def f(*):
                 ^

    En supposant que vous définissiez une fonction, vous avez besoin
    de remplacer `*` soit par `*arguments` ou
    par `*, argument=valeur`.
    

(50) def: misused as code block
-------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_code_block.py", line 3
        def :
            ^
    SyntaxError: invalid syntax
    
        Une fonction a besoin d’un nom.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_code_block.py'
    à l'endroit indiqué.
    
       3: def :
              ^

    Vous vouliez définir une fonction, mais vous avez fait des erreurs de syntaxe.
    La syntaxe correct est :
    
        def nom ( ... ):
    

(51) def: misused as code block - 2
-----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_code_block_2.py", line 2
        def :
            ^
    SyntaxError: invalid syntax
    
        Les fonctions et les méthodes ont besoin d’un nom.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_code_block_2.py'
    à l'endroit indiqué.
    
       2:     def :
                  ^

    Vous vouliez définir une fonction ou une méthode, mais vous avez fait des erreurs de syntaxe.
    La syntaxe correct est :
    
        def nom ( ... ):
    

(52) Dotted name as function argument
-------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_dotted_argument.py", line 3
        def test(x.y):
                  ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié une virgule ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_dotted_argument.py'
    à l'endroit indiqué.
    
       3: def test(x.y):
                    ^

    Vous avez tenté d'utiliser un objet avec un attribut comme argument de fonction.
    Vous vouliez peut-être écrire une virgule.
    

(53) Dotted name as function argument
-------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_dotted_argument_2.py", line 2
        def test(x., y):
                  ^
    SyntaxError: invalid syntax
    
        Vous avez tenté d'utiliser un objet avec un attribut comme argument de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_dotted_argument_2.py'
    à l'endroit indiqué.
    
       2: def test(x., y):
                    ^

    Vous avez tenté d'utiliser un objet avec un attribut comme argument de fonction.
    

(54) Dotted function name
-------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_dotted_function_name.py", line 3
        def test.x():
                ^
    SyntaxError: invalid syntax
    
        Vous avez tenté d'utiliser un objet avec un attribut comme nom de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_dotted_function_name.py'
    à l'endroit indiqué.
    
       3: def test.x():
                  ^

    Vous avez tenté d'utiliser un objet avec un attribut comme nom de fonction.
    

(55) def: dict as argument
--------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_dict_as_arg.py", line 1
        def test({'a': 1}, y):  # dict as first argument
                 ^
    SyntaxError: invalid syntax
    
        Vous ne pouvez pas avoir des `dict` ou des `set` explicite comme arguments de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_dict_as_arg.py'
    à l'endroit indiqué.
    
       1: def test({'a': 1}, y):  # dict as first argument
                   ^

    Vous ne pouvez pas avoir des `dict` ou des `set` explicite comme arguments de fonction.
    Vous ne pouvez utiliser que des identifiants (noms de variables) comme arguments de fonction.
    

(56) def: arguments must be unique in function definition
---------------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_duplicate_arg.py", line 4
        def f(aa=1, aa=2):
        ^
    SyntaxError: duplicate argument 'aa' in function definition
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_duplicate_arg.py'
    à l'endroit indiqué.
    
       4: def f(aa=1, aa=2):
                ^^    ^^

    Vous avez défini une fonction répétant l'argument
    
        aa
    Chaque argument ne doit apparaître qu'une seule fois dans une définition de fonction.
    

(57) def: semicolon after colon
-------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_extra_semi_colon.py", line 1
        def test():;
                   ^
    SyntaxError: invalid syntax
    
        Avez-vous écrit quelque chose par erreur après les deux points `:` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_extra_semi_colon.py'
    à l'endroit indiqué.
    
       1: def test():;
                     ^

    Une définition de fonction doit se terminer par deux point, `:`.
    Un bloc de code doit venir après les deux points.
    Si vous supprimez `;`, cela pourrait possiblement résoudre le problème.
    

(58) def: extra comma
---------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_extra_comma.py", line 1
        def test(a,,b):
                   ^
    SyntaxError: invalid syntax
    
        Voulez-vous écrire `,`?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_extra_comma.py'
    à l'endroit indiqué.
    
       1: def test(a,,b):
                     ^

    Je soupçonne que vous avez écrit `,` par erreur.
    L’énoncé suivant ne contient aucune erreur de syntaxe :
    
        def test(a,b):

(59) def: unspecified keywords before /
---------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_forward_slash_1.py", line 1
        def test(a, **kwargs, /):
                              ^
    SyntaxError: invalid syntax
    
        Les arguments nommés doivent apparaître après le symbole `/`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_forward_slash_1.py'
    à l'endroit indiqué.
    
       1: def test(a, **kwargs, /):
                                ^

    `/` indique que les arguments précédents dans une définition de fonction
    sont des arguments positionnels.
    Vous avez quelques arguments nommés arbitraires qui apparaissent avant
    le symbole `/`.
    

(60) def: / before star
-----------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_forward_slash_2.py", line 1
        def test(a, *, b, /):
                          ^
    SyntaxError: invalid syntax
    
        `*` doit apparaître après `/` dans une définition de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_forward_slash_2.py'
    à l'endroit indiqué.
    
       1: def test(a, *, b, /):
                            ^

    `/` indique que les arguments précédents dans une définition de fonction
    sont des arguments positionnels.
    Toutefois, `*` indique que les arguments
    qui suivent doivent être des arguments nommés.
    Lorsqu’ils sont utilisés ensemble, `/` doit apparaître avant `*`.
    

(61) def: / before star arg
---------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_forward_slash_3.py", line 1
        def test(a, *arg, /):
                          ^
    SyntaxError: invalid syntax
    
        `*arg` doit apparaître après `/` dans une définition de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_forward_slash_3.py'
    à l'endroit indiqué.
    
       1: def test(a, *arg, /):
                            ^

    `/` indique que les arguments précédents dans une définition de fonction
    sont des arguments positionnels.
    `*arg` doit apparaître après `/` dans une définition de fonction.
    

(62) def: / used twice
----------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_forward_slash_4.py", line 1
        def test(a, /, b, /):
                          ^
    SyntaxError: invalid syntax
    
        Vous ne pouvez utiliser `/` qu’une seule fois dans une définition de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_forward_slash_4.py'
    à l'endroit indiqué.
    
       1: def test(a, /, b, /):
                            ^

    Vous ne pouvez utiliser `/` qu’une seule fois dans une définition de fonction.
    

(63) def: non-identifier as a function name
-------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_function_name_invalid.py", line 3
        def 2be():
            ^
    SyntaxError: invalid syntax
    
        Vous avez écrit un nom de fonction invalide.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_function_name_invalid.py'
    à l'endroit indiqué.
    
       3: def 2be():
              ^

    Le nom d’une fonction doit être un identificateur Python valide,
    c’est-à-dire un nom qui commence par une lettre ou un caractère de soulignement, `_`,
    et qui ne contient que des lettres, des chiffres ou le caractère de soulignement.
    

(64) def: using a string as a function name
-------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_function_name_string.py", line 3
        def "function"():
            ^
    SyntaxError: invalid syntax
    
        Le nom d’une fonction doit être un identificateur Python valide,
        c’est-à-dire un nom qui commence par une lettre ou un caractère de soulignement, `_`,
        et qui ne contient que des lettres, des chiffres ou le caractère de soulignement.
        Vous avez essayé d’utiliser une chaîne de caractères comme nom de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_function_name_string.py'
    à l'endroit indiqué.
    
       3: def "function"():
              ^^^^^^^^^^

    Le nom d’une fonction doit être un identificateur Python valide,
    c’est-à-dire un nom qui commence par une lettre ou un caractère de soulignement, `_`,
    et qui ne contient que des lettres, des chiffres ou le caractère de soulignement.
    Vous avez essayé d’utiliser une chaîne de caractères comme nom de fonction.
    

(65) def: keyword cannot be argument in def - 1
-----------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_keyword_as_arg_1.py", line 5
        def f(None=1):
              ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_keyword_as_arg_1.py'
    à l'endroit indiqué.
    
       5: def f(None=1):
                ^^^^

    Vous avez tenté d'utiliser le mot clé Python `None` comme argument
    dans la définition d'une fonction où un identificateur
    (nom de variable) était attendu.
    

(66) def: keyword cannot be argument in def - 2
-----------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_keyword_as_arg_2.py", line 5
        def f(x, True):
                 ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_keyword_as_arg_2.py'
    à l'endroit indiqué.
    
       5: def f(x, True):
                   ^^^^

    Vous avez tenté d'utiliser le mot clé Python `True` comme argument
    dans la définition d'une fonction où un identificateur
    (nom de variable) était attendu.
    

(67) def: keyword cannot be argument in def - 3
-----------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_keyword_as_arg_3.py", line 5
        def f(*None):
               ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_keyword_as_arg_3.py'
    à l'endroit indiqué.
    
       5: def f(*None):
                 ^^^^

    Vous avez tenté d'utiliser le mot clé Python `None` comme argument
    dans la définition d'une fonction où un identificateur
    (nom de variable) était attendu.
    

(68) def: keyword cannot be argument in def - 4
-----------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_keyword_as_arg_4.py", line 5
        def f(**None):
                ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_keyword_as_arg_4.py'
    à l'endroit indiqué.
    
       5: def f(**None):
                  ^^^^

    Vous avez tenté d'utiliser le mot clé Python `None` comme argument
    dans la définition d'une fonction où un identificateur
    (nom de variable) était attendu.
    

(69) def: Python keyword as function name
-----------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_keyword_as_name.py", line 3
        def pass():
            ^
    SyntaxError: invalid syntax
    
        Vous avez tenté d'utiliser le mot clé Python `{kwd}` comme nom de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_keyword_as_name.py'
    à l'endroit indiqué.
    
       3: def pass():
              ^^^^

    Vous avez tenté d'utiliser le mot clé Python `pass` comme nom de fonction.
    Ceci n’est pas permis.
    
    
    Il y a au moins une autre erreur de syntaxe plus tard dans votre code.
    

(70) def: list as argument - 1
------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_list_as_arg_1.py", line 1
        def test([x], y):  # list as first argument
                 ^
    SyntaxError: invalid syntax
    
        Vous ne pouvez pas avoir de listes explicites comme arguments de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_list_as_arg_1.py'
    à l'endroit indiqué.
    
       1: def test([x], y):  # list as first argument
                   ^

    Vous ne pouvez pas avoir de listes explicites comme arguments de fonction.
    Vous ne pouvez utiliser que des identifiants (noms de variables) comme arguments de fonction.
    

(71) def: list as argument - 2
------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_list_as_arg_2.py", line 1
        def test(x, [y]):  # list as second argument, after comma
                    ^
    SyntaxError: invalid syntax
    
        Vous ne pouvez pas avoir de listes explicites comme arguments de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_list_as_arg_2.py'
    à l'endroit indiqué.
    
       1: def test(x, [y]):  # list as second argument, after comma
                      ^

    Vous ne pouvez pas avoir de listes explicites comme arguments de fonction.
    Vous ne pouvez utiliser que des identifiants (noms de variables) comme arguments de fonction.
    

(72) def: missing colon
-----------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_missing_colon.py", line 1
        def test()
                  ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié d’ajouter les deux points `:` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_missing_colon.py'
    à l'endroit indiqué.
    
       1: def test()
                    ^

    Une définition de fonction doit se terminer par deux point, `:`.
    

(73) def: missing comma between function args
---------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_missing_comma.py", line 4
        def a(b, c d):
                   ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié une virgule ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_missing_comma.py'
    à l'endroit indiqué.
    
       4: def a(b, c d):
                   ^^^

    Python indique que l’erreur est causée par `d` écrit tout juste après `c`.
    Il est possible que vous ayez oublié une virgule entre les éléments d'un tuple,
    ou entre les arguments d'une fonction,
    à la position indiquée par ^.
    Vous vouliez peut-être dire
    
        def a(b, c, d):
                  ^
    
    

(74) def: missing parentheses
-----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_missing_parens.py", line 3
        def name:
                ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié d’ajouter des parenthèses ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_missing_parens.py'
    à l'endroit indiqué.
    
       3: def name:
                  ^

    Vous avez peut-être oublié d’inclure des parenthèses.
    Vous avez peut-être voulu écrire 
    
        def name():
    

(75) def: missing parentheses around arguments
----------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_missing_parens_2.py", line 2
        def name a, b:
                 ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié d’ajouter des parenthèses ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_missing_parens_2.py'
    à l'endroit indiqué.
    
       2: def name a, b:
                   ^

    Vous avez peut-être oublié d’inclure des parenthèses.
    Vous avez peut-être voulu écrire 
    
        def name (a, b):
    

(76) def: missing function name
-------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_missing_name.py", line 3
        def ( arg )  :
            ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_missing_name.py'
    à l'endroit indiqué.
    
       3: def ( arg )  :
              ^

    Vous avez oublié de nommer votre fonction.
    La syntaxe correct est :
    
        def nom ( ... ):
    

(77) def: name is parameter and global
--------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_name_is_parameter_and_global.py", line 6
        global x
        ^
    SyntaxError: name 'x' is parameter and global
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_name_is_parameter_and_global.py'
    à l'endroit indiqué.
    
       6:     global x
              ^^^^^^

    Vous avec inclus l'énoncé
    
            global x
    
    
    indiquant que `x` est une variable définie en dehors d'une fonction.
    Vous utilisez également le même `x` comme un argument pour cette
    fonction; un argument de fonction est une variable locale connue seulement
    à l'intérieur de cette fonction, ce qui est le contraire de ce que `global` sous-entendait.
    

(78) def: non-default argument follows default argument
-------------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_non_default_after_default.py", line 5
        def test(a=1, b):
                       ^
    SyntaxError: non-default argument follows default argument
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_non_default_after_default.py'
    à l'endroit indiqué.
    
       5: def test(a=1, b):
                         ^

    Dans Python, vous pouvez définir les fonctions avec seulement des arguments de position
    
        def test(a, b, c): ...
    
    ou seulement des arguments nommés
    
        def test(a=1, b=2, c=3): ...
    
    ou une combinaison des deux
    
        def test(a, b, c=3): ...
    
    mais avec les arguments nommés apparaissant après tous les arguments positionnels.
    Selon Python, vous avez utilisé des arguments positionnels après des arguments nommés.
    

(79) Single number used as arg in function def
----------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_number_as_arg.py", line 1
        def f(1):
              ^
    SyntaxError: invalid syntax
    
        Vous ne pouvez pas utiliser un nombre comme argument de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_number_as_arg.py'
    à l'endroit indiqué.
    
       1: def f(1):
                ^

    Vous avez utilisé un nombre comme argument lors de la définition d’une fonction.
    Vous ne pouvez utiliser que des identificateurs (noms de variables) comme arguments de fonction.
    

(80) Operator after ``**``
--------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_operator_after_2star.py", line 1
        def test(**):
                   ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_operator_after_2star.py'
    à l'endroit indiqué.
    
       1: def test(**):
                     ^

    L'opérateur `**` doit être suivi d'un identifiant (nom de variable).
    

(81) def: operator instead of comma
-----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_operator_instead_of_comma.py", line 1
        def test(a + b):
                   ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié une virgule ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_operator_instead_of_comma.py'
    à l'endroit indiqué.
    
       1: def test(a + b):
                     ^

    Vous ne pouvez pas avoir d’opérateurs comme arguments de fonction.
    Je soupçonne que vous avez écrit `+` au lieu d’une virgule.
    L’énoncé suivant ne contient aucune erreur de syntaxe :
    
        def test(a , b):

(82) def: operator instead of equal
-----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_operator_instead_of_equal.py", line 1
        def test(a, b=3, c+None):
                          ^
    SyntaxError: invalid syntax
    
        Voulez-vous écrire un signe égal ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_operator_instead_of_equal.py'
    à l'endroit indiqué.
    
       1: def test(a, b=3, c+None):
                            ^

    Vous ne pouvez pas avoir d’opérateurs comme arguments de fonction.
    Je soupçonne que vous avez écrit `+` au lieu d’un signe d'égalité.
    L’énoncé suivant ne contient aucune erreur de syntaxe :
    
        def test(a, b=3, c=None):

(83) def: operator instead of name
----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_operator_instead_of_name.py", line 1
        def test(a, +, b):
                    ^
    SyntaxError: invalid syntax
    
        Vous ne pouvez pas utiliser `+` comme argument.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_operator_instead_of_name.py'
    à l'endroit indiqué.
    
       1: def test(a, +, b):
                      ^

    Je soupçonne que vous avez écrit `+` par erreur.
    Si vous le remplacez par un nom de variable unique,
    le résultat n'aura aucun erreur de syntaxe.
    

(84) def: positional argument follows keyword argument
------------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_positional_after_keyword_arg.py", line 5
        test(a=1, b)
                   ^
    SyntaxError: positional argument follows keyword argument
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_positional_after_keyword_arg.py'
    à l'endroit indiqué.
    
       5: test(a=1, b)
                     ^

    Dans Python, vous pouvez invoquer les fonctions avec seulement des arguments de position
    
        test(1, 2, 3)
    
    ou seulement des arguments nommés
    
        test (a=1, b=2, c=3)
    
    ou une combinaison des deux
    
        test(1, 2, c=3)
    
    mais avec les arguments nommés apparaissant après tous les arguments positionnels.
    Selon Python, vous avez utilisé des arguments positionnels après des arguments nommés.
    

(85) def: semicolon instead of colon
------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_semi_colon_instead_of_colon.py", line 1
        def test();
                  ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié d’ajouter les deux points `:` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_semi_colon_instead_of_colon.py'
    à l'endroit indiqué.
    
       1: def test();
                    ^

    Une définition de fonction doit se terminer par deux point, `:`.
    Tu as écrit `;` au lieu de deux points, `:`.
    

(86) def: set as argument
-------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_set_as_arg.py", line 1
        def test(y, {'a', 'b'}):  # set as second argument, after comma
                    ^
    SyntaxError: invalid syntax
    
        Vous ne pouvez pas avoir des `dict` ou des `set` explicite comme arguments de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_set_as_arg.py'
    à l'endroit indiqué.
    
       1: def test(y, {'a', 'b'}):  # set as second argument, after comma
                      ^

    Vous ne pouvez pas avoir des `dict` ou des `set` explicite comme arguments de fonction.
    Vous ne pouvez utiliser que des identifiants (noms de variables) comme arguments de fonction.
    

(87) def: ``*arg`` before /
---------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_star_arg_before_slash.py", line 1
        def test(a, *arg, /):
                          ^
    SyntaxError: invalid syntax
    
        `*arg` doit apparaître après `/` dans une définition de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_star_arg_before_slash.py'
    à l'endroit indiqué.
    
       1: def test(a, *arg, /):
                            ^

    `/` indique que les arguments précédents dans une définition de fonction
    sont des arguments positionnels.
    `*arg` doit apparaître après `/` dans une définition de fonction.
    

(88) def: ``*`` used twice
--------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_star_used_only_once.py", line 1
        def test(a, *arg, *, b=1):
                          ^
    SyntaxError: invalid syntax
    
        Vous ne pouvez utiliser `*` qu’une seule fois dans une définition de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_star_used_only_once.py'
    à l'endroit indiqué.
    
       1: def test(a, *arg, *, b=1):
                            ^

    Vous ne pouvez utiliser `*` qu’une seule fois dans une définition de fonction.
    Il doit être utilisé soit par lui-même, `*`,
    soit sous la forme `*arg`, mais pas les deux.
    

(89) def: ``*`` used twice
--------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_star_used_only_once_1.py", line 1
        def test(a, *, *):
                       ^
    SyntaxError: invalid syntax
    
        Vous ne pouvez utiliser `*` qu’une seule fois dans une définition de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_star_used_only_once_1.py'
    à l'endroit indiqué.
    
       1: def test(a, *, *):
                         ^

    Vous ne pouvez utiliser `*` qu’une seule fois dans une définition de fonction.
    

(90) def: ``*`` used twice
--------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_star_used_only_once_2.py", line 1
        def test(a, *arg, *other):
                          ^
    SyntaxError: invalid syntax
    
        Vous ne pouvez utiliser `*` qu’une seule fois dans une définition de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_star_used_only_once_2.py'
    à l'endroit indiqué.
    
       1: def test(a, *arg, *other):
                            ^

    Vous ne pouvez utiliser `*` qu’une seule fois dans une définition de fonction.
    Vous l'avez utilisé deux fois, avec `*arg` et `*other`.
    

(91) def: ``*`` after ``**``
----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_star_after_2star.py", line 1
        def test(**kw, *arg):
                       ^
    SyntaxError: invalid syntax
    
        Vous ne pouvez utiliser `*` qu’une seule fois dans une définition de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_star_after_2star.py'
    à l'endroit indiqué.
    
       1: def test(**kw, *arg):
                         ^

    `*arg` doit apparaître avant `**kw`.
    

(92) def: ``*`` after ``**``
----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_star_after_2star_2.py", line 1
        def test(**kw, *):
                       ^
    SyntaxError: invalid syntax
    
        Vous ne pouvez utiliser `*` qu’une seule fois dans une définition de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_star_after_2star_2.py'
    à l'endroit indiqué.
    
       1: def test(**kw, *):
                         ^

    `**kw` doit apparaître après l'opérateur `*`.
    

(93) Single string used as arg in function def
----------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_string_as_arg.py", line 1
        def f("1"):
              ^
    SyntaxError: invalid syntax
    
        Vous ne pouvez pas utiliser les chaînes comme arguments de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_string_as_arg.py'
    à l'endroit indiqué.
    
       1: def f("1"):
                ^^^

    Vous avez utilisé une chaîne comme argument lors de la définition d’une fonction.
    Vous ne pouvez utiliser que des identificateurs (noms de variables) comme arguments de fonction.
    

(94) def: tuple as function argument
------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_tuple_as_arg_1.py", line 1
        def test((a, b), c):
                 ^
    SyntaxError: invalid syntax
    
        Vous ne pouvez pas avoir des tuples explicites comme arguments de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_tuple_as_arg_1.py'
    à l'endroit indiqué.
    
       1: def test((a, b), c):
                   ^

    Vous ne pouvez pas avoir des tuples explicites comme arguments de fonction.
    Vous ne pouvez utiliser que des identifiants (noms de variables) comme arguments de fonction.
    Assignez n’importe quel tuple à un paramètre et dépaquetez-le
    dans le corps de la fonction.
    

(95) def: tuple as function argument - 2
----------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\def_tuple_as_arg_2.py", line 1
        def test(a, (b, c)):
                    ^
    SyntaxError: invalid syntax
    
        Vous ne pouvez pas avoir des tuples explicites comme arguments de fonction.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\def_tuple_as_arg_2.py'
    à l'endroit indiqué.
    
       1: def test(a, (b, c)):
                      ^

    Vous ne pouvez pas avoir des tuples explicites comme arguments de fonction.
    Vous ne pouvez utiliser que des identifiants (noms de variables) comme arguments de fonction.
    Assignez n’importe quel tuple à un paramètre et dépaquetez-le
    dans le corps de la fonction.
    

(96) Deleting star expression - 1
---------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\del_paren_star_1.py", line 1
        del (*x)
             ^
    SyntaxError: can't use starred expression here
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\del_paren_star_1.py'
    à l'endroit indiqué.
    
       1: del (*x)
               ^

    L’opérateur astérisque `*` est interprété comme signifiant que
    le déballage itérable doit être utilisé pour attribuer un nom
    à chaque élément d’un itérable, ce qui n’a pas de sens ici.
    Vous ne pouvez supprimer que les noms d'objets, ou des éléments
    dans des conteneurs mutables comme `list`, `set`, ou `dict`.
    

(97) Deleting star expression - 2
---------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\del_paren_star_2.py", line 1
        del (*x,)
             ^
    SyntaxError: cannot delete starred
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\del_paren_star_2.py'
    à l'endroit indiqué.
    
       1: del (*x,)
               ^

    L’opérateur astérisque `*` est interprété comme signifiant que
    le déballage itérable doit être utilisé pour attribuer un nom
    à chaque élément d’un itérable, ce qui n’a pas de sens ici.
    Vous ne pouvez supprimer que les noms d'objets, ou des éléments
    dans des conteneurs mutables comme `list`, `set`, ou `dict`.
    

(98) Cannot delete a constant
-----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\delete_constant_keyword.py", line 1
        del True
            ^
    SyntaxError: cannot delete True
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\delete_constant_keyword.py'
    à l'endroit indiqué.
    
       1: del True
              ^^^^

    Vous ne pouvez pas supprimer la constante `True`.
    Vous ne pouvez supprimer que les noms d'objets, ou des éléments
    dans des conteneurs mutables comme `list`, `set`, ou `dict`.
    

(99) Cannot delete expression
-----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\delete_expression.py", line 1
        del a.b.c[0] + 2
            ^
    SyntaxError: cannot delete operator
    
        Vous ne pouvez supprimer que les noms d'objets, ou des éléments
        dans des conteneurs mutables comme `list`, `set`, ou `dict`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\delete_expression.py'
    à l'endroit indiqué.
    
       1: del a.b.c[0] + 2
              ^

    Vous ne pouvez pas supprimer l'expression `a.b.c[0] + 2`.
    Vous ne pouvez supprimer que les noms d'objets, ou des éléments
    dans des conteneurs mutables comme `list`, `set`, ou `dict`.
    

(100) Cannot delete function call
---------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\delete_function_call.py", line 5
        del f(a)
            ^
    SyntaxError: cannot delete function call
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\delete_function_call.py'
    à l'endroit indiqué.
    
       5: del f(a)
              ^

    Vous avez tenté de supprimer un appel de fonction
    
        del f(a)
    au lieu de supprimer le nom de la fonction
    
        del f
    

(101) Cannot delete named expression
------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\delete_named_expression.py", line 1
        del (a := 5)
             ^
    SyntaxError: cannot delete named expression
    
        Vous ne pouvez supprimer que les noms d'objets, ou des éléments
        dans des conteneurs mutables comme `list`, `set`, ou `dict`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\delete_named_expression.py'
    à l'endroit indiqué.
    
       1: del (a := 5)
               ^

    Vous ne pouvez pas supprimer l'expression nommée `(a := 5)`.
    Vous ne pouvez supprimer que les noms d'objets, ou des éléments
    dans des conteneurs mutables comme `list`, `set`, ou `dict`.
    

(102) Delete only names or items
--------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\delete_names_or_items.py", line 1
        del a += b
              ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\delete_names_or_items.py'
    à l'endroit indiqué.
    
       1: del a += b
                ^^

    Vous ne pouvez supprimer que les noms d'objets, ou des éléments
    dans des conteneurs mutables comme `list`, `set`, ou `dict`.
    

(103) Deleting string literal
-----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\delete_string_literal.py", line 1
        del "Hello world!"
            ^
    SyntaxError: cannot delete literal
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\delete_string_literal.py'
    à l'endroit indiqué.
    
       1: del "Hello world!"
              ^^^^^^^^^^^^^^

    Vous ne pouvez pas supprimer le littéral `"Hello world!"`.
    Vous ne pouvez supprimer que les noms d'objets, ou des éléments
    dans des conteneurs mutables comme `list`, `set`, ou `dict`.
    

(104) Value missing in dict - 1
-------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\dict_value_missing_1.py", line 1
        a = {1:2, 3}
                   ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié d'écrire une valeur pour un `dict` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\dict_value_missing_1.py'
    à l'endroit indiqué.
    
       1: a = {1:2, 3}
                     ^

    Il semble que l'erreur se soit produite lorsque vous écriviez un `dict` Python.
    Vous avez peut-être écrit une clé de `dict` sans écrire la valeur correspondante.
    

(105) Value missing in dict - 2
-------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\dict_value_missing_2.py", line 2
        a = {1:2, 3:}
                    ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié d'écrire une valeur pour un `dict` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\dict_value_missing_2.py'
    à l'endroit indiqué.
    
       2: a = {1:2, 3:}
                      ^

    Il semble que l'erreur se soit produite alors que vous écriviez un `dict` Python.
    Vous avez peut-être oublié d'écrire une valeur après les deux points.
    

(106) Value missing in dict - 3
-------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\dict_value_missing_3.py", line 3
        a = {1:2, 3, 4:5}
                   ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié d'écrire une valeur pour un `dict` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\dict_value_missing_3.py'
    à l'endroit indiqué.
    
       3: a = {1:2, 3, 4:5}
                     ^

    Il semble que l'erreur se soit produite lorsque vous écriviez un `dict` Python.
    Vous avez peut-être écrit une clé de `dict` sans écrire la valeur correspondante.
    

(107) Value missing in dict - 4
-------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\dict_value_missing_4.py", line 4
        a = {1:2, 3:, 4:5}
                    ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié d'écrire une valeur pour un `dict` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\dict_value_missing_4.py'
    à l'endroit indiqué.
    
       4: a = {1:2, 3:, 4:5}
                      ^

    Il semble que l'erreur se soit produite alors que vous écriviez un `dict` Python.
    Vous avez peut-être oublié d'écrire une valeur après les deux points.
    

(108) Different operators in a row
----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\different_operators_in_a_row.py", line 1
        3 */ 4
           ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\different_operators_in_a_row.py'
    à l'endroit indiqué.
    
       1: 3 */ 4
            ^^

    Vous ne pouvez pas avoir ces deux opérateurs, `*` et `/`,
    qui se suivent. Peut-être avez-vous écrit l’un d’eux par erreur
    ou vous avez oublié d’écrire quelque chose entre les deux.
    

(109) Dot followed by parenthesis
---------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\dot_before_paren.py", line 3
        print(len.('hello'))
                  ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\dot_before_paren.py'
    à l'endroit indiqué.
    
       3: print(len.('hello'))
                    ^

    Vous ne pouvez pas avoir un point `.` suivi de `(`.
    Peut-être que vous devez remplacer le point par une virgule.
    

(110) Extra token
-----------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\duplicate_token.py", line 1
        print(1 , , 2)
                  ^
    SyntaxError: invalid syntax
    
        Avez-vous écrit `,` deux fois par erreur ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\duplicate_token.py'
    à l'endroit indiqué.
    
       1: print(1 , , 2)
                    ^

    Je suppose que vous avez écrit `,` deux fois de suite par erreur.
    Si c’est le cas, vous devez supprimer le second.
    

(111) elif with no matching if
------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\elif_not_matching_if.py", line 3
        elif True:
        ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\elif_not_matching_if.py'
    à l'endroit indiqué.
    
       3:    elif True:
             ^^^^

    Le mot clé `elif` ne commence pas un bloc de code qui correspond à un bloc
    un bloc `if`, peut-être parce que `elif` n'est pas indenté correctement.
    

(112) else with no matching statement
-------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\else_no_matching_statement.py", line 3
        else:
        ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\else_no_matching_statement.py'
    à l'endroit indiqué.
    
       3:    else:
             ^^^^

    Le mot-clé `else` ne commence pas un bloc de code qui correspond à
    un bloc de code valide, peut-être parce que `else` n'est pas indenté correctement.
    

(113) Write elif, not else if
-----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\else_if_instead_of_elif.py", line 5
        else if True:
             ^
    SyntaxError: invalid syntax
    
        Peut-être que vous vouliez plutôt `elif`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\else_if_instead_of_elif.py'
    à l'endroit indiqué.
    
       5: else if True:
          ^^^^-^^

    Vous avez écrit `else if`
    au lieu d'utiliser le mot-clé `elif`.
    
    

(114) Write elif, not elseif
----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\elseif_instead_of_elif.py", line 5
        elseif True:
               ^
    SyntaxError: invalid syntax
    
        Peut-être que vous vouliez plutôt `elif`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\elseif_instead_of_elif.py'
    à l'endroit indiqué.
    
       5: elseif True:
          ^^^^^^

    Vous avez écrit `elseif`
    au lieu d'utiliser le mot-clé `elif`.
    
    

(115) EOL while scanning string literal
---------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\eol_string_literal.py", line 3
        alphabet = 'abc
                       ^
    SyntaxError: EOL while scanning string literal
    
        Avez-vous oublié d’ajouter un guillemet ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\eol_string_literal.py'
    à l'endroit indiqué.
    
       3: alphabet = 'abc
                      ^^^

    Vous aviez commencé à écrire une chaîne de caractères
    avec un guillemet simple ou double, mais n'avez jamais
    terminé la chaîne avec un autre guillemet sur cette ligne.
    

(116) Used equal sign instead of colon
--------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\equal_sign_instead_of_colon.py", line 4
        ages = {'Alice'=22, 'Bob'=24}
                       ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\equal_sign_instead_of_colon.py'
    à l'endroit indiqué.
    
       4: ages = {'Alice'=22, 'Bob'=24}
                         ^

    Il est possible que vous ayez utilisé un signe d'égalité `=` au lieu de deux points `:`
    pour attribuer des valeurs à une clé d'un dictionnaire
    avant ou exactement à la position indiquée par ^.
    

(117) Parens around multiple exceptions
---------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\except_multiple_exceptions.py", line 3
        except NameError, ValueError as err:
                        ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié d’ajouter des parenthèses ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\except_multiple_exceptions.py'
    à l'endroit indiqué.
    
       3: except NameError, ValueError as err:
                          ^

    Je suppose que vous vouliez utiliser un énoncé `except`
    avec plusieurs types d’exception. Si c’est le cas, vous devez
    les entourer de parenthèses.
    

(118) Extra token
-----------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\extra_token.py", line 1
        print(1 / 2) ==
                       ^
    SyntaxError: invalid syntax
    
        Avez-vous écrit `==` par erreur ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\extra_token.py'
    à l'endroit indiqué.
    
       1: print(1 / 2) ==
                       ^^

    Je suppose que vous avez écrit `==` par erreur.
    Écrire simplement `print(1 / 2)` semble corriger l’erreur.
    

(119) Binary f-string not allowed
---------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\f_string_binary.py", line 1
        greet = bf"Hello {name}"
                  ^
    SyntaxError: invalid syntax
    
        `bf` est un préfixe de chaîne illégal.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\f_string_binary.py'
    à l'endroit indiqué.
    
       1: greet = bf"Hello {name}"
                    ^^^^^^^^^^^^^^

    Je devine que vous vouliez une chaîne de caractères formatés (f-string) binaire;
    ceci n’est pas permis.
    

(120) f-string: closing } not allowed
-------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\f_string_curly_not_allowed.py", line 1
        f"ab}"
              ^
    SyntaxError: f-string: single '}' is not allowed
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\f_string_curly_not_allowed.py'
    à l'endroit indiqué.
    
       1: f"ab}"
          ^^^^^^

    Vous avez écrit une chaîne f-string qui contient un `}` non apparié.
    Si vous voulez imprimer un seul `}`, vous devez écrire `}}` dans la chaîne de caractères ;
    sinon, vous devez ajouter un `{` d'ouverture.
    

(121) f-string: missing closing }
---------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\f_string_expected_curly.py", line 1
        f"{ab"
              ^
    SyntaxError: f-string: expecting '}'
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\f_string_expected_curly.py'
    à l'endroit indiqué.
    
       1: f"{ab"
          ^^^^^^

    Vous avez écrit une chaîne f-string qui contient un `{` non apparié.
    Si vous voulez imprimer un seul `{`, vous devez écrire `{{` dans la chaîne f-string ;
    sinon, vous devez ajouter un `}` de fermeture.
    

(122) f-string: unterminated string
-----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\f_string_unterminated.py", line 4
        print(f"Bob is {age['Bob]} years old.")
                                              ^
    SyntaxError: f-string: unterminated string
    
        Avez-vous oublié d’ajouter un guillemet ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\f_string_unterminated.py'
    à l'endroit indiqué.
    
       4: print(f"Bob is {age['Bob]} years old.")
                                                ^

    À l'intérieur de la chaîne `f"Bob is {age['Bob]} years old."`, qui est une chaîne de caractères préfixée de la lettre f,
    vous avez une autre chaîne de caractère qui débute soit avec un apostrophe (')
    ou des guillemets ("), mais n'est pas terminé par un autre caractère semblable.
    

(123) f-string with backslash
-----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\f_string_with_backslash.py", line 2
        print(f"{'\n'.join(names)}")
                                   ^
    SyntaxError: f-string expression part cannot include a backslash
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\f_string_with_backslash.py'
    à l'endroit indiqué.
    
       2: print(f"{'\n'.join(names)}")
                                     ^

    Vous avez écrit une chaîne de caractères formatés (f-string) dont le contenu `{...}`
    comprend une barre oblique inverse; ce n’est pas permis.
    Peut-être pouvez-vous remplacer la partie qui contient une barre oblique inverse par
    une variable. Par exemple, supposons que vous avez une chaîne comme suit :
    
        f"{... 'bonjour\n'...}"
    
    vous pourriez écrire ceci comme
    
        bonjour = 'bonjour\n'
        f"{... bonjour ...}"
    

(124) Missing terms in for statement
------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\for_missing_terms.py", line 1
        for:
           ^
    SyntaxError: invalid syntax
    
        Une boucle `for` doit avoir plus de termes.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\for_missing_terms.py'
    à l'endroit indiqué.
    
       1: for:
             ^

    Une boucle `for` est une itération sur une séquence :
    
        for élément in séquence:
            ...
    
    

(125) Not a chance!
-------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\future_braces.py", line 1
        from __future__ import braces
        ^
    SyntaxError: not a chance
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\future_braces.py'
    à l'endroit indiqué.
    
       1: from __future__ import braces
          ^^^^

    Je soupçonne que vous avez écrit `from __future__ import braces`
    suivant une suggestion de quelqu’un d’autre. Ça ne marchera jamais.
    
    Contrairement à d’autres langages de programmation, les blocs de code Python sont définis par
    leur niveau d’indentation, et non pas en utilisant des accolades, comme `{...}`.
    

(126) Do not import * from __future__
-------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\future_import_star.py", line 1
        from __future__ import *
        ^
    SyntaxError: future feature * is not defined
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\future_import_star.py'
    à l'endroit indiqué.
    
       1: from __future__ import *
          ^^^^

    Lors de l’utilisation d’un énoncé `from __future__ import`,
    vous devez importer des noms spécifiques.
    
    Les valeurs disponibles sont `nested_scopes,
     generators,
     division,
     absolute_import,
     with_statement,
     print_function,
     unicode_literals,
     barry_as_FLUFL,
     generator_stop,
     annotations`.
    

(127) __future__ at beginning
-----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\future_must_be_first.py", line 3
        from __future__ import generators
        ^
    SyntaxError: from __future__ imports must occur at the beginning of the file
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\future_must_be_first.py'
    à l'endroit indiqué.
    
       3:     from __future__ import generators
              ^^^^

    Une instruction `from __future__ import` change la façon dont Python
    interprète le code dans un fichier.
    Une telle instruction doit apparaître au début du fichier.

(128) Typo in __future__
------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\future_typo.py", line 1
        from __future__ import divisio
        ^
    SyntaxError: future feature divisio is not defined
    
        Vouliez-vous dire `division` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\future_typo.py'
    à l'endroit indiqué.
    
       1: from __future__ import divisio
          ^^^^

    Au lieu de `divisio`, peut-être que vous vouliez plutôt importer `division`.
    

(129) Unknown feature in __future__
-----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\future_unknown.py", line 1
        from __future__ import something
        ^
    SyntaxError: future feature something is not defined
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\future_unknown.py'
    à l'endroit indiqué.
    
       1: from __future__ import something
          ^^^^

    `something` n’est pas un attribut valide du module `__future__`.
    
    Les valeurs disponibles sont `nested_scopes,
     generators,
     division,
     absolute_import,
     with_statement,
     print_function,
     unicode_literals,
     barry_as_FLUFL,
     generator_stop,
     annotations`.
    

(130) Parenthesis around generator expression
---------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\generator_expression_parens.py", line 6
        f(x for x in L, 1)
          ^
    SyntaxError: Generator expression must be parenthesized
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\generator_expression_parens.py'
    à l'endroit indiqué.
    
       6: f(x for x in L, 1)
            ^

    Vous utilisez une expression de générateur, quelque chose de la forme
    
        x for x in objet
    
    Vous devez ajouter des parenthèses qui entourent cette expression.
    

(131) Space between names
-------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\hyphen_instead_of_underscore.py", line 4
        a-b = 2
        ^
    SyntaxError: cannot assign to operator
    
        Vouliez-vous dire `a_b` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\hyphen_instead_of_underscore.py'
    à l'endroit indiqué.
    
       4: a-b = 2
          ^

    Vous avez écrit une expression qui inclut des opérations mathématiques
    du côté gauche du signe d'égalité; ceci devrait être
    utilisé uniquement pour attribuer une valeur à une variable.
    Peut-être que vous vouliez plutôt écrire `a_b` au lieu de `a-b`.
    

(132) Missing condition in if statement
---------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\if_missing_condition.py", line 1
        if:
          ^
    SyntaxError: invalid syntax
    
        Vous avez oublié d’ajouter une condition.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\if_missing_condition.py'
    à l'endroit indiqué.
    
       1: if:
            ^

    Un énoncé `if` doit inclure une condition :
    
        if condition:
            ...
    
    

(133) use j instead of i
------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\imaginary_i.py", line 3
        a = 3.0i
               ^
    SyntaxError: invalid syntax
    
        Vouliez-vous dire `3.0j` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\imaginary_i.py'
    à l'endroit indiqué.
    
       3: a = 3.0i
                 ^

    Peut-être pensiez-vous que `i` pouvait être utilisé pour représenter
    la racine carrée de `-1`. Dans Python, le symbole utilisé pour ceci est `j`
    et la partie imaginaire d'un nombre complexe a la forme `nombre`
    suivie immédiatement par `j` sans aucun espace entre les deux.
    Peut-être que vous vouliez écrire `3.0j`.
    

(134) Import inversion: import X from Y
---------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\import_from.py", line 3
        import pen from turtle
                   ^
    SyntaxError: invalid syntax
    
        Vouliez-vous dire `from turtle import pen` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\import_from.py'
    à l'endroit indiqué.
    
       3: import pen from turtle
          ^^^^^^     ^^^^

    Vous avez écrit quelque chose comme
    
        import pen from turtle
    au lieu de
    
        from turtle import pen
    
    

(135) IndentationError: expected an indented block
--------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\indentation_error_1.py", line 4
        pass
        ^
    IndentationError: expected an indented block
    
    Une exception de type `IndentationError` se produit lorsqu'une ligne de code
    n'est pas indentée (c'est-à-dire alignée verticalement avec les autres lignes)
    de la façon attendue.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\indentation_error_1.py'
    à l'endroit indiqué.
    
       4: pass
          ^^^^

    La ligne `4` identifiée ci-dessus était censée commencer un nouveau bloc indenté.
    

(136) IndentationError: unexpected indent
-----------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\indentation_error_2.py", line 4
        pass
        ^
    IndentationError: unexpected indent
    
    Une exception de type `IndentationError` se produit lorsqu'une ligne de code
    n'est pas indentée (c'est-à-dire alignée verticalement avec les autres lignes)
    de la façon attendue.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\indentation_error_2.py'
    à l'endroit indiqué.
    
       4:       pass
                ^^^^

    La ligne `4` indiquée ci-dessus est plus indentée que prévu.
    

(137) IndentationError: unindent does not match ...
---------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\indentation_error_3.py", line 5
        pass
            ^
    IndentationError: unindent does not match any outer indentation level
    
    Une exception de type `IndentationError` se produit lorsqu'une ligne de code
    n'est pas indentée (c'est-à-dire alignée verticalement avec les autres lignes)
    de la façon attendue.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\indentation_error_3.py'
    à l'endroit indiqué.
    
       5:     pass
              ^^^^

    La ligne `5` identifiée ci-dessus est moins indentée que prévu.
    

(138) IndentationError: missing continuation line
-------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\indentation_error_4.py", line 6
        "c"
        ^
    IndentationError: unexpected indent
    
    Une exception de type `IndentationError` se produit lorsqu'une ligne de code
    n'est pas indentée (c'est-à-dire alignée verticalement avec les autres lignes)
    de la façon attendue.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\indentation_error_4.py'
    à l'endroit indiqué.
    
       6:          "c"
                   ^^^

    La ligne `6` indiquée ci-dessus est plus indentée que prévu.
    
    Toutefois, la ligne 6, qui est identifiée comme ayant un problème,
    se compose d’une seule chaîne, ce qui est également le cas
    pour la ligne précédente.
    Peut-être que vous vouliez inclure un caractère de continuation, '\',
    à la fin de la ligne 5.
    

(139) Forgot 'o' for octal
--------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\integer_with_leading_zero_1.py", line 1
        x = 01
             ^
    SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
    
        Vouliez-vous dire `0o1` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\integer_with_leading_zero_1.py'
    à l'endroit indiqué.
    
       1: x = 01
               ^

    Peut-être que vous vouliez écrire le nombre octal `0o1`
    et oublié la lettre 'o', ou peut-être vous vouliez écrire
    un entier décimal et ne saviez pas qu’il ne pouvait pas commencer par des zéros.
    

(140) Integer with leading zeros
--------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\integer_with_leading_zero_2.py", line 1
        x = 000_123_456
                      ^
    SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
    
        Vouliez-vous dire `123_456` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\integer_with_leading_zero_2.py'
    à l'endroit indiqué.
    
       1: x = 000_123_456
                 ^^^^^^^^

    Peut-être que vous vouliez écrire l'entier décimal `123_456`
    et ne saviez pas qu’il ne pouvait pas commencer par des zéros.
    

(141) Invalid character in identifier
-------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\invalid_character_in_identifier.py", line 6
        🤖 = 'Reeborg'
        ^
    SyntaxError: invalid character '🤖' (U+1F916)
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\invalid_character_in_identifier.py'
    à l'endroit indiqué.
    
       6: 🤖 = 'Reeborg'
          ^

    Python indique que vous avez utilisé le caractère unicode `🤖`
    ce qui n’est pas permis.
    

(142) Invalid decimal literal - 1
---------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\invalid_decimal_literal1.py", line 1
        a = 1e
             ^
    SyntaxError: invalid syntax
    
        Peut-être avez-vous oublié un opérateur de multiplication, `1 * e`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\invalid_decimal_literal1.py'
    à l'endroit indiqué.
    
       1: a = 1e
               ^

    Les noms valides ne peuvent pas commencer par un chiffre.
    Peut-être avez-vous oublié un opérateur de multiplication, `1 * e`.
    
    

(143) Invalid encoding
----------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\invalid_encoding.py", line 2, in <module>
        compile(source, filename="example.py", mode="exec")
      File "TESTS:\example.py", line 0
    SyntaxError: encoding problem: utf8 with BOM
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\example.py'
    .
    
    L'encodage du fichier n'était pas valide.
    

(144) Invalid hexadecimal number
--------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\invalid_hexadecimal.py", line 3
        a = 0x123g4
                 ^
    SyntaxError: invalid syntax
    
        Avez-vous fait une erreur en écrivant un entier hexadécimal ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\invalid_hexadecimal.py'
    à l'endroit indiqué.
    
       3: a = 0x123g4
                   ^^

    On dirait que vous avez utilisé un caractère invalide ('g') dans un nombre hexadecimal.
    
    Les nombres hexadécimaux sont des entiers en base 16 qui utilisent les symboles `0` à `9`
    pour représenter les valeurs 0 à 9, et les lettres `a` à `f` (ou `A` à `F`)
    pour représenter les valeurs 10 à 15.
    Dans Python, les nombres hexadécimaux commencent par `0x` ou `0X`,
    suivi des caractères utilisés pour représenter la valeur du nombre.
    

(145) Valid names cannot begin with a number
--------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\invalid_identifier.py", line 3
        36abc = 3
          ^
    SyntaxError: invalid syntax
    
        Les noms valides ne peuvent pas commencer par un chiffre.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\invalid_identifier.py'
    à l'endroit indiqué.
    
       3: 36abc = 3
            ^^^

    Les noms valides ne peuvent pas commencer par un chiffre.
    

(146) Valid names cannot begin with a number - 2
------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\invalid_identifier_2.py", line 3
        tau = 2pi
               ^
    SyntaxError: invalid syntax
    
        Peut-être avez-vous oublié un opérateur de multiplication, `2 * pi`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\invalid_identifier_2.py'
    à l'endroit indiqué.
    
       3: tau = 2pi
                 ^^

    Les noms valides ne peuvent pas commencer par un chiffre.
    Peut-être avez-vous oublié un opérateur de multiplication, `2 * pi`.
    
    

(147) Valid names cannot begin with a number - 3
------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\invalid_identifier_3.py", line 1
        3job  # could be entered in a repl
          ^
    SyntaxError: invalid syntax
    
        Peut-être avez-vous oublié un opérateur de multiplication, `3 * job`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\invalid_identifier_3.py'
    à l'endroit indiqué.
    
       1: 3job  # could be entered in a repl
            ^^

    Les noms valides ne peuvent pas commencer par un chiffre.
    Peut-être avez-vous oublié un opérateur de multiplication, `3 * job`.
    
    [N.B.: `3j * ob` serait également valide
    puisque `3j` est un nombre complexe.]
    

(148) Valid names cannot begin with a number - 4
------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\invalid_identifier_4.py", line 1
        3job = 1
          ^
    SyntaxError: invalid syntax
    
        Les noms valides ne peuvent pas commencer par un chiffre.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\invalid_identifier_4.py'
    à l'endroit indiqué.
    
       1: 3job = 1
            ^^

    Les noms valides ne peuvent pas commencer par un chiffre.
    

(149) Valid names cannot begin with a number - 5
------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\invalid_identifier_5.py", line 1
        print(42java)
                 ^
    SyntaxError: invalid syntax
    
        Peut-être avez-vous oublié un opérateur de multiplication, `42 * java`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\invalid_identifier_5.py'
    à l'endroit indiqué.
    
       1: print(42java)
                   ^^^

    Les noms valides ne peuvent pas commencer par un chiffre.
    Peut-être avez-vous oublié un opérateur de multiplication, `42 * java`.
    
    [N.B.: `42j * ava` serait également valide
    puisque `42j` est un nombre complexe.]
    

(150) Keyword can't be an expression
------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\invalid_keyword_argument.py", line 7
        a = dict('key'=1)
                 ^
    SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\invalid_keyword_argument.py'
    à l'endroit indiqué.
    
       7: a = dict('key'=1)
                   ^^^^^

    Vous avez probablement appelé une fonction avec un argument :
    
        une_fonction (invalide=quelque_chose)
    
    où `invalide` n'est pas un nom de variable valide dans Python
    soit parce qu'il commence par un chiffre, soit qu'il est une chaîne,
    ou qu'il contient un point, etc.
    

(151) Named argument can't be a Python keyword
----------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\invalid_keyword_argument_2.py", line 7
        a = dict(True=1)
                 ^
    SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
    
        Vous ne pouvez pas attribuer une valeur à `True`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\invalid_keyword_argument_2.py'
    à l'endroit indiqué.
    
       7: a = dict(True=1)
                   ^^^^

    Vous avez probablement invoqué une fonction en utilisant le mot-clé Python `True` comme argument :
    
        une_fonction(True=quelque_chose)
    
    ce que Python a interprété comme une tentative d'attribuer une valeur à un mot-clé Python.
    
    Vous ne pouvez pas attribuer une valeur à `True`.
    

(152) Invalid octal number
--------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\invalid_octal.py", line 3
        b = 0O1876
               ^
    SyntaxError: invalid digit '8' in octal literal
    
        Avez-vous fait une erreur en écrivant un entier octal ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\invalid_octal.py'
    à l'endroit indiqué.
    
       3: b = 0O1876
                 ^^^

    On dirait que vous avez utilisé un caractère invalide ('8') dans un nombre octal.
    
    Les nombres octaux sont des entiers de base 8 qui n’utilisent que les symboles `0` à `7`
    pour représenter les valeurs.
    Dans Python, les nombres octaux commencent par `0o` ou `0O`,
    (le chiffre zéro suivi de la lettre `o`)
    suivi des caractères utilisés pour représenter la valeur de cet entier.
    

(153) Inverted operators 1
--------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\inverted_operators.py", line 1
        a =< 3
           ^
    SyntaxError: invalid syntax
    
        Avez-vous écrit des opérateurs dans un mauvais ordre ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\inverted_operators.py'
    à l'endroit indiqué.
    
       1: a =< 3
            ^^

    On dirait que vous avez écrit deux opérateurs (`=` et `<`)
    dans le mauvais ordre: `=<` au lieu de `<=`.
    

(154) Inverted operators 2
--------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\inverted_operators_2.py", line 1
        a =<* 3
           ^
    SyntaxError: invalid syntax
    
        Avez-vous écrit des opérateurs dans un mauvais ordre ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\inverted_operators_2.py'
    à l'endroit indiqué.
    
       1: a =<* 3
            ^^

    On dirait que vous avez écrit deux opérateurs (`=` et `<`)
    dans le mauvais ordre: `=<` au lieu de `<=`.
    
    Toutefois, un tel changement ne corrigerait pas
    toutes les erreurs de syntaxe dans le code que vous avez écrit.
    

(155) Iteration variable unpacking in comprehension
---------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\iteration_unpacking_in_comprehension.py", line 1
        [*x for x in xs]
         ^
    SyntaxError: iterable unpacking cannot be used in comprehension
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\iteration_unpacking_in_comprehension.py'
    à l'endroit indiqué.
    
       1: [*x for x in xs]
           ^

    Vous ne pouvez pas utiliser l'opérateur `*` pour déballer la variable d'itération
    dans une compréhension.
    
    L'énoncé suivant ne comporte pas d'erreur de syntaxe :
    
        [x for x in xs]
    

(156) Keyword arg only once in function call
--------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\keyword_arg_repeated.py", line 4
        f(ad=1, ad=2)
                ^
    SyntaxError: keyword argument repeated: ad
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\keyword_arg_repeated.py'
    à l'endroit indiqué.
    
       4: f(ad=1, ad=2)
                  ^^

    Vous avez invoqué une fonction en répétant le même argument nommé (`ad`).
    Chaque argument de ce type ne peut apparaître qu'une seule fois.
    

(157) Keyword as attribute
--------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\keyword_as_attribute.py", line 12
        a.pass = 2
          ^
    SyntaxError: invalid syntax
    
        `pass` ne peut pas être utilisé comme n attribut.
        
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\keyword_as_attribute.py'
    à l'endroit indiqué.
    
       12: a.pass = 2
             ^^^^

    Vous avez tenté d'utiliser le mot clé Python `pass` comme attribut.
    Ceci n’est pas permis.
    
    

(158) lambda with parentheses around arguments
----------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\lambda_with_parens.py", line 2
        x = lambda (a, b): a + b
                   ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\lambda_with_parens.py'
    à l'endroit indiqué.
    
       2: x = lambda (a, b): a + b
                     ^

    `lambda` ne permet pas de parenthèses autour de ses arguments.
    Cela était permis dans Python 2, mais il ne l'est plus dans Python 3.
    

(159) lambda with tuple as argument
-----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\lambda_with_tuple_argument.py", line 2
        x = lambda a, (b, c): a + b + b
                      ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\lambda_with_tuple_argument.py'
    à l'endroit indiqué.
    
       2: x = lambda a, (b, c): a + b + b
                        ^

    Vous ne pouvez pas avoir des tuples explicites comme arguments.
    Attribuez n’importe quel tuple à un paramètre et dépaquetez-le
    dans le corps de la fonction.
    

(160) Assign to literal in for loop
-----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\literal_in_for_loop.py", line 1
        for "char" in "word":
            ^
    SyntaxError: cannot assign to literal
    
        Vous ne pouvez assigner des objets qu’à des identifiants (noms de variables).
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\literal_in_for_loop.py'
    à l'endroit indiqué.
    
       1: for "char" in "word":
              ^^^^^^

    Une boucle for doit avoir la forme:
    
        for ... in séquence:
    
    où `...` doit contenir seulement des identifiants (noms de variables)
    et non pas des littéraux comme `"char"`.
    

(161) IndentationError/SyntaxError depending on version
-------------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\missing_code_block.py", line 4
    IndentationError: expected an indented block
    
    Une exception de type `IndentationError` se produit lorsqu'une ligne de code
    n'est pas indentée (c'est-à-dire alignée verticalement avec les autres lignes)
    de la façon attendue.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\missing_code_block.py'
    à l'endroit indiqué.
    
       3: for i in range(10):
    -->4: 
                            ^

    La ligne `4` identifiée ci-dessus était censée commencer un nouveau bloc indenté.
    

(162) IndentationError/SyntaxError depending on version - 2
-----------------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\missing_code_block_2.py", line 6
    IndentationError: expected an indented block
    
    Une exception de type `IndentationError` se produit lorsqu'une ligne de code
    n'est pas indentée (c'est-à-dire alignée verticalement avec les autres lignes)
    de la façon attendue.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\missing_code_block_2.py'
    .
    
       3: for i in "test":
       4: 

    La ligne `6` identifiée ci-dessus était censée commencer un nouveau bloc indenté.
    

(163) Missing colon - if
------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\missing_colon_if.py", line 3
        if True
               ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié d’ajouter les deux points `:` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\missing_colon_if.py'
    à l'endroit indiqué.
    
       3: if True
                 ^

    Vous avez écrit un énoncé débutant avec
    `if` mais vous avez oublié d’ajouter deux points `:` à la fin.
    
    

(164) Missing colon - while
---------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\missing_colon_while.py", line 3
        while True  # a comment
                    ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié d’ajouter les deux points `:` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\missing_colon_while.py'
    à l'endroit indiqué.
    
       3: while True  # a comment
                    ^

    Vous vouliez débuter une boucle `while`
    mais vous avez oublié d’ajouter deux points `:` à la fin.
    
    

(165) Missing comma in a dict
-----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\missing_comma_in_dict.py", line 5
        'c': 3,
        ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié une virgule ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\missing_comma_in_dict.py'
    à l'endroit indiqué.
    
       3: a = {'a': 1,
    -->4:      'b': 2
                    ^-->
    -->5:      'c': 3,
               ^^^
       6: }

    Python indique que l’erreur est causée par `'c'` écrit tout juste après `2`.
    Il est possible que vous ayez oublié une virgule entre les éléments d'un ensemble ou d'un dict
    à la position indiquée par ^.
    Vous vouliez peut-être dire
    
        a = {'a': 1,
             'b': 2, 
                   ^
             'c': 3,
        }
    
    

(166) Missing comma between strings in a dict
---------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\missing_comma_in_dict_2.py", line 4
        'c': '3',
           ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié une virgule ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\missing_comma_in_dict_2.py'
    à l'endroit indiqué.
    
       2: a = {'a': '1',
       3:      'b': '2'
    -->4:      'c': '3',
                  ^
       5: }

    Je crois que vous avez oublié une virgule entre deux chaînes de caractères
    lors de la définition d’un dictionnaire.
    
    ```
    a = {'a': '1',
         'b': '2',
                 ^
         'c': '3',
    }
    ```

(167) Missing comma in a list
-----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\missing_comma_in_list.py", line 3
        a = [1, 2  3]
                   ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié quelque chose entre `2` et `3` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\missing_comma_in_list.py'
    à l'endroit indiqué.
    
       3: a = [1, 2  3]
                  ^^^^

    Python indique que l’erreur est causée par `3` écrit tout juste après `2`.
    Il est possible que vous ayez oublié une virgule entre les éléments d'une liste
    à la position indiquée par ^.
    Peut-être que vous vouliez insérer un opérateur comme `+, -, *`
    entre `2` et `3`.
    Les lignes de code suivantes ne causeraient pas des `SyntaxError :
    
        a = [1, 2,   3]
        a = [1, 2 +   3]
        a = [1, 2 -   3]
        a = [1, 2 *   3]
    Remarque : ce ne sont là que quelques-uns des choix possibles et
    certains d’entre eux pourraient soulever d’autres types d’exceptions.
    

(168) Missing comma in a set
----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\missing_comma_in_set.py", line 3
        a = {1, 2  3}
                   ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié quelque chose entre `2` et `3` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\missing_comma_in_set.py'
    à l'endroit indiqué.
    
       3: a = {1, 2  3}
                  ^^^^

    Python indique que l’erreur est causée par `3` écrit tout juste après `2`.
    Il est possible que vous ayez oublié une virgule entre les éléments d'un ensemble ou d'un dict
    à la position indiquée par ^.
    Peut-être que vous vouliez insérer un opérateur comme `+, -, *`
    entre `2` et `3`.
    Les lignes de code suivantes ne causeraient pas des `SyntaxError :
    
        a = {1, 2,   3}
        a = {1, 2 +   3}
        a = {1, 2 -   3}
        a = {1, 2 *   3}
    Remarque : ce ne sont là que quelques-uns des choix possibles et
    certains d’entre eux pourraient soulever d’autres types d’exceptions.
    

(169) Missing comma in a tuple
------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\missing_comma_in_tuple.py", line 3
        a = (1, 2  3)
                   ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié quelque chose entre `2` et `3` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\missing_comma_in_tuple.py'
    à l'endroit indiqué.
    
       3: a = (1, 2  3)
                  ^^^^

    Python indique que l’erreur est causée par `3` écrit tout juste après `2`.
    Il est possible que vous ayez oublié une virgule entre les éléments d'un tuple,
    ou entre les arguments d'une fonction,
    à la position indiquée par ^.
    Peut-être que vous vouliez insérer un opérateur comme `+, -, *`
    entre `2` et `3`.
    Les lignes de code suivantes ne causeraient pas des `SyntaxError :
    
        a = (1, 2,   3)
        a = (1, 2 +   3)
        a = (1, 2 -   3)
        a = (1, 2 *   3)
    Remarque : ce ne sont là que quelques-uns des choix possibles et
    certains d’entre eux pourraient soulever d’autres types d’exceptions.
    

(170) Missing parenthesis for range
-----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\missing_parens_for_range.py", line 1
        for i in range 3:
                       ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié d’ajouter des parenthèses ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\missing_parens_for_range.py'
    à l'endroit indiqué.
    
       1: for i in range 3:
                         ^

    Il semble que vous avez oublié d’utiliser des parenthèses
    avec `range`. Peut-être que vous vouliez dire:
    
        for i in range( 3):
    
    

(171) Misspelled Python keyword
-------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\misspelled_keyword.py", line 2
        is i in range(3):
        ^
    SyntaxError: invalid syntax
    
        Vouliez-vous dire `if i in range(3):` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\misspelled_keyword.py'
    à l'endroit indiqué.
    
       2: is i in range(3):
          ^^

    Peut-être que vous vouliez écrire `if` et que vous avez fait une faute.
    Si c'est le cas, la ligne correcte pourrait être `if i in range(3):`.
    

(172) Name is global and nonlocal
---------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\name_is_global_and_nonlocal.py", line 7
        global xy
        ^
    SyntaxError: name 'xy' is nonlocal and global
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\name_is_global_and_nonlocal.py'
    à l'endroit indiqué.
    
       7:     global xy
              ^^^^^^

    Vous avez utilisé `xy` comme étant une variable non locale et globale.
    Une variable peut être d'un seul type à la fois: soit globale, soit non locale, ou soit locale.
    

(173) Name is parameter and nonlocal
------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\name_is_param_and_nonlocal.py", line 5
        nonlocal x
        ^
    SyntaxError: name 'x' is parameter and nonlocal
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\name_is_param_and_nonlocal.py'
    à l'endroit indiqué.
    
       5:     nonlocal x
              ^^^^^^^^

    Vous avez utilisé `x` comme paramètre pour une fonction
    avant de la déclarer également comme une variable non locale :
    `x` ne peut pas être les deux en même temps.
    

(174) nonlocal variable not found
---------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\no_binding_for_nonlocal.py", line 5
        nonlocal ab
        ^
    SyntaxError: no binding for nonlocal 'ab' found
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\no_binding_for_nonlocal.py'
    à l'endroit indiqué.
    
       5:     nonlocal ab
              ^^^^^^^^

    Vous avez déclaré la variable `ab` comme non locale
    mais elle n'existe pas ailleurs.
    

(175) nonlocal variable not found at module level
-------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\nonlocal_at_module.py", line 4
        nonlocal cd
        ^
    SyntaxError: nonlocal declaration not allowed at module level
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\nonlocal_at_module.py'
    à l'endroit indiqué.
    
       4: nonlocal cd
          ^^^^^^^^

    Vous avez utilisé le mot clé nonlocal au niveau d'un module.
    Le mot clé nonlocal fait référence à une variable à l'intérieur d'une fonction
    qui a une valeur attribuée à l'extérieur de cette fonction.

(176) Same operator twice in a row
----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\operator_twice_in_a_row.py", line 1
        4****5
           ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\operator_twice_in_a_row.py'
    à l'endroit indiqué.
    
       1: 4****5
           ^^^^

    Vous ne pouvez pas écrire le même opérateur, `**`, deux fois de suite.
    Peut-être avez-vous écrit l’un d’eux par erreur
    ou vous avez oublié d’écrire quelque chose entre les deux.
    

(177) Using pip from interpreter
--------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\pip_install_1.py", line 2
        pip install friendly
            ^
    SyntaxError: invalid syntax
    
        Pip ne peut pas être utilisé dans un interprète Python.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\pip_install_1.py'
    à l'endroit indiqué.
    
       2: pip install friendly
              ^^^^^^^

    Il semble que vous essayez d’utiliser pip pour installer un module.
    `pip` est une commande qui doit être invoquée dans un terminal,
    pas dans un interprète Python.
    

(178) Using pip from interpreter 2
----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\pip_install_2.py", line 2
        python -m pip install friendly
                  ^
    SyntaxError: invalid syntax
    
        Pip ne peut pas être utilisé dans un interprète Python.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\pip_install_2.py'
    à l'endroit indiqué.
    
       2: python -m pip install friendly
                    ^^^

    Il semble que vous essayez d’utiliser pip pour installer un module.
    `pip` est une commande qui doit être invoquée dans un terminal,
    pas dans un interprète Python.
    

(179) print is a function
-------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\print_is_a_function.py", line 2
        print 'hello'
              ^
    SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello')?
    
        Vouliez-vous dire `print('hello')` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\print_is_a_function.py'
    à l'endroit indiqué.
    
       2: print 'hello'
                ^^^^^^^

    Peut-être que vous avez besoin d'écrire
    
         print('hello')
    
    Dans l'ancienne version de Python, `print` était un mot clé.
    Maintenant, `print` est une fonction; vous devez utiliser des parenthèses pour l'invoquer.
    

(180) print is a function 2
---------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\print_is_a_function_2.py", line 2
        print len('hello')
              ^
    SyntaxError: invalid syntax
    
        Vouliez-vous dire `print(len('hello'))` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\print_is_a_function_2.py'
    à l'endroit indiqué.
    
       2: print len('hello')
                ^^^

    Peut-être que vous avez besoin d'écrire
    
         print(len('hello'))
    
    Dans l'ancienne version de Python, `print` était un mot clé.
    Maintenant, `print` est une fonction; vous devez utiliser des parenthèses pour l'invoquer.
    

(181) print is a function 3
---------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\print_is_a_function_3.py", line 1
        print """This is a very long string which results in a very long error message."""
              ^
    SyntaxError: Missing parentheses in call to 'print'. Did you mean print("""This is a very long string which results in a very long error message.""")?
    
        Vouliez-vous dire `print(...)` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\print_is_a_function_3.py'
    à l'endroit indiqué.
    
       1: print """This is a very long string which results in a very long error message."""
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Peut-être que vous avez besoin d'écrire
    
         print(...)
    
    Dans l'ancienne version de Python, `print` était un mot clé.
    Maintenant, `print` est une fonction; vous devez utiliser des parenthèses pour l'invoquer.
    

(182) print is a function 4
---------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\print_is_a_function_4.py", line 2
        print len("""This is a long string
              ^
    SyntaxError: invalid syntax
    
        Vouliez-vous dire `print(...)` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\print_is_a_function_4.py'
    à l'endroit indiqué.
    
    -->2: print len("""This is a long string
                ^^^
       3:           that spans multiple lines.""")

    Peut-être que vous avez besoin d'écrire
    
         print(...)
    
    Dans l'ancienne version de Python, `print` était un mot clé.
    Maintenant, `print` est une fonction; vous devez utiliser des parenthèses pour l'invoquer.
    

(183) print is a function 5
---------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\print_is_a_function_5.py", line 2
        print len('This is a long string that fits on a single line.')
              ^
    SyntaxError: invalid syntax
    
        Vouliez-vous dire `print(...)` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\print_is_a_function_5.py'
    à l'endroit indiqué.
    
       2: print len('This is a long string that fits on a single line.')
                ^^^

    Peut-être que vous avez besoin d'écrire
    
         print(...)
    
    Dans l'ancienne version de Python, `print` était un mot clé.
    Maintenant, `print` est une fonction; vous devez utiliser des parenthèses pour l'invoquer.
    

(184) print is a function 6
---------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\print_non_paren_non_string1.py", line 1
        print hello world!
              ^
    SyntaxError: Missing parentheses in call to 'print'. Did you mean print(hello world!)?
    
        Vouliez-vous dire `print(...)` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\print_non_paren_non_string1.py'
    à l'endroit indiqué.
    
       1: print hello world!
                ^^^^^

    Peut-être que vous avez besoin d'écrire
    
         print(...)
    
    Dans l'ancienne version de Python, `print` était un mot clé.
    Maintenant, `print` est une fonction; vous devez utiliser des parenthèses pour l'invoquer.
    Notez que les arguments de `print` doivent être séparés par des virgules.
    

(185) print is a function 7
---------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\print_non_paren_non_string2.py", line 1
        print len("hello") hello
              ^
    SyntaxError: invalid syntax
    
        Vouliez-vous dire `print(...)` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\print_non_paren_non_string2.py'
    à l'endroit indiqué.
    
       1: print len("hello") hello
                ^^^

    Peut-être que vous avez besoin d'écrire
    
         print(...)
    
    Dans l'ancienne version de Python, `print` était un mot clé.
    Maintenant, `print` est une fonction; vous devez utiliser des parenthèses pour l'invoquer.
    Notez que les arguments de `print` doivent être séparés par des virgules.
    

(186) Calling python from interpreter
-------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\python_interpreter.py", line 1
        python -i friendly
                  ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\python_interpreter.py'
    à l'endroit indiqué.
    
       1: python -i friendly
                    ^^^^^^^^

    Je suppose que vous essayez d’utiliser Python pour exécuter un programme.
    Vous devez le faire à partir d’un terminal et non d’un interprète Python.
    

(187) problem with assigning a variable to Python
-------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\python_not_interpreter.py", line 1
        python = a b
                   ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié quelque chose entre `a` et `b` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\python_not_interpreter.py'
    à l'endroit indiqué.
    
       1: python = a b
                   ^^^

    Python indique que l’erreur est causée par `b` écrit tout juste après `a`.
    Peut-être que vous vouliez insérer un opérateur comme `+; -; *; ,`
    entre `a` et `b`.
    Les lignes de code suivantes ne causeraient pas des `SyntaxError :
    
        python = a +  b
        python = a -  b
        python = a *  b
        python = a,  b
    Remarque : ce ne sont là que quelques-uns des choix possibles et
    certains d’entre eux pourraient soulever d’autres types d’exceptions.
    

(188) Quote inside a string
---------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\quote_inside_string.py", line 3
        message = 'I don't mind.'
                         ^
    SyntaxError: invalid syntax
    
        Vous avez peut-être oublié d'échapper un guillemet.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\quote_inside_string.py'
    à l'endroit indiqué.
    
       3: message = 'I don't mind.'
                           ^

    Je soupçonne que vous avez essayé d'utiliser un guillemet à l'intérieur d'une chaîne de caractères
    qui était entourée de guillemets du même type.
    Vous auriez peut-être dû échapper ce guillemet interne :
    
        message = 'I don\'t mind.'
                        ^^
    

(189) Raising multiple exceptions
---------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\raise_multiple_exceptions.py", line 2
        raise X, Y
               ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\raise_multiple_exceptions.py'
    à l'endroit indiqué.
    
       2: raise X, Y
                 ^

    Je crois que vous essayez de lever une exception en utilisant la syntaxe de Python 2.
    

(190) Cannot use return outside function
----------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\return_outside_function.py", line 3
        return
        ^
    SyntaxError: 'return' outside function
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\return_outside_function.py'
    à l'endroit indiqué.
    
       3: return
          ^^^^^^

    Vous ne pouvez utiliser un énoncé `return` qu'à l’intérieur d’une fonction ou d’une méthode.
    

(191) Semicolon instead of colon
--------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\semi_colon_instead_of_colon.py", line 1
        if True;  # A comment
               ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié d’ajouter les deux points `:` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\semi_colon_instead_of_colon.py'
    à l'endroit indiqué.
    
       1: if True;  # A comment
                 ^

    Vous avez écrit un point-virgule, `;`, au lieu des deux points `:`.
    

(192) Semicolon instead of comma - 1
------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\semi_colon_instead_of_comma_1.py", line 1
        a = [1, 2; 3]
                 ^
    SyntaxError: invalid syntax
    
        Avez-vous oublié une virgule ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\semi_colon_instead_of_comma_1.py'
    à l'endroit indiqué.
    
       1: a = [1, 2; 3]
                   ^

    Vous avez écrit un point-virgule, `;`, au lieu d'une virgule.
    

(193) Semicolon instead of commas - 2
-------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\semi_colon_instead_of_comma_2.py", line 1
        a = [1; 2; 3]
              ^
    SyntaxError: invalid syntax
    
        Vouliez-vous écrire des virgules ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\semi_colon_instead_of_comma_2.py'
    à l'endroit indiqué.
    
       1: a = [1; 2; 3]
                ^

    Vous avez écrit des points-virgules, `;`, au lieu de virgules.
    

(194) Semicolon instead of commas - 3
-------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\semi_colon_instead_of_comma_3.py", line 1
        a = [1; 2; 3];
              ^
    SyntaxError: invalid syntax
    
        Vouliez-vous écrire des virgules ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\semi_colon_instead_of_comma_3.py'
    à l'endroit indiqué.
    
       1: a = [1; 2; 3];
                ^

    Vous avez écrit des points-virgules, `;`, au lieu de virgules.
    

(195) Code block inside comprehension
-------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\should_be_comprehension.py", line 2
        for i in 1, 2, 3:
        ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\should_be_comprehension.py'
    à l'endroit indiqué.
    
       1: a = [
    -->2:     for i in 1, 2, 3:
              ^^^
       3:         i**2
       4: ]

    Vous avez peut-être écrit un énoncé au début d'un bloc de code
    destiné à faire partie d'une compréhension de liste.
    Vous ne pouvez pas avoir de blocs de code séparés à l'intérieur des compréhensions de liste.
    
    Si cette explication est incorrecte, veuillez signaler ce cas.
    

(196) Single = instead of double == with if
-------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\single_equal_with_if.py", line 3
        if i % 2 = 0:
                 ^
    SyntaxError: invalid syntax
    
        Peut-être que vous aviez besoin de `==` au lieu de `=`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\single_equal_with_if.py'
    à l'endroit indiqué.
    
       3:     if i % 2 = 0:
                       ^

    Vous avez utilisé un opérateur d’affectation `=` au lieu d’un opérateur d'égalité `==` 
    L'énoncé suivant ne contient pas d'erreur de syntaxe :
    
        if i % 2 == 0:

(197) Single = instead of double == with elif
---------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\single_equal_with_elif.py", line 5
        elif i % 2 = 0:
                   ^
    SyntaxError: invalid syntax
    
        Peut-être que vous aviez besoin de `==` au lieu de `=`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\single_equal_with_elif.py'
    à l'endroit indiqué.
    
       5:     elif i % 2 = 0:
                         ^

    Vous avez utilisé un opérateur d’affectation `=` au lieu d’un opérateur d'égalité `==` 
    L'énoncé suivant ne contient pas d'erreur de syntaxe :
    
        elif i % 2 == 0:

(198) Single = instead of double == with while
----------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\single_equal_with_while.py", line 4
        while a = 1:
                ^
    SyntaxError: invalid syntax
    
        Peut-être que vous aviez besoin de `==` ou `:=` au lieu de `=`.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\single_equal_with_while.py'
    à l'endroit indiqué.
    
       4: while a = 1:
                  ^

    Vous avez utilisé un opérateur d’affectation `=`; vous vouliez peut-être utiliser 
    un opérateur d'égalité, `==`, ou l'opérateur `:=`.
    

(199) Space between operators 1
-------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\space_between_operators_1.py", line 1
        a = 2 * * 5
                ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\space_between_operators_1.py'
    à l'endroit indiqué.
    
       1: a = 2 * * 5
                ^ ^

    Vous ne pouvez pas écrire le même opérateur, `*`, deux fois de suite.
    Peut-être avez-vous écrit l’un d’eux par erreur
    ou vous avez oublié d’écrire quelque chose entre les deux.
    Ou peut-être avez-vous inclus un espace par erreur entre les deux opérateurs
    et vouliez écrire l'opérateur `**`.
    

(200) Space between operators 2
-------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\space_between_operators_2.py", line 1
        a / = b
            ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\space_between_operators_2.py'
    à l'endroit indiqué.
    
       1: a / = b
            ^ ^

    Vous ne pouvez pas avoir ces deux opérateurs, `/` et `=`,
    qui se suivent. Peut-être avez-vous écrit l’un d’eux par erreur
    ou vous avez oublié d’écrire quelque chose entre les deux.
    Ou peut-être avez-vous inclus un espace par erreur entre les deux opérateurs
    et vouliez écrire l'opérateur `/=`.
    

(201) Space in variable name
----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\space_in_variable_name.py", line 1
        my name = André
           ^
    SyntaxError: invalid syntax
    
        Vouliez-vous dire `my_name` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\space_in_variable_name.py'
    à l'endroit indiqué.
    
       1: my name = André
             ^^^^

    Vous ne pouvez pas avoir d'espaces dans les identifiants (noms de variables).
    Peut-être vouliez-vous écrire `my_name` ?
    

(202) Wrong target for star assignment
--------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\star_assignment_target.py", line 1
        *a = 1
        ^
    SyntaxError: starred assignment target must be in a list or tuple
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\star_assignment_target.py'
    à l'endroit indiqué.
    
       1: *a = 1
          ^

    Une affectation utilisant l'opérateur étoile doit être de la forme :
    
        ... *nom = liste_ou_tuple
    
    

(203) Too many nested blocks
----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\too_many_nested_blocks.py", line 22
        while 22:
        ^
    SyntaxError: too many statically nested blocks
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\too_many_nested_blocks.py'
    à l'endroit indiqué.
    
       22:                      while 22:
                                ^^^^^

    Votre code est trop complexe pour Python :
    vous devez réduire le nombre de blocs de code indentés
    contenus dans d'autres blocs de code.
    

(204) Too many nested parentheses.
----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\too_many_parentheses.py", line 4
        ((((((((((((((((((((((((((((((((((
                                         ^
    SyntaxError: too many nested parentheses
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\too_many_parentheses.py'
    à l'endroit indiqué.
    
       1: ((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
       2:     ((((((((((((((((((((((((((((((((((((((((((((((((((((((((
       3:         (((((((((((((((((((((((((((((((((((((((((((((((((((
    -->4:             ((((((((((((((((((((((((((((((((((
                                                       ^
       5:                                              ))))))))))))))))))))))))))))))))))))))))))))))))))
       6:         )))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
       7:     ))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

    Votre code est trop complexe pour Python :
    vous devez réduire le nombre de parenthèses
    contenues dans d'autres parenthèses.
    

(205) Trailing comma in import statement
----------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\trailing_comma_in_import.py", line 2
        from math import sin, cos,
                                  ^
    SyntaxError: trailing comma not allowed without surrounding parentheses
    
        Avez-vous écrit une virgule par erreur ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\trailing_comma_in_import.py'
    à l'endroit indiqué.
    
       2: from math import sin, cos,
                                   ^

    Python indique que vous devez utiliser des parenthèses
    pour entourer une expression se terminant par une virgule.
    Toutefois, si vous supprimez la dernière virgule, il n'y aura pas d'erreur de syntaxe.
    Peut-être que vous vouliez écrire
    
    `from math import sin, cos`
    

(206) Triple-equal sign
-----------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\triple_equal.py", line 3
        x = y === z
                ^
    SyntaxError: invalid syntax
    
        Voulez-vous utiliser `is` au lieu de `===`?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\triple_equal.py'
    à l'endroit indiqué.
    
       3: x = y === z
                ^^^

    Vous avez écrit trois signes égaux de suite ce qui est utilisé dans certains
    langages de programmation, mais pas en Python. Pour vérifier si deux objets
    sont égaux, utilisent deux signes d'égalité, `==`; pour voir si deux noms représentent
    exactement le même objet, utilisez l’opérateur `is`.
    

(207) Unclosed bracket
----------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unclosed_bracket.py", line 7
        print(foo())
        ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unclosed_bracket.py'
    à l'endroit indiqué.
    
       5:     return [1, 2, 3
       6: 
    -->7: print(foo())
          ^^^^^
       8: 

    Le symbole crochet `[` à la ligne 5 n'est pas fermé par le symbole correspondant.
    
        5:     return [1, 2, 3
                      ^
    

(208) Unclosed parenthesis - 1
------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unclosed_paren_1.py", line 3
        if x == 1:
                 ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unclosed_paren_1.py'
    à l'endroit indiqué.
    
       2: x = int('1'
    -->3: if x == 1:
                   ^
       4:     print('yes')
       5: 

    Le symbole parenthèse `(` à la ligne 2 n'est pas fermé par le symbole correspondant.
    
        2: x = int('1'
                  ^
    

(209) Unclosed parenthesis - 2
------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unclosed_paren_2.py", line 3
        d = a*a
        ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unclosed_paren_2.py'
    à l'endroit indiqué.
    
       2: a = (b+c
    -->3: d = a*a
          ^
       4: 

    Le symbole parenthèse `(` à la ligne 2 n'est pas fermé par le symbole correspondant.
    
        2: a = (b+c
               ^
    

(210) Unclosed parenthesis - 3
------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unclosed_paren_3.py", line 7
        if 2:
            ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unclosed_paren_3.py'
    à l'endroit indiqué.
    
       5:         print(((123))
       6: 
    -->7: if 2:
              ^
       8:     print(123))

    Le symbole parenthèse `(` à la ligne 5 n'est pas fermé par le symbole correspondant.
    
        5:         print(((123))
                        ^
    
    Si cela est incorrect, veuillez signaler ce cas.
    

(211) Unclosed parenthesis - 4
------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unclosed_paren_4.py", line 4
        def test():
        ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unclosed_paren_4.py'
    à l'endroit indiqué.
    
       2: print('hello'
       3: 
    -->4: def test():
          ^^^

    Le symbole parenthèse `(` à la ligne 2 n'est pas fermé par le symbole correspondant.
    
        2: print('hello'
                ^
    

(212) Content passed continuation line character
------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unexpected_after_continuation_character.py", line 5
        print(\t)
               ^
    SyntaxError: unexpected character after line continuation character
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unexpected_after_continuation_character.py'
    à l'endroit indiqué.
    
       5: print(\t)
                 ^

    Vous utilisez le caractère de continuation `\` en dehors d'une chaîne de caractères,
    et il est suivi par au moins un autre caractère.
    Je suppose que vous avez oublié d’enfermer du contenu dans une chaîne de caractères.
    

(213) Unexpected EOF while parsing
----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unexpected_eof.py", line 8
    SyntaxError: unexpected EOF while parsing
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unexpected_eof.py'
    à l'endroit indiqué.
    
       5:     return [1, 2, 3,
       6: 
       7: print(foo())
    -->8: 
                     ^

    Python nous dit qu'il a atteint la fin du fichier
    et s'attendait à plus de contenu.
    
    Je vais essayer de donner un peu plus d'informations.
    
    
    Le symbole crochet `[` à la ligne 5 n'est pas fermé par le symbole correspondant.
    
        5:     return [1, 2, 3,
                      ^
    

(214) Invalid character (unicode fraction 3/4)
----------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unicode_fraction.py", line 1
        a = ¾  # 3/4
            ^
    SyntaxError: invalid character '¾' (U+00BE)
    
        Voulez-vous dire `3/4` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unicode_fraction.py'
    à l'endroit indiqué.
    
       1: a = ¾  # 3/4
              ^

    Avez-vous utilisé le copier-coller ?
    Python indique que vous avez utilisé le caractère unicode `¾`
    ce qui n’est pas permis.
    Vous avez utilisé le caractère unicode ¾ qui est connu sous le nom de
    VULGAR FRACTION THREE QUARTERS
    Je pense que vous vouliez plutôt écrire la fraction `3/4`.
    

(215) Invalid character (unicode fraction 1/2)
----------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unicode_fraction2.py", line 1
        a = 1½  # 1 1/2
             ^
    SyntaxError: invalid character '½' (U+00BD)
    
        Voulez-vous dire `1/2` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unicode_fraction2.py'
    à l'endroit indiqué.
    
       1: a = 1½  # 1 1/2
               ^

    Avez-vous utilisé le copier-coller ?
    Python indique que vous avez utilisé le caractère unicode `½`
    ce qui n’est pas permis.
    Vous avez utilisé le caractère unicode ½ qui est connu sous le nom de
    VULGAR FRACTION ONE HALF
    Je pense que vous vouliez plutôt écrire la fraction `1/2`.
    

(216) Invalid character (unicode fraction slash)
------------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unicode_fraction3.py", line 1
        a = 22 ⁄ 7
               ^
    SyntaxError: invalid character '⁄' (U+2044)
    
        Did you mean to use the division operator, `/`?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unicode_fraction3.py'
    à l'endroit indiqué.
    
       1: a = 22 ⁄ 7
                 ^

    Avez-vous utilisé le copier-coller ?
    Python indique que vous avez utilisé le caractère unicode `⁄`
    ce qui n’est pas permis.
    Je soupçonne que vous avez utilisé le caractère unicode connu sous le nom de
    FRACTION SLASH', qui ressemble à
    mais est différent de l'opérateur de division `/`.
    

(217) Invalid character (unicode quote)
---------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unicode_quote.py", line 3
        a = « hello »
            ^
    SyntaxError: invalid character '«' (U+00AB)
    
        Vouliez vous utiliser un guillemet normal, `'` ou `"` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unicode_quote.py'
    à l'endroit indiqué.
    
       3: a = « hello »
              ^

    Avez-vous utilisé le copier-coller ?
    Python indique que vous avez utilisé le caractère unicode `«`
    ce qui n’est pas permis.
    Je soupçonne que vous avez utilisé un guillemet unicode
    dont le nom est LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    au lieu d'un guillemet normal (simple ou double) pour une chaîne de caractères.
    

(218) Invalid character (unicode quote2)
----------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unicode_quote2.py", line 2
        a = ‹ hello ›
            ^
    SyntaxError: invalid character '‹' (U+2039)
    
        Vouliez vous utiliser un guillemet normal, `'` ou `"` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unicode_quote2.py'
    à l'endroit indiqué.
    
       2: a = ‹ hello ›
              ^

    Avez-vous utilisé le copier-coller ?
    Python indique que vous avez utilisé le caractère unicode `‹`
    ce qui n’est pas permis.
    Je soupçonne que vous avez utilisé un guillemet unicode
    dont le nom est SINGLE LEFT-POINTING ANGLE QUOTATION MARK
    au lieu d'un guillemet normal (simple ou double) pour une chaîne de caractères.
    

(219) Invalid character (mistaken <)
------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unicode_quote3.py", line 2
        if a ‹ hello:
             ^
    SyntaxError: invalid character '‹' (U+2039)
    
        Vouliez vous utiliser un guillemet normal, `'` ou `"` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unicode_quote3.py'
    à l'endroit indiqué.
    
       2: if a ‹ hello:
               ^

    Avez-vous utilisé le copier-coller ?
    Python indique que vous avez utilisé le caractère unicode `‹`
    ce qui n’est pas permis.
    Je soupçonne que vous avez utilisé un guillemet unicode
    dont le nom est SINGLE LEFT-POINTING ANGLE QUOTATION MARK
    au lieu d'un guillemet normal (simple ou double) pour une chaîne de caractères.
    Ou peut-être avez-vous voulu écrire un signe plus petit que, `<`.
    

(220) Invalid character (mistaken >)
------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unicode_quote4.py", line 2
        if a › hello:
             ^
    SyntaxError: invalid character '›' (U+203A)
    
        Vouliez vous utiliser un guillemet normal, `'` ou `"` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unicode_quote4.py'
    à l'endroit indiqué.
    
       2: if a › hello:
               ^

    Avez-vous utilisé le copier-coller ?
    Python indique que vous avez utilisé le caractère unicode `›`
    ce qui n’est pas permis.
    Je soupçonne que vous avez utilisé un guillemet unicode
    dont le nom est SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
    au lieu d'un guillemet normal (simple ou double) pour une chaîne de caractères.
    Ou peut-être avez-vous voulu écrire un signe plus grand que, `>`.
    

(221) Invalid character (mistaken comma)
----------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unicode_quote5.py", line 2
        a = (1‚ 2)
              ^
    SyntaxError: invalid character '‚' (U+201A)
    
        Vouliez vous utiliser un guillemet normal, `'` ou `"` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unicode_quote5.py'
    à l'endroit indiqué.
    
       2: a = (1‚ 2)
                ^

    Avez-vous utilisé le copier-coller ?
    Python indique que vous avez utilisé le caractère unicode `‚`
    ce qui n’est pas permis.
    Je soupçonne que vous avez utilisé un guillemet unicode
    dont le nom est SINGLE LOW-9 QUOTATION MARK
    au lieu d'un guillemet normal (simple ou double) pour une chaîne de caractères.
    Ou peut-être, vous vouliez écrire une virgule.
    

(222) Unmatched closing curly bracket
-------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unmatched_closing_curly.py", line 6
        3, 4,}}
              ^
    SyntaxError: unmatched '}'
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unmatched_closing_curly.py'
    à l'endroit indiqué.
    
       4: a = {1,
       5:     2,
    -->6:     3, 4,}}
                    ^

    Le symbole accolade `}` à la ligne 6 n'a pas de symbole ouvrant qui lui correspond.
    

(223) Unmatched closing parenthesis
-----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unmatched_closing_paren.py", line 6
        3, 4,))
              ^
    SyntaxError: unmatched ')'
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unmatched_closing_paren.py'
    à l'endroit indiqué.
    
       4: a = (1,
       5:     2,
    -->6:     3, 4,))
                    ^

    Le symbole parenthèse `)` à la ligne 6 n'a pas de symbole ouvrant qui lui correspond.
    

(224) Mismatched brackets - 1
-----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unmatched_closing_bracket_1.py", line 2
        x = (1, 2, 3]
                    ^
    SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unmatched_closing_bracket_1.py'
    à l'endroit indiqué.
    
       2: x = (1, 2, 3]
              ^       ^

    Le symbole crochet `]` à la ligne 2 ne correspond pas au symbole parenthèse `(` à la ligne 2.
    
        2: x = (1, 2, 3]
               ^       ^
    

(225) Mismatched brackets - 2
-----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unmatched_closing_bracket_2.py", line 4
        3]
         ^
    SyntaxError: closing parenthesis ']' does not match opening parenthesis '(' on line 2
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unmatched_closing_bracket_2.py'
    à l'endroit indiqué.
    
    -->2: x = (1,
              ^
       3:      2,
    -->4:      3]
                ^

    Le symbole crochet `]` à la ligne 4 ne correspond pas au symbole parenthèse `(` à la ligne 2.
    
        2: x = (1,
               ^
        4:      3]
                 ^
    

(226) Unmatched brackets - 3
----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unmatched_closing_bracket_3.py", line 3
        3]]
          ^
    SyntaxError: unmatched ']'
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unmatched_closing_bracket_3.py'
    à l'endroit indiqué.
    
       1: x = [1,
       2:      2,
    -->3:      3]]
                 ^

    Le symbole crochet `]` à la ligne 3 n'a pas de symbole ouvrant qui lui correspond.
    

(227) Unpacking a dict value
----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unpacking_dict_value.py", line 1
        {'a': *(1, 2, 3)}
              ^
    SyntaxError: invalid syntax
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unpacking_dict_value.py'
    à l'endroit indiqué.
    
       1: {'a': *(1, 2, 3)}
              ^ ^

    Vous ne pouvez pas avoir ces deux opérateurs, `:` et `*`,
    l'un après l'autre.
    Il semble que vous ayez essayé d'utiliser une expression étoilée comme valeur de `dict` ;
    ceci n'est pas permis.
    
    L'énoncé suivant ne comporte pas d'erreur de syntaxe :
    
        {'a': (1, 2, 3)}
    

(228) Unterminated triple quoted string
---------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unterminated_triple_quote_string.py", line 4
        some_text = """In a land
    populated by weird animals,
    a ...
                                                                   ^
    SyntaxError: EOF while scanning triple-quoted string literal
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unterminated_triple_quote_string.py'
    .
    
       1: some_text = """In a land
       2: 

    Vous avez commencé à écrire une chaîne débutant avec des triples guillemets,
    sans inclure les triples guillemets nécessaires pour mettre fin à la chaîne.
    

(229) TabError
--------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\tab_error.py", line 7
        pass
        ^
    TabError: inconsistent use of tabs and spaces in indentation
    
    Une exception de type `TabError` indique que vous avez utilisé des espaces
    ainsi que des caractères de tabulation pour indenter votre code.
    Cela n’est pas autorisé dans Python.
    L’indentation de votre code signifie que le bloc de codes est aligné
    verticalement en insérant des espaces ou des tabulations au début des lignes.
    La recommandation de Python est de toujours utiliser des espaces
    pour indenter votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\tab_error.py'
    à l'endroit indiqué.
    
       7: 	pass
           ^^^^

(230) EOL unescaped backslash
-----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unescaped_backslash.py", line 1
        a = "abc\"
                  ^
    SyntaxError: EOL while scanning string literal
    
        Avez-vous oublié d’échapper un caractère barre oblique inverse ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unescaped_backslash.py'
    à l'endroit indiqué.
    
       1: a = "abc\"
                   ^

    Vous aviez commencé à écrire une chaîne de caractères
    avec un guillemet simple ou double, mais n'avez jamais
    terminé la chaîne avec un autre guillemet sur cette ligne.
    Peut-être que vous vouliez écrire une barre oblique inverse, `\`
    comme le dernier caractère de la chaîne et vous oublié que vous
    deviez en écrire deux `\` d’affilée.
    

(231) Using the backquote character
-----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\use_backquote.py", line 3
        a = `1`
            ^
    SyntaxError: invalid syntax
    
        Vous ne devez pas utiliser le caractère accent grave.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\use_backquote.py'
    à l'endroit indiqué.
    
       3: a = `1`
              ^

    Vous utilisez le charactère d'accent grave.
    Soit que vous vouliez utiliser un apostrophe, ',
    ou que vous avez copié du code de Python 2;
    dans ce dernier cas, utilisez la fonction `repr(x)`.

(232) unicode error
-------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\unicode_error.py", line 1
        path = "c:\Users\andre"
                               ^
    SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
    
        Il faut peut-être doubler les caractères barres obliques inversées.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\unicode_error.py'
    à l'endroit indiqué.
    
       1: path = "c:\Users\andre"
                 ^^^^^^^^^^^^^^^^

    Je pense que vous avez écrit une chaîne qui contient
    une barre oblique inversée, `\` suivie d'un "U" majuscule et d'autres caractères.
    Python a probablement interprété cela comme indiquant le début de
    ce que l'on appelle une séquence d'échappement pour les caractères unicode spéciaux.
    Pour résoudre ce problème, écrivez une "chaîne brute" (raw string)
    en ajoutant la lettre `r` en tant que préfixe devant
    la chaîne de caractères, ou remplacez `\U` par `\\U`.
    

(233) Walrus instead of equal
-----------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\walrus_instead_of_equal.py", line 1
        a := 3
              ^
    SyntaxError: invalid syntax
    
        Voulez-vous utiliser `=` ?
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\walrus_instead_of_equal.py'
    à l'endroit indiqué.
    
       1: a := 3
               ^

    Vous utilisez l’opérateur d’affectation augmentée `:=` là où
    l’opérateur d’affectation normal `=` était requis.
    

(234) Missing condition in while statement
------------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\while_missing_condition.py", line 1
        while:
             ^
    SyntaxError: invalid syntax
    
        Vous avez oublié d’ajouter une condition.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\while_missing_condition.py'
    à l'endroit indiqué.
    
       1: while:
               ^

    Une boucle `while` doit inclure une condition :
    
        while condition:
            ...
    
    

(235) Would-be variable declaration
-----------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\would_be_type_declaration_1.py", line 3
        if var start := begin < end:
               ^
    SyntaxError: invalid syntax
    
        Vous n’avez pas besoin de déclarer des variables dans Python.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\would_be_type_declaration_1.py'
    à l'endroit indiqué.
    
       3: if var start := begin < end:
                 ^^^^^

    Il semble que vous essayiez de déclarer que `start` est
    une variable utilisant le mot `var`.
    Si vous supprimez `var`, vous aurez une instruction Python valide.
    

(236) Would-be variable declaration - 2
---------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\would_be_type_declaration_2.py", line 5
        var start := begin < end
            ^
    SyntaxError: invalid syntax
    
        Vous n’avez pas besoin de déclarer des variables dans Python.
        
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\would_be_type_declaration_2.py'
    à l'endroit indiqué.
    
       4: if (
    -->5:     var start := begin < end
                  ^^^^^
       6:    ):

    Il semble que vous essayiez de déclarer que `start` est
    une variable utilisant le mot `var`.
    Si vous supprimez `var`, vous aurez une instruction Python valide.
    

(237) Cannot use yield outside function
---------------------------------------

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\trb_syntax_common.py", line 49, in create_tracebacks
        __import__(name)
      File "TESTS:\syntax\yield_outside_function.py", line 1
        (yield i) == 3
         ^
    SyntaxError: 'yield' outside function
    
    Une exception de type `SyntaxError` se produit lorsque Python ne peut pas comprendre votre code.
    
    Python ne peut pas comprendre le code du fichier
    'TESTS:\syntax\yield_outside_function.py'
    à l'endroit indiqué.
    
       1: (yield i) == 3
           ^^^^^

    Vous ne pouvez utiliser une instruction `yield` qu'à l'intérieur d'une fonction.
    
