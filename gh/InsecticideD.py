from constantes import *

class InsecticideD:
    def __init__(self):
        self.position = 1
        self.delai_attente = 1
        self.etat = Constantes.NORMAL

    def actualiserEtat(self):
        self.delai_attente -= 1
        if self.delai_attente <= 0:
            self.delai_attente = 1
            self.position += 1
            if self.position == 4:
                self.etat = Constantes.TERMINE
