# Autor: Gerard Benaiges Murria
# Data: 01/10/2025
# Versió: 1
# Descripció: paraula ficada al reves
# Especificaicons de entrada: ficar una paraula

text = str(input("Fica un paraula "))
nom = len(text)
contador = nom - 1

while contador >= 0:
    print(text[contador], end='')
    contador = contador - 1