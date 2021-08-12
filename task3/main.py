# Variables Declaration

investigation = input()
investigation = investigation.replace(" ", "")

saver = []
letra = ""
counter = 0
numeros = []

# For Dev

for i in investigation:
    if counter == 0:
        letra = i
        counter = counter + 1
    elif i == letra:
        counter = counter + 1
    elif i != letra:
        numeros.append(counter)
        saver.append(letra)
        counter = 1
        letra = i

saver.append(letra)
numeros.append(counter)

# End

print(" ".join(saver))
print(" ".join(str(x) for x in numeros))
