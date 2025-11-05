# Autor: Gerard Benaiges Murria
# Data: 31/10/2025
# Versió: 1
# Descripció: canvia les lletres a per @
# Especificacions de entrada: ficar una cadena de caracters

text = str(input("Fica un a paraula "))

contador = 0

while contador < (len(text)):
    if text[contador] == "a":
        print(text.replace("a", "@"))
    if text[contador] == "A":
        print(text.replace("A", "@"))
    contador += 1
