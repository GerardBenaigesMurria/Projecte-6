# Autor: Gerard Benaiges Murria
# Data: 14/11/2025
# Versió: 1
# Descripció: Llegir un fitxer: Crea un fitxer de text anomenat missatge.txt amb contingut a mà (o des del codi). Escriu un programa que llegeixi i mostri el contingut per pantalla
# Especificacions de entrada: 


fitxer = open("missatge.txt", "r")

contingut = fitxer.read()

fitxer.close()

print(contingut)