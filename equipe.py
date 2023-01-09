
class Equipe:
    def __init__(self, id, nom, date_creation, stade, entraineur, president):
        self.id = id
        self.nom = nom
        self.date_creation = date_creation
        self.stade = stade
        self.entraineur = entraineur
        self.president = president
        self.mGagne = 0
        self.mNul = 0
        self.mPerdu = 0
    
    def afficher(self):
        print("Equipe: ", self.nom)
        print("Date de création: ", self.date_creation)
        print("Stade: ", self.stade)
        print("Entraineur: ", self.entraineur)
        print("Président: ", self.president, "\n")
        
    def ajoutMatch(self, mGagne = 0, mNul = 0, mPerdu = 0):
        self.mGagne += mGagne
        self.mNul += mNul
        self.mPerdu += mPerdu