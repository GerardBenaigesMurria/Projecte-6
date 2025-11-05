# Autor: Gerard Benaiges Murria
# Data: 31/10/2025
# Versió: 1
# Descripció: et diu quantes vocals té una frase
# Especificacions de entrada: ficar una cadena de caracters

text = str(input("Fica un a paraula o frase "))
contador = 0
vocals = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
num_vocals = 0
while contador < (len(text)):
    if text[contador] in vocals:
        num_vocals += 1
    contador += 1
print ("La teva cadena té", num_vocals ,"vocals")