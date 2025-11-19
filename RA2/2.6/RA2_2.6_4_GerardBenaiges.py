# Autor: Gerard Benaiges Murria
# Data: 14/11/2025
# Versió: 1
# Descripció: Comptar línies: Llegeix un fitxer i mostra quantes línies té.
# Especificacions de entrada: 

with open("sortida.txt", "r") as f:
    linies = f.readlines()
    print("El fitxer té", len(linies), "línies.")