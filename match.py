from equipe import Equipe

class Match:
    def __init__(self, score_equipe1, score_equipe2, numero_journee, equipe1, equipe2):
        score_equipe1 = int(score_equipe1)
        score_equipe2 = int(score_equipe2)
        numero_journee = int(numero_journee)
        equipe1 = str(equipe1)
        equipe2 = str(equipe2)