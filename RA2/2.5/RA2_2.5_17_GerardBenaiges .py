# Autor: Gerard Benaiges Murria
# Data: 07/10/2025
# Versió: 1
# Descripció: Fes un mòdul constants.py amb valors com PI, GRAVETAT, etc. Fes servir-los des d’un altre fitxer per calcular coses com la força gravitatòria.
# Especificacions de entrada: 

import constants as const

massa = 5.0  
forca = massa * const.GRAVETAT
print(f"La força gravitatòria és {forca} N")

radi = 2.0  
area = const.PI * radi**2
print(f"L'àrea del cercle és {area} m^2")
