# Autor: Gerard Benaiges Murria
# Data: 31/10/2025
# Versió: 1
# Descripció: et diu si la paraula es un polindrom o no
# Especificacions de entrada: ficar una cadena de caracters

text = str(input("Fica un a paraula"))

text_reves = text[::-1]
if text_reves == text:
    print ("És un palindrom")
        
if text_reves != text:
    print("No és un palidrom")