# Lista original de recordatorios
recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
                 ['2021-05-01', "15:00", "No trabajar"],
                 ['2021-07-15', "13:00", "No hacer nada es feriado"],
                 ['2021-09-18', "16:00", "Ramadas"],
                 ['2021-12-25', "00:00", "Navidad"]]

# 1. Agregar el evento "Empezar el Año" el 2 de febrero de 2021 a las 6:00.
recordatorios.append(['2021-02-02', "06:00", "Empezar el Año"])

# 2. Editar el evento del 15 de julio para que sea el 16 de julio.
for recordatorio in recordatorios:
    if recordatorio[0] == '2021-07-15':
        recordatorio[0] = '2021-07-16'

# 3. Eliminar el evento del 1 de mayo.
recordatorios = [recordatorio for recordatorio in recordatorios if recordatorio[0] != '2021-05-01']

# 4. Agregar la cena de Navidad y de Año Nuevo.
recordatorios.append(['2021-12-25', "22:00", "Cena de Navidad"])
recordatorios.append(['2021-12-31', "22:00", "Cena de Año Nuevo"])

# Ordenar los recordatorios para mantener el orden temporal
recordatorios.sort()

# Mostrar la lista de recordatorios actualizada
print(recordatorios)
