class GestionChampionnat:
    
    def __init__(self):
        self.championnats = []
        
    def menu(self):
        print("1. Ajouter un championnat")
        print("2. Afficher les championnats")
        print("3. Quitter")
    
    def ajouterChampionnat(self, championnat):
        self.championnats.append(championnat)
    
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