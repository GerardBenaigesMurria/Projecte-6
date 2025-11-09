# Autor: Gerard Benaiges Murria
# Data: 07/10/2025
# Versió: 1
# Descripció: Mòdul amb validacions Crea validacions.py amb funcions: es_email_valid(email), es_telefon_valid(telefon)
# Fes proves des d’un script amb dades vàlides i no vàlides.
# Especificacions de entrada: 

def es_email_valid(email):
    import re
    patró_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patró_email, email) is not None
def es_telefon_valid(telefon):
    import re
    patró_telefon = r'^\+?\d{9,15}$'
    return re.match(patró_telefon, telefon) is not None