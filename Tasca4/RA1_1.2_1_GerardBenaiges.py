"""""
● Quines són les constants?
La constant és PI
● Quines són les variables?
Les variables són radi i area
● Quina part és una funció?
És la part de calcular_area
● Quina línia llegeix dades de l’usuari?
La linea de radi concretament a partir del input
● Quina línia mostra el resultat?
L'ultima linea, el print mostra el resultat en pantalla
"""""

import math # importar una llibreria

PI = 3.1416  # Constant

def calcular_area(radi): #definir una funció
    return PI * radi ** 2

radi = float(input("Introdueix el radi: "))  # llegeix el radi del usuari
area = calcular_area(radi) # crida a la funció definida anteriorment
print("L'area del cercle és:", area) # imprimeix a pantalla l'area del cercle