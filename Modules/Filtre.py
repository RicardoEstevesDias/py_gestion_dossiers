from os.path import splitext


class Filtre:


    def __init__(self, listeFichiers):
        
        self.listeFichiers = listeFichiers
        
      
    def filtreNom(self, nom):
        
        if not nom:
            return []
        
        result = list()
        print("\n--Filtrage des fichiers par nom")
        for fichier in self.listeFichiers:
            nom_fichier = splitext(fichier)[0]
            if nom in nom_fichier:
                result.append(fichier)
    
        return result
     
     
    def filtreExtension(self, extension):
        
        result = list()
        print("\n--Filtrage des fichiers par extension")
        for fichier in self.listeFichiers:
            extension_fichier = splitext(fichier)[1]
            if extension == extension_fichier:
                result.append(fichier)
                
        return result
     

