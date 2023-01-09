from equipe import Equipe

class Match:
    def __init__(self, score_equipe1, score_equipe2, numero_journee, equipe1, equipe2):
        self.score_equipe1 = int(score_equipe1)
        self.score_equipe2 = int(score_equipe2)
        self.numero_journee = int(numero_journee)
        self.equipe1 = str(equipe1)
        self.equipe2 = str(equipe2)
        
        