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
    
    def ajouterEquipe(self):
        equipe = Equipe(self.idEquipe, str(input("Nom de l'équipe : ")), str(input("Date de création : ")), str(input("Stade : ")), str(input("Entraineur : ")), str(input("Président : ")))
        self.idEquipe += 1
        
        championnat = str(input("nom du championnat"))
        if championnat == self.rechercheChampionnat():
            self.championnats.append(equipe)
        else:
            print("Championnat inexistant")
        
    def rechercheChampionnat(self, nomChampionnat):
        for championnat in self.championnats:
            if championnat.nom == nomChampionnat:
                return True
        return False
        
    def ajouterMatch(self):
        match = Match(self.idMatch, str(input("Nom du match : ")), str(input("Date du match : ")), str(input("Heure du match : ")), str(input("Lieu du match : ")), str(input("Equipe domicile : ")), str(input("Equipe extérieur : ")), str(input("Score : ")))
        self.idMatch += 1
        
        championnat = str(input("nom du championnat"))
        if championnat == self.rechercheChampionnat():
            self.championnats.append(championnat)
        else:
            print("Championnat inexistant")


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
