from constantes import *

class ChenilleD:
    def __init__(self):
        self.position = 0
        self.delai_attente = 6
        self.etat = Constantes.NORMAL

    def actualiserEtat(self):
        self.delai_attente -= 1
        if self.delai_attente <= 0:
            self.delai_attente = 6
            self.position += 1
            if self.position == 7:  # mange la fleure
                self.etat = Constantes.TERMINE
