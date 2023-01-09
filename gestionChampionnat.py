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

    #affiche equipes pour un championna précis
    def afficherEquipes(self, nomChampionnat):
        for championnat in self.championnats:
            if championnat.nom == nomChampionnat:
                for equipe in championnat.equipes:
                    equipe.afficher()
            
    def afficherClassement(self, nomChampionnat):
        for championnat in self.championnats:
            if championnat.nom == nomChampionnat:
                championnat.afficher_classement()