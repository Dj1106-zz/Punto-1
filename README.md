Analizador sintáctico en Python

En este punto se implementó un analizador sintáctico en Python para reconocer expresiones aritméticas y construir su árbol sintáctico.

Inicialmente se partió de una gramática que tenía recursión por la izquierda, lo cual genera problemas al momento de implementar un parser descendente recursivo. Por esta razón, fue necesario transformarla a una versión equivalente sin recursión izquierda, de manera que pudiera ser procesada correctamente por el programa.

La gramática utilizada finalmente fue:

E  → T E'
E' → + T E' | ε
T  → F T'
T' → * F T' | ε
F  → (E) | id

El analizador se implementó usando funciones recursivas, donde cada función representa una regla de la gramática. A medida que el programa va leyendo los tokens de entrada, va validando que la estructura sea correcta según la gramática definida.

Además, se construyó un árbol sintáctico utilizando nodos, lo que permite representar de forma clara cómo se organiza la expresión. Cada nodo corresponde a un símbolo de la gramática, y sus hijos representan las derivaciones que se van aplicando.

El proceso comienza desde el símbolo inicial y avanza consumiendo los tokens uno por uno. Si en algún momento la cadena no cumple con la estructura esperada, el programa lanza un error, indicando que hay un problema sintáctico.

En general, este tipo de analizador es eficiente, ya que recorre la cadena una sola vez, lo que lo hace de complejidad lineal. Esto demuestra que, con una gramática bien definida, es posible construir analizadores rápidos y funcionales.
