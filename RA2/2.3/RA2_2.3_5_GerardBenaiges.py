# Autor: Gerard Benaiges Murria
# Data: 22/10/2025
# Versió: 1
# Descripció: comprova tots els numeros primers fins al numero ficat
# Especificacions de entrada: ficar un numero enter positiu

try:
    num = int(input("Introdueix un numero "))
    if num < 2:
        print(f"No hi ha nombres primers fins a {num}")
    else:
        for i in range(2, num + 1):
            is_prime = True
            contador = 2
            while contador * contador <= i:
                if i % contador == 0:
                    is_prime = False
                contador += 1
            if is_prime:
                print(i)
except ValueError:
    print("Has de ficar un nombre enter")