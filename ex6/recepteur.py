from random import *
from constantes import *

class Recepteur:
    def __init__(self):
        self.delai = randint(20, 80)
        self.etat = Constantes.ABSENT

    # ------------------------------------------------------------------------
    # gérer les états possibles du récepteur du colis

    def actualiserEtat(self, collision):
        if collision == True:
            self.delai = 5
            self.etat = Constantes.PRESENT_2
        else:
            self.delai -= 1

            if self.delai == 0:
                if self.etat == Constantes.ABSENT:
                    self.delai = randint(20, 80)
                    self.etat = Constantes.PRESENT
                else:
                    self.delai = randint(20, 80)
                    self.etat = Constantes.ABSENT
