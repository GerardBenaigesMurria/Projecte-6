# Autor: Gerard Benaiges Murria
# Data: 14/11/2025
# Versió: 1
# Descripció: Afegir continguts: Afegeix una línia nova a un fitxer existent (sortida.txt) sense esborrar el que ja hi ha.
# Especificacions de entrada: 

with open("sortida.txt", "a") as f:
    f.write("Una altra linea\n")