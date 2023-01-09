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
    
    def afficher():
        print("Fonction afficher")
    
    def afficher_classement():
        print("Afficher Classement")
    
    def calculer_point():
        print("Calculer point")