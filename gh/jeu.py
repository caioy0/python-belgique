import time
from presentation import *
from stanley import *
from Ennemis import *
from Guepe import *
from ChenilleG import *
from ChenilleD import *
from AraigneeG import *
from AraigneeD import *
from InsecticideG import *
from InsecticideD import *

class Jeu:
    def __init__(self):
        self.presentation = Presentation()   # attribut pour la couche présentation
        self.stanley = Stanley()             # attribut pour Stanley
        self.ami = [Constantes.NORMAL for i in range(5)]
        self.ennemis = Ennemis()
        self.guepe = None
        self.echec = 0
        self.score = 0
        self.chenilleG = []
        self.chenilleD = []
        self.araigneeG = []
        self.araigneeD = []
        self.insecticideG = []
        self.insecticideD = []

    # ----------------------------------------------------------------------------
    # méthode qui contient la boucle principale du jeu

    def demarrer(self):
        while self.echec < 3:
            # le code de gestion du déplacement des ennemis et des collisions va venir ici ...
            self.gererGuepe()
            self.gererChenilleG()
            self.gererChenilleD()
            self.gererAraigneeG()
            self.gererAraigneeD()
            self.gererInsecticideG()
            self.gererInsecticideD()
            self.gererCollisionInsecticide()

            # le code de génération des ennemis va venir ici ...
            ennemi_type = self.ennemis.actualiserEtat()  # Création de l'ennemi
            self.genererEnnemis(ennemi_type)

            # récupérer l'événement du joueur et changer l'état de Stanley
            self.stanley.actualiserEtat(self.presentation.lireEvenement())

            # mettre à jour l'image à l'écran
            self.actualiserEcran()

            # attendre 100 millisecondes (délai de référence)
            time.sleep(0.1)

        # Fin du jeu
        self.presentation.attendreFermetureFenetre()

    # ----------------------------------------------------------------------------
    # méthode qui genere les ennemi
    def genererEnnemis(self, ennemi_type):
        if ennemi_type == Constantes.GUEPE:
            if not self.guepe:
                self.guepe = Guepe()
        elif ennemi_type == Constantes.CHENILLE_G:
            self.chenilleG.append(ChenilleG())
        elif ennemi_type == Constantes.CHENILLE_D:
            self.chenilleD.append(ChenilleD())
        elif ennemi_type == Constantes.ARAIGNEE_G:
            self.araigneeG.append(AraigneeG())
        elif ennemi_type == Constantes.ARAIGNEE_D:
            self.araigneeD.append(AraigneeD())

    # ----------------------------------------------------------------------------
    # Guepe
    def gererGuepe(self):
        if self.guepe:  # deplacement + collision de guepe
            self.guepe.actualiserEtat()
            if self.guepe.etat == Constantes.TERMINE:
                self.echec += 1
                self.ami[Constantes.CHAT] = Constantes.TOUCHE
                self.actualiserEcran()
                time.sleep(1.5)
                self.guepe = None
                self.ami[Constantes.CHAT] = Constantes.NORMAL

    # ----------------------------------------------------------------------------
    # ChenilleG
    def gererChenilleG(self):
        for chenille in self.chenilleG[:]:
            chenille.actualiserEtat()
            if chenille.etat == Constantes.TERMINE:
                self.echec += 1
                self.ami[Constantes.FLEUR_HG] = Constantes.TOUCHE
                self.actualiserEcran()
                time.sleep(1.5)
                self.chenilleG.remove(chenille)
                self.ami[Constantes.FLEUR_HG] = Constantes.NORMAL

    # ----------------------------------------------------------------------------
    # ChenilleD
    def gererChenilleD(self):
        for chenille in self.chenilleD[:]:
            chenille.actualiserEtat()
            if chenille.etat == Constantes.TERMINE:
                self.echec += 1
                self.ami[Constantes.FLEUR_HD] = Constantes.TOUCHE
                self.actualiserEcran()
                time.sleep(1.5)
                self.chenilleD.remove(chenille)
                self.ami[Constantes.FLEUR_HD] = Constantes.NORMAL

    # ----------------------------------------------------------------------------
    # araigneeG
    def gererAraigneeG(self):
        for araignee in self.araigneeG[:]:
            araignee.actualiserEtat()
            if araignee.etat == Constantes.TERMINE:
                self.echec += 1
                self.ami[Constantes.FLEUR_BG] = Constantes.TOUCHE
                self.actualiserEcran()
                time.sleep(1.5)
                self.araigneeG.remove(araignee)
                self.ami[Constantes.FLEUR_BG] = Constantes.NORMAL

    # ----------------------------------------------------------------------------
    # araigneeD
    def gererAraigneeD(self):
        for araignee in self.araigneeD[:]:
            araignee.actualiserEtat()
            if araignee.etat == Constantes.TERMINE:
                self.echec += 1
                self.ami[Constantes.FLEUR_BD] = Constantes.TOUCHE
                self.actualiserEcran()
                time.sleep(1.5)
                self.araigneeD.remove(araignee)
                self.ami[Constantes.FLEUR_BD] = Constantes.NORMAL

    # ----------------------------------------------------------------------------
    # methode qui gere une insecticideG
    def gererInsecticideG(self):
        self.insecticideG = [nuage for nuage in self.insecticideG if nuage.etat != Constantes.TERMINE]
        for nuage1 in self.insecticideG:
            nuage1.actualiserEtat()
            araignees_restant = []
            for araignee in self.araigneeG:
                if araignee.position != nuage1.position:
                    araignees_restant.append()
                    time.sleep(0.1)
            self.score += len(self.araigneeG) - len(araignees_restant)
            if araignees_restant != self.araigneeG:
                self.insecticideG = self.insecticideG[1:]
            self.araigneeG = araignees_restant

    # ----------------------------------------------------------------------------
    # methode qui gere une insecticideD
    def gererInsecticideD(self):
        self.insecticideD = [nuage for nuage in self.insecticideD if nuage.etat != Constantes.TERMINE]
        for nuage2 in self.insecticideD:
            nuage2.actualiserEtat()
            araignees_restant = [araignee for araignee in self.araigneeD if araignee.position != nuage2.position]
            self.score += len(self.araigneeD) - len(araignees_restant)
            if araignees_restant != self.araigneeD:
                self.insecticideD = self.insecticideD[1:]
            self.araigneeD = araignees_restant

    # ----------------------------------------------------------------------------
    # methode collision insecticide

    def gererCollisionInsecticide(self):
        if self.stanley.action == Constantes.SPRAY:
            self.appliquerEffetInsecticide()

    def appliquerEffetInsecticide(self):
        # Pour les guêpes
        if self.guepe and self.stanley.etat == Constantes.BAS and self.stanley.position == 2:
            if self.guepe.position == 0 or self.guepe.position == 1:
                self.guepe = None
                self.score += 1

        # Pour les chenilles à gauche
        positions_cibles = self.calculerPositionsCiblesChenilleG()
        chenilles_restant = [chenille for chenille in self.chenilleG if chenille.position not in positions_cibles]
        self.score += len(self.chenilleG) - len(chenilles_restant)
        self.chenilleG = chenilles_restant

        # Pour les chenilles à droite
        positions_cibles = self.calculerPositionsCiblesChenilleD()
        chenilles_restant = [chenille for chenille in self.chenilleD if chenille.position not in positions_cibles]
        self.score += len(self.chenilleD) - len(chenilles_restant)
        self.chenilleD = chenilles_restant

        # Pour les araignees à gauche
        positions_cibles = self.calculerPositionsCiblesAraigneeG()
        araignees_restant = [araignee for araignee in self.araigneeG if araignee.position not in positions_cibles]
        self.score += len(self.araigneeG) - len(araignees_restant)
        if positions_cibles:
            self.insecticideG.insert(1, InsecticideG())
        self.araigneeG = araignees_restant

        # Pour les araignees à droite
        positions_cibles = self.calculerPositionsCiblesAraigneeD()
        araignees_restant = [araignee for araignee in self.araigneeD if araignee.position not in positions_cibles]
        self.score += len(self.araigneeD) - len(araignees_restant)
        if positions_cibles:
            self.insecticideD.insert(1, InsecticideD())
        self.araigneeD = araignees_restant

    def calculerPositionsCiblesChenilleG(self):
        if self.stanley.etat == Constantes.HAUT and self.stanley.position == 0:
            return [0, 1]
        elif self.stanley.etat == Constantes.HAUT and self.stanley.position == 1:
            return [2, 3]
        return []

    def calculerPositionsCiblesChenilleD(self):
        if self.stanley.etat == Constantes.HAUT and self.stanley.position == 3:
            return [1, 2]
        elif self.stanley.etat == Constantes.HAUT and self.stanley.position == 4:
            return [3, 4]
        elif self.stanley.etat == Constantes.HAUT and self.stanley.position == 5:
            return [5, 6]
        return []

    def calculerPositionsCiblesAraigneeG(self):
        if self.stanley.etat == Constantes.BAS and self.stanley.position == 0:
            return [4]
        return []

    def calculerPositionsCiblesAraigneeD(self):
        if self.stanley.etat == Constantes.BAS and self.stanley.position == 3:
            return [0]
        return []
    # ----------------------------------------------------------------------------
    # méthode qui met à jour l'image du jeu à l'écran

    def actualiserEcran(self):
        self.presentation.effacerImageInterne()

        self.presentation.afficherStanley(self.stanley.etat, self.stanley.position,
                                          self.stanley.action)

        self.presentation.afficherAmi(Constantes.FLEUR_HG, self.ami[Constantes.FLEUR_HG])
        self.presentation.afficherAmi(Constantes.FLEUR_HD, self.ami[Constantes.FLEUR_HD])
        self.presentation.afficherAmi(Constantes.FLEUR_BG, self.ami[Constantes.FLEUR_BG])
        self.presentation.afficherAmi(Constantes.FLEUR_BD, self.ami[Constantes.FLEUR_BD])
        self.presentation.afficherAmi(Constantes.CHAT, self.ami[Constantes.CHAT])
        if self.guepe:
            self.presentation.afficherGuepe(self.guepe.position)
        self.presentation.afficherEchecs(self.echec)
        self.presentation.afficherScore(self.score)
        for chenille in self.chenilleG:
            self.presentation.afficherChenilleG(chenille.position)
        for chenille in self.chenilleD:
            self.presentation.afficherChenilleD(chenille.position)
        for araignee in self.araigneeG:
            self.presentation.afficherAraigneeG(araignee.position)
        for araignee in self.araigneeD:
            self.presentation.afficherAraigneeD(araignee.position)
        for nuage in self.insecticideG:
            self.presentation.afficherInsecticideG(nuage.position)
        for nuage in self.insecticideD:
            self.presentation.afficherInsecticideD(nuage.position)
        self.presentation.actualiserFenetreGraphique()