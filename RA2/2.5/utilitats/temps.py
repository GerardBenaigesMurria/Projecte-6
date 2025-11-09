# Autor: Gerard Benaiges Murria
# Data: 07/10/2025
# Versió: 1
# Descripció: Crea una carpeta utilitats amb: __init__.py (pot estar buit),temps.py (funcions per convertir segons a hores, minuts, etc.),
# moneda.py (funció per convertir entre euros i dòlars). Fes servir el paquet des d’un fitxer principal.
# Especificacions de entrada: 

def segons_a_hores(segons):
    return segons / 3600
def segons_a_minuts(segons):
    return segons / 60
def minuts_a_segons(minuts):
    return minuts * 60
def hores_a_segons(hores):
    return hores * 3600
