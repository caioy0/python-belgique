from constantes import *

class ChenilleG:
    def __init__(self):
        self.position = 4
        self.delai_attente = 6
        self.etat = Constantes.NORMAL

    def actualiserEtat(self):
        self.delai_attente -= 1
        if self.delai_attente <= 0:
            self.delai_attente = 6
            self.position -= 1
            if self.position == -1:  # mange la fleure
                self.etat = Constantes.TERMINE