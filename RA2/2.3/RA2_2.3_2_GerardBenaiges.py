# Autor: Gerard Benaiges Murria
# Data: 17/10/2025
# Versió: 1
# Descripció: suma tots els numeros des de el 1 fins al numero del usuari
# Especificacions de entrada: un numero enter

try:
    num = int(input("Introduix un numero "))

    for i in range(1, num+1):
        resultat = sum(range(1, num+1))
    print (resultat)
except NameError:
    print("Fica un numero positiu")
except ValueError:
    print("Has de ficar un nombre enter")

