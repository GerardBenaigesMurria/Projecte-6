# Autor: Gerard Benaiges Murria
# Data: 07/10/2025
# Versió: 1
# Descripció: Crea una carpeta utilitats amb: __init__.py (pot estar buit),temps.py (funcions per convertir segons a hores, minuts, etc.),
# moneda.py (funció per convertir entre euros i dòlars). Fes servir el paquet des d’un fitxer principal.
# Especificacions de entrada: 

import utilitats.temps as tp
import utilitats.moneda as md

segons = 7200
hores = tp.segons_a_hores(segons) 
minuts = tp.segons_a_minuts(segons)
print(f"{segons} segons són {hores} hores")
print(f"{segons} segons són {minuts} minuts")

euros = 100
dolars = md.euros_a_dolars(euros)
print(f"{euros} euros són {dolars} dòlars")
