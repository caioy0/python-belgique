from constantes import *

class AraigneeG:
    def __init__(self):
        self.position = 0
        self.delai_attente = 10
        self.etat = Constantes.NORMAL

    def actualiserEtat(self):
        self.delai_attente -= 1
        if self.delai_attente <= 0:
            self.delai_attente = 10
            self.position += 1
            if self.position == 5:  # mange la fleure
                self.etat = Constantes.TERMINE
