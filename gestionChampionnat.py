class GestionChampionnat:
    
    def __init__(self):
        self.championnats = []
        
    def menu(self):
        print("1. Ajouter un championnat")
        print("2. Afficher les championnats")
        print("3. Quitter")
    
    def ajouterChampionnat(self, championnat, nom, pays, nb_equipes, point_win, point_nul, point_lose, ex_aequo):
        self.championnats.append(championnat)
        self.nom = str(input("Nom du championnat : "))
        self.pays = str(input("Pays du championnat : "))
        self.nb_equipes = int(input("Nombre d'équipes : "))
        self.point_win = int(input("Points pour une victoire : "))
        self.point_nul = int(input("Points pour un match nul : "))
        self.point_lose = int(input("Points pour une défaite : "))
    
    def ajouterEquipe(self, equipe):
        self.championnats.append(equipe)
        
    def ajouterMatch(self, match):
        self.championnats.append(match)
        
    def afficherEquipes(self):
        for equipe in self.championnats:
            equipe.afficher()
            
    def afficherClassement(self):
        for equipe in self.championnats:
            equipe.afficher()