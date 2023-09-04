'''
  Autor: Nicolás Montañez Velasco
  Fecha: 04/09/2023 (DD/MM/AAAA)
  Objetivo: ¿Cuántas intervenciones que terminan en pregunta realiza cada personaje?
 '''

import re

# Carga el texto fuente del archivo anexo que contiene la obra
text = open('./data.txt', 'r').read()

# Crea un diccionario con los personajes y sus inicializaciones en 0
personae = {
  "ESCALUS" : 0,
  "MERCUTIO" : 0,
  "PARIS":  0,
  "MONTAGUE":  0,
  "LADY MONTAGUE":  0,
  "ROMEO":  0,
  "BENVOLIO":  0,
  "ABRAM":  0,
  "BALTHASAR":  0,
  "CAPULET":  0,
  "LADY CAPULET":  0,
  "JULIET":  0,
  "TYBALT":  0,
  "CAPULET’S COUSIN":  0,
  "NURSE":  0,
  "PETER":  0,
  "SAMPSON":  0,
  "GREGORY":  0,
  "FRIAR LAURENCE":  0,
  "FRIAR JOHN":  0,
}

# Por cada personaje
for person in personae:
  ''' 
    Aplica la expresión regular para encontrar las intervenciones que terminan en pregunta.
    La expresión regular y su explicación se encuentra en el archivo de instrucciones: README.md
  '''
  question = r"(^("+person+")\.$\n){1}(^(\w|[ ,\.?’;\-\!:\"*])+$\n)*(^.*\?$\n$){1}"
  # Cuenta las correspondencias y las asigna a la entrada del personaje
  personae[person] = re.findall(question, text, re.MULTILINE).__len__()

print("¿Cuántas intervenciones que terminan en pregunta realiza cada personaje?: \n")

# Ordena el diccionario por el valor de las intervenciones
personae = sorted(personae.items(), key=lambda x: x[1], reverse=True)

# Imprime el resultado
for person in personae:
  print(person[0], ":", person[1])