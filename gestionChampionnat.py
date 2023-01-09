class GestionChampionnat:
    
    def __init__(self, nom, pays, nb_equipes, point_win, point_nul, point_lose, ex_aequo):
        self.championnats = []
        self.nom = nom
        self.pays = pays
        self.nb_equipes = nb_equipes
        self.point_win = point_win
        self.point_nul = point_nul
        self.point_lose = point_lose
        self.ex_aequo = ex_aequo
        
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
