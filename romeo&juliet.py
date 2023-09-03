import re

text = open('./data.txt', 'r').read()

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


for person in personae:
  question = r"(^("+person+")\.$\n){1}(^(\w|[ ,\.?’;\-\!:\"*])+$\n)*(^.*\?$\n$){1}"
  personae[person] = re.findall(question, text, re.MULTILINE).__len__()

print("¿Cuántas intervenciones que terminan en pregunta realiza cada personaje?: \n")
personae = sorted(personae.items(), key=lambda x: x[1], reverse=True)

for person in personae:
  print(person[0], ":", person[1])