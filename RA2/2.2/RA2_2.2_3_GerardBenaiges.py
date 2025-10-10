# Autor: Gerard Benaiges Murria
# Data: 01/10/2025
# Versió: 1
# Descripció: Et fa la taula del numero que fiquis
# Especificaicons de entrada:  

from time import sleep
num = int(input("Introdueix un numero "))

for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i,"*", num, "=", i * num)
    sleep (0.25)