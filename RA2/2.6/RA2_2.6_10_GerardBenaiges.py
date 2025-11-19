# Autor: Gerard Benaiges Murria
# Data: 14/11/2025
# Versió: 1
# Descripció: Assegurar el tancament del fitxer (amb error): Simula una operació amb fitxers on pot haver-hi un error durant la lectura. Assegura’t que el fitxer es tanqui sempre, fins i tot si es produeix un error en llegir-lo.
# Especificacions de entrada: 

f = None

try:
    f = open("missatge.txt", "r")
    contingut = f.read()
    print(contingut)

    a = 10 / 0     

except Exception as e:
    print("S'ha produït un error:", e)

finally:
    if f is not None:
        f.close()
        print("Fitxer tancat correctament.")
