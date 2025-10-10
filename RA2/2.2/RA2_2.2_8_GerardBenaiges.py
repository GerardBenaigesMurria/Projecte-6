# Autor: Gerard Benaiges Murria
# Data: 10/10/2025
# Versió: 1
# Descripció: Demano una frase i compto les vocals
# Especificaicons de entrada: ficar una frase

frase = str(input("Fica una frase: "))
vocals = "aeiouAEIOU"
contadorvocals = 0
contador = 0


while contador < len(frase):
    if frase[contador] in vocals:
        contadorvocals = contadorvocals + 1
    contador = contador + 1

print("El nombre de vocals és:", contadorvocals)
