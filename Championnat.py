from match import Match
from equipe import Equipe

class Championnat:

    def __init__(self, id, nom, date_debut, date_fin, point_gagne, point_perdu, point_nul, type_classement):
        self.id = id
        self.nom = nom
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.point_gagne = point_gagne
        self.point_perdu = point_perdu
        self.point_nul = point_nul
        self.type_classement = type_classement
        self.equipes = []
        self.matchs = []
    
    def afficher(self):
        print("Nom : ", self.nom)
        print("Date de début / fin : ", self.date_debut, " / ", self.date_fin, "\n")
    
    def afficher_classement(self):
        print("Classement")
        print("\t\t Pts \t Joués \t Gagné \t Nul \t Perdu")
        
    def calculer_point(self):
        print("Calculer point")
        
    def ajouterEquipe(self, equipe):
        self.equipes.append(equipe)
        
    def ajouterMatch(self, match):
        self.matchs.append(match)