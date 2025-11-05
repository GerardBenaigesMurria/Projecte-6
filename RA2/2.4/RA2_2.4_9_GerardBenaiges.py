# Autor: Gerard Benaiges Murria
# Data: 31/10/2025
# Versió: 1
# Descripció: divideix una frase en paraules i les mostra
# Especificacions de entrada: ficar una cadena de caracters

text = input("Fica una paraula o frase ")
paraules = text.split()

print("Les paraules són")
for paraula in paraules:
    print(paraula)