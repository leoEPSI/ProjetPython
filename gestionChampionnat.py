class GestionChampionnat:
    
    def __init__(self):
        self.championnats = []
        
    def menu(self):
        print("1. Ajouter un championnat")
        print("2. Afficher les championnats")
        print("3. Quitter")
    
    def ajouterChampionnat(self, championnat, nom, pays, nb_equipes, point_win, point_nul, point_lose, ex_aequo):
        self.nom = nom
        self.pays = pays
        self.nb_equipes = nb_equipes
        self.point_win = point_win
        self.point_nul = point_nul
        self.point_lose = point_lose
        self.ex_aequo = ex_aequo
        self.championnats.append(championnat)
        nom = str(input("Nom du championnat : "))
        pays = str(input("Pays du championnat : "))
        nb_equipes = int(input("Nombre d'équipes : "))
        point_win = int(input("Points pour une victoire : "))
        point_nul = int(input("Points pour un match nul : "))
        point_lose = int(input("Points pour une défaite : "))
        print(nom, pays, nb_equipes, point_win, point_nul, point_lose)
    
    def ajouterEquipe(self, equipe):
        self.championnats.append(equipe)
        
    def ajouterMatch(self, match):
        self.championnats.append(match)

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