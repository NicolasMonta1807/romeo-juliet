
# Romeo & Juliet

Este programa analiza la obra de "Romeo y Julieta" de William Shakespeare, tomada del proyecto [Gutenberg](https://www.gutenberg.org/cache/epub/1513/pg1513.txt).

El objetivo del análisis en contar cuántas intervenciones terminadas en pregunta realiza cada personaje a través del uso de expresiones regulares multilínea.

## Intervenciones Válidas

Una intervención está compuesta por las siguientes partes: El nombre de quién interviene
(siempre en mayúsculas fijas y con un punto al final), un cambio de línea, un párrafo con una o
más líneas y un salto de línea para marcar el final de la intervención.

El objetivo es encontrar aquellas intervenciones cuya última frase, en la última línea, sea una pregunta. Es decir, contiene las siguientes parted: 
* El nombre de quien hace la intervención.
* 0 o más líneas de diálogo cualesquiera 
* Una línea que termina en pregunta y finaliza la intervención.

### La siguiente es una intervención válida para el programa:

ROMEO. \
Ay me, sad hours seem long. \
Was that my father that went hence so fast?

### Mientras que las siguientes no lo son:

JULIET. \
Good pilgrim, you do wrong your hand too much, \
Which mannerly devotion shows in this; \
For saints have hands that pilgrims’ hands do touch, \
And palm to palm is holy palmers’ kiss. 

ROMEO. \
Alas that love, whose view is muffled still, \
Should, without eyes, see pathways to his will! \
Where shall we dine? O me! What fray was here? \
Yet tell me not, for I have heard it all.


## Grupos de aceptación

### Personaje de la intervención
Como se mencionó en un principio, una intervención comienza con el nombre de quién interviene
siempre en mayúsculas fijas y con un punto al final.

```regex
(^(PERSONAE)\.$\n){1}
```

En esta expresión regular se busca:
* ^ : Inicio de linea
* PERSONAE :     Nombre del personaje
* \\. :           Punto final
* $ :            Final de línea
* \n :           Salto de línea
* {1} :          Todo el grupo una única vez

Esto nos permite encontrar el inicio de cada intervención del personaje dado, a reemplazar por "PERSONAE".

Dentro de la intervención válida dada al inicio, este grupo coincide con: \
ROMEO.

### Líneas de diálogo
En medio de una intervención puede haber 0 o más líneas de diálogo cualesquiera.

```regex
(^(\w|[ ,\.?’;\-\!:\"*])+$\n)*
```
En esta expresión regular se busca:
* ^ : Inicio de línea
    * \w : Cualquier caracter alfabético
    ó
    * [ ,\.?’;\-\!:\"*] : Cualquier signo de puntuación dentro del grupo
    * \+ : Este grupo 1 o más veces
* $ : Final de línea
* \n : Salto de línea
* \* : Este grupo 0 o más veces

Esto nos permite considerar cualquier cantidad de líneas de diálogo (incluso 0) que, en esencia, están compuestas por caracteres alfabéticos con signos de puntuación intermedios.

Dentro de la intervención válida dada al inicio, este grupo coincide con: \
Ay me, sad hours seem long.

### Frase de pregunta y final de intervención
Al final de una intervención válida, se debe encontrar una frase terminada en pregunta y dar fin a esa intervención de ese personaje.

```regex
(^.*\?$\n$){1}
```

En esta expresión regular se busca:
* ^ : Inicio de línea
* .* : Cualquier caracter 0 o más veces
* \\? : Signo de pregunta
* $ : Final de línea
* \n : Salto de línea
* $ : Final de línea
* {1} : Todo el grupo una única vez

Esto nos permite encontrar una línea terminada en pregunta seguido del final de la intervención marcado con un salto de línea único.

Dentro de la intervención válida dada al inicio, este grupo coincide con: \
"Was that my father that went hence so fast? \
"

### Composición Final:
```regex
(^(PERSONAE)\.$\n){1}(^(\w|[ ,\.?’;\-\!:\"*])+$\n)*(^.*\?$\n$){1}
```

## Funcionamiento del programa
El programa inicialmente crea un diccionario cuya llave es el nombre de cada personaje de la obra y cuyo valor inicial es 0 que, finalmente, indicará cuántas intervenciones válidas tuvo ese personaje.

Luego, por cada personaje, se analiza el texto y se añade la cantidad de correspondencias con la expresión regular y se añade a su entrada en el diccionario.

Últimamente, se ordena el diccionario de mayor a menor, es decir, del personaje que más intervenciones finalizadas en pregunta al que menos; y se imprime en pantalla.