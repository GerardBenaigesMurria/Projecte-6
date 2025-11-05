# Autor: Gerard Benaiges Murria
# Data: 31/10/2025
# Versió: 1
# Descripció: et fica una cadena de paraules al reves
# Especificacions de entrada: ficar una cadena de caracters

text = str(input("Fica un a paraula o frase "))

num_lletres = len(text)

contador = num_lletres - 1

while contador >= 0:
    print(text[contador], end="")
    contador -= 1