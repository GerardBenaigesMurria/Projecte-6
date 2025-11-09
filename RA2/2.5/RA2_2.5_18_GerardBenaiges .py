# Autor: Gerard Benaiges Murria
# Data: 07/10/2025
# Versió: 1
# Descripció: Ús de datetime, Fes un programa que mostri la data i hora actual i la formati de manera llegible (dd/mm/yyyy hh:mm). Calcula quants dies falten per una data determinada (com Nadal o el teu aniversari).
# Especificacions de entrada: 

from datetime import datetime
data_hora_actual = datetime.now()
data_formatejada = data_hora_actual.strftime("%d/%m/%Y %H:%M")
print(f"La data i hora actual és: {data_formatejada}")

data_objectiu = datetime(data_hora_actual.year, 12, 25)  
dies_fins_objectiu = (data_objectiu - data_hora_actual).days
print(f"Queden {dies_fins_objectiu} dies per Nadal")