class Nom:
    
    
    def __init__(self, fichier):
        
        self.fichier = fichier
        
        
    def nomCopie(self, nomFichier, extensionFichier):
        
        nouveau_nom = ""
        
        if self.fichier[-9:] == "Copie.txt":
            chiffre = 1
            nouveau_nom = f"{nomFichier}-{chiffre}{extensionFichier}"
            
        else:
            indexDebut = self.fichier.index("Copie (")
            indexFin = self.fichier.index(f"){extensionFichier}")
            chiffre = self.fichier[indexDebut+7:indexFin]
            nouveau_nom = f"{nomFichier}-{chiffre}{extensionFichier}"
               
        return nouveau_nom
