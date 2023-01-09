from equipe import Equipe
from match import Match

class GestionChampionnat:
    idEquipe = 0
    idMatch = 0
    
    def __init__(self):
        self.championnats = []
        
    def menu(self):
        print("1. Afficher les championnats")
        print("2. Ajouter un championnat")
        print("3. Ajouter une équipe à un championnat")
        print("4. Ajouter un match à un championnat")
        print("5. Quitter")
    
    def ajouterChampionnat(self, championnat):
        self.championnats.append(championnat)
        nom = str(input("Nom du championnat : "))
        pays = str(input("Pays du championnat : "))
        nb_equipes = int(input("Nombre d'équipes : "))
        point_win = int(input("Points pour une victoire : "))
        point_nul = int(input("Points pour un match nul : "))
        point_lose = int(input("Points pour une défaite : "))
        print(nom, pays, nb_equipes, point_win, point_nul, point_lose)
    
    # EQUIPE ###########################################
    def creerEquipe(self):
        equipe = Equipe(self.idEquipe, str(input("Nom de l'équipe : ")), str(input("Date de création : ")), str(input("Stade : ")), str(input("Entraineur : ")), str(input("Président : ")))
        self.idEquipe += 1
        
        championnat = str(input("nom du championnat"))
        
        championnatIndex = self.rechercheChampionnat(championnat) 
        if championnatIndex != None:
            self.ajouterEquipe(equipe, championnatIndex)
        else:
            print("Championnat inexistant")
               
    def ajouterEquipe(self, equipe, championnatIndex):
            self.championnats[championnatIndex].equipes.append(equipe)        
    ###########################################
    
    # MATCH ###########################################  
    def creerMatch(self):
        match = Match(self.idMatch, str(input("Nom du match : ")), str(input("Date du match : ")), str(input("Heure du match : ")), str(input("Lieu du match : ")), str(input("Equipe domicile : ")), str(input("Equipe extérieur : ")), str(input("Score : ")))
        self.idMatch += 1
        
        championnat = str(input("nom du championnat"))
        
        championnatIndex = self.rechercheChampionnat(championnat) 
        if championnatIndex != None:
            self.ajouterMatch(match, championnatIndex)
        else:
            print("Championnat inexistant")
        
    def ajouterMatch(self, match, championnatIndex):
        self.championnats[championnatIndex].matchs.append(match)   
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
                for equipe in championnat.equipes:
                    equipe.afficher()
            
    #affiche le classement pour un championnat précis
    def afficherClassement(self, nomChampionnat):
        for championnat in self.championnats:
            if championnat.nom == nomChampionnat:
                championnat.afficher_classement()

    def afficherChampionnat(self):
        print("Liste des championnats : ")
        for championnat in self.championnats:
            print(championnat.afficher())
        print("")

gestion = GestionChampionnat()
choix = 0

while choix != 5:
    gestion.menu()
    choix = int(input("Choix : "))

    if choix == 1:
        gestion.afficherChampionnat()
    elif choix == 2:
        gestion.ajouterChampionnat()
    elif choix == 3:
        gestion.ajouterEquipe()
    elif choix == 4:
        gestion.ajouterMatch()
