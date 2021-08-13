# Library

import json

# Variables Declaration

diccionario_costos = input()
diccionario_costos = json.loads(diccionario_costos)
category = input()
category_final = category.replace(" ","")
sum = 0

# List

categories = []

# For Dev

for i in category_final:
  if i in diccionario_costos:
    categories.append(i)
    sum = diccionario_costos.get(i) + sum

print(sum)
print(f"{' '.join(categories)}.")
