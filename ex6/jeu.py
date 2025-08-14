from transporteur import *
from recepteur import *
from tortue import *
from poisson import *
from presentation import *

class Jeu:
    def __init__(self):
        self.presentation = Presentation()
        self.transporteur = Transporteur()
        self.recepteur = Recepteur()
        self.poissons = [Poisson(),
                         Poisson(),
                         Poisson(),
                         Poisson()]
        self.tortues = [Tortue(),
                        Tortue(),
                        Tortue(),
                        Tortue()]
        self.score = 0

    # ----------------------------------------------------------------------------
    # Méthode contenant la boucle principale du jeu

    def demarrer(self):
        evenement = pygame.K_RIGHT

        while True:
            # Tester quelle tortue peut plonger pour attraper un poisson à proximité et
            # faire évoluer l'état de chaque tortue et de chaque poisson

            for i in range(4):
                if self.tortues[i].etat == Constantes.PRESENT_2 and \
                        self.poissons[i].etat == Constantes.PRESENT_2:
                    self.tortues[i].actualiserEtat(True)
                    self.poissons[i].actualiserEtat(True)
                else:
                    self.tortues[i].actualiserEtat(False)
                    self.poissons[i].actualiserEtat(False)

            # Si le transporteur veut remettre un colis et que le récepteur est présent,
            # alors le colis est remis et le score est augmenté et
            # faire évoluer l'état du récepteur

            if self.transporteur.etat == Constantes.SAUT_DROITE and \
                    self.transporteur.colis == Constantes.PRESENT \
                    and self.recepteur.etat == Constantes.PRESENT:
                self.transporteur.colis = Constantes.ABSENT
                self.recepteur.actualiserEtat(True)
                self.score += 1
            else:
                self.recepteur.actualiserEtat(False)

            # Obtenir l'événement du joueur seulement si le transporteur peut se déplacer

            if self.transporteur.etat == Constantes.REPOS and self.transporteur.delai == 1:
                evenement = self.presentation.lireEvenement()

            # Tester si la tortue est présente à la position où le transporteur est posé et
            # faire évoluer l'état du transporteur

            if self.transporteur.etat == Constantes.REPOS and \
                    self.tortues[self.transporteur.position].etat == Constantes.ABSENT:
                self.transporteur.actualiserEtat(Constantes.AUCUN_EVENEMENT, True)
                self.actualiserEcran()
                self.presentation.attendreFermetureFenetre()
            else:
                self.transporteur.actualiserEtat(evenement, False)

            # Mettre à jour l'image à l'écran

            self.actualiserEcran()

            # attendre 100 millisecondes (délai de référence)

            time.sleep(0.1)

    # ----------------------------------------------------------------------------
    # mettre à jour l'image à l'écran

    def actualiserEcran(self):
        self.presentation.effacerImageInterne()

        self.presentation.afficherScore(self.score)
        self.presentation.afficherTransporteur(self.transporteur.position,
                                               self.transporteur.etat,
                                               self.transporteur.colis)
        self.presentation.afficherRecepteur(self.recepteur.etat)
        for i in range(len(self.tortues)):
            self.presentation.afficherTortue(i, self.tortues[i].etat)
        for i in range(len(self.poissons)):
            self.presentation.afficherPoisson(i, self.poissons[i].etat)

        self.presentation.actualiserFenetreGraphique()