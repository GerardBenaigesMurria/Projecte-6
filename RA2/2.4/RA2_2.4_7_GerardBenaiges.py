# Autor: Gerard Benaiges Murria
# Data: 31/10/2025
# Versió: 1
# Descripció: compta quantes vegades apareix una lletra en concret
# Especificacions de entrada: ficar una cadena de caracters

text = str(input("Fica un a paraula o frase "))

lletra = str(input("Fica la lletra que vols comptar "))

contador = text.count(lletra)

print(f"La lletra {lletra} apareix {contador} vegades")

