from constantes import *
from random import randint

class Ennemis:
    def __init__(self):
        self.delai = 16
        self.iteration = [100, 15] #[10 secondes, delai entre 1s et 15s]

    def actualiserEtat(self):
        self.delai -= 1
        self.iteration[0] -= 1

        if self.iteration[0] == 0:
            self.iteration[0] = 100
            self.iteration[1] = randint(10, 15)  # fin du 10s, changement de delai

        if self.delai <= 0:
            self.delai = self.iteration[1]
            choice = randint(0, 4)
            if choice == 0:
                return Constantes.GUEPE
            elif choice == 1:
                return Constantes.CHENILLE_G
            elif choice == 2:
                return Constantes.CHENILLE_D
            elif choice == 3:
                return Constantes.ARAIGNEE_G
            elif choice == 4:
                return Constantes.ARAIGNEE_D
        else:
            return Constantes.AUCUN_ENNEMI