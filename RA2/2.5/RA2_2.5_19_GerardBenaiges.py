# Autor: Gerard Benaiges Murria
# Data: 07/10/2025
# Versió: 1
# Descripció: Mòdul amb validacions Crea validacions.py amb funcions: es_email_valid(email), es_telefon_valid(telefon)
# Fes proves des d’un script amb dades vàlides i no vàlides.
# Especificacions de entrada: 

import validacions as val
email = str(input("Introdueix un email: "))
telefon = str(input("Introdueix un número de telèfon: "))


if val.es_email_valid(email):
    print(f"L'email {email} és vàlid.")
else:
    print(f"L'email {email} no és vàlid.")

if val.es_telefon_valid(telefon):
    print(f"El número de telèfon {telefon} és vàlid.")
else:
    print(f"El número de telèfon {telefon} no és vàlid.")
