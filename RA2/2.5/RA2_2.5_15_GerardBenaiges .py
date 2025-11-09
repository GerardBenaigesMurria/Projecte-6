# Autor: Gerard Benaiges Murria
# Data: 07/10/2025
# Versió: 1
# Descripció: Crida de mòduls amb àlies, Crea un mòdul textos.py amb una funció que posi en majúscules, minúscules i capitalitzi textos. Importa’l amb un àlies (import textos as tx) i prova les funcions amb frases diferents.
# Especificacions de entrada: ficar una cadena de text


import textos as tx

text = str(input("Introdueix un text: "))

text_majuscules = tx.majuscules(text)
print("Text en majúscules:", text_majuscules)

text_minuscules = tx.minuscules(text)
print("Text en minúscules:", text_minuscules)

text_capitalitzat = tx.capitalitza(text)
print("Text capitalitzat:", text_capitalitzat)