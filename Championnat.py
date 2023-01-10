from match import Match
from equipe import Equipe
import operator

class Championnat:

    def __init__(self, id, nom, date_debut, date_fin, point_gagne, point_perdu, point_nul, type_classement):
        self.id = id
        self.nom = nom
        self.date_debut = date_debut
        self.date_fin = date_fin
        
        #c'est simplement des coefficient pour calculer les points
        self.point_gagne = point_gagne
        self.point_perdu = point_perdu
        self.point_nul = point_nul
        #############################
        
        self.type_classement = type_classement
        self.equipes = []
        self.matchs = []
    
    def ajouterMatch(self, match):
        self.matchs.append(match)
        if match.score_equipe1 > match.score_equipe2:
            match.equipe1.ajoutMatch(mGagne = 1)
            match.equipe2.ajoutMatch(mPerdu = 1)
        elif match.score_equipe1 < match.score_equipe2:
            match.equipe1.ajoutMatch(mPerdu = 1)
            match.equipe2.ajoutMatch(mGagne = 1)
        else:
            match.equipe1.ajoutMatch(mNul = 1)
            match.equipe2.ajoutMatch(mNul = 1)

    def afficher(self):
        print("Nom : ", self.nom)
        print("Date de début / fin : ", self.date_debut, " / ", self.date_fin, "\n")
    
    def afficher_classement(self):
        tableauEquipe = []
        
        for equipe in self.equipes:
            tableauEquipe.append([equipe, self.calculer_point(equipe)])
        
        self.sortedEquipe(tableauEquipe)
        #sorted(tableauEquipe, key=operator.itemgetter(1), reverse=True)
        print("========================================================")
        print("Classement |")
        print("===========")
        print("\t\t Pts \t Joués \t Gagné \t Nul \t Perdu")
        for equipe in tableauEquipe:
            self.afficherEquipePoint(equipe[0], tableauEquipe.index(equipe) + 1)
        print("========================================================")
    
    def afficherEquipePoint(self, equipe, classement):
        print(str(classement), equipe.nom +"\t\t "+ str(self.calculer_point(equipe)) +"\t "+ str(self.calculer_match_joue(equipe)) +"\t "+ str(equipe.mGagne) +"\t "+ str(equipe.mNul) +"\t "+ str(equipe.mPerdu))
        
    def calculer_point(self, equipe):
        point = 0
        point += equipe.mGagne * self.point_gagne
        point += equipe.mNul * self.point_nul
        point += equipe.mPerdu * self.point_perdu
        return point
    
    def calculer_match_joue(self, equipe):
        return equipe.mGagne + equipe.mNul + equipe.mPerdu
        
    def ajouterEquipe(self, equipe):
        self.equipes.append(equipe)
        
    def sortedEquipe(self,tableauEquipe):
        #pour chaque case du tableau
        for i in range(0, len(tableauEquipe)):
            #pour chaque case du tableau après la case i
            for j in range(i + 1, len(tableauEquipe)):
                if tableauEquipe[i][1] != tableauEquipe[j][1]:
                    if tableauEquipe[i][1] < tableauEquipe[j][1]:
                        temp = tableauEquipe[i]
                        tableauEquipe[i] = tableauEquipe[j]
                        tableauEquipe[j] = temp
                else:
                    equip1 = tableauEquipe[i][0]
                    equip2 = tableauEquipe[j][0]
                    nbrBut1 = 0
                    nbrBut2 = 0

                    for match in self.matchs:
                        if match.equipe1.id == equip1.id :
                            nbrBut1 += match.score_equipe1
                        if match.equipe2.id == equip1.id :
                            nbrBut1 += match.score_equipe2
                        if match.equipe1.id == equip2.id :
                            nbrBut2 += match.score_equipe1
                        if match.equipe2.id == equip2.id :
                            nbrBut2 += match.score_equipe2
                    
                    print(equip1.nom, nbrBut1, equip2.nom,nbrBut2)
                    if nbrBut1 < nbrBut2:
                        temp = tableauEquipe[i]
                        tableauEquipe[i] = tableauEquipe[j]
                        tableauEquipe[j] = temp
