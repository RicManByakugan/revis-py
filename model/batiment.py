class Batiment:
    
    def __init__(self, etage, adress):
        self.etage = etage
        self.adresse = adress
        
    def get_etage(self):
        return self.etage
    
    def get_adresse(self):
        return self.adresse
    
class Immeuble(Batiment):
    
    def __init__(self, etage, adresse, superficie):
        super().__init__(etage, adresse)
        self.superficie = superficie
    
    def get_superficie(self):
        return self.superficie
    
class SuperMarche(Batiment):
    
    def __init__(self, etage, adresse, rayon):
        super().__init__(etage, adresse)
        self.rayon = rayon
        
    def get_rayon(self):
        return self.rayon