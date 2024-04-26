"""
Attention : Script pas trés pertinent
Script pour changer des copies de fichiers en fichier énumerés
Exemple pour fichier "Fichier.txt", x étant le nombre de la copie:
Fichier - Copie (x).txt' => 'Fichierx.txt
"""

from Modules.confirmation import confirmation
from Modules.Filtre import Filtre
from Modules.Nom import Nom
from os import listdir, rename, remove
from os.path import join, split
from time import sleep



while True:
    
    while True:
        
        confirmation_user = None
        
        try:
            chemin = input(r"Donnez le chemin vers le dossier souhaité: ")
            elementsDossier = listdir(chemin)
                
        except:
            print("Le chemin spécifié n'existe pas...")
            continue
        
        print("\n--Répertoire trouvé")
        
        if not elementsDossier:
            
            while True:
                  
                confirmation_user = confirmation(str(input(f"Le répertoire est vide, voulez-vous selectionner un autre? '{chemin}'? o/n: ")))
                if confirmation_user == "Erreur":
                    print("Veillez entrer une des deux valeurs demandés")
                    continue

                elif confirmation_user == "Non valide":
                    print("L'opération est finie avec succés") 
                    exit()
                  
                break
                
                
        if confirmation_user == "Valide":
            continue
        
        break
    
    
    while True:
        confirmation_user = confirmation(str(input(f"Confirmez-vous avoir sélectioné '{chemin}'? o/n: ")))
        if confirmation_user == "Erreur":
            print("Veillez entrer une des deux valeurs demandés")
            continue
        break
    
    if confirmation_user == "Non valide":
        continue
    
    break
    

print(f"\n--Récuperation des fichiers dans '{chemin}'")
# Création instance de l'objet Filtre avec le dossier de fichiers
objFiltre = Filtre(elementsDossier)

while True:
    
    confirmation_user = None
    nomMod = str(input("Veuillez entrer le mot-clé des fichiers à modifier:"))
    fichierFiltre = objFiltre.filtreNom(nomMod)
    
    if not fichierFiltre:
        print("Le mot clé spécifié n'existe pas dans ce répertoire, veuillez en sélectionner un autre...")
        continue
    
    print("\n--Nom fichier trouvé")
    
    while True:
        confirmation_user = confirmation(str(input(f"Confirmez-vous avoir sélectioné '{nomMod}'? o/n: ")))
        if confirmation_user == "Erreur":
            print("Veillez entrer une des deux valeurs demandés")
            continue
        break
    
    if confirmation_user == "Non valide":
        continue
    
    break

objFiltre.listeFichiers = fichierFiltre






while True:
    
    confirmation_user = None
    extMod = str(input("Veuillez entrer l'extension des fichiers à modifier, ne pas mettre de point (ex:txt):"))
    fichierFiltre = objFiltre.filtreExtension(f".{extMod}")
    
    if not fichierFiltre:
        print(f"Aucun fichier avec le mot-clé '{nomMod}', à l'extension spécifié, veuillez en sélectionner une autre...")
        continue
    
    print("\n-- Extension trouvé")
    
    while True:
        confirmation_user = confirmation(str(input(f"Confirmez-vous avoir sélectioné l'extension '.{extMod}'? o/n: ")))
        if confirmation_user == "Erreur":
            print("Veillez entrer une des deux valeurs demandés")
            continue
        break
    
    if confirmation_user == "Non valide":
        continue
    
    break


print("\n--Début de renommage des fichiers")


objNom = Nom("")
suppresion = 0
modification = 0

for fichier in fichierFiltre:
    
    objNom.fichier = fichier
    
    if "Copie" in fichier:
        nouveau_nom = objNom.nomCopie(nomMod, f".{extMod}")
    else:
        continue
    
    chemin_vieux_nom = join(chemin, fichier)
    chemin_nouveau_nom = join(chemin, nouveau_nom)
    
    if nouveau_nom not in elementsDossier:
        rename(chemin_vieux_nom, chemin_nouveau_nom)
        print("(modification) '%s' à été renommé en '%s'" %(fichier, nouveau_nom))
        modification += 1
    else:
        remove(chemin_vieux_nom)
        print("(suppression) '%s' existe déja, suppression de '%s'" %(nouveau_nom, fichier))
        suppresion += 1
    
    sleep(0.1)


# Retour pour la fin
print("\n--L'opération est finie avec succés")
if modification and suppresion:
    print(f"--{modification} fichiers renommées.\n{suppresion} fichiers supprimés")
elif modification:
    print(f"--{modification} fichiers renommées.")
elif suppresion:
    print(f"--{suppresion} fichiers supprimés")
else:
    print("--Aucun fichier n'a été modifié, assurez-vous qu'il existe des copies dans le repertoire selectioné")
    
exit()