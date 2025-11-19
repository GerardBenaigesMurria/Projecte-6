# Autor: Gerard Benaiges Murria
# Data: 14/11/2025
# Versió: 1
# Descripció: Llegir i escriure: Obre un fitxer en mode lectura i escriptura (r+). Mostra el contingut per pantalla i afegeix una línia al final sense esborrar el contingut anterior
# Especificacions de entrada: 

with open("sortida.txt", "r+") as f:
    print("Contingut actual:")
    print(f.read())

    f.write("\nNova linia afegida ")
    print(f.read())