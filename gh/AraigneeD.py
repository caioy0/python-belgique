from constantes import *

class AraigneeD:
    def __init__(self):
        self.position = 4
        self.delai_attente = 4
        self.etat = Constantes.NORMAL

    def actualiserEtat(self):
        self.delai_attente -= 1
        if self.delai_attente <= 0:
            self.delai_attente = 4
            self.position -= 1
            if self.position == -1:  # mange la fleure
                self.etat = Constantes.TERMINE
