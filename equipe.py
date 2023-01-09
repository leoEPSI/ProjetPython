
class Equipe:
    def __init__(self, id, nom, date_creation, stade, entraineur, president):
        self.id = id
        self.nom = nom
        self.date_creation = date_creation
        self.stade = stade
        self.entraineur = entraineur
        self.president = president
    
    def afficher(self):
        print("Equipe: ", self.nom)
        print("Date de création: ", self.date_creation)
        print("Stade: ", self.stade)
        print("Entraineur: ", self.entraineur)
        print("Président: ", self.president, "\n") 