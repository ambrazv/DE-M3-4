import sys

with open("lorem_ipsum.txt", "r") as file:
    texto = file.read()

#variables
numero_caracteres_distintos = len(set(texto))
numero_palabras_distintas = len(set(texto.split()))

print(f"El número de caracteres distintos es {numero_caracteres_distintos} ")
print(f"El número de palabras distintas es {numero_palabras_distintas}")