import sys

#Datos a ingresar
tasaconversion_solperuano = float(sys.argv[1])
tasaconversion_pesoargentino = float(sys.argv[2])
tasaconversion_dolaramericano = float(sys.argv[3])
valorpesochileno_convertir = float(sys.argv[4])

#Multiplicación de variables
soles_peruanos = valorpesochileno_convertir * tasaconversion_solperuano
peso_argentino = valorpesochileno_convertir * tasaconversion_pesoargentino
dolar_americano = valorpesochileno_convertir * tasaconversion_dolaramericano

#Respuestas
print(f"Los {valorpesochileno_convertir} pesos equivalen a: ")
print(f"{soles_peruanos} Soles")
print(f"{peso_argentino} Pesos argentinos")
print(f"{dolar_americano} Dólares")