# Autor: Gerard Benaiges Murria
# Data: 14/11/2025
# Versió: 1
# Descripció: Comprovar si el fitxer existeix abans de llegir-lo: Fes un programa que intenti llegir un fitxer anomenat dades.txt, però abans comprovi si existeix. Si no existeix, mostra un missatge d’error amigable.
# Especificacions de entrada: 

import os

if os.path.exists("dades.txt"):
    with open("dades.txt", "r") as f:
        print(f.read())
else:
    print("ERROR: El fitxer dades.txt no existeix.")