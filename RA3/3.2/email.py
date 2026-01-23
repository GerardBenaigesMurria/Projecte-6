# Autor: Gerard Benaiges Murria
# Data: 21/01/2026
# Versió: 1
# Descripció: Classe CompteUsuari amb atribut privat __email
# Especificaicons de entrada: 

class compteusuari:
    def __init__(self, email):
        self.email = email  

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nou_email):
        if "@" in nou_email and "." in nou_email:
            self.__email = nou_email
        else:
            raise ValueError("L'email ha de contenir '@' i '.'")


