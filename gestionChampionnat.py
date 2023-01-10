from equipe import Equipe
from Championnat import Championnat
from match import Match

class GestionChampionnat:
    idEquipe = 0
    idMatch = 0
    idChampionnat = 0
    
    def __init__(self):
        self.championnats = []
        
    def menu(self):
        print("1. Afficher les championnats")
        print("2. Ajouter un championnat")
        print("3. Ajouter une équipe à un championnat")
        print("4. Ajouter un match à un championnat")
        print("5. Quitter")
    
    # CHAMPIONNAT ###########################################
    def creerChampionnat(self):
        championnat = Championnat(self.idChampionnat, str(input("Nom du championnat : ")), str(input("Date de début : ")), str(input("Date de fin : ")), str(input("Point gagné : ")), str(input("Point perdu : ")), str(input("Point nul : ")), str(input("Type de classement : ")))
        self.idChampionnat += 1
        self.ajouterChampionnat(championnat)
        
    def ajouterChampionnat(self,championnat):
        self.championnats.append(championnat)
        
    
    # EQUIPE ###########################################
    def creerEquipe(self):
        equipe = Equipe(self.idEquipe, str(input("Nom de l'équipe : ")), str(input("Date de création : ")), str(input("Stade : ")), str(input("Entraineur : ")), str(input("Président : ")))
        self.idEquipe += 1
        
        championnat = str(input("nom du championnat"))
        
        championnatIndex = self.rechercheChampionnat(championnat) 
        if championnatIndex != None:
            self.championnats[championnatIndex].ajouterEquipe(equipe)
        else:
            print("Championnat inexistant")

    ###########################################
    
    # MATCH ###########################################  
    def creerMatch(self):
        match = Match(self.idMatch, str(input("Nom du match : ")), str(input("Date du match : ")), str(input("Heure du match : ")), str(input("Lieu du match : ")), str(input("Equipe domicile : ")), str(input("Equipe extérieur : ")), str(input("Score : ")))
        self.idMatch += 1
        
        championnat = str(input("nom du championnat"))
        
        championnatIndex = self.rechercheChampionnat(championnat) 
        if championnatIndex != None:
            self.championnats[championnatIndex].ajouterMatch(match)
        else:
            print("Championnat inexistant")
        
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
        print("============================")
        print("Liste des championnats : ")
        print("============================")
        for championnat in self.championnats:
            if championnat.afficher() != None:
                print(championnat.afficher())

#TESTS
#CHAMPINNAT****************
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

championnat1.ajouterEquipe(equipe1)
championnat1.ajouterEquipe(equipe2)
championnat2.ajouterEquipe(equipe3)
championnat2.ajouterEquipe(equipe4)
championnat3.ajouterEquipe(equipe3)
championnat3.ajouterEquipe(equipe1)
"""
championnat.ajouterEquipe(equipe1, championnat1)
championnat.ajouterEquipe(equipe2, championnat1)
championnat.ajouterEquipe(equipe3, championnat2)
championnat.ajouterEquipe(equipe4, championnat2)
championnat.ajouterEquipe(equipe3, championnat3)
championnat.ajouterEquipe(equipe1, championnat3)
"""
match1 = Match(1, 2, 1, equipe1, equipe2)
match2 = Match(2, 2, 1, equipe2, equipe1)
match3 = Match(3, 2, 1, equipe3, equipe4)
match4 = Match(1, 2, 1, equipe4, equipe3)
match5 = Match(1, 1, 1, equipe3, equipe1)
match6 = Match(1, 3, 1, equipe1, equipe3)

championnat1.ajouterMatch(match1)
championnat1.ajouterMatch(match2)
championnat2.ajouterMatch(match3)
championnat2.ajouterMatch(match4)
championnat3.ajouterMatch(match5)
championnat3.ajouterMatch(match6)
"""
championnat1 = championnat.ajouterMatch(match2)
championnat2 = championnat.ajouterMatch(match3)
championnat2 = championnat.ajouterMatch(match4)
championnat3 = championnat.ajouterMatch(match5)
championnat3 = championnat.ajouterMatch(match6)
"""
championnat.afficherChampionnat()

championnat.afficherClassement("Coupe du monde 2002")
championnat.afficherClassement("Coupe du monde 2006")
championnat.afficherClassement("Coupe d'Europe 2008")

championnat.afficherEquipes("Coupe du monde 2002")
championnat.afficherEquipes("Coupe du monde 2006")
championnat.afficherEquipes("Coupe d'Europe 2008")

# championnat.ajouterEquipe()
# gestion = GestionChampionnat()
# choix = 0

# while choix != 5:
#     gestion.menu()
#     choix = int(input("Choix : "))

#     if choix == 1:
#         gestion.afficherChampionnat()
#     elif choix == 2:
#         gestion.ajouterChampionnat()
#     elif choix == 3:
#         gestion.ajouterEquipe()
#     elif choix == 4:
#         gestion.ajouterMatch()
