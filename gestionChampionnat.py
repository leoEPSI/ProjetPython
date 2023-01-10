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
        print("5. Quitter")
    
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
        championnatIndex = self.rechercheChampionnat(nomChampionnat)
        if championnatIndex == None:
            print("Championnat inexistant")
            return

        try:
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
        nomChampionnat = str(inputTestStr("Nom du championnat : "))
        championnatIndex = self.rechercheChampionnat(nomChampionnat) 
        if championnatIndex == None:
            print("Championnat inexistant")
            return
        #affichage des equipes
        self.afficherEquipes(nomChampionnat)

        try:
            equipeMatch1 = str(inputTestStr("Nom de l'équipe 1 : "))
            equipeMatch2 = str(inputTestStr("Nom de l'équipe 2 : "))
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
        return None

    #affiche equipes pour un championna précis
    def afficherEquipes(self, nomChampionnat):
        for championnat in self.championnats:
            if championnat.nom == nomChampionnat:
                print("Championnat :", championnat.id, "-", championnat.nom)
                for equipe in championnat.equipes:
                    equipe.afficher()
            
    #affiche le classement pour un championnat précis
    def afficherClassement(self, nomChampionnat):
        for championnat in self.championnats:
            if championnat.nom == nomChampionnat:
                championnat.afficher_classement()
        print("")    

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

    match1 = Match(1, 2, 1, equipe1, equipe2)
    match2 = Match(2, 2, 1, equipe2, equipe1)
    match3 = Match(3, 2, 1, equipe3, equipe4)
    match4 = Match(1, 2, 1, equipe4, equipe3)
    match5 = Match(1, 1, 1, equipe3, equipe1)
    match6 = Match(1, 3, 1, equipe1, equipe3)
    match7 = Match(1, 3, 1, equipe5, equipe6)
    match8 = Match(2, 3, 1, equipe2, equipe5)

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

main()
#test()