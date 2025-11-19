# Autor: Gerard Benaiges Murria
# Data: 14/11/2025
# Versió: 1
# Descripció: Crear el fitxer si no existeix: Intenta obrir un fitxer en mode lectura. Si no existeix, crea’l automàticament i escriu-hi una línia per defecte: "Fitxer creat automàticament".
# Especificacions de entrada: 

try:
    with open("prova.txt", "r") as f:
        print("Ja existeix aquest fitxer:")
        print(f.read())
except FileNotFoundError:
    with open("prova.txt", "w") as f:
        f.write("Fitxer creat automaticament\n")
    print("S'ha creat un fitxer perque no existia")