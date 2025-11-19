# Autor: Gerard Benaiges Murria
# Data: 14/11/2025
# Versió: 1
# Descripció: Escriure en un fitxer: Crea un programa que escrigui les següents 3 línies en un fitxer nou anomenat sortida.txt. El contingut anterior (si n'hi ha) ha de desaparèixer.
# Especificacions de entrada: 

linies = [
    "Primera linia\n",
    "Segona linia\n",
    "Tercera linia\n"
]

with open("sortida.txt", "w") as f:
    f.writelines(linies)