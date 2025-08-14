from random import *
from constantes import *

class Poisson:
    def __init__(self):
        self.delai = randint(50, 100)
        self.etat = Constantes.ABSENT

    # --------------------------------------------------------------------------
    # gérer les états possibles d'un poisson

    def actualiserEtat(self, collision):
        if collision == True:
            self.delai = randint(50, 100)
            self.etat = Constantes.ABSENT
        else:
            self.delai -= 1

            if self.delai == 0:
                self.delai = randint(50, 100)

                if self.etat == Constantes.ABSENT:
                    self.etat = Constantes.PRESENT
                elif self.etat == Constantes.PRESENT:
                    self.etat = Constantes.PRESENT_2
                elif self.etat == Constantes.PRESENT_2:
                    self.etat = Constantes.ABSENT