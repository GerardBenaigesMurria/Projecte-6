# Autor: Gerard Benaiges Murria
# Data: 14/01/2026
# Versió: 1
# Descripció: 
# Especificaicons de entrada: 

# Cotxe Crea dos cotxes amb la classe Cotxe i imprimeix-ne la informaci

from cotxe import cotxe

cotxe1 = cotxe("Audi", "A4", "2009")
cotxe2 = cotxe("Lamborgini","Urus","2018")
cotxe1.descriure()
cotxe2.descriure()

# Rectangle Crea 3 rectangles amb diferents mides. Mostra l’àrea de cadascun

from rectangle import rectangle

rectangle1 = rectangle(4,7)
rectangle2 = rectangle(6,3)
rectangle3 = rectangle(8,9)

rectangle1.area()
rectangle2.area()
rectangle3.area()

# Estudiant Crea una llista d’estudiants. Mostra només els que han aprovat

from estudiant import estudiant

estudiant1 = estudiant("Joan", 7)
estudiant2 = estudiant("Maria", 4)
estudiant3 = estudiant("Pere", 5)

estudiant1.aprovat()
estudiant2.aprovat()
estudiant3.aprovat()

# Compte Bancari Crea un compte bancari i simula 3 operacions: ingrés, retirada vàlida i retirada superior al saldo
from comptebancari import comptebancari

compte1 = comptebancari(1000)

compte1.ingressar()
compte1.retirar()    
compte1.retirar()

# Productes  Fes una funció que rebi una llista de productes i apliqui un descompte del 10% a tots

from producte import producte

producte1 = producte("Llum", 20)
producte2 = producte("Cadira", 50)
producte3 = producte("Taula", 100)

producte1.descompte()
producte2.descompte()
producte3.descompte()

# Punts  Crea dos punts i calcula la distància entre ells

from punt import Punt
punt1 = Punt(3,4)
punt2 = Punt(6,8)

punt1.distancia(punt2)

# Animal Crea una classe Gos que hereti d’Animal i sobreescrigui fer_soroll() per dir “Bup bup!”

from animal import animal
class gos(animal):
    def fer_sorroll(self):
        print("Bup bup!")

gos1 = gos("Firulais", "Gos")
gos1.fer_sorroll()

# Llibres Fes una classe Biblioteca que pugui afegir llibres (objectes Llibre) i mostrar-los tots

from llibre import llibre
class biblioteca(llibre):
    def __init__(self):
        self.llistallibres = []
    
    def afegir_llibre(self, llibre):
        self.llistallibres.append(llibre)
    
    def mostrar_llibres(self):
        for llibre in self.llistallibres:
            print("Títol:", llibre.titol, ", Autor:", llibre.autor)

biblioteca1 = biblioteca()
llibre1 = llibre("El Quijote", "Cervantes", 1605)
llibre2 = llibre("1984", "George Orwell", 1949)

biblioteca1.afegir_llibre(llibre1)
biblioteca1.afegir_llibre(llibre2)
biblioteca1.mostrar_llibres()

# Cercles  Crea un llistat de cercles i mostra quins tenen àrea superior a 50

from cercle import cercle

cercle1 = cercle(4)
cercle2 = cercle(3)
cercle3 = cercle(6)

cercle_llista = [cercle1, cercle2, cercle3]
for i in cercle_llista:
    area = 3.141592 * i.radi ** 2
    if area > 50:
        print("El cercle amb radi", i.radi, "té àrea superior a 50:", area)


# Persones Fes una funció que rebi una llista de persones i imprimeixi només les que tenen més de 30 anys

from persona import persona

persona1 = persona("Mohammed", 25)
persona2 = persona("Nil", 35)
persona3 = persona("Luis", 40)
persona_llista = [persona1, persona2, persona3]
for i in persona_llista:
    if i.edat > 30:
        i.presentarse()

