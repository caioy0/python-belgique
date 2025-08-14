import pygame
from constantes import *

class Transporteur:
    def __init__(self):
        self.position = 0
        self.delai = 3
        self.colis = Constantes.PRESENT
        self.etat = Constantes.SAUT_GAUCHE

    # ------------------------------------------------------------------------
    # gérer les états et positions possibles du transporteur du colis

    def actualiserEtat(self, direction, collision):
        if collision == True:
            self.etat = Constantes.ECHEC
        else:
            self.delai -= 1

            if self.delai == 0:
                if self.etat == Constantes.REPOS:
                    if direction == pygame.K_RIGHT:
                        if self.position < 3:
                            self.etat = Constantes.SAUT
                        else:
                            if self.colis == Constantes.PRESENT:
                                self.etat = Constantes.SAUT_DROITE
                    elif direction == pygame.K_LEFT:
                        if self.position > 0:
                            self.position -= 1
                            self.etat = Constantes.SAUT
                        else:
                            if self.colis == Constantes.ABSENT:
                                self.colis = Constantes.PRESENT
                                self.etat = Constantes.SAUT_GAUCHE

                elif self.etat == Constantes.SAUT:
                    if direction == pygame.K_RIGHT:
                        self.position += 1
                        self.etat = Constantes.REPOS
                    elif direction == pygame.K_LEFT:
                        self.etat = Constantes.REPOS

                elif self.etat == Constantes.SAUT_DROITE:
                    self.etat = Constantes.REPOS

                elif self.etat == Constantes.SAUT_GAUCHE:
                    self.etat = Constantes.REPOS

                self.delai = 3