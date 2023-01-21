from equipe import Equipe
from Championnat import Championnat
from match import Match
import os

class GestionChampionnat:
    idEquipe = 0
    idMatch = 0
    idChampionnat = 0
    
    def __init__(self):
        self.championnats = []
        
    def menu(self):
        cls()
        print("Que voulez-vous faire ?")
        print("1. Afficher les championnats")
        print("2. Ajouter un championnat")
        print("3. Ajouter une équipe à un championnat")
        print("4. Ajouter un match à un championnat")
        print("5. Afficher classement")
        print("6. Afficher equipes")
        print("7. Quitter")
    
    # CHAMPIONNAT ###########################################
    def creerChampionnat(self):

        try:
            nom = str(inputTestStr("Nom du championnat : "))
            dd = str(inputTestStr("Date de début : "))
            df = str(inputTestStr("Date de fin : "))
            pg = int(inputTestInt("Coefficient des point gagné : "))
            pp = int(inputTestInt("Coefficient des point perdu : "))
            pn = int(inputTestInt("Coefficient des point nul : "))
            tc = int(inputTestInt("Type de classement : "))
        except:
            print("Erreur de saisie")
            input("Appuyez sur une touche pour continuer")
            return

        championnat = Championnat(self.idChampionnat, nom, dd, df, pg, pp, pn, tc)
        self.idChampionnat += 1
        self.ajouterChampionnat(championnat)
        
    def ajouterChampionnat(self,championnat):
        self.championnats.append(championnat)
        
    
    # EQUIPE ###########################################
    def creerEquipe(self):
        self.afficherChampionnat()

        nomChampionnat = str(inputTestStr("Nom du championnat : "))

        try:
            championnatIndex = self.rechercheChampionnat(nomChampionnat)
            ne = str(inputTestStr("Nom de l'équipe : "))
            dc = str(inputTestStr("Date de création : "))
            s = str(inputTestStr("Stade : "))
            e = str(inputTestStr("Entraineur : "))
            p = str(inputTestStr("Président : "))
        except:
            print("Erreur de saisie")
            input("Appuyez sur une touche pour continuer")
            return

        equipe = Equipe(self.idEquipe, ne, dc, s, e, p)
        self.idEquipe += 1

        #le test est deja effectue au dessus
        self.championnats[championnatIndex].ajouterEquipe(equipe)    
    ###########################################
    
    # MATCH ###########################################  
    def creerMatch(self):
        self.afficherChampionnat()
        nomChampionnat = str(inputTestStr("Nom du championnat : "))
        
        try:
            championnatIndex = self.rechercheChampionnat(nomChampionnat) 
            #affichage des equipes
            self.afficherEquipes(nomChampionnat)
    
            #besoin de rechercher les equipes pour ne pas inserer simplement des string
            equipeMatch1 = self.rechercheEquipe(championnatIndex, str(inputTestStr("Nom de l'équipe 1 : ")))
            equipeMatch2 = self.rechercheEquipe(championnatIndex, str(inputTestStr("Nom de l'équipe 2 : ")))
            scoreEquipe1 = int(inputTestInt("Score de l'équipe 1 : "))
            scoreEquipe2 = int(inputTestInt("Score de l'équipe 2 : "))
            nj = str(inputTestStr("Numéro de journée (1) : "))
            
        except:
            print("Erreur de saisie")
            input("Appuyez sur une touche pour continuer")
            return

        match = Match(self.idMatch, scoreEquipe1, scoreEquipe2, nj, equipeMatch1, equipeMatch2)
        self.idMatch += 1
                
        self.championnats[championnatIndex].ajouterMatch(match)
    ###########################################
    
    # retourne index du championnat et si pas trouvé retourne none
    def rechercheChampionnat(self, nomChampionnat):
        i = 0
        for championnat in self.championnats:
            if championnat.nom == nomChampionnat:
                return i
            i += 1
        raise ValueError("Championnat inexistant")

    #retourne l'equipe et si pas trouvé retourne erreur
    def rechercheEquipe(self, indexChampionnat, nomEquipe):
        
        for equipe in self.championnats[indexChampionnat].equipes:
            #print(equipe.nom, nomEquipe)
            if equipe.nom == nomEquipe:
                return equipe
        raise ValueError("Equipe inexistant")
        
    #affiche equipes pour un championna précis
    def afficherEquipesSaisie(self):
        self.afficherChampionnat()
        try:
            nomChampionnat = str(inputTestStr("Nom du championnat : "))
            championnatIndex = self.rechercheChampionnat(nomChampionnat)
        except:
            print("Erreur de saisie")
            input("Appuyez sur une touche pour continuer")
            return
        self.afficherEquipes(nomChampionnat)
        
    def afficherEquipes(self, nomChampionnat):
        cls()
        for championnat in self.championnats:
            if championnat.nom == nomChampionnat:
                print("Championnat :", championnat.id, "-", championnat.nom)
                for equipe in championnat.equipes:
                    equipe.afficher()
        input("Appuyez sur une touche pour continuer")
        
    #affiche le classement pour un championnat précis
    def afficherClassementSaisie(self):
        self.afficherChampionnat()
        try:
            nomChampionnat = str(inputTestStr("Nom du championnat : "))
            championnatIndex = self.rechercheChampionnat(nomChampionnat)
        except:
            print("Erreur de saisie")
            input("Appuyez sur une touche pour continuer")
            return
        self.afficherClassement(nomChampionnat)
        
    def afficherClassement(self, nomChampionnat):
        cls()
        for championnat in self.championnats:
            if championnat.nom == nomChampionnat:
                championnat.afficher_classement()
        print("")    
        input("Appuyez sur une touche pour continuer")

    def afficherChampionnat(self):
        cls()
        print("============================")
        print("Liste des championnats : ")
        print("============================")
        for championnat in self.championnats:
            if championnat.afficher() != None:
                print(championnat.afficher())
        input("Appuyez sur une touche pour continuer")

    
def inputTestStr(afficher):
        valeur = input(afficher)
        if valeur == None or valeur == "":
            raise ValueError("Valeur incorrecte")

        return valeur

def inputTestInt(afficher):
        valeur = input(afficher)
        return valeur

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#TESTS
#CHAMPINNAT****************
def test():
    championnat = GestionChampionnat()
    championnat1 = Championnat(1, "Coupe du monde 2002", "13/04/2002", "13/05/2002", 3, 0, 1, 1)
    championnat2 = Championnat(2, "Coupe du monde 2006", "02/07/2006", "02/08/2006", 3, 0, 1, 2)
    championnat3 = Championnat(3, "Coupe d'Europe 2008", "25/10/2008", "25/11/2008", 3, 0, 1, 3)

    championnat.ajouterChampionnat(championnat1)
    championnat.ajouterChampionnat(championnat2)
    championnat.ajouterChampionnat(championnat3)

    equipe1 = Equipe(1, "ST", "13/02/1987", "Stade 1", "Bruno", "Leo")
    equipe2 = Equipe(2, "OL", "05/09/1977", "Stade 2", "Theo", "Lucas")
    equipe3 = Equipe(3, "OM", "16/01/2002", "Stade 3", "Rayan", "Leon")
    equipe4 = Equipe(4, "PSG", "18/10/1995", "Stade 4", "Fred", "Marie Curie")
    equipe5 = Equipe(5, "OM2", "16/01/2002", "Stade 3", "Rayan2", "Leon2")
    equipe6 = Equipe(6, "OM3", "16/01/2002", "Stade 3", "Rayan3", "Leon3")

    championnat1.ajouterEquipe(equipe1)
    championnat1.ajouterEquipe(equipe2)
    championnat1.ajouterEquipe(equipe5)
    championnat1.ajouterEquipe(equipe6)
    championnat2.ajouterEquipe(equipe3)
    championnat2.ajouterEquipe(equipe4)
    championnat3.ajouterEquipe(equipe3)
    championnat3.ajouterEquipe(equipe1)

    match1 = Match(1, 1, 2, 1, equipe1, equipe2)
    match2 = Match(2, 2, 2, 1, equipe2, equipe1)
    match3 = Match(3, 3, 2, 1, equipe3, equipe4)
    match4 = Match(4, 1, 2, 1, equipe4, equipe3)
    match5 = Match(5, 1, 1, 1, equipe3, equipe1)
    match6 = Match(6, 1, 3, 1, equipe1, equipe3)
    match7 = Match(7, 1, 3, 1, equipe5, equipe6)
    match8 = Match(8, 2, 3, 1, equipe2, equipe5)

    championnat1.ajouterMatch(match1)
    championnat1.ajouterMatch(match2)
    championnat1.ajouterMatch(match7)
    championnat1.ajouterMatch(match8)
    championnat2.ajouterMatch(match3)
    championnat2.ajouterMatch(match4)
    championnat3.ajouterMatch(match5)
    championnat3.ajouterMatch(match6)

    championnat.afficherChampionnat()

    championnat.afficherClassement("Coupe du monde 2002")
    championnat.afficherClassement("Coupe du monde 2006")
    championnat.afficherClassement("Coupe d'Europe 2008")

    championnat.afficherEquipes("Coupe du monde 2002")
    championnat.afficherEquipes("Coupe du monde 2006")
    championnat.afficherEquipes("Coupe d'Europe 2008")

def testPartiel():
    gestion = GestionChampionnat()
    choix = 0
    
    championnat1 = Championnat(1, "C", "13/04/2002", "13/05/2002", 3, 0, 1, 1)
    gestion.ajouterChampionnat(championnat1)
    
    equipe1 = Equipe(1, "ST", "13/02/1987", "Stade 1", "Bruno", "Leo")
    equipe2 = Equipe(2, "OL", "05/09/1977", "Stade 2", "Theo", "Lucas")
    
    gestion.championnats[0].ajouterEquipe(equipe1)
    gestion.championnats[0].ajouterEquipe(equipe2)
    
    match1 = Match(0,1, 2, 1, equipe1, equipe2)
    gestion.championnats[0].ajouterMatch(match1)
    
    while choix != 7:
        gestion.menu()
        choix = int(input("Choix : "))

        if choix == 1:
            gestion.afficherChampionnat()
        elif choix == 2:
            gestion.creerChampionnat()
        elif choix == 3:
            gestion.creerEquipe()
        elif choix == 4:
            gestion.creerMatch()
        elif choix == 5:
            gestion.afficherClassementSaisie()
        elif choix == 6:
            gestion.afficherEquipesSaisie()


def main():
    gestion = GestionChampionnat()
    choix = 0
    while choix != 5:
        gestion.menu()
        choix = int(input("Choix : "))

        if choix == 1:
            gestion.afficherChampionnat()
        elif choix == 2:
            gestion.creerChampionnat()
        elif choix == 3:
            gestion.creerEquipe()
        elif choix == 4:
            gestion.creerMatch()
        elif choix == 5:
            gestion.afficherClassementSaisie()
        elif choix == 6:
            gestion.afficherEquipesSaisie()

#main()
#test()
testPartiel()