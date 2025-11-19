# Autor: Gerard Benaiges Murria
# Data: 14/11/2025
# Versió: 1
# Descripció: Gestionar errors d'escriptura: Escriu un programa que intenti escriure en un fitxer anomenat resultats.txt, però gestiona l'error que es pot produir si el fitxer és només de lectura o si el sistema impedeix escriure-hi (permisos denegats).
# Especificacions de entrada: 

try:
    with open("resultats.txt", "w") as f:
        f.write("Això es una prova de que puc escriure\n")
except PermissionError:
    print("ERROR: No tens permís per escriure al fitxer resultats.txt.")
