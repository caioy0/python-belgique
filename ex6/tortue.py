from random import *
from constantes import *

class Tortue:
    def __init__(self):
        self.delai = randint(50, 100)
        self.etat = Constantes.PRESENT

    # ------------------------------------------------------------------------
    # gérer les états possibles d'une tortue

    def actualiserEtat(self, collision):
        if collision == True:
            self.delai = randint(20, 40)
            self.etat = Constantes.ABSENT
        else:
            self.delai -= 1

            if self.delai == 0:
                self.delai = randint(50, 100)

                if randint(1, 2) == Constantes.PRESENT:
                    self.etat = Constantes.PRESENT_2
                else:
                    self.etat = Constantes.PRESENT