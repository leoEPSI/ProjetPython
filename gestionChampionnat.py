class GestionChampionnat:
    
    def __init__(self):
        self.championnats = []
        
    def menu(self):
        print("1. Afficher les championnats")
        print("2. Ajouter un championnat")
        print("3. Ajouter une équipe à un championnat")
        print("4. Ajouter un match à un championnat")
        print("5. Quitter")
    
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
        for championnat in self.championnats:
            print(championnat)
        
    def afficherEquipes(self):
        for equipe in self.championnats:
            equipe.afficher()
            
    def afficherClassement(self):
        for equipe in self.championnats:
            equipe.afficher()

    choix = 0
    while choix != 7:
        menu()
        choix = int(input("Choix : "))

        if choix == 1:
            afficherChampionnat()
        elif choix == 2:
            ajouterChampionnat()
        elif choix == 3:
            ajouterEquipe()
        elif choix == 4:
            ajouterMatch()
