
|france| Friendly tracebacks - en Français
===========================================

Le but principal de friendly est de fournir des rétroactions plus
conviviales que les fameux **tracebacks** de Python lorsqu'une exception survient.

.. note::

     Le contenu de cette page a été généré par l'exécution de
     `trb_french.py` situé dans le répertoire ``tests/``.
     Ceci a besoin d'être fait de manière explicite lorsqu'on veut
     faire des corrections ou des ajouts, avant de faire la mise
     à jour du reste de la documentation avec Sphinx.

Friendly-traceback version: 0.7.53
Python version: 3.10.6



ArithmeticError
---------------


Generic
~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_arithmetic_error.py", line 9, in test_Generic
        raise ArithmeticError('error')
    ArithmeticError: error
    
    `ArithmeticError` est la classe de base pour les exceptions
    qui sont soulevées pour diverses erreurs arithmétiques.
    
    Exception levée à la ligne `9` du fichier 'TESTS:\runtime\test_arithmetic_error.py'.
    
        4| def test_Generic():
        5|     try:
        6|         # I am not aware of any way in which this error is raised directly
        7|         # Usually, a subclass such as ZeroDivisionError, etc., would
        8|         # likely be raised.
    --> 9|         raise ArithmeticError('error')
       10|     except ArithmeticError as e:

            ArithmeticError:  <class ArithmeticError>
        


AssertionError
--------------


Generic
~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_assertion_error.py", line 8, in test_Generic
        raise AssertionError("Fake message")
    AssertionError: Fake message
    
    Dans Python, le mot clé `assert` est utilisé dans des énoncés ayant la forme
    `assert condition`, pour confirmer que `condition` n’est pas `False`;
    ni équivalente à `False` comme une liste vide, etc.
    
    Si `condition` est `False` ou son équivalent, une exception de type `AssertionError` est levée.
    
    Exception levée à la ligne `8` du fichier 'TESTS:\runtime\test_assertion_error.py'.
    
       4| def test_Generic():
       5|     try:
       6|         # We raise it explicitly, rather than with the keyword assert, since
       7|         # we don't want pytest to rewrite out test.
    -->8|         raise AssertionError("Fake message")
       9|     except AssertionError as e:

            AssertionError:  <class AssertionError>
        


AttributeError
--------------


Attribute from other module
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_attribute_error.py", line 336, in test_Attribute_from_other_module
        keyword.pi
    AttributeError: module 'keyword' has no attribute 'pi'
    
        Vouliez-vous dire l’un des modules suivants: `math, cmath` ?
    Une exception `AttributeError` se produit lorsque le code contient quelque chose comme
        `object.x`
    et `x` n’est pas une méthode ou un attribut (variable) appartenant à `objet`.
    
    Au lieu du module `keyword`, peut-être vouliez-vous utiliser l’attribut `pi` de 
    l'un des modules suivants:
    `math, cmath` .
    
    Exception levée à la ligne `336` du fichier 'TESTS:\runtime\test_attribute_error.py'.
    
       332|     assert "Did you mean `math`?" in result
       333| 
       334| import cmath
       335| try:
    -->336|     keyword.pi
                ^^^^^^^^^^
       337| except AttributeError as e:

            keyword:  <module keyword> from PYTHON_LIB:\keyword.py
        


Builtin function
~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_attribute_error.py", line 229, in test_Builtin_function
        len.text
    AttributeError: 'builtin_function_or_method' object has no attribute 'text'
    
        Vouliez-vous dire `len(text)` ?
        
    Une exception `AttributeError` se produit lorsque le code contient quelque chose comme
        `object.x`
    et `x` n’est pas une méthode ou un attribut (variable) appartenant à `objet`.
    
    `len` est une fonction. Peut-être que vous vouliez écrire
    `len(text)`
    
    Exception levée à la ligne `229` du fichier 'TESTS:\runtime\test_attribute_error.py'.
    
       226| def test_Builtin_function():
       227|     text = 'Hello world!'
       228|     try:
    -->229|         len.text
                    ^^^^^^^^
       230|     except AttributeError as e:

            text:  'Hello world!'
            len:  <builtin function len>
        


Builtin module with no file
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_attribute_error.py", line 247, in test_Builtin_module_with_no_file
        sys.foo
    AttributeError: module 'sys' has no attribute 'foo'
    
    Une exception `AttributeError` se produit lorsque le code contient quelque chose comme
        `object.x`
    et `x` n’est pas une méthode ou un attribut (variable) appartenant à `objet`.
    
    Python nous dit qu’aucun objet avec le nom `foo` n’est
    dans le module `sys`.
    
    Exception levée à la ligne `247` du fichier 'TESTS:\runtime\test_attribute_error.py'.
    
       243| """Issue 116"""
       244| import sys
       245| 
       246| try:
    -->247|     sys.foo
                ^^^^^^^
       248| except AttributeError as e:

            sys:  <module sys (builtin)>
        


Circular import
~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_attribute_error.py", line 368, in test_Circular_import
        import my_turtle1
      File "TESTS:\my_turtle1.py", line 4, in <module>
        a = my_turtle1.something
    AttributeError: partially initialized module 'my_turtle1' has no attribute 'something' (most likely due to a circular import)
    
        Avez-vous donné à votre programme le même nom qu’un module Python ?
        
    Une exception `AttributeError` se produit lorsque le code contient quelque chose comme
        `object.x`
    et `x` n’est pas une méthode ou un attribut (variable) appartenant à `objet`.
    
    Je soupçonne que vous avez utilisé le nom `my_turtle1.py` pour votre programme
    et que vous vouliez aussi importer un module du même nom
    de la bibliothèque standard de Python.
    Si c’est le cas, vous devriez utiliser un nom différent pour votre programme.
    
    L'exécution s'est arrêtée à la ligne `368` du fichier 'TESTS:\runtime\test_attribute_error.py'
    
       365| from friendly_traceback.runtime_errors import stdlib_modules
       366| stdlib_modules.names.add("my_turtle1")
       367| try:
    -->368|    import my_turtle1
       369| except AttributeError as e:

    Exception levée à la ligne `4` du fichier 'TESTS:\my_turtle1.py'.
    
       1| """To test attribute error of partially initialized module."""
       2| import my_turtle1
       3| 
    -->4| a = my_turtle1.something
              ^^^^^^^^^^^^^^^^^^^^

            my_turtle1:  <module my_turtle1> from TESTS:\my_turtle1.py
        


Circular import b
~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_attribute_error.py", line 386, in test_Circular_import_b
        import circular_c
      File "TESTS:\circular_c.py", line 4, in <module>
        a = circular_c.something
    AttributeError: partially initialized module 'circular_c' has no attribute 'something' (most likely due to a circular import)
    
        Vous avez une importation circulaire.
        
    Une exception `AttributeError` se produit lorsque le code contient quelque chose comme
        `object.x`
    et `x` n’est pas une méthode ou un attribut (variable) appartenant à `objet`.
    
    Python a indiqué que le module `{module}` n'était pas complètement importé.
    Cela peut se produire si, pendant l'exécution du code du module `circular_c`
    une tentative est faite d'importer à nouveau le même module.
    
    L'exécution s'est arrêtée à la ligne `386` du fichier 'TESTS:\runtime\test_attribute_error.py'
    
       384| def test_Circular_import_b():
       385|     try:
    -->386|         import circular_c
       387|     except AttributeError as e:

    Exception levée à la ligne `4` du fichier 'TESTS:\circular_c.py'.
    
       1| # Attribute error for partially initialize module
       2| import circular_c
       3| 
    -->4| a = circular_c.something
              ^^^^^^^^^^^^^^^^^^^^

            circular_c:  <module circular_c> from TESTS:\circular_c.py
        


Generic
~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_attribute_error.py", line 26, in test_Generic
        A.x  # testing type
    AttributeError: type object 'A' has no attribute 'x'
    
    Une exception `AttributeError` se produit lorsque le code contient quelque chose comme
        `object.x`
    et `x` n’est pas une méthode ou un attribut (variable) appartenant à `objet`.
    
    L’objet `A` n’a pas d’attribut nommé `x`.
    
    Exception levée à la ligne `26` du fichier 'TESTS:\runtime\test_attribute_error.py'.
    
       22| class A:
       23|     pass
       24| 
       25| try:
    -->26|     A.x  # testing type
               ^^^
       27| except AttributeError as e:

            A:  <class A> defined in <function test_attribute_error.test_Generic>
        


Generic different frame
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_attribute_error.py", line 50, in test_Generic_different_frame
        a.attr
    AttributeError: 'A' object has no attribute 'attr'. Did you mean: 'attr2'?
    
        Vouliez-vous dire `attr2` ?
        
    Une exception `AttributeError` se produit lorsque le code contient quelque chose comme
        `object.x`
    et `x` n’est pas une méthode ou un attribut (variable) appartenant à `objet`.
    
    L’objet `a` n’a pas d’attribut nommé `attr`.
    Peut-être que vous vouliez plutôt écrire : `a.attr2` au lieu de `a.attr`.
    
    Exception levée à la ligne `50` du fichier 'TESTS:\runtime\test_attribute_error.py'.
    
       46|     return A()
       47| 
       48| a = f()
       49| try:
    -->50|     a.attr
               ^^^^^^
       51| except AttributeError as e:

            a:  <A object>
                defined in <function test_attribute_error.test_Generic_different_frame.<locals>.f>
        


Generic instance
~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_attribute_error.py", line 69, in test_Generic_instance
        a.x
    AttributeError: 'A' object has no attribute 'x'
    
    Une exception `AttributeError` se produit lorsque le code contient quelque chose comme
        `object.x`
    et `x` n’est pas une méthode ou un attribut (variable) appartenant à `objet`.
    
    L’objet `a` n’a pas d’attribut nommé `x`.
    
    Exception levée à la ligne `69` du fichier 'TESTS:\runtime\test_attribute_error.py'.
    
       66|     pass
       67| a = A()
       68| try:
    -->69|     a.x
               ^^^
       70| except AttributeError as e:

            a:  <A object>
                defined in <function test_attribute_error.test_Generic_instance>
        


Module attribute typo
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_attribute_error.py", line 150, in test_Module_attribute_typo
        math.cost
    AttributeError: module 'math' has no attribute 'cost'. Did you mean: 'cos'?
    
        Vouliez-vous dire `cos` ?
        
    Une exception `AttributeError` se produit lorsque le code contient quelque chose comme
        `object.x`
    et `x` n’est pas une méthode ou un attribut (variable) appartenant à `objet`.
    
    Au lieu d’écrire `math.cost`, peut-être que vous vouliez écrire
    l'un des attributs suivants du module `math` :
    cos, cosh
    
    Exception levée à la ligne `150` du fichier 'TESTS:\runtime\test_attribute_error.py'.
    
       145|     assert "Did you mean `ascii_lowercase`" in result
       146| 
       147| import math
       148| 
       149| try:
    -->150|     math.cost
                ^^^^^^^^^
       151| except AttributeError as e:

            math:  <module math (builtin)>
        


Nonetype
~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_attribute_error.py", line 191, in test_Nonetype
        a.b
    AttributeError: 'NoneType' object has no attribute 'b'
    
    Une exception `AttributeError` se produit lorsque le code contient quelque chose comme
        `object.x`
    et `x` n’est pas une méthode ou un attribut (variable) appartenant à `objet`.
    
    Vous tentez d’accéder à l’attribut `b`
    pour une variable dont la valeur est `None`.
    Exception levée à la ligne `191` du fichier 'TESTS:\runtime\test_attribute_error.py'.
    
       188| def test_Nonetype():
       189|     a = None
       190|     try:
    -->191|         a.b
                    ^^^
       192|     except AttributeError as e:

            a:  None
        


Object attribute typo
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_attribute_error.py", line 86, in test_Object_attribute_typo
        a.appendh(4)
    AttributeError: 'list' object has no attribute 'appendh'. Did you mean: 'append'?
    
        Vouliez-vous dire `append` ?
        
    Une exception `AttributeError` se produit lorsque le code contient quelque chose comme
        `object.x`
    et `x` n’est pas une méthode ou un attribut (variable) appartenant à `objet`.
    
    L’objet `a` n’a pas d’attribut nommé `appendh`.
    Peut-être que vous vouliez plutôt écrire : `a.append` au lieu de `a.appendh`.
    
    Exception levée à la ligne `86` du fichier 'TESTS:\runtime\test_attribute_error.py'.
    
       82| def test_Object_attribute_typo():
       83|     #
       84|     try:
       85|         a = [1, 2, 3]
    -->86|         a.appendh(4)
                   ^^^^^^^^^
       87|     except AttributeError as e:

            a:  [1, 2, 3]
        


Perhaps comma
~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_attribute_error.py", line 213, in test_Perhaps_comma
        .defg]
    AttributeError: 'str' object has no attribute 'defg'
    
        Vouliez-vous séparer les noms d’objets par une virgule ?
        
    Une exception `AttributeError` se produit lorsque le code contient quelque chose comme
        `object.x`
    et `x` n’est pas une méthode ou un attribut (variable) appartenant à `objet`.
    
    `defg` n’est pas un attribut de `abcd`.
    Cependant, les objets `abcd` et `defg` sont des objets connus.
    Peut-être avez-vous écrit une période pour séparer ces deux objets, 
    au lieu d’utiliser une virgule.
    
    Exception levée à la ligne `213` du fichier 'TESTS:\runtime\test_attribute_error.py'.
    
       208| defg = "world"
       209| 
       210| # fmt: off
       211| try:
       212|     a = [abcd
                     ^^^^
    -->213|     .defg]
                ^^^^^
       214| # fmt: on

            abcd:  'hello'
            defg:  'world'
        


Read only
~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_attribute_error.py", line 289, in test_Read_only
        f.b = 1
    AttributeError: 'F' object attribute 'b' is read-only
    
    Une exception `AttributeError` se produit lorsque le code contient quelque chose comme
        `object.x`
    et `x` n’est pas une méthode ou un attribut (variable) appartenant à `objet`.
    
    L'objet `f` utilise `__slots__` pour spécifier quels attributs peuvent être
    être modifiés. La valeur de l'attribut `f.b` ne peut pas être modifiée.
    The only attribute of `f` whose value can be changed is`a`.
    
    Exception levée à la ligne `289` du fichier 'TESTS:\runtime\test_attribute_error.py'.
    
       285|     b = 2
       286| 
       287| f = F()
       288| try:
    -->289|     f.b = 1
                ^^^
       290| except AttributeError as e:

            f:  <F object>
                defined in <function test_attribute_error.test_Read_only>
            f.b:  2
        


Shadow stdlib module
~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_attribute_error.py", line 172, in test_Shadow_stdlib_module
        turtle.Pen
    AttributeError: module 'turtle' has no attribute 'Pen'
    
        Avez-vous donné à votre programme le même nom qu’un module Python ?
        
    Une exception `AttributeError` se produit lorsque le code contient quelque chose comme
        `object.x`
    et `x` n’est pas une méthode ou un attribut (variable) appartenant à `objet`.
    
    Vous avez importé un module nommé `turtle` de `TESTS:\turtle.py`.
    Il y a aussi un module nommé `turtle` dans la bibliothèque standard de Python.
    Peut-être avez-vous besoin de renommer votre module.
    
    Exception levée à la ligne `172` du fichier 'TESTS:\runtime\test_attribute_error.py'.
    
       168| def test_Shadow_stdlib_module():
       169|     import turtle
       170| 
       171|     try:
    -->172|         turtle.Pen
                    ^^^^^^^^^^
       173|     except AttributeError as e:

            turtle:  <module turtle> from TESTS:\turtle.py
        


Tuple by accident
~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_attribute_error.py", line 305, in test_Tuple_by_accident
        something.upper()
    AttributeError: 'tuple' object has no attribute 'upper'
    
        Avez-vous écrit une virgule par erreur ?
        
    Une exception `AttributeError` se produit lorsque le code contient quelque chose comme
        `object.x`
    et `x` n’est pas une méthode ou un attribut (variable) appartenant à `objet`.
    
    `something` est un tuple qui contient un seul élément
    ayant `upper` comme attribut.
    Peut-être avez-vous ajouté une virgule par erreur à la fin de la ligne
    lorsque vous avez défini `something`.
    
    Exception levée à la ligne `305` du fichier 'TESTS:\runtime\test_attribute_error.py'.
    
       302| def test_Tuple_by_accident():
       303|     something = "abc",  # note trailing comma
       304|     try:
    -->305|         something.upper()
                    ^^^^^^^^^^^^^^^
       306|     except AttributeError as e:

            something:  ('abc',)
        


Use builtin
~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_attribute_error.py", line 103, in test_Use_builtin
        a.length()
    AttributeError: 'list' object has no attribute 'length'
    
        Vouliez-vous utiliser `len(a)` ?
        
    Une exception `AttributeError` se produit lorsque le code contient quelque chose comme
        `object.x`
    et `x` n’est pas une méthode ou un attribut (variable) appartenant à `objet`.
    
    L’objet `a` n’a pas d’attribut nommé `length`.
    Peut-être pouvez-vous utiliser la fonction Python builtin `len` à la place:
    `len(a)`.
    Exception levée à la ligne `103` du fichier 'TESTS:\runtime\test_attribute_error.py'.
    
        99| def test_Use_builtin():
       100|     #
       101|     try:
       102|         a = [1, 2, 3]
    -->103|         a.length()
                    ^^^^^^^^
       104|     except AttributeError as e:

            a:  [1, 2, 3]
        


Use join with str
~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_attribute_error.py", line 351, in test_Use_join_with_str
        a = ['a', '2'].join('abc') + ['b', '3'].join('\n')
    AttributeError: 'list' object has no attribute 'join'
    
        Voulez-vous dire `'abc'.join(['a', '2'])` ?
        
    Une exception `AttributeError` se produit lorsque le code contient quelque chose comme
        `object.x`
    et `x` n’est pas une méthode ou un attribut (variable) appartenant à `objet`.
    
    L’objet `['a', '2']` n’a pas d’attribut nommé `join`.
    Vous vouliez peut-être plutôt écrire quelque chose comme `'abc'.join(['a', '2'])`.
    
    Exception levée à la ligne `351` du fichier 'TESTS:\runtime\test_attribute_error.py'.
    
       349| def test_Use_join_with_str():
       350|     try:
    -->351|         a = ['a', '2'].join('abc') + ['b', '3'].join('\n')
                        ^^^^^^^^^^^^^^^
       352|     except AttributeError as e:


Use synonym
~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_attribute_error.py", line 120, in test_Use_synonym
        a.add(4)
    AttributeError: 'list' object has no attribute 'add'
    
        Vouliez-vous dire `append` ?
        
    Une exception `AttributeError` se produit lorsque le code contient quelque chose comme
        `object.x`
    et `x` n’est pas une méthode ou un attribut (variable) appartenant à `objet`.
    
    L’objet `a` n’a pas d’attribut nommé `add`.
    Toutefois, `a` a les attributs suivants avec des sens similaires:
    'append, extend, insert'.
    
    Exception levée à la ligne `120` du fichier 'TESTS:\runtime\test_attribute_error.py'.
    
       116| def test_Use_synonym():
       117|     #
       118|     try:
       119|         a = [1, 2, 3]
    -->120|         a.add(4)
                    ^^^^^
       121|     except AttributeError as e:

            a:  [1, 2, 3]
        


Using slots
~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_attribute_error.py", line 268, in test_Using_slots
        f.b = 1
    AttributeError: 'F' object has no attribute 'b'
    
    Une exception `AttributeError` se produit lorsque le code contient quelque chose comme
        `object.x`
    et `x` n’est pas une méthode ou un attribut (variable) appartenant à `objet`.
    
    L’objet `f` n’a pas d’attribut nommé `b`.
    Notez que l’objet `f` utilise `__slots__` qui empêche
    la création de nouveaux attributs.
    Voici quelques-uns de ses attributs connus :
    `a`.
    Exception levée à la ligne `268` du fichier 'TESTS:\runtime\test_attribute_error.py'.
    
       264|     __slots__ = ["a"]
       265| 
       266| f = F()
       267| try:
    -->268|     f.b = 1
                ^^^
       269| except AttributeError as e:

            f:  <F object>
                defined in <function test_attribute_error.test_Using_slots>
        


FileNotFoundError
-----------------


Directory not found
~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_file_not_found_error.py", line 73, in test_Directory_not_found
        open("does_not_exist/file.txt")
    FileNotFoundError: [Errno 2] No such file or directory: 'does_not_exist/file.txt'
    
    Une exception `FileNotFoundError` indique que vous
    essayez d’importer un module qui ne peut pas être trouvé par Python.
    Cela pourrait être parce que vous fait une faute d'orthographe en
    écrivant le nom du fichier.
    
    Dans votre programme, le nom du fichier inconnu est `file.txt`.
    does_not_exist
    n'est pas un répertoire valide.
    
    Exception levée à la ligne `73` du fichier 'TESTS:\runtime\test_file_not_found_error.py'.
    
       71| def test_Directory_not_found():
       72|     try:
    -->73|         open("does_not_exist/file.txt")
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
       74|     except FileNotFoundError as e:

            open:  <builtin function open>
        


Filename not found
~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_file_not_found_error.py", line 7, in test_Filename_not_found
        open("does_not_exist")
    FileNotFoundError: [Errno 2] No such file or directory: 'does_not_exist'
    
    Une exception `FileNotFoundError` indique que vous
    essayez d’importer un module qui ne peut pas être trouvé par Python.
    Cela pourrait être parce que vous fait une faute d'orthographe en
    écrivant le nom du fichier.
    
    Dans votre programme, le nom du fichier inconnu est `does_not_exist`.
    On s'attendait à ce qu'il soit trouvé dans le répertoire
    `C:\Users\Andre\github\friendly-traceback\tests`.
    Je n’ai pas d’informations supplémentaires pour vous.
    
    Exception levée à la ligne `7` du fichier 'TESTS:\runtime\test_file_not_found_error.py'.
    
       5| def test_Filename_not_found():
       6|     try:
    -->7|         open("does_not_exist")
                  ^^^^^^^^^^^^^^^^^^^^^^
       8|     except FileNotFoundError as e:

            open:  <builtin function open>
        


Filename not found 2
~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_file_not_found_error.py", line 31, in test_Filename_not_found_2
        open("setupp.py")
    FileNotFoundError: [Errno 2] No such file or directory: 'setupp.py'
    
        Vouliez-vous dire `setup.py` ?
        
    Une exception `FileNotFoundError` indique que vous
    essayez d’importer un module qui ne peut pas être trouvé par Python.
    Cela pourrait être parce que vous fait une faute d'orthographe en
    écrivant le nom du fichier.
    
    Dans votre programme, le nom du fichier inconnu est `setupp.py`.
    On s'attendait à ce qu'il soit trouvé dans le répertoire
    `C:\Users\Andre\github\friendly-traceback`.
    Le fichier `setup.py` a un nom semblable.
    
    Exception levée à la ligne `31` du fichier 'TESTS:\runtime\test_file_not_found_error.py'.
    
       27| if chdir:
       28|     os.chdir("..")
       29| 
       30| try:
    -->31|     open("setupp.py")
               ^^^^^^^^^^^^^^^^^
       32| except FileNotFoundError as e:

            open:  <builtin function open>
        


Filename not found 3
~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_file_not_found_error.py", line 54, in test_Filename_not_found_3
        open("setup.pyg")
    FileNotFoundError: [Errno 2] No such file or directory: 'setup.pyg'
    
        Vouliez-vous dire `setup.py` ?
        
    Une exception `FileNotFoundError` indique que vous
    essayez d’importer un module qui ne peut pas être trouvé par Python.
    Cela pourrait être parce que vous fait une faute d'orthographe en
    écrivant le nom du fichier.
    
    Dans votre programme, le nom du fichier inconnu est `setup.pyg`.
    On s'attendait à ce qu'il soit trouvé dans le répertoire
    `C:\Users\Andre\github\friendly-traceback`.
    Vous vouliez peut-être un des fichiers suivants ayant des noms semblables :
    `setup.py`, `setup.cfg`
    
    Exception levée à la ligne `54` du fichier 'TESTS:\runtime\test_file_not_found_error.py'.
    
       51| if chdir:
       52|     os.chdir("..")
       53| try:
    -->54|     open("setup.pyg")
               ^^^^^^^^^^^^^^^^^
       55| except FileNotFoundError as e:

            open:  <builtin function open>
        


ImportError
-----------


Simple import error
~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_import_error.py", line 56, in test_Simple_import_error
        from math import Pi
    ImportError: cannot import name 'Pi' from 'math' (unknown location)
    
        Vouliez-vous dire `pi` ?
        
    L'exception `ImportError` indique qu’un certain objet n’a pas pu
    être importé à partir d’un module ou d’un paquet. Très souvent, c’est
    parce que le nom de l’objet n’est pas écrit correctement.
    
    Peut-être que vous vouliez importer `pi` (de `math`) au lieu de `Pi`.
    
    Exception levée à la ligne `56` du fichier 'TESTS:\runtime\test_import_error.py'.
    
       52| multiple_import_on_same_line()
       53| wrong_case()
       54| 
       55| try:
    -->56|     from math import Pi
       57| except ImportError as e:


IndexError
----------


Assignment
~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_index_error.py", line 87, in test_Assignment
        a[13] = 1
    IndexError: list assignment index out of range
    
    Une exception `IndexError` se produit lorsque vous essayez d’obtenir un élément
    d'une liste, d'un tuple, ou d'un objet similaire (séquence), à l’aide d’un indice qui
    n’existe pas; typiquement, c’est parce que l’indice que vous donnez
    est plus grand que la longueur de la séquence.
    
    Vous avez essayé d'assigner une valeur à l'indice `13` de `a`,
    une liste (`list`) de longueur `10`.
    Les indices valides de `a` sont les entiers allant de `-10` à `9`.
    
    Exception levée à la ligne `87` du fichier 'TESTS:\runtime\test_index_error.py'.
    
       83|     assert "You have tried to assign a value to index `1` of `b`," in result
       84|     assert "a `list` which contains no item." in result
       85| 
       86| try:
    -->87|     a[13] = 1
               ^^^^^
       88| except IndexError as e:

            a:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        


Empty
~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_index_error.py", line 42, in test_Empty
        c = a[1]
    IndexError: list index out of range
    
        `a` ne contient aucun élément.
        
    Une exception `IndexError` se produit lorsque vous essayez d’obtenir un élément
    d'une liste, d'un tuple, ou d'un objet similaire (séquence), à l’aide d’un indice qui
    n’existe pas; typiquement, c’est parce que l’indice que vous donnez
    est plus grand que la longueur de la séquence.
    
    Vous avez essayé d’obtenir l’élément avec l’indice `1` de `a`,
    une liste (`list`) qui ne contient aucun élément.
    
    Exception levée à la ligne `42` du fichier 'TESTS:\runtime\test_index_error.py'.
    
       39| def test_Empty():
       40|     a = []
       41|     try:
    -->42|         c = a[1]
                       ^^^^
       43|     except IndexError as e:

            a:  []
        


Long list
~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_index_error.py", line 27, in test_Long_list
        print(a[60], b[0])
    IndexError: list index out of range
    
    Une exception `IndexError` se produit lorsque vous essayez d’obtenir un élément
    d'une liste, d'un tuple, ou d'un objet similaire (séquence), à l’aide d’un indice qui
    n’existe pas; typiquement, c’est parce que l’indice que vous donnez
    est plus grand que la longueur de la séquence.
    
    Vous avez essayé d’obtenir l’élément avec l’indice `60` de `a`,
    une liste (`list`) de longueur `40`.
    Les indices valides de `a` sont les entiers allant de `-40` à `39`.
    
    Exception levée à la ligne `27` du fichier 'TESTS:\runtime\test_index_error.py'.
    
       24| a = list(range(40))
       25| b = tuple(range(50))
       26| try:
    -->27|     print(a[60], b[0])
                     ^^^^^
       28| except IndexError as e:

            a:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, ...]
                len(a): 40
        
        


Short tuple
~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_index_error.py", line 10, in test_Short_tuple
        print(a[3], b[2])
    IndexError: tuple index out of range
    
        N’oubliez pas : le premier élément d'un objet de type `un `tuple`` est à l’indice 0
        et non pas à l'indice 1.
        
    Une exception `IndexError` se produit lorsque vous essayez d’obtenir un élément
    d'une liste, d'un tuple, ou d'un objet similaire (séquence), à l’aide d’un indice qui
    n’existe pas; typiquement, c’est parce que l’indice que vous donnez
    est plus grand que la longueur de la séquence.
    
    Vous avez essayé d’obtenir l’élément avec l’indice `3` de `a`,
    un `tuple` de longueur `3`.
    Les indices valides de `a` sont les entiers allant de `-3` à `2`.
    
    Exception levée à la ligne `10` du fichier 'TESTS:\runtime\test_index_error.py'.
    
        7| a = (1, 2, 3)
        8| b = [1, 2, 3]
        9| try:
    -->10|     print(a[3], b[2])
                     ^^^^
       11| except IndexError as e:

            a:  (1, 2, 3)
        


KeyError
--------


ChainMap
~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "PYTHON_LIB:\collections\__init__.py", line 1056, in pop
        return self.maps[0].pop(key, *args)
    KeyError: 42
    
        During handling of the above exception, another exception occurred:
    
    Traceback (most recent call last):
      File "TESTS:\runtime\test_key_error.py", line 65, in test_ChainMap
        d.pop(42)
    KeyError: 'Key not found in the first mapping: 42'
    
    Une `KeyError` est levée lorsqu'une valeur n'est pas trouvée en tant que
    clé dans un dict Python ou dans un objet similaire.
    
    La clé `42` est introuvable dans `d`, un objet de type `ChainMap`.
    
    Exception levée à la ligne `65` du fichier 'TESTS:\runtime\test_key_error.py'.
    
       62| from collections import ChainMap
       63| d = ChainMap({}, {})
       64| try:
    -->65|     d.pop(42)
               ^^^^^^^^^
       66| except KeyError as e:

            d:  ChainMap({}, {})
            d.pop:  <bound method ChainMap.pop> of ChainMap({}, {})
        


Forgot to convert to string
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_key_error.py", line 120, in test_Forgot_to_convert_to_string
        print(squares[2])
    KeyError: 2
    
        Avez-vous oublié de convertir `2` en une chaîne ?
        
    Une `KeyError` est levée lorsqu'une valeur n'est pas trouvée en tant que
    clé dans un dict Python ou dans un objet similaire.
    
    La clé `2` est introuvable dans le dict `squares`.
    `squares` contient une clé identique à `str(2)`.
    Peut-être avez-vous oublié de convertir la clé en une chaîne.
    
    Exception levée à la ligne `120` du fichier 'TESTS:\runtime\test_key_error.py'.
    
       117| def test_Forgot_to_convert_to_string():
       118|     squares = {"1": 1, "2": 4, "3": 9}
       119|     try:
    -->120|         print(squares[2])
                          ^^^^^^^^^^
       121|     except KeyError as e:

            squares:  {'1': 1, '2': 4, '3': 9}
        


Generic key error
~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_key_error.py", line 46, in test_Generic_key_error
        d["c"]
    KeyError: 'c'
    
    Une `KeyError` est levée lorsqu'une valeur n'est pas trouvée en tant que
    clé dans un dict Python ou dans un objet similaire.
    
    La clé `'c'` est introuvable dans le dict `d`.
    
    Exception levée à la ligne `46` du fichier 'TESTS:\runtime\test_key_error.py'.
    
       43| def test_Generic_key_error():
       44|     d = {"a": 1, "b": 2}
       45|     try:
    -->46|         d["c"]
                   ^^^^^^
       47|     except KeyError as e:

            d:  {'a': 1, 'b': 2}
        


Popitem empty ChainMap
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "PYTHON_LIB:\collections\__init__.py", line 1049, in popitem
        return self.maps[0].popitem()
    KeyError: 'popitem(): dictionary is empty'
    
        During handling of the above exception, another exception occurred:
    
    Traceback (most recent call last):
      File "TESTS:\runtime\test_key_error.py", line 27, in test_Popitem_empty_ChainMap
        alpha.popitem()
    KeyError: 'No keys found in the first mapping.'
    
        `alpha` est une `ChainMap` vide.
        
    Une `KeyError` est levée lorsqu'une valeur n'est pas trouvée en tant que
    clé dans un dict Python ou dans un objet similaire.
    
    Vous avez essayé de récupérer un élément de `alpha` qui est une `ChainMap` vide.
    
    Exception levée à la ligne `27` du fichier 'TESTS:\runtime\test_key_error.py'.
    
       24| from collections import ChainMap
       25| alpha = ChainMap({}, {})
       26| try:
    -->27|     alpha.popitem()
               ^^^^^^^^^^^^^^^
       28| except KeyError as e:

            alpha:  ChainMap({}, {})
            alpha.popitem:  <bound method ChainMap.popitem> of ChainMap({}, {})
        


Popitem empty dict
~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_key_error.py", line 8, in test_Popitem_empty_dict
        d.popitem()
    KeyError: 'popitem(): dictionary is empty'
    
        `d` est un `dict` vide.
        
    Une `KeyError` est levée lorsqu'une valeur n'est pas trouvée en tant que
    clé dans un dict Python ou dans un objet similaire.
    
    Vous avez essayé de récupérer un élément de `d` qui est un `dict` vide.
    
    Exception levée à la ligne `8` du fichier 'TESTS:\runtime\test_key_error.py'.
    
       5| def test_Popitem_empty_dict():
       6|     d = {}
       7|     try:
    -->8|         d.popitem()
                  ^^^^^^^^^^^
       9|     except KeyError as e:

            d:  {}
            d.popitem:  <builtin method popitem of dict object>
        


Similar names
~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_key_error.py", line 151, in test_Similar_names
        a = second["alpha"]
    KeyError: 'alpha'
    
        Vouliez-vous dire `'alpha0'` ?
        
    Une `KeyError` est levée lorsqu'une valeur n'est pas trouvée en tant que
    clé dans un dict Python ou dans un objet similaire.
    
    La clé `'alpha'` est introuvable dans le dict `second`.
    `second` a quelques clés similaires à `'alpha'` dont :
    `'alpha0', 'alpha11', 'alpha12'`.
    
    Exception levée à la ligne `151` du fichier 'TESTS:\runtime\test_key_error.py'.
    
       147|     assert ok, diff
       148| 
       149| second = {"alpha0": 1, "alpha11": 2, "alpha12": 3}
       150| try:
    -->151|     a = second["alpha"]
                    ^^^^^^^^^^^^^^^
       152| except KeyError as e:

            second:  {'alpha0': 1, 'alpha11': 2, 'alpha12': 3}
        


String by mistake
~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_key_error.py", line 102, in test_String_by_mistake
        d["(0, 0)"]
    KeyError: '(0, 0)'
    
        Avez-vous converti `(0, 0)` en une chaîne par erreur ?
        
    Une `KeyError` est levée lorsqu'une valeur n'est pas trouvée en tant que
    clé dans un dict Python ou dans un objet similaire.
    
    La clé `'(0, 0)'` est introuvable dans le dict `d`.
    `'(0, 0)'` est une chaîne de caractères.
    Il y a une clé de `d` dont la représentation en une chaîne
    est identique à `'(0, 0)'`.
    
    Exception levée à la ligne `102` du fichier 'TESTS:\runtime\test_key_error.py'.
    
        98| chain_map_string_by_mistake()  # do not show in docs
        99| 
       100| d = {(0, 0): "origin"}
       101| try:
    -->102|     d["(0, 0)"]
                ^^^^^^^^^^^
       103| except KeyError as e:

            d:  {(0, 0): 'origin'}
        


LookupError
-----------


Generic
~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_lookup_error.py", line 10, in test_Generic
        raise LookupError("Fake message")
    LookupError: Fake message
    
    `LookupError` est la classe de base pour les exceptions qui sont levées
    lorsqu’une clé ou un indice utilisé sur un tableau de correspondance ou une séquence est invalide.
    Elle peut également être levée directement par codecs.lookup().
    
    Exception levée à la ligne `10` du fichier 'TESTS:\runtime\test_lookup_error.py'.
    
        4| def test_Generic():
        5|     try:
        6|         # LookupError is the base class for KeyError and IndexError.
        7|         # It should normally not be raised by user code,
        8|         # other than possibly codecs.lookup(), which is why we raise
        9|         # it directly here for our example.
    -->10|         raise LookupError("Fake message")
       11|     except LookupError as e:

            LookupError:  <class LookupError>
        


ModuleNotFoundError
-------------------


Need to install module
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_module_not_found_error.py", line 80, in test_Need_to_install_module
        import alphabet
    ModuleNotFoundError: No module named 'alphabet'
    
    Une exception `ModuleNotFoundError` indique que vous
    essayez d’importer un module qui ne peut pas être trouvé par Python.
    Cela pourrait être parce que vous fait une faute d'orthographe en
    écrivant le nom du module, ou parce qu’il n’est pas installé sur votre ordinateur.
    
    Aucun module nommé `alphabet` ne peut être importé.
    Vous devez peut-être l'installer.
    
    Exception levée à la ligne `80` du fichier 'TESTS:\runtime\test_module_not_found_error.py'.
    
       78| def test_Need_to_install_module():
       79|     try:
    -->80|         import alphabet
       81|     except ModuleNotFoundError as e:


Not a package
~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_module_not_found_error.py", line 23, in test_Not_a_package
        import os.xxx
    ModuleNotFoundError: No module named 'os.xxx'; 'os' is not a package
    
    Une exception `ModuleNotFoundError` indique que vous
    essayez d’importer un module qui ne peut pas être trouvé par Python.
    Cela pourrait être parce que vous fait une faute d'orthographe en
    écrivant le nom du module, ou parce qu’il n’est pas installé sur votre ordinateur.
    
    `xxx` ne peut pas être importé de `os`.
    
    
    Exception levée à la ligne `23` du fichier 'TESTS:\runtime\test_module_not_found_error.py'.
    
       20| def test_Not_a_package():
       21| 
       22|     try:
    -->23|         import os.xxx
       24|     except ModuleNotFoundError as e:


Not a package similar name
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_module_not_found_error.py", line 37, in test_Not_a_package_similar_name
        import os.pathh
    ModuleNotFoundError: No module named 'os.pathh'; 'os' is not a package
    
        Vouliez-vous dire `import os.path` ?
        
    Une exception `ModuleNotFoundError` indique que vous
    essayez d’importer un module qui ne peut pas être trouvé par Python.
    Cela pourrait être parce que vous fait une faute d'orthographe en
    écrivant le nom du module, ou parce qu’il n’est pas installé sur votre ordinateur.
    
    Peut-être que vous vouliez dire `import os.path`.
    `path` est un nom semblable à `pathh` et est un module qui
    peut être importé de `os`.
    
    Exception levée à la ligne `37` du fichier 'TESTS:\runtime\test_module_not_found_error.py'.
    
       35| def test_Not_a_package_similar_name():
       36|     try:
    -->37|         import os.pathh
       38|     except ModuleNotFoundError as e:


Object not module
~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_module_not_found_error.py", line 51, in test_Object_not_module
        import os.open
    ModuleNotFoundError: No module named 'os.open'; 'os' is not a package
    
        Vouliez-vous dire `from os import open` ?
        
    Une exception `ModuleNotFoundError` indique que vous
    essayez d’importer un module qui ne peut pas être trouvé par Python.
    Cela pourrait être parce que vous fait une faute d'orthographe en
    écrivant le nom du module, ou parce qu’il n’est pas installé sur votre ordinateur.
    
    `open` n’est pas un module distinct, mais un objet qui fait partie de `os`.
    
    Exception levée à la ligne `51` du fichier 'TESTS:\runtime\test_module_not_found_error.py'.
    
       49| def test_Object_not_module():
       50|     try:
    -->51|         import os.open
       52|     except ModuleNotFoundError as e:

            open:  <builtin function open>
        


Similar object not module
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_module_not_found_error.py", line 65, in test_Similar_object_not_module
        import os.opend
    ModuleNotFoundError: No module named 'os.opend'; 'os' is not a package
    
        Vouliez-vous dire `from os import open` ?
        
    Une exception `ModuleNotFoundError` indique que vous
    essayez d’importer un module qui ne peut pas être trouvé par Python.
    Cela pourrait être parce que vous fait une faute d'orthographe en
    écrivant le nom du module, ou parce qu’il n’est pas installé sur votre ordinateur.
    
    Peut-être vouliez-vous dire `from os import open`.
    `open` est un nom similaire à `opend` et est un objet qui
    peut être importé de `os`.
    D’autres objets avec des noms similaires qui font partie de
    `os` comprennent `popen`.
    
    Exception levée à la ligne `65` du fichier 'TESTS:\runtime\test_module_not_found_error.py'.
    
       63| def test_Similar_object_not_module():
       64|     try:
    -->65|         import os.opend
       66|     except ModuleNotFoundError as e:


Standard library module
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_module_not_found_error.py", line 7, in test_Standard_library_module
        import Tkinter
    ModuleNotFoundError: No module named 'Tkinter'
    
        Vouliez-vous dire `tkinter` ?
        
    Une exception `ModuleNotFoundError` indique que vous
    essayez d’importer un module qui ne peut pas être trouvé par Python.
    Cela pourrait être parce que vous fait une faute d'orthographe en
    écrivant le nom du module, ou parce qu’il n’est pas installé sur votre ordinateur.
    
    Aucun module nommé `Tkinter` ne peut être importé.
    Vous devez peut-être l'installer.
    Les modules existants suivants ont des noms similaires 
    au module que vous avez essayé d’importer : `tkinter, _tkinter`
    
    Exception levée à la ligne `7` du fichier 'TESTS:\runtime\test_module_not_found_error.py'.
    
       5| def test_Standard_library_module():
       6|     try:
    -->7|         import Tkinter
       8|     except ModuleNotFoundError as e:


no curses
~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_module_not_found_error.py", line 97, in test_no_curses
        import curses
    ModuleNotFoundError: No module named '_curses'
    
        Le module curses est rarement installé avec Python sur Windows.
        
    Une exception `ModuleNotFoundError` indique que vous
    essayez d’importer un module qui ne peut pas être trouvé par Python.
    Cela pourrait être parce que vous fait une faute d'orthographe en
    écrivant le nom du module, ou parce qu’il n’est pas installé sur votre ordinateur.
    
    Vous avez essayé d’importer le module curses.
    Le module curses est rarement installé avec Python sur Windows.
    
    Exception levée à la ligne `97` du fichier 'TESTS:\runtime\test_module_not_found_error.py'.
    
       95| def test_no_curses():
       96|     try:
    -->97|         import curses
       98|     except ModuleNotFoundError as e:


NameError
---------


Annotated variable
~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_name_error.py", line 31, in test_Annotated_variable
        y = x
    NameError: name 'x' is not defined
    
        Avez-vous utilisé deux points au lieu d’un signe égal ?
        
    Une exception `NameError` indique que le nom d'une variable
    ou d'une fonction n'est pas connue par Python.
    Habituellement, ceci indique une simple faute d'orthographe.
    Cependant, cela peut également indiquer que le nom a été
    utilisé avant qu'on ne lui ait associé une valeur.
    
    Dans votre programme, aucun objet portant le nom `x` n'existe.
    Une annotation de type a été trouvée pour `x` dans la portée 'global'
    Peut-être que vous aviez utilisé deux points au lieu d’un signe égal et écrit
    
        x : 3
    
    au lieu de
    
        x = 3
    
    Exception levée à la ligne `31` du fichier 'TESTS:\runtime\test_name_error.py'.
    
       29| def test_Annotated_variable():
       30|     try:
    -->31|         y = x
                       ^
       32|     except NameError as e:


Custom name
~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_name_error.py", line 234, in test_Custom_name
        python
    NameError: name 'python' is not defined
    
        Vous utilisez déjà Python!
    Une exception `NameError` indique que le nom d'une variable
    ou d'une fonction n'est pas connue par Python.
    Habituellement, ceci indique une simple faute d'orthographe.
    Cependant, cela peut également indiquer que le nom a été
    utilisé avant qu'on ne lui ait associé une valeur.
    
    Vous utilisez déjà Python!
    Exception levée à la ligne `234` du fichier 'TESTS:\runtime\test_name_error.py'.
    
       232| def test_Custom_name():
       233|     try:
    -->234|         python
                    ^^^^^^
       235|     except NameError as e:


Free variable referenced
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_name_error.py", line 217, in test_Free_variable_referenced
        outer()
      File "TESTS:\runtime\test_name_error.py", line 213, in outer
        inner()
      File "TESTS:\runtime\test_name_error.py", line 212, in inner
        return var
    NameError: free variable 'var' referenced before assignment in enclosing scope. Did you mean: 'vars'?
    
    Une exception `NameError` indique que le nom d'une variable
    ou d'une fonction n'est pas connue par Python.
    Habituellement, ceci indique une simple faute d'orthographe.
    Cependant, cela peut également indiquer que le nom a été
    utilisé avant qu'on ne lui ait associé une valeur.
    
    Dans votre programme, `var` est un nom inconnu
    qui existe dans une portée englobante,
    mais qui n'a pas encore reçu de valeur.
    
    L'exécution s'est arrêtée à la ligne `217` du fichier 'TESTS:\runtime\test_name_error.py'
    
       213|     inner()
       214|     var = 4
       215| 
       216| try:
    -->217|     outer()
                ^^^^^^^
       218| except NameError as e:

            outer:  <function outer>
                defined in <function test_Free_variable_referenced>
        
    Exception levée à la ligne `212` du fichier 'TESTS:\runtime\test_name_error.py'.
    
       211| def inner():
    -->212|     return var
                       ^^^


Generic
~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_name_error.py", line 15, in test_Generic
        this = something
    NameError: name 'something' is not defined
    
    Une exception `NameError` indique que le nom d'une variable
    ou d'une fonction n'est pas connue par Python.
    Habituellement, ceci indique une simple faute d'orthographe.
    Cependant, cela peut également indiquer que le nom a été
    utilisé avant qu'on ne lui ait associé une valeur.
    
    Dans votre programme, aucun objet portant le nom `something` n'existe.
    Je n’ai pas d’informations supplémentaires pour vous.
    
    Exception levée à la ligne `15` du fichier 'TESTS:\runtime\test_name_error.py'.
    
       13| def test_Generic():
       14|     try:
    -->15|         this = something
                          ^^^^^^^^^
       16|     except NameError as e:


Missing import
~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_name_error.py", line 138, in test_Missing_import
        unicodedata.something
    NameError: name 'unicodedata' is not defined
    
        Avez-vous oublié d’importer `unicodedata` ?
        
    Une exception `NameError` indique que le nom d'une variable
    ou d'une fonction n'est pas connue par Python.
    Habituellement, ceci indique une simple faute d'orthographe.
    Cependant, cela peut également indiquer que le nom a été
    utilisé avant qu'on ne lui ait associé une valeur.
    
    
    Le nom `unicodedata` n’est pas défini dans votre programme.
    Peut-être avez-vous oublié d’importer `unicodedata` qui se trouve
    dans la bibliothèque standard de Python.
    
    
    Exception levée à la ligne `138` du fichier 'TESTS:\runtime\test_name_error.py'.
    
       134| if friendly_traceback.get_lang() == "en":
       135|     assert "I have no additional information for you." in result
       136| 
       137| try:
    -->138|     unicodedata.something
                ^^^^^^^^^^^
       139| except NameError as e:


Missing module name
~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_name_error.py", line 320, in test_Missing_module_name
        frame = Frame()
    NameError: name 'Frame' is not defined. Did you mean: 'frame'?
    
        Avez-vous oublié d’ajouter `tkinter.` ?
        
    Une exception `NameError` indique que le nom d'une variable
    ou d'une fonction n'est pas connue par Python.
    Habituellement, ceci indique une simple faute d'orthographe.
    Cependant, cela peut également indiquer que le nom a été
    utilisé avant qu'on ne lui ait associé une valeur.
    
    Dans votre programme, aucun objet portant le nom `Frame` n'existe.
    
    L’objet global `tkinter`
    a un attribut nommé `Frame`.
    Peut-être que vous auriez dû écrire `tkinter.Frame`
    au lieu de `Frame`.
    
    `Frame` est un nom trouvé dans les modules suivants :
    tkinter, tracemalloc.
    Vous avez peut-être oublié d'importer `Frame` de l'un de ces modules.
    
    Exception levée à la ligne `320` du fichier 'TESTS:\runtime\test_name_error.py'.
    
       317| @pytest.mark.skipif(not tkinter, reason="tkinter not present; likely MacOS")
       318| def test_Missing_module_name():
       319|     try:
    -->320|         frame = Frame()
                            ^^^^^
       321|     except NameError as e:


Missing self 1
~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_name_error.py", line 270, in test_Missing_self_1
        str(a)
      File "TESTS:\runtime\test_name_error.py", line 261, in __str__
        toys_list = add_toy(  # ensure that it can see 'self' on following line
    NameError: name 'add_toy' is not defined
    
        Avez-vous écrit `self` au mauvais endroit ?
        
    Une exception `NameError` indique que le nom d'une variable
    ou d'une fonction n'est pas connue par Python.
    Habituellement, ceci indique une simple faute d'orthographe.
    Cependant, cela peut également indiquer que le nom a été
    utilisé avant qu'on ne lui ait associé une valeur.
    
    Dans votre programme, aucun objet portant le nom `add_toy` n'existe.
    
    L’objet local `<Pet object> defined in <function test_name_error.test_Missing_self_1>` a un attribut nommé `add_toy`.
    Peut-être que vous auriez dû écrire `self.add_toy(...`
    au lieu de `add_toy(self, ...`.
    
    L'exécution s'est arrêtée à la ligne `270` du fichier 'TESTS:\runtime\test_name_error.py'
    
       266|             return "{} has no toys".format(self.name)
       267| 
       268| a = Pet('Fido')
       269| try:
    -->270|     str(a)
                ^^^^^^
       271| except NameError as e:

            a:  <Pet object>
                defined in <function test_name_error.test_Missing_self_1>
            str:  <class str>
        
    Exception levée à la ligne `261` du fichier 'TESTS:\runtime\test_name_error.py'.
    
       259| def __str__(self):
       260|     # self at the wrong place
    -->261|     toys_list = add_toy(  # ensure that it can see 'self' on following line
                            ^^^^^^^
       262|                         self, 'something')
       263|     if self.toys:


Missing self 2
~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_name_error.py", line 305, in test_Missing_self_2
        str(a)
      File "TESTS:\runtime\test_name_error.py", line 297, in __str__
        toys_list = add_toy('something')
    NameError: name 'add_toy' is not defined
    
        Avez-vous oublié d’ajouter `self.` ?
        
    Une exception `NameError` indique que le nom d'une variable
    ou d'une fonction n'est pas connue par Python.
    Habituellement, ceci indique une simple faute d'orthographe.
    Cependant, cela peut également indiquer que le nom a été
    utilisé avant qu'on ne lui ait associé une valeur.
    
    Dans votre programme, aucun objet portant le nom `add_toy` n'existe.
    
    Un objet local, `<Pet object> defined in <function test_name_error.test_Missing_self_2>`,
    a un attribut nommé `add_toy`.
    Peut-être que vous auriez dû écrire `self.add_toy`
    au lieu de `add_toy`.
    
    L'exécution s'est arrêtée à la ligne `305` du fichier 'TESTS:\runtime\test_name_error.py'
    
       301|             return "{} has no toys".format(self.name)
       302| 
       303| a = Pet('Fido')
       304| try:
    -->305|     str(a)
                ^^^^^^
       306| except NameError as e:

            a:  <Pet object>
                defined in <function test_name_error.test_Missing_self_2>
            str:  <class str>
        
    Exception levée à la ligne `297` du fichier 'TESTS:\runtime\test_name_error.py'.
    
       295| def __str__(self):
       296|     # Missing self.
    -->297|     toys_list = add_toy('something')
                            ^^^^^^^
       298|     if self.toys:


Synonym
~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_name_error.py", line 97, in test_Synonym
        cost  # wrote from math import * above
    NameError: name 'cost' is not defined. Did you mean: 'cos'?
    
        Vouliez-vous dire `cos` ?
        
    Une exception `NameError` indique que le nom d'une variable
    ou d'une fonction n'est pas connue par Python.
    Habituellement, ceci indique une simple faute d'orthographe.
    Cependant, cela peut également indiquer que le nom a été
    utilisé avant qu'on ne lui ait associé une valeur.
    
    Dans votre programme, aucun objet portant le nom `cost` n'existe.
    Au lieu d’écrire `cost`, peut-être que vous vouliez écrire l'un des noms suivants :
    *    Portée globale : `cos`, `cosh`
    
    Exception levée à la ligne `97` du fichier 'TESTS:\runtime\test_name_error.py'.
    
       93| if friendly_traceback.get_lang() == "en":
       94|     assert "The Python builtin `chr` has a similar name." in result
       95| 
       96| try:
    -->97|     cost  # wrote from math import * above
               ^^^^
       98| except NameError as e:


missing import2
~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_name_error.py", line 153, in test_missing_import2
        ABCMeta
    NameError: name 'ABCMeta' is not defined
    
    Une exception `NameError` indique que le nom d'une variable
    ou d'une fonction n'est pas connue par Python.
    Habituellement, ceci indique une simple faute d'orthographe.
    Cependant, cela peut également indiquer que le nom a été
    utilisé avant qu'on ne lui ait associé une valeur.
    
    Dans votre programme, aucun objet portant le nom `ABCMeta` n'existe.
    `ABCMeta` est un nom trouvé dans les modules suivants :
    selectors, typing, abc, numbers.
    Vous avez peut-être oublié d'importer `ABCMeta` de l'un de ces modules.
    
    Exception levée à la ligne `153` du fichier 'TESTS:\runtime\test_name_error.py'.
    
       151| def test_missing_import2():
       152|     try:
    -->153|         ABCMeta
                    ^^^^^^^
       154|     except NameError as e:


missing import3
~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_name_error.py", line 168, in test_missing_import3
        AF_APPLETALK
    NameError: name 'AF_APPLETALK' is not defined
    
    Une exception `NameError` indique que le nom d'une variable
    ou d'une fonction n'est pas connue par Python.
    Habituellement, ceci indique une simple faute d'orthographe.
    Cependant, cela peut également indiquer que le nom a été
    utilisé avant qu'on ne lui ait associé une valeur.
    
    Dans votre programme, aucun objet portant le nom `AF_APPLETALK` n'existe.
    `AF_APPLETALK` est un nom trouvé dans le module `socket`.
    Vous avez peut-être oublié d'écrire
    
        from socket import AF_APPLETALK
    
    Exception levée à la ligne `168` du fichier 'TESTS:\runtime\test_name_error.py'.
    
       166| def test_missing_import3():
       167|     try:
    -->168|         AF_APPLETALK
                    ^^^^^^^^^^^^
       169|     except NameError as e:


missing import from other 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_name_error.py", line 183, in test_missing_import_from_other_1
        plt.something
    NameError: name 'plt' is not defined
    
        Avez-vous oublié d'importer `matplotlib.pyplot` ?
        
    Une exception `NameError` indique que le nom d'une variable
    ou d'une fonction n'est pas connue par Python.
    Habituellement, ceci indique une simple faute d'orthographe.
    Cependant, cela peut également indiquer que le nom a été
    utilisé avant qu'on ne lui ait associé une valeur.
    
    
    Le nom `plt` n'est pas défini dans votre programme.
    Vous avez peut-être oublié d'écrire
    
        import matplotlib.pyplot as plt
    
    
    Exception levée à la ligne `183` du fichier 'TESTS:\runtime\test_name_error.py'.
    
       180| def test_missing_import_from_other_1():
       181|     friendly_traceback.add_other_module_names_synonyms({"plt": "matplotlib.pyplot"})
       182|     try:
    -->183|         plt.something
                    ^^^
       184|     except NameError as e:


missing import from other 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_name_error.py", line 197, in test_missing_import_from_other_2
        show()
    NameError: name 'show' is not defined
    
    Une exception `NameError` indique que le nom d'une variable
    ou d'une fonction n'est pas connue par Python.
    Habituellement, ceci indique une simple faute d'orthographe.
    Cependant, cela peut également indiquer que le nom a été
    utilisé avant qu'on ne lui ait associé une valeur.
    
    Dans votre programme, aucun objet portant le nom `show` n'existe.
    `show` est un nom trouvé dans les modules suivants :
    mailcap, matplotlib.pyplot, funny.
    Vous avez peut-être oublié d'importer `show` de l'un de ces modules.
    
    Exception levée à la ligne `197` du fichier 'TESTS:\runtime\test_name_error.py'.
    
       194| def test_missing_import_from_other_2():
       195|     friendly_traceback.add_other_attribute_names({"show": ["matplotlib.pyplot", "funny"] })
       196|     try:
    -->197|         show()
                    ^^^^
       198|     except NameError as e:


special keyword
~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_name_error.py", line 352, in test_special_keyword
        brek
    NameError: name 'brek' is not defined
    
        Vouliez-vous dire `break` ?
        
    Une exception `NameError` indique que le nom d'une variable
    ou d'une fonction n'est pas connue par Python.
    Habituellement, ceci indique une simple faute d'orthographe.
    Cependant, cela peut également indiquer que le nom a été
    utilisé avant qu'on ne lui ait associé une valeur.
    
    Cependant, je soupçonne que vous avez écrit le mot-clé `break` par erreur.
    
    Exception levée à la ligne `352` du fichier 'TESTS:\runtime\test_name_error.py'.
    
       349| if friendly_traceback.get_lang() == "en":
       350|     assert "Did you mean `continue`" in result
       351| try:
    -->352|     brek
                ^^^^
       353| except NameError as e:


OsError
-------


Urllib error
~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "PYTHON_LIB:\urllib\request.py", line 1348, in do_open
           ... Plus de lignes non affichées. ...
      File "PYTHON_LIB:\socket.py", line 824, in create_connection
        for res in getaddrinfo(host, port, 0, SOCK_STREAM):
      File "PYTHON_LIB:\socket.py", line 955, in getaddrinfo
        for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
    socket.gaierror: [Errno 11001] getaddrinfo failed
    
        During handling of the above exception, another exception occurred:
    
    Traceback (most recent call last):
      File "TESTS:\runtime\test_os_error.py", line 10, in test_Urllib_error
        request.urlopen("http://does_not_exist")
    URLError: <urlopen error [Errno 11001] getaddrinfo failed>
    
    Une exception de type `URLError` est une sous-classe de `OSError`.
    Rien de plus précis n'est connu au sujet de `URLError`.
    
    Une exception `OSError` est généralement levée par le système d’exploitation
    pour indiquer qu’une opération n’est pas autorisée ou
    qu'une ressource n’est pas disponible.
    
    Je soupçonne que vous essayez de vous connecter à un serveur et
    qu’une connexion ne peut être faite.
    
    Si c’est le cas, vérifiez les fautes de frappe dans l’URL
    et vérifiez votre connectivité Internet.
    
    Exception levée à la ligne `10` du fichier 'TESTS:\runtime\test_os_error.py'.
    
        6| @pytest.mark.skipif(random.randint(0, 50) < 59, reason="very long test")
        7| def test_Urllib_error():
        8|     from urllib import request, error
        9|     try:
    -->10|         request.urlopen("http://does_not_exist")
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
       11|     except error.URLError as e:

            request:  <module urllib.request> from PYTHON_LIB:\urllib\request.py
            request.urlopen:  <function urlopen>
        


invalid argument
~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_os_error.py", line 50, in test_invalid_argument
        open("c:\test.txt")
    OSError: [Errno 22] Invalid argument: 'c:\test.txt'
    
        Il faut peut-être doubler les caractères barres obliques inversées.
        
    Une exception `OSError` est généralement levée par le système d’exploitation
    pour indiquer qu’une opération n’est pas autorisée ou
    qu'une ressource n’est pas disponible.
    
    Je soupçonne que vous avez écrit un nom de fichier ou un chemin qui contient
    au moins un caractère Barre oblique inversée, `\`.
    Python a probablement interprété ce caractère comme indiquant le début de
    ce que l'on appelle une séquence d'échappement.
    Pour résoudre ce problème, écrivez une "chaîne brute" (raw string)
    en ajoutant la lettre `r` comme préfixe devant le nom de
    fichier ou du chemin d'accès, ou remplacer tous les caractères
    simples, `\`, par des caractères doubles : `\\`.
    
    Exception levée à la ligne `50` du fichier 'TESTS:\runtime\test_os_error.py'.
    
       47| if os.name != "nt":
       48|     return "Windows test only", "No result"
       49| try:
    -->50|     open("c:\test.txt")
               ^^^^^^^^^^^^^^^^^^^
       51| except OSError as e:

            open:  <builtin function open>
        


no information
~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_os_error.py", line 30, in test_no_information
        raise OSError("Some unknown message")
    OSError: Some unknown message
    
        Friendly-traceback ne connaît pas la cause de cette erreur.
        
    Une exception `OSError` est généralement levée par le système d’exploitation
    pour indiquer qu’une opération n’est pas autorisée ou
    qu'une ressource n’est pas disponible.
    
    Aucune information n’est disponible au sujet de cette exception.
    Veuillez signaler cet exemple à
    https://github.com/friendly-traceback/friendly-traceback/issues/new
    Si vous utilisez un REPL, utilisez `www('bug')` pour le faire.
    
    Si vous utilisez la console Friendly, utilisez `www()` pour
    faire une recherche sur Internet pour ce cas particulier.
    
    Exception levée à la ligne `30` du fichier 'TESTS:\runtime\test_os_error.py'.
    
       27| old_debug = friendly_traceback.debug_helper.DEBUG
       28| friendly_traceback.debug_helper.DEBUG = False
       29| try:
    -->30|     raise OSError("Some unknown message")
       31| except OSError as e:

            OSError:  <class OSError>
        


OverflowError
-------------


Generic
~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_overflow_error.py", line 6, in test_Generic
        2.0 ** 1600
    OverflowError: (34, 'Result too large')
    
    Une exception de type `OverflowError` est levée lorsque le résultat d’une opération arithmétique
    est trop grand pour être manipulé par le processeur de l’ordinateur.
    
    Exception levée à la ligne `6` du fichier 'TESTS:\runtime\test_overflow_error.py'.
    
       4| def test_Generic():
       5|     try:
    -->6|         2.0 ** 1600
                  ^^^^^^^^^^^
       7|     except OverflowError as e:


Huge lenght
~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_overflow_error.py", line 25, in test_Huge_lenght
        len(huge)
    OverflowError: Python int too large to convert to C ssize_t
    
    Une exception de type `OverflowError` est levée lorsque le résultat d’une opération arithmétique
    est trop grand pour être manipulé par le processeur de l’ordinateur.
    
    Exception levée à la ligne `25` du fichier 'TESTS:\runtime\test_overflow_error.py'.
    
       22| def test_Huge_lenght():
       23|     huge = range(1<<10000)
       24|     try:
    -->25|         len(huge)
                   ^^^^^^^^^
       26|     except OverflowError as e:

            huge:  range(0, ...)
                   len(huge): Objet trop grand pour être traité par Python.
        
            len:  <builtin function len>
        


RecursionError
--------------


Generic
~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_recursion_error.py", line 8, in test_Generic
        a()
           ... Plus de lignes non affichées. ...
      File "TESTS:\runtime\test_recursion_error.py", line 6, in a
        return a()
      File "TESTS:\runtime\test_recursion_error.py", line 6, in a
        return a()
    RecursionError: maximum recursion depth exceeded
    
    Une exception de type `RecursionError` est levée lorsqu’une fonction s'invoque elle-même,
    directement ou indirectement, trop de fois.
    Cette exception indique presque toujours que vous avez fait une erreur dans votre code
    et que votre programme ne terminerait jamais.
    
    L'exécution s'est arrêtée à la ligne `8` du fichier 'TESTS:\runtime\test_recursion_error.py'
    
       5| def a():
       6|     return a()
       7| try:
    -->8|     a()
              ^^^
       9| except RecursionError as e:

            a:  <function a> defined in <function test_Generic>
        
    Exception levée à la ligne `6` du fichier 'TESTS:\runtime\test_recursion_error.py'.
    
       5| def a():
    -->6|     return a()
                     ^^^

            a:  <function a> defined in <function test_Generic>
        


TypeError
---------


Argument of object is not iterable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 843, in test_Argument_of_object_is_not_iterable
        a in b
    TypeError: argument of type 'object' is not iterable
    
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Un itérable est un objet capable de retourner ses membres un par un.
    Les conteneurs Python (`list, tuple, dict`, etc.) sont des itérables.
    b' n'est pas un conteneur. Un conteneur est nécessaire ici.
    
    Exception levée à la ligne `843` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       840| a = object()
       841| b = object()
       842| try:
    -->843|     a in b
                ^^^^^^
       844| except TypeError as e:

            a:  <object object>
            b:  <object object>
        


Bad type for unary operator
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 427, in test_Bad_type_for_unary_operator
        a =+ "def"
    TypeError: bad operand type for unary +: 'str'
    
        Peut-être que vous vouliez plutôt écrire `+=` au lieu de `=+`
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Vous avez essayé d’utiliser l’opérateur unaire '+'
    avec le type d’objet suivant: une chaîne de caractères (`str`).
    Cette opération n’est pas définie pour ce type d’objet.
    
    Peut-être que vous vouliez plutôt écrire `+=` au lieu de `=+`
    
    Exception levée à la ligne `427` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       422|     assert "You tried to use the unary operator '~'" in result
       423| 
       424| try:
       425|     # fmt: off
       426|     a = "abc"
    -->427|     a =+ "def"
                   ^^^^^^^
       428|     # fmt: on


Builtin has no len
~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 901, in test_Builtin_has_no_len
        len("Hello world".split)
    TypeError: object of type 'builtin_function_or_method' has no len()
    
        Avez-vous oublié d’invoquer `"Hello world".split` ?
        
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Je soupçonne que vous avez oublié d’ajouter des parenthèses pour invoquer `"Hello world".split`.
    Vous avez peut-être voulu écrire :
    `len("Hello world".split())`
    
    Exception levée à la ligne `901` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       899| def test_Builtin_has_no_len():
       900|     try:
    -->901|         len("Hello world".split)
                    ^^^^^^^^^^^^^^^^^^^^^^^^
       902|     except TypeError as e:

            len:  <builtin function len>
            "Hello world".split:  <builtin method split of str object>
        


Can only concatenate
~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 39, in test_Can_only_concatenate
        result = a_tuple + a_list
    TypeError: can only concatenate tuple (not "list") to tuple
    
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Vous avez essayé de concaténer (additionner) deux types d’objets différents:
    un `tuple` et une liste (`list`).
    
    Exception levée à la ligne `39` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       36| try:
       37|     a_tuple = (1, 2, 3)
       38|     a_list = [1, 2, 3]
    -->39|     result = a_tuple + a_list
                        ^^^^^^^^^^^^^^^^
       40| except TypeError as e:

            a_list:  [1, 2, 3]
            a_tuple:  (1, 2, 3)
        


Cannot convert dictionary update sequence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 886, in test_Cannot_convert_dictionary_update_sequence
        dd.update([1, 2, 3])
    TypeError: cannot convert dictionary update sequence element #0 to a sequence
    
        Peut-être que vous vouliez plutôt utiliser la méthode `dict.fromkeys()`.
        
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    `dict.update()` n’accepte pas une séquence comme argument.
    Au lieu d’écrire `dd.update([1, 2, 3])`
    peut-être devriez-vous utiliser la méthode `dict.fromkeys()` : `dd.update( dict.fromkeys([1, 2, 3]) )`.
    
    Exception levée à la ligne `886` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       882|     assert "you should use the `dict.fromkeys()`" in result
       883| 
       884| dd = {"a": "a"}
       885| try:
    -->886|     dd.update([1, 2, 3])
                ^^^^^^^^^^^^^^^^^^^^
       887| except TypeError as e:

            dd:  {'a': 'a'}
            dd.update:  <builtin method update of dict object>
        


Cannot multiply by non int
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 652, in test_Cannot_multiply_by_non_int
        "a" * "2"
    TypeError: can't multiply sequence by non-int of type 'str'
    
        Avez-vous oublié de convertir `"2"` en un entier ?
        
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Vous ne pouvez multiplier les séquences, telles que
    les listes, les tuples, les chaînes, etc., que par des entiers.
    Peut-être avez-vous oublié de convertir `"2"` en un entier.
    
    Exception levée à la ligne `652` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       648| if friendly_traceback.get_lang() == "en":
       649|     assert "Did you forget to convert `c` into an integer?" in result
       650| 
       651| try:
    -->652|     "a" * "2"
                ^^^^^^^^^
       653| except TypeError as e:


Cannot unpack non iterable object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 857, in test_Cannot_unpack_non_iterable_object
        a, b = 42.0
    TypeError: cannot unpack non-iterable float object
    
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Le dépaquetage ('unpack') est un moyen pratique d’attribuer un nom
    à chaque élément d’un itérable.
    Un itérable est un objet capable de renvoyer ses membres un à la fois.
    Les contenants python (`list, tuple, dict`, etc.) sont itérables,
    mais pas les objets de type `float`.
    
    Exception levée à la ligne `857` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       855| def test_Cannot_unpack_non_iterable_object():
       856|     try:
    -->857|         a, b = 42.0
       858|     except TypeError as e:


Cant mod complex numbers
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 54, in test_Cant_mod_complex_numbers
        3 + 3j % 2
    TypeError: unsupported operand type(s) for %: 'complex' and 'int'
    
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Vous ne pouvez pas utiliser des nombres complexes avec l'opérateur modulo `%`.
    
    Exception levée à la ligne `54` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       52| def test_Cant_mod_complex_numbers():
       53|     try:
    -->54|         3 + 3j % 2
                       ^^^^^^
       55|     except TypeError as e:


Comparison not supported
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 375, in test_Comparison_not_supported
        b >= a
    TypeError: '>=' not supported between instances of 'int' and 'str'
    
        Avez-vous oublié de convertir `a` en un entier (`int`) ?
        
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    En utilisant >=, vous avez tenté de comparer
    deux types d’objets incompatibles:
    un entier (`int`) et une chaîne de caractères (`str`).
    Peut-être avez-vous oublié de convertir `a` en un entier (`int`).
    
    Exception levée à la ligne `375` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       372| try:
       373|     a = "2"
       374|     b = 42
    -->375|     b >= a
                ^^^^^^
       376| except TypeError as e:

            a:  '2'
            b:  42
        


Derive from BaseException
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 594, in test_Derive_from_BaseException
        raise "exception"  # noqa
    TypeError: exceptions must derive from BaseException
    
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Les exceptions doivent être dérivées de `BaseException`.
    Il est recommandé que les exceptions que vous définissez dérivent
    d'`Exception`, une sous-classe de `BaseException`.
    
    Exception levée à la ligne `594` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       590| if friendly_traceback.get_lang() == "en":
       591|     assert "you must only have classes that derive from `BaseException`" in result
       592| 
       593| try:
    -->594|     raise "exception"  # noqa
       595| except TypeError as e:


Generator has no len
~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 1062, in test_Generator_has_no_len
        nb = len(letter
    TypeError: object of type 'generator' has no len()
    
        Vous devez d'abord établir une liste.
        
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Je suppose que vous essayiez de compter le nombre d'éléments
    produits par une expression de générateur. Vous devez d'abord les capturer
    dans une liste :
    
        len([letter                 for letter in "word"])
    
    Exception levée à la ligne `1062` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       1060| def test_Generator_has_no_len():
       1061|     try:
    -->1062|         nb = len(letter
                          ^^^^^^^^^^
       1063|                  for letter in "word")
                              ^^^^^^^^^^^^^^^^^^^^^
       1064|     except TypeError as e:

            len:  <builtin function len>
        


Indices must be integers or slices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 736, in test_Indices_must_be_integers_or_slices
        [1, 2, 3]["2"]
    TypeError: list indices must be integers or slices, not str
    
        Avez-vous oublié de convertir `"2"` en un entier ?
        
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Dans l’expression `[1, 2, 3]["2"]`
    ce qui est inclus entre les crochets, `[...]`,
    doit être soit un entier ou une tranche
    (`start:stop` ou `start:stop:step`) 
    et vous l’avez utilisé une chaîne de caractères (`str`) la place.
    
    Peut-être avez-vous oublié de convertir `"2"` en un entier.
    
    Exception levée à la ligne `736` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       732| if friendly_traceback.get_lang() == "en":
       733|     assert "Perhaps you forgot to convert `2.0` into an integer." in result
       734| 
       735| try:
    -->736|     [1, 2, 3]["2"]
                ^^^^^^^^^^^^^^
       737| except TypeError as e:


Not an integer
~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 698, in test_Not_an_integer
        range(c, d)
    TypeError: 'str' object cannot be interpreted as an integer
    
        Avez-vous oublié de convertir `c, d` en entiers ?
        
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Vous avez écrit un objet de type `str` là où un entier était attendu.
    Peut-être avez-vous oublié de convertir `c, d` en entiers.
    Exception levée à la ligne `698` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       694|     assert "Perhaps you forgot to convert `1.0" in result
       695| 
       696| c, d = "2", "3"
       697| try:
    -->698|     range(c, d)
                ^^^^^^^^^^^
       699| except TypeError as e:

            c:  '2'
            d:  '3'
            range:  <class range>
        


Not callable
~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 561, in test_Not_callable
        _ = [1, 2](a + b)
    TypeError: 'list' object is not callable
    
        Vouliez-vous dire `[1, 2][a + b]` ?
        
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    En raison des parenthees, `(a + b)` est interprété par Python
    comme indiquant une invocation de fonction pour 
    `[1, 2]`, qui est un objet de type `list`
    ne pouvant pas être invoqué.
    
    Cependant, `[1, 2]` est une séquence.
    Peut-être que vous vouliez utiliser `[]` au lieu de `()` et écrire
    `[1, 2][a + b]`
    
    Exception levée à la ligne `561` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       557|     assert "b.a_list[3]" in result
       558| 
       559| try:
       560|     a, b = 3, 7
    -->561|     _ = [1, 2](a + b)
                    ^^^^^^^^^^^^^
       562| except TypeError as e:

            a:  3
            b:  7
            a + b:  10
        


Object is not iterable
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 826, in test_Object_is_not_iterable
        list(42)
    TypeError: 'int' object is not iterable
    
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Un itérable est un objet capable de renvoyer ses membres un à la fois.
    Les contenants python (`list, tuple, dict`, etc.) sont itérables.
    Une itérable est requis ici.
    
    Exception levée à la ligne `826` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       824| def test_Object_is_not_iterable():
       825|     try:
    -->826|         list(42)
                    ^^^^^^^^
       827|     except TypeError as e:

            list:  <class list>
        


Object is not subscriptable
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 811, in test_Object_is_not_subscriptable
        a = f[1]
    TypeError: 'function' object is not subscriptable
    
        Vouliez-vous dire `f(1)` ?
        
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Les objets subscriptibles sont généralement des conteneurs à partir
    desquels on peut tirer des éléments en utilisant la notation `[...]`.
    
    Peut-être que vous vouliez plutôt écrire `f(1)`.
    
    Exception levée à la ligne `811` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       807| def f():
       808|     pass
       809| 
       810| try:
    -->811|     a = f[1]
                    ^^^^
       812| except TypeError as e:

            f:  <function f>
                defined in <function test_Object_is_not_subscriptable>
        


Slice indices must be integers or None
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 751, in test_Slice_indices_must_be_integers_or_None
        [1, 2, 3][1.0:2.0]
    TypeError: slice indices must be integers or None or have an __index__ method
    
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Lors de l’utilisation d’une tranche pour extraire une gamme d’éléments
    d’une séquence, c’est-à-dire quelque chose comme
    `[start:stop]` ou `[start:stop:step]`
    chacune des variables `start`, `stop`, et `step` doit être soit un entier, soit `None`,
    ou possiblement un autre objet ayant une méthode `__index__`.
    
    Exception levée à la ligne `751` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       749| def test_Slice_indices_must_be_integers_or_None():
       750|     try:
    -->751|         [1, 2, 3][1.0:2.0]
                    ^^^^^^^^^^^^^^^^^^
       752|     except TypeError as e:


Too few positional argument
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 500, in test_Too_few_positional_argument
        fn(1)
    TypeError: test_Too_few_positional_argument.<locals>.fn() missing 2 required positional arguments: 'b' and 'c'
    
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Vous avez apparemment invoqué la fonction 'test_Too_few_positional_argument.<locals>.fn()' avec
    moins d'arguments positionnels qu'il n'en faut (2 manquent).
    
    Exception levée à la ligne `500` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       496| def fn(a, b, c):
       497|     pass
       498| 
       499| try:
    -->500|     fn(1)
                ^^^^^
       501| except TypeError as e:

            fn:  <function fn>
                defined in <function test_Too_few_positional_argument>
        


Too many positional argument
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 480, in test_Too_many_positional_argument
        A().f(1)
    TypeError: test_Too_many_positional_argument.<locals>.A.f() takes 1 positional argument but 2 were given
    
        Peut-être avez-vous oublié `self` lors de la définition de `A.f`.
        
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Vous avez apparemment invoqué la fonction `A.f` avec
    2 arguments positionnels alors qu'elle en requiert 1.
    Peut-être avez-vous oublié `self` lors de la définition de `A.f`.
    
    Exception levée à la ligne `480` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       476|     def f(x):
       477|         pass
       478| 
       479| try:
    -->480|     A().f(1)
                ^^^^^^^^
       481| except TypeError as e:

            A:  <class A>
                defined in <function test_type_error.test_Too_many_positional_argument>
        


Tuple no item assignment
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 446, in test_Tuple_no_item_assignment
        a[0] = 0
    TypeError: 'tuple' object does not support item assignment
    
        Voulez-vous utiliser une liste?
        
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Dans Python, certains objets sont connus comme immuables:
    une fois définis, leur valeur ne peut pas être modifiée.
    Vous avez essayé de modifier une partie d’un tel objet immuable: un `tuple`,
    probablement en utilisant une opération d’indexation.
    Peut-être que vous vouliez plutôt utiliser une liste.
    
    Exception levée à la ligne `446` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       443| def test_Tuple_no_item_assignment():
       444|     a = (1, 2, 3)
       445|     try:
    -->446|         a[0] = 0
                    ^^^^
       447|     except TypeError as e:

            a:  (1, 2, 3)
            a[0]:  1
        


Unhachable type
~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 769, in test_Unhachable_type
        {[1, 2]: 1}
    TypeError: unhashable type: 'list'
    
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Seuls les objets hachables peuvent être utilisés
    comme éléments de `set` ou des clés de `dict`.
    Les objets hachables sont des objets qui ne changent pas de valeur
    une fois qu’ils ont été créés.Au lieu d’utiliser une liste (`list`), envisagez d’utiliser un `tuple`.
    
    Exception levée à la ligne `769` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       767| def test_Unhachable_type():
       768|     try:
    -->769|         {[1, 2]: 1}
       770|     except TypeError as e:


Unsupported operand types
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 325, in test_Unsupported_operand_types
        a @= b
    TypeError: unsupported operand type(s) for @=: 'str' and 'int'
    
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Vous avez essayé d’utiliser l’opérateur @=
    à l’aide de deux types d’objets incompatibles:
    une chaîne de caractères (`str`) et un entier (`int`).
    Cet opérateur est normalement utilisé uniquement
    pour la multiplication des matrices.
    
    Exception levée à la ligne `325` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       322| try:
       323|     a = "a"
       324|     b = 2
    -->325|     a @= b
       326| except TypeError as e:

            a:  'a'
            b:  2
        


divmod
~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 69, in test_divmod
        result = divmod(a, b)
    TypeError: unsupported operand type(s) for divmod(): 'int' and 'complex'
    
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Les arguments de `divmod` doivent être des nombres entiers (`int`) ou réels (`float`).
    Au moins un des arguments était un nombre complexe.
    
    Exception levée à la ligne `69` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       66| a = 2
       67| b = 3 + 2j
       68| try:
    -->69|     result = divmod(a, b)
                        ^^^^^^^^^^^^
       70| except TypeError as e:

            a:  2
            b:  (3+2j)
            divmod:  <builtin function divmod>
        


function got multiple argument
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 996, in test_function_got_multiple_argument
        fn2(0, a=1)
    TypeError: test_function_got_multiple_argument.<locals>.fn2() got multiple values for argument 'a'
    
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Vous avez spécifié la valeur de l'argument `a` plus d'une fois
    lors de l'appel de la fonction nommée `fn2`.
    Cette fonction a les arguments suivants :
    `a, b=1`
    
    Exception levée à la ligne `996` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       992| def fn2(a, b=1):
       993|     pass
       994| 
       995| try:
    -->996|     fn2(0, a=1)
                ^^^^^^^^^^^
       997| except TypeError as e:

            fn2:  <function fn2>
                defined in <function test_function_got_multiple_argument>
        


function has no len
~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 919, in test_function_has_no_len
        len(bad)
    TypeError: object of type 'function' has no len()
    
        Avez-vous oublié d’invoquer `bad` ?
        
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Je soupçonne que vous avez oublié d’ajouter des parenthèses pour invoquer `bad`.
    Vous avez peut-être voulu écrire :
    `len(bad())`
    
    Exception levée à la ligne `919` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       915| def bad():
       916|     pass
       917| 
       918| try:
    -->919|     len(bad)
                ^^^^^^^^
       920| except TypeError as e:

            bad:  <function bad> defined in <function test_function_has_no_len>
            len:  <builtin function len>
        


getattr attribute name must be string
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 1044, in test_getattr_attribute_name_must_be_string
        getattr("__repr__", 1)  # as reported in issue #77
    TypeError: getattr(): attribute name must be string
    
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Le deuxième argument de la fonction `getattr()` doit être une chaîne de caractères.
    
    Exception levée à la ligne `1044` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       1037| if friendly_traceback.get_lang() == "en":
       1038|     assert (
       1039|         "The second argument of the function `hasattr()` must be a string."
       1040|         in result
       1041|     )
       1042| 
       1043| try:
    -->1044|     getattr("__repr__", 1)  # as reported in issue #77
                 ^^^^^^^^^^^^^^^^^^^^^^
       1045| except TypeError as e:

            getattr:  <builtin function getattr>
        


method got multiple argument
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 1016, in test_method_got_multiple_argument
        t.some_method(0, a=1)
    TypeError: test_method_got_multiple_argument.<locals>.T.some_method() got multiple values for argument 'a'
    
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    Vous avez spécifié la valeur de l'argument `a` plus d'une fois
    lors de l'appel de la fonction nommée `t.some_method`.
    Cette fonction n'a qu'un seul argument : `a`
    
    Exception levée à la ligne `1016` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       1012|         pass
       1013| 
       1014| t = T()
       1015| try:
    -->1016|     t.some_method(0, a=1)
                 ^^^^^^^^^^^^^^^^^^^^^
       1017| except TypeError as e:

            t:  <T object>
                defined in <function test_type_error.test_method_got_multiple_argument>
            t.some_method:  <bound method T.some_method>
                of <T object>
                defined in <function test_type_error.test_method_got_multiple_argument>
        


vars arg must have dict
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_type_error.py", line 964, in test_vars_arg_must_have_dict
        vars(f)
    TypeError: vars() argument must have __dict__ attribute
    
    Une exception `TypeError` est généralement causée par une tentative
    de combiner deux types d’objets incompatibles,
    en invoquant une fonction avec le mauvais type d’objet,
    ou en tentant d'effectuer une opération non permise sur un type d'objet donné.
    
    La fonction `vars` est utilisée pour lister le contenu
    de l'attribut `__dict__` d'un objet.
    L'objet `f` utilise `__slots__` au lieu de `__dict__`.
    
    Exception levée à la ligne `964` du fichier 'TESTS:\runtime\test_type_error.py'.
    
       960|     assert no_slots not in result
       961|     assert use_slots not in result
       962| 
       963| try:
    -->964|     vars(f)
                ^^^^^^^
       965| except TypeError as e:

            f:  <F object>
                defined in <function test_type_error.test_vars_arg_must_have_dict>
            vars:  <builtin function vars>
        


UnboundLocalError
-----------------


Missing both
~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_unbound_local_error.py", line 65, in test_Missing_both
        outer_missing_both()
      File "TESTS:\runtime\test_unbound_local_error.py", line 22, in outer_missing_both
        inner()
      File "TESTS:\runtime\test_unbound_local_error.py", line 21, in inner
        spam_missing_both += 1
    UnboundLocalError: local variable 'spam_missing_both' referenced before assignment
    
        Avez-vous oublié d’ajouter soit `global spam_missing_both` ou 
        `nonlocal spam_missing_both` ?
        
    En Python, les variables utilisées à l’intérieur d’une fonction sont appelées
    variables «locales».
    Avant d’utiliser une variable locale, une valeur doit lui être attribuée.
    Une variable utilisée avant l’attribution d’une valeur est supposée
    être définie en dehors de cette fonction;
    elle est connu comme une variable «globale» (`global` ou parfois `nonlocal`).
    Vous ne pouvez pas assigner une valeur à une telle variable globale
    à l’intérieur d’une fonction sans d’abord confirmer à python
    qu’il s’agit d’une variable globale, sinon vous verrez une exception `UnboundLocalError`.
    
    Vous essayez d'utiliser le nom `spam_missing_both` identifié par Python comme se trouvant
    dans la portée locale d'une fonction avant de lui avoir attribué une valeur.
    
    Le nom `spam_missing_both` existe à la fois dans la portée globale et non locale.
    Cela peut être assez déroutant et n’est pas recommandé.
    Selon la variable à laquelle vous vouliez vous référer, vous deviez ajouter
    
        global spam_missing_both
    
    ou
    
        nonlocal spam_missing_both
    
    comme la première ligne à l’intérieur de votre fonction.
    
    L'exécution s'est arrêtée à la ligne `65` du fichier 'TESTS:\runtime\test_unbound_local_error.py'
    
       63| def test_Missing_both():
       64|     try:
    -->65|         outer_missing_both()
                   ^^^^^^^^^^^^^^^^^^^^
       66|     except UnboundLocalError as e:

            global outer_missing_both:  <function outer_missing_both>
        
    Exception levée à la ligne `21` du fichier 'TESTS:\runtime\test_unbound_local_error.py'.
    
       20| def inner():
    -->21|     spam_missing_both += 1

            global spam_missing_both:  1
        


Missing global
~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_unbound_local_error.py", line 27, in test_Missing_global
        outer_missing_global()
      File "TESTS:\runtime\test_unbound_local_error.py", line 10, in outer_missing_global
        inner()
      File "TESTS:\runtime\test_unbound_local_error.py", line 9, in inner
        spam_missing_global += 1
    UnboundLocalError: local variable 'spam_missing_global' referenced before assignment
    
        Avez-vous oublié d’ajouter `global spam_missing_global` ?
        
    En Python, les variables utilisées à l’intérieur d’une fonction sont appelées
    variables «locales».
    Avant d’utiliser une variable locale, une valeur doit lui être attribuée.
    Une variable utilisée avant l’attribution d’une valeur est supposée
    être définie en dehors de cette fonction;
    elle est connu comme une variable «globale» (`global` ou parfois `nonlocal`).
    Vous ne pouvez pas assigner une valeur à une telle variable globale
    à l’intérieur d’une fonction sans d’abord confirmer à python
    qu’il s’agit d’une variable globale, sinon vous verrez une exception `UnboundLocalError`.
    
    Vous essayez d'utiliser le nom `spam_missing_global` identifié par Python comme se trouvant
    dans la portée locale d'une fonction avant de lui avoir attribué une valeur.
    
    Le nom `spam_missing_global` existe dans la portée global.
    Peut-être la déclaration
    
        global spam_missing_global
    
    aurait dû être incluse comme première ligne à l’intérieur de votre fonction.
    
    L'exécution s'est arrêtée à la ligne `27` du fichier 'TESTS:\runtime\test_unbound_local_error.py'
    
       25| def test_Missing_global():
       26|     try:
    -->27|         outer_missing_global()
                   ^^^^^^^^^^^^^^^^^^^^^^
       28|     except UnboundLocalError as e:

            global outer_missing_global:  <function outer_missing_global>
        
    Exception levée à la ligne `9` du fichier 'TESTS:\runtime\test_unbound_local_error.py'.
    
       8| def inner():
    -->9|     spam_missing_global += 1

            global spam_missing_global:  1
        


Missing nonlocal
~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_unbound_local_error.py", line 46, in test_Missing_nonlocal
        outer_missing_nonlocal()
      File "TESTS:\runtime\test_unbound_local_error.py", line 16, in outer_missing_nonlocal
        inner()
      File "TESTS:\runtime\test_unbound_local_error.py", line 15, in inner
        spam_missing_nonlocal += 1
    UnboundLocalError: local variable 'spam_missing_nonlocal' referenced before assignment
    
        Avez-vous oublié d’ajouter `nonlocal spam_missing_nonlocal` ?
        
    En Python, les variables utilisées à l’intérieur d’une fonction sont appelées
    variables «locales».
    Avant d’utiliser une variable locale, une valeur doit lui être attribuée.
    Une variable utilisée avant l’attribution d’une valeur est supposée
    être définie en dehors de cette fonction;
    elle est connu comme une variable «globale» (`global` ou parfois `nonlocal`).
    Vous ne pouvez pas assigner une valeur à une telle variable globale
    à l’intérieur d’une fonction sans d’abord confirmer à python
    qu’il s’agit d’une variable globale, sinon vous verrez une exception `UnboundLocalError`.
    
    Vous essayez d'utiliser le nom `spam_missing_nonlocal` identifié par Python comme se trouvant
    dans la portée locale d'une fonction avant de lui avoir attribué une valeur.
    
    Le nom `spam_missing_nonlocal` existe dans la portée nonlocal.
    Peut-être la déclaration
    
        nonlocal spam_missing_nonlocal
    
    aurait dû être incluse comme première ligne à l’intérieur de votre fonction.
    
    L'exécution s'est arrêtée à la ligne `46` du fichier 'TESTS:\runtime\test_unbound_local_error.py'
    
       44| def test_Missing_nonlocal():
       45|     try:
    -->46|         outer_missing_nonlocal()
                   ^^^^^^^^^^^^^^^^^^^^^^^^
       47|     except UnboundLocalError as e:

            global outer_missing_nonlocal:  <function outer_missing_nonlocal>
        
    Exception levée à la ligne `15` du fichier 'TESTS:\runtime\test_unbound_local_error.py'.
    
       14| def inner():
    -->15|     spam_missing_nonlocal += 1


Typo in local
~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_unbound_local_error.py", line 104, in test_Typo_in_local
        test2()
      File "TESTS:\runtime\test_unbound_local_error.py", line 101, in test2
        alpha3 += 1
    UnboundLocalError: local variable 'alpha3' referenced before assignment
    
        Vouliez-vous dire `alpha1` ?
        
    En Python, les variables utilisées à l’intérieur d’une fonction sont appelées
    variables «locales».
    Avant d’utiliser une variable locale, une valeur doit lui être attribuée.
    Une variable utilisée avant l’attribution d’une valeur est supposée
    être définie en dehors de cette fonction;
    elle est connu comme une variable «globale» (`global` ou parfois `nonlocal`).
    Vous ne pouvez pas assigner une valeur à une telle variable globale
    à l’intérieur d’une fonction sans d’abord confirmer à python
    qu’il s’agit d’une variable globale, sinon vous verrez une exception `UnboundLocalError`.
    
    Au lieu d’écrire `alpha3`, peut-être que vous vouliez écrire l'un des noms suivants :
    *    Portée locale : `alpha1`, `alpha2`
    
    L'exécution s'est arrêtée à la ligne `104` du fichier 'TESTS:\runtime\test_unbound_local_error.py'
    
       100|     alpha2 = 1
       101|     alpha3 += 1
       102| 
       103| try:
    -->104|     test2()
                ^^^^^^^
       105| except UnboundLocalError as e:

            test2:  <function test2> defined in <function test_Typo_in_local>
        
    Exception levée à la ligne `101` du fichier 'TESTS:\runtime\test_unbound_local_error.py'.
    
        98| def test2():
        99|     alpha1 = 1
       100|     alpha2 = 1
    -->101|     alpha3 += 1


Using name of builtin
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_unbound_local_error.py", line 125, in test_Using_name_of_builtin
        dist([])
      File "TESTS:\runtime\test_unbound_local_error.py", line 121, in dist
        max = max(points)
    UnboundLocalError: local variable 'max' referenced before assignment
    
    En Python, les variables utilisées à l’intérieur d’une fonction sont appelées
    variables «locales».
    Avant d’utiliser une variable locale, une valeur doit lui être attribuée.
    Une variable utilisée avant l’attribution d’une valeur est supposée
    être définie en dehors de cette fonction;
    elle est connu comme une variable «globale» (`global` ou parfois `nonlocal`).
    Vous ne pouvez pas assigner une valeur à une telle variable globale
    à l’intérieur d’une fonction sans d’abord confirmer à python
    qu’il s’agit d’une variable globale, sinon vous verrez une exception `UnboundLocalError`.
    
    `max` est une fonction Python de type 'builtin'.
    Vous avez essayé d'attribuer une valeur à `max` dans une fonction
    tout en utilisant sa signification originale dans cette même fonction.
    
    Notez que ce n'est généralement pas une bonne idée de donner à une variable locale
    le même nom qu'une fonction Python de type 'builtin' (comme `max`).
    
    L'exécution s'est arrêtée à la ligne `125` du fichier 'TESTS:\runtime\test_unbound_local_error.py'
    
       122|     min = min(points)
       123|     return max - min
       124| try:
    -->125|     dist([])
                ^^^^^^^^
       126| except UnboundLocalError as e:

            dist:  <function dist> defined in <function test_Using_name_of_builtin>
        
    Exception levée à la ligne `121` du fichier 'TESTS:\runtime\test_unbound_local_error.py'.
    
       120| def dist(points):
    -->121|     max = max(points)
                      ^^^
       122|     min = min(points)

            max:  <builtin function max>
        


UnknownError
------------


Generic
~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_unknown_error.py", line 24, in test_Generic
        raise UnknownException("Some informative message about an unknown exception.")
    UnknownException: Some informative message about an unknown exception.
    
    Une exception de type `UnknownException` est une sous-classe de `Exception`.
    Rien de plus précis n'est connu au sujet de `UnknownException`.
    
    Toutes les exceptions intégrées définies par Python sont dérivées de `Exception`.
    Toutes les exceptions définies par l'utilisateur doivent également être dérivées de cette classe.
    
    Exception levée à la ligne `24` du fichier 'TESTS:\runtime\test_unknown_error.py'.
    
       20| result = friendly_traceback.get_output()
       21| assert "UnknownException -> Exception" in result
       22| 
       23| try:
    -->24|     raise UnknownException("Some informative message about an unknown exception.")
       25| except Exception as e:

            global UnknownException:  <class test_unknown_error.UnknownException>
        


ValueError
----------


Convert to int
~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_value_error.py", line 194, in test_Convert_to_int
        int('13a')
    ValueError: invalid literal for int() with base 10: '13a'
    
    Une exception `ValueError` indique qu'une fonction ou une opération
    a reçu un argument du bon type, mais une valeur inappropriée.
    
    `'13a'` est un argument invalide pour `int()` dans la base `10`.
    En base `10`, `int()` est le plus souvent utilisé pour convertir une chaîne de caractères
    contenant les chiffres `0` à `9` en un nombre entier.
    Les caractères suivants ne sont pas permis : `a`.
    
    Exception levée à la ligne `194` du fichier 'TESTS:\runtime\test_value_error.py'.
    
       190| if english:
       191|     assert "needs to be first converted using `float()`" in result
       192| 
       193| try:
    -->194|     int('13a')
                ^^^^^^^^^^
       195| except ValueError as e:

            int:  <class int>
        


Could not convert to float
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_value_error.py", line 92, in test_Could_not_convert_to_float
        float("42b")
    ValueError: could not convert string to float: '42b'
    
    Une exception `ValueError` indique qu'une fonction ou une opération
    a reçu un argument du bon type, mais une valeur inappropriée.
    
    La chaîne de caractères `42b` ne peut pas être convertie en `float`
    car elle ne représente pas un nombre.
    
    Exception levée à la ligne `92` du fichier 'TESTS:\runtime\test_value_error.py'.
    
       90| def test_Could_not_convert_to_float():
       91|     try:
    -->92|         float("42b")
                   ^^^^^^^^^^^^
       93|     except ValueError as e:

            float:  <class float>
        


Date invalid month
~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_value_error.py", line 60, in test_Date_invalid_month
        d = date(2021, 13, 1)
    ValueError: month must be in 1..12
    
        Avez-vous spécifié un mois inexistant ?
        
    Une exception `ValueError` indique qu'une fonction ou une opération
    a reçu un argument du bon type, mais une valeur inappropriée.
    
    Je crois que vous avez indiqué une valeur non valide pour le mois
    dans un objet de type `date`. Les valeurs valides sont les entiers de 1 à 12.
    
    Exception levée à la ligne `60` du fichier 'TESTS:\runtime\test_value_error.py'.
    
       57| def test_Date_invalid_month():
       58|     from datetime import date
       59|     try:
    -->60|         d = date(2021, 13, 1)
                       ^^^^^^^^^^^^^^^^^
       61|     except ValueError as e:

            date:  <class datetime.date>
        


Not enough values to unpack
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_value_error.py", line 28, in test_Not_enough_values_to_unpack
        a, b, c = d
    ValueError: not enough values to unpack (expected 3, got 2)
    
    Une exception `ValueError` indique qu'une fonction ou une opération
    a reçu un argument du bon type, mais une valeur inappropriée.
    
    Le dépaquetage ('unpack') est un moyen pratique d’attribuer un nom
    à chaque élément d’un itérable.
    Dans ce cas-ci, il y a plus de noms (3)
    que la longueur de l’itérable, une chaîne de caractères (`str`) de longueur 2.
    
    Exception levée à la ligne `28` du fichier 'TESTS:\runtime\test_value_error.py'.
    
       24| assert "ValueError: not enough values to unpack (expected 3, got 2)" in result
       25| 
       26| d = "ab"
       27| try:
    -->28|     a, b, c = d
       29| except ValueError as e:

            d:  'ab'
        


Pow third arg cannot be zero
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_value_error.py", line 108, in test_Pow_third_arg_cannot_be_zero
        pow(2, 4, a)
    ValueError: pow() 3rd argument cannot be 0
    
    Une exception `ValueError` indique qu'une fonction ou une opération
    a reçu un argument du bon type, mais une valeur inappropriée.
    
    Le troisième argument de la fonction `pow()` ne peut pas être zéro.
    
    Exception levée à la ligne `108` du fichier 'TESTS:\runtime\test_value_error.py'.
    
       105| def test_Pow_third_arg_cannot_be_zero():
       106|     a = 0
       107|     try:
    -->108|         pow(2, 4, a)
                    ^^^^^^^^^^^^
       109|     except ValueError as e:

            a:  0
            pow:  <builtin function pow>
        


Slots conflicts with class variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_value_error.py", line 75, in test_Slots_conflicts_with_class_variable
        class F:
    ValueError: 'a' in __slots__ conflicts with class variable
    
    Une exception `ValueError` indique qu'une fonction ou une opération
    a reçu un argument du bon type, mais une valeur inappropriée.
    
    Le nom `a` est utilisé à la fois comme nom d'une variable de classe
    et comme élément de chaîne de caractères dans l'attribut `__slots__` d'une classe ;
    ceci n'est pas autorisé.
    
    Exception levée à la ligne `75` du fichier 'TESTS:\runtime\test_value_error.py'.
    
       73| def test_Slots_conflicts_with_class_variable():
       74|     try:
    -->75|         class F:
       76|             __slots__ = ["a", "b"]


Too many values to unpack
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_value_error.py", line 44, in test_Too_many_values_to_unpack
        a, b = c
    ValueError: too many values to unpack (expected 2)
    
    Une exception `ValueError` indique qu'une fonction ou une opération
    a reçu un argument du bon type, mais une valeur inappropriée.
    
    Le dépaquetage ('unpack') est un moyen pratique d’attribuer un nom
    à chaque élément d’un itérable.
    Dans ce cas-ci, il y a moins de noms (2)
    que la longueur de l’itérable, une liste (`list`) de longueur 3.
    
    Exception levée à la ligne `44` du fichier 'TESTS:\runtime\test_value_error.py'.
    
       41| def test_Too_many_values_to_unpack():
       42|     c = [1, 2, 3]
       43|     try:
    -->44|         a, b = c
       45|     except ValueError as e:

            c:  [1, 2, 3]
        


int base not in range
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_value_error.py", line 209, in test_int_base_not_in_range
        int('18', base=37)
    ValueError: int() base must be >= 2 and <= 36, or 0
    
    Une exception `ValueError` indique qu'une fonction ou une opération
    a reçu un argument du bon type, mais une valeur inappropriée.
    
    L'argument `base` de `int()` doit être soit zéro
    ou un nombre entier de 2 à 36.
    Vous avez écrit 37, ce qui n'est pas valide.
    
    Exception levée à la ligne `209` du fichier 'TESTS:\runtime\test_value_error.py'.
    
       207| def test_int_base_not_in_range():
       208|     try:
    -->209|         int('18', base=37)
                    ^^^^^^^^^^^^^^^^^^
       210|     except ValueError as e:

            int:  <class int>
        


remove item not in list
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_value_error.py", line 236, in test_remove_item_not_in_list
        a_list.remove(b)
    ValueError: list.remove(x): x not in list
    
    Une exception `ValueError` indique qu'une fonction ou une opération
    a reçu un argument du bon type, mais une valeur inappropriée.
    
    Vous avez tenté de supprimer `b` de la liste `a_list`.
    Cependant, `a_list` ne contient pas `b`.
    
    Exception levée à la ligne `236` du fichier 'TESTS:\runtime\test_value_error.py'.
    
       233| a_list = [1, 2, 3]
       234| b = 4
       235| try:
    -->236|     a_list.remove(b)
                ^^^^^^^^^^^^^^^^
       237| except ValueError as e:

            a_list:  [1, 2, 3]
            b:  4
            a_list.remove:  <builtin method remove of list object>
        


time strptime incorrect format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_value_error.py", line 133, in test_time_strptime_incorrect_format
        time.strptime("2020-01-01", "%d %m %Y")
    ValueError: time data '2020-01-01' does not match format '%d %m %Y'
    
    Une exception `ValueError` indique qu'une fonction ou une opération
    a reçu un argument du bon type, mais une valeur inappropriée.
    
    La valeur que vous avez donnée pour l'heure n'est pas dans le format que vous avez spécifié.
    Veillez à utiliser le même séparateur entre les éléments
    (par exemple, entre le jour et le mois) et conservez le même ordre
    dans les données fournies et dans le format que vous avez spécifié.
    Le tableau suivant pourrait vous être utile :
    https://docs.python.org/fr/3/library/time.html#time.strftime
    Le site suivant peut également être utile : https://www.strfti.me/ (anglais seulement).
    
    Exception levée à la ligne `133` du fichier 'TESTS:\runtime\test_value_error.py'.
    
       129|     return
       130| 
       131| import time
       132| try:
    -->133|     time.strptime("2020-01-01", "%d %m %Y")
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
       134| except ValueError as e:

            time:  <module time (builtin)>
            time.strptime:  <builtin function strptime>
        


ZeroDivisionError
-----------------


Complex division
~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_zero_division_error.py", line 180, in test_Complex_division
        1 / zero
    ZeroDivisionError: complex division by zero
    
    Une exception de type `ZeroDivisionError` se produit lorsque vous essayez de diviser une valeur
    par zéro soit directement ou en utilisant une autre opération mathématique.
    
    Vous divisez par le terme suivant
    
         zero
    
    qui est égal à zéro.
    
    Exception levée à la ligne `180` du fichier 'TESTS:\runtime\test_zero_division_error.py'.
    
       177| def test_Complex_division():
       178|     zero = 0j
       179|     try:
    -->180|         1 / zero
                    ^^^^^^^^
       181|     except ZeroDivisionError as e:

            zero:  0j
        


Division by zero literal
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_zero_division_error.py", line 229, in test_Division_by_zero_literal
        1.0 / 0
    ZeroDivisionError: float division by zero
    
    Une exception de type `ZeroDivisionError` se produit lorsque vous essayez de diviser une valeur
    par zéro soit directement ou en utilisant une autre opération mathématique.
    
    Vous divisez par zéro.
    
    Exception levée à la ligne `229` du fichier 'TESTS:\runtime\test_zero_division_error.py'.
    
       225| if friendly_traceback.get_lang() == "en":
       226|     assert "Using the modulo operator, `%`, you are dividing by zero" in result
       227| 
       228| try:
    -->229|     1.0 / 0
                ^^^^^^^
       230| except ZeroDivisionError as e:


Division operator
~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_zero_division_error.py", line 20, in test_Division_operator
        1 / zero
    ZeroDivisionError: division by zero
    
    Une exception de type `ZeroDivisionError` se produit lorsque vous essayez de diviser une valeur
    par zéro soit directement ou en utilisant une autre opération mathématique.
    
    Vous divisez par le terme suivant
    
         zero
    
    qui est égal à zéro.
    
    Exception levée à la ligne `20` du fichier 'TESTS:\runtime\test_zero_division_error.py'.
    
       13| if friendly_traceback.get_lang() == "en":
       14|     assert (
       15|         "The following mathematical expression includes a division by zero"
       16|         in result
       17|     )
       18| 
       19| try:
    -->20|     1 / zero
               ^^^^^^^^
       21| except ZeroDivisionError as e:

            zero:  0
        


Divmod
~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_zero_division_error.py", line 100, in test_Divmod
        divmod(1, zero)
    ZeroDivisionError: integer division or modulo by zero
    
    Une exception de type `ZeroDivisionError` se produit lorsque vous essayez de diviser une valeur
    par zéro soit directement ou en utilisant une autre opération mathématique.
    
    Le deuxième argument de la fonction `divmod()` est égal à zéro.
    
    Exception levée à la ligne `100` du fichier 'TESTS:\runtime\test_zero_division_error.py'.
    
        97| def test_Divmod():
        98|     zero = 0
        99|     try:
    -->100|         divmod(1, zero)
                    ^^^^^^^^^^^^^^^
       101|     except ZeroDivisionError as e:

            zero:  0
            divmod:  <builtin function divmod>
        


Float division
~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_zero_division_error.py", line 148, in test_Float_division
        1 / zero
    ZeroDivisionError: float division by zero
    
    Une exception de type `ZeroDivisionError` se produit lorsque vous essayez de diviser une valeur
    par zéro soit directement ou en utilisant une autre opération mathématique.
    
    Vous divisez par le terme suivant
    
         zero
    
    qui est égal à zéro.
    
    Exception levée à la ligne `148` du fichier 'TESTS:\runtime\test_zero_division_error.py'.
    
       145| def test_Float_division():
       146|     zero = 0.0
       147|     try:
    -->148|         1 / zero
                    ^^^^^^^^
       149|     except ZeroDivisionError as e:

            zero:  0.0
        


Float divmod
~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_zero_division_error.py", line 164, in test_Float_divmod
        divmod(1, zero)
    ZeroDivisionError: float divmod()
    
    Une exception de type `ZeroDivisionError` se produit lorsque vous essayez de diviser une valeur
    par zéro soit directement ou en utilisant une autre opération mathématique.
    
    Le deuxième argument de la fonction `divmod()` est égal à zéro.
    
    Exception levée à la ligne `164` du fichier 'TESTS:\runtime\test_zero_division_error.py'.
    
       161| def test_Float_divmod():
       162|     zero = 0.0
       163|     try:
    -->164|         divmod(1, zero)
                    ^^^^^^^^^^^^^^^
       165|     except ZeroDivisionError as e:

            zero:  0.0
            divmod:  <builtin function divmod>
        


Float modulo
~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_zero_division_error.py", line 132, in test_Float_modulo
        1 % zero
    ZeroDivisionError: float modulo
    
    Une exception de type `ZeroDivisionError` se produit lorsque vous essayez de diviser une valeur
    par zéro soit directement ou en utilisant une autre opération mathématique.
    
    En utilisant l'opérateur modulo, `%`, vous divisez par le terme suivant
    
         zero
    
    qui est égal à zéro.
    
    Exception levée à la ligne `132` du fichier 'TESTS:\runtime\test_zero_division_error.py'.
    
       125|     assert (
       126|         "The following mathematical expression includes a division by zero"
       127|         in result
       128|     )
       129|     assert "done using the modulo operator" in result
       130| 
       131| try:
    -->132|     1 % zero
                ^^^^^^^^
       133| except ZeroDivisionError as e:

            zero:  0.0
        


Integer division operator
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_zero_division_error.py", line 49, in test_Integer_division_operator
        1 // zero
    ZeroDivisionError: integer division or modulo by zero
    
    Une exception de type `ZeroDivisionError` se produit lorsque vous essayez de diviser une valeur
    par zéro soit directement ou en utilisant une autre opération mathématique.
    
    Vous divisez par le terme suivant
    
         zero
    
    qui est égal à zéro.
    
    Exception levée à la ligne `49` du fichier 'TESTS:\runtime\test_zero_division_error.py'.
    
       42| if friendly_traceback.get_lang() == "en":
       43|     assert (
       44|         "The following mathematical expression includes a division by zero"
       45|         in result
       46|     )
       47| 
       48| try:
    -->49|     1 // zero
               ^^^^^^^^^
       50| except ZeroDivisionError as e:

            zero:  0
        


Mixed operations
~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_zero_division_error.py", line 243, in test_Mixed_operations
        a = divmod(8, 1 // 2)
    ZeroDivisionError: integer division or modulo by zero
    
    Une exception de type `ZeroDivisionError` se produit lorsque vous essayez de diviser une valeur
    par zéro soit directement ou en utilisant une autre opération mathématique.
    
    L’expression mathématique suivante inclut une division par zéro :
    
        divmod(8, 1 // 2)
    
    Exception levée à la ligne `243` du fichier 'TESTS:\runtime\test_zero_division_error.py'.
    
       241| def test_Mixed_operations():
       242|     try:
    -->243|         a = divmod(8, 1 // 2)
                        ^^^^^^^^^^^^^^^^^
       244|     except ZeroDivisionError as e:

            divmod:  <builtin function divmod>
            1 // 2:  0
        


Modulo operator
~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_zero_division_error.py", line 81, in test_Modulo_operator
        1 % zero
    ZeroDivisionError: integer division or modulo by zero
    
    Une exception de type `ZeroDivisionError` se produit lorsque vous essayez de diviser une valeur
    par zéro soit directement ou en utilisant une autre opération mathématique.
    
    En utilisant l'opérateur modulo, `%`, vous divisez par le terme suivant
    
         zero
    
    qui est égal à zéro.
    
    Exception levée à la ligne `81` du fichier 'TESTS:\runtime\test_zero_division_error.py'.
    
       74| if friendly_traceback.get_lang() == "en":
       75|     assert (
       76|         "The following mathematical expression includes a division by zero"
       77|         in result
       78|     )
       79| 
       80| try:
    -->81|     1 % zero
               ^^^^^^^^
       82| except ZeroDivisionError as e:

            zero:  0
        


Raise zero negative power
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none


    Traceback (most recent call last):
      File "TESTS:\runtime\test_zero_division_error.py", line 196, in test_Raise_zero_negative_power
        zero**-1
    ZeroDivisionError: 0.0 cannot be raised to a negative power
    
    Une exception de type `ZeroDivisionError` se produit lorsque vous essayez de diviser une valeur
    par zéro soit directement ou en utilisant une autre opération mathématique.
    
    Vous essayez d'élever le nombre 0 à une puissance négative
    ce qui équivaut à diviser par zéro.
    
    Exception levée à la ligne `196` du fichier 'TESTS:\runtime\test_zero_division_error.py'.
    
       193| def test_Raise_zero_negative_power():
       194|     zero = 0
       195|     try:
    -->196|         zero**-1
                    ^^^^^^^^
       197|     except ZeroDivisionError as e:

            zero:  0
        

