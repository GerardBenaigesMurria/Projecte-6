# Autor: Gerard Benaiges Murria
# Data: 14/01/2026
# Versió: 1
# Descripció:
# Especificaicons de entrada: 

class EmailNotificador:
    def enviar (self, missatge):
        print(f"Enviant email: {missatge}")

class Comanda:
    def __init__(self, client,notificador):
        self.client = client
        self.notificador = notificador 

    def confirmar (self):
        print(f"Comanda confirmada per {self.client}")
        self.notificador.enviar (f"Hola {self.client}, la teva comanda ha estat confirmada.")

servei = EmailNotificador()
comanda = Comanda("Gerard",servei)
comanda.confirmar()