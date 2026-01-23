# Autor: Gerard Benaiges Murria
# Data: 14/01/2026
# Versió: 1
# Descripció: Crear objectes de les classes
# Especificaicons de entrada: 

# Compte Bancari Simple
from comptebancari import compte_bancari

compte_bancari1 = compte_bancari(1000)

print(compte_bancari1.consultar_saldo())

# Estudiant amb nota protegida
from estudiant import estudiant

estudiant1 = estudiant(8)

print(estudiant1.consultar_nota())

estudiant1.sumar(1)
print(estudiant1.consultar_nota())

estudiant1.restar(4)
print(estudiant1.consultar_nota())

# Termòstat
from termostat import termostat

termostat1 = termostat(25)
print(termostat1.temperatura)

# Contrasenya segura
from contrasenyasegura import usuari

usuari1 = usuari(12345678)

print("Verificació inicial (esperat True):", usuari1.verificar_contrasenya(12345678))

nova = "ContrasenyaSegura2026"
usuari1.canviar_contrasenya(nova)

print("Després canvi vàlid (esperat True):", usuari1.verificar_contrasenya(nova))

print("Verificació amb antiga (esperat False):", usuari1.verificar_contrasenya(12345678))

# Sensor amb valors limitats
from sensor import sensor

sensor1 = sensor(40)
print(sensor1.valor_get())  

sensor1.valor_set (80)
print(sensor1.valor_get()) 

# Producte amb preu controlat
from producte import producte

producte1 = producte("Botella d'aigua",1)

print(producte1.consultar_preu())

producte1.modificar_preu(2)

print(producte1.consultar_preu())

# Temps en hores
from temps import rellotge

rellotge1 = rellotge(12)

rellotge1.hores

print(rellotge1.mostrar_hora())

# Alumne amb edat controlada
from alumne import alumne

alumne1 = alumne(14)
print(alumne1.edat_get())

# Gestor de puntuació
from puntació import joc

joc1 = joc()

joc1.sumar_punts(5)

print(joc1.puntuacio())

joc1.reiniciar_puntuacio()

print(joc1.puntuacio())

# Email d’un usuari
from email import compteusuari

usuari1 = compteusuari("gbenaiges@iesjulioantonio.cat")
print(usuari1.email_get())
