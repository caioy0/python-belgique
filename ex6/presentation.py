import pygame
import time
from constantes import *

class Presentation:
    def __init__(self):
        pygame.init()

        # charger toutes les images du jeu

        self.imgFondEcran = pygame.image.load("./images/autres/fondEcran.png")
        self.imgTrColis1 = pygame.image.load("./images/transporteur/colis1.png")
        self.imgTrColis2 = pygame.image.load("./images/transporteur/colis2.png")
        self.imgTrColis3 = pygame.image.load("./images/transporteur/colis3.png")
        self.imgTrColis4 = pygame.image.load("./images/transporteur/colis4.png")
        self.imgTrVide1 = pygame.image.load("./images/transporteur/vide1.png")
        self.imgTrVide2 = pygame.image.load("./images/transporteur/vide2.png")
        self.imgTrVide3 = pygame.image.load("./images/transporteur/vide3.png")
        self.imgTrPlonge1 = pygame.image.load("./images/transporteur/plonge1.png")
        self.imgTrPlonge2 = pygame.image.load("./images/transporteur/plonge2.png")
        self.imgEmetteur = pygame.image.load("./images/autres/emetteur.png")
        self.imgRecepteur1 = pygame.image.load("./images/autres/recepteur1.png")
        self.imgRecepteur2 = pygame.image.load("./images/autres/recepteur2.png")
        self.imgTortue0 = pygame.image.load("./images/autres/tortue0.png")
        self.imgTortue1 = pygame.image.load("./images/autres/tortue1.png")
        self.imgTortue2 = pygame.image.load("./images/autres/tortue2.png")
        self.imgPoisson1 = pygame.image.load("./images/autres/poisson1.png")
        self.imgPoisson2 = pygame.image.load("./images/autres/poisson2.png")
        self.imgChiffre0 = pygame.image.load("./images/chiffres/Zero.png")
        self.imgChiffre1 = pygame.image.load("./images/chiffres/Un.png")
        self.imgChiffre2 = pygame.image.load("./images/chiffres/Deux.png")
        self.imgChiffre3 = pygame.image.load("./images/chiffres/Trois.png")
        self.imgChiffre4 = pygame.image.load("./images/chiffres/Quatre.png")
        self.imgChiffre5 = pygame.image.load("./images/chiffres/Cinq.png")
        self.imgChiffre6 = pygame.image.load("./images/chiffres/Six.png")
        self.imgChiffre7 = pygame.image.load("./images/chiffres/Sept.png")
        self.imgChiffre8 = pygame.image.load("./images/chiffres/Huit.png")
        self.imgChiffre9 = pygame.image.load("./images/chiffres/Neuf.png")

        # créer la fenêtre avec l'image du fond et le titre

        pygame.display.set_caption("Turtle bridge")
        pygame.display.set_icon(pygame.image.load("./images/autres/iconeFenetre.png"))
        self.ecran = pygame.display.set_mode((760, 420))
        self.ecran.blit(self.imgFondEcran, (0, 0))

        pygame.display.update()

    # ------------------------------------------------------------------------
    # retourner la touche sur laquelle a appuyé le joueur ou fermer la fenêtre
    # si clic sur la croix

    def lireEvenement(self):
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                    return evenement.key
        return Constantes.AUCUN_EVENEMENT

    # ------------------------------------------------------------------------
    # fermer la fenêtre si clic sur la croix

    def attendreFermetureFenetre(self):
        while True:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            time.sleep(0.2)

    # ------------------------------------------------------------------------
    # afficher les différentes images du transporteur avec ou sans colis

    def afficherTransporteur(self, position, etat, colis):
        if etat == Constantes.SAUT_GAUCHE:
            self.afficherImage(200, 80, self.imgEmetteur)
            self.afficherImage(200, 120, self.imgTrColis4)
        else:
            if colis == Constantes.PRESENT:
                if etat == Constantes.REPOS:
                    self.afficherImage(240 + position * 80, 160, self.imgTrColis1)
                elif etat == Constantes.SAUT:
                    self.afficherImage(280 + position * 80, 120, self.imgTrColis2)
                elif etat == Constantes.SAUT_DROITE:
                    self.afficherImage(240 + position * 80, 120, self.imgTrColis3)
                elif etat == Constantes.ECHEC:
                    self.afficherImage(240 + position * 80, 160, self.imgTrPlonge2)
                    self.afficherImage(240 + position * 80, 200, self.imgTrPlonge1)
            elif colis == Constantes.ABSENT:
                if etat == Constantes.REPOS:
                    self.afficherImage(240 + position * 80, 160, self.imgTrVide1)
                elif etat == Constantes.SAUT:
                    self.afficherImage(280 + position * 80, 120, self.imgTrVide2)
                elif etat == Constantes.SAUT_DROITE:
                    self.afficherImage(240 + position * 80, 120, self.imgTrVide3)
                elif etat == Constantes.ECHEC:
                    self.afficherImage(240 + position * 80, 200, self.imgTrPlonge1)

    # ------------------------------------------------------------------------
    # afficher le récepteur du colis

    def afficherRecepteur(self, etat):
        if etat == Constantes.PRESENT:
            self.afficherImage(520, 120, self.imgRecepteur1)
        elif etat == Constantes.PRESENT_2:
            self.afficherImage(520, 120, self.imgRecepteur2)

    # ------------------------------------------------------------------------
    # afficher les différentes images d'un poisson

    def afficherPoisson(self, position, etat):
        if etat == Constantes.PRESENT:
            self.afficherImage(200 + position * 80, 280, self.imgPoisson1)
        elif etat == Constantes.PRESENT_2:
            self.afficherImage(200 + position * 80, 280, self.imgPoisson2)

    # ------------------------------------------------------------------------
    # afficher les différentes images d'une tortue

    def afficherTortue(self, position, etat):
        if etat == Constantes.ABSENT:
            self.afficherImage(240 + position * 80, 240, self.imgTortue0)
        elif etat ==  Constantes.PRESENT:
            self.afficherImage(240 + position * 80, 200, self.imgTortue1)
        elif etat ==  Constantes.PRESENT_2:
            self.afficherImage(240 + position * 80, 200, self.imgTortue2)

    # ------------------------------------------------------------------------
    # afficher le score

    def afficherScore(self, score):
        self.afficherChiffre(640, score // 10)
        self.afficherChiffre(680, score % 10)

    # ------------------------------------------------------------------------
    # afficher les différents chiffres

    def afficherChiffre(self, colonne, chiffre):
        if chiffre == 0:
            self.afficherImage(colonne, 80, self.imgChiffre0)
        elif chiffre == 1:
            self.afficherImage(colonne, 80, self.imgChiffre1)
        elif chiffre == 2:
            self.afficherImage(colonne, 80, self.imgChiffre2)
        elif chiffre == 3:
            self.afficherImage(colonne, 80, self.imgChiffre3)
        elif chiffre == 4:
            self.afficherImage(colonne, 80, self.imgChiffre4)
        elif chiffre == 5:
            self.afficherImage(colonne, 80, self.imgChiffre5)
        elif chiffre == 6:
            self.afficherImage(colonne, 80, self.imgChiffre6)
        elif chiffre == 7:
            self.afficherImage(colonne, 80, self.imgChiffre7)
        elif chiffre == 8:
            self.afficherImage(colonne, 80, self.imgChiffre8)
        elif chiffre == 9:
            self.afficherImage(colonne, 80, self.imgChiffre9)

    # ------------------------------------------------------------------------
    # afficher l'image d'un personnage sur l'image de fond d'écran initiale

    def afficherImage(self, x, y, image):
        rect = image.get_rect()
        rect.x = x
        rect.y = y
        self.ecran.blit(image, rect)

    # ------------------------------------------------------------------------
    # restaurer en mémoire l'image d'origine de l'écran (ceci provoque
    # l'effacement de tous les personnages)

    def effacerImageInterne(self):
        self.ecran.blit(self.imgFondEcran, (0, 0, 760, 420), (0, 0, 760, 420))

    # ------------------------------------------------------------------------
    # mettre à jour l'image visible l'écran

    def actualiserFenetreGraphique(self):
        pygame.display.update()