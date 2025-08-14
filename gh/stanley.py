import pygame
from constantes import *

class Stanley:
    def __init__(self):
        self.etat = Constantes.BAS
        self.position = 1
        self.action = Constantes.NORMAL

#Keyboard commands
    def actualiserEtat(self, evenement):
        if evenement == pygame.K_SPACE:
            if self.etat == Constantes.ECHELLE:
                self.action = Constantes.NORMAL
            else:
                self.action = Constantes.SPRAY
        else:
            self.action = Constantes.NORMAL
#Place base section commands
            if self.etat == Constantes.BAS:
                if evenement == pygame.K_RIGHT:
                    if self.position < 3:
                        self.position += 1
                elif evenement == pygame.K_LEFT:
                    if self.position > 0:
                        self.position -= 1 
                elif evenement == pygame.K_UP and self.position == 1:
                    self.etat = Constantes.ECHELLE
#Echelle commands
            elif self.etat == Constantes.ECHELLE:
#Key_up -- Haut
                if evenement == pygame.K_UP:
                    if self.position > -1:
                        self.position -= 1
                    if self.position == -1:
                        self.etat = Constantes.HAUT         #Go to 2f
                        self.position = 2
#Key_down -- Bas
                elif evenement == pygame.K_DOWN:
                    if self.position < 2:
                        self.position += 1
                    if self.position == 2:
                        self.etat = Constantes.BAS            #go to 1f
                        self.position = 1
#2f commands
            elif self.etat == Constantes.HAUT:
                if evenement == pygame.K_RIGHT:
                    if self.position < 5:
                        self.position += 1
                elif evenement == pygame.K_LEFT:
                    if self.position > 0:
                        self.position -= 1 
                elif evenement == pygame.K_DOWN and self.position == 2:
                    self.etat = Constantes.ECHELLE
                    self.position = 0
