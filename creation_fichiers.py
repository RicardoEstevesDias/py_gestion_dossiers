"""
Script qui crée des fichiers énumerés de 1 a x, x étant un chiffre entier supérieur à 0 que l'utilisateur doit spécifier
Le script prend en entrée le chemin ou il veut créer le/les fichiers, le nombre de fichiers à créer, le nom des fichier et leur extension.
"""

from Modules.confirmation import confirmation
from Modules.Nom import Nom
from os import listdir #create
from os.path import join, split
# from time import sleep



while True:
    
    while True:
        
        confirmation_user = None
        
        try:
            chemin = input(r"Donnez le chemin vers le dossier souhaité: ")
            elementsDossier = listdir(chemin)
                
        except:
            print("Le chemin spécifié n'existe pas...")
            continue
        
        print("--Répertoire trouvé\n")
        
        
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

print("--Répertoire confirmé\n")

while True:
    
    confirmation_user = None
    
    try:
        nbFichiers = int(input("Veuillez écrire le nombre (entier plus grand que zéro) de fichiers à créer: "))
             
    except:
        print("Veuilez donner un nombre entier...")
        continue
    
    if nbFichiers < 1:
        print("Veuillez écrire un nombre plus grand que zéro...")
        continue

    print(f"--Nombre de fichiers à créer: {nbFichiers}\n")
    
    while True:
        confirmation_user = confirmation(str(input(f"Confirmez-vous vouloir créer {nbFichiers} nouveaux fichiers? o/n: ")))
        if confirmation_user == "Erreur":
            print("Veillez entrer une des deux valeurs demandés")
            continue
        break
    
    if confirmation_user == "Non valide":
        continue
    
    break


print("--Nombre de fichiers confirmé\n")


while True:
    
    confirmation_user = None
    
    while True:
        nom = str(input("Veuillez entrer le nom des fichiers:"))
        if not nom:
            print("Il faut un nom pour les fichiers!")
            continue
        break
    
    print(f"--Nom selectionné: {nom}\n")
    
    while True:
        confirmation_user = confirmation(str(input(f"Confirmez-vous avoir sélectioné '{nom}'? o/n: ")))
        if confirmation_user == "Erreur":
            print("Veillez entrer une des deux valeurs demandés")
            continue
        break
    
    if confirmation_user == "Non valide":
        continue
    
    break


print("--Nom des fichiers confirmé\n")


while True:
    
    confirmation_user = None
    extension = str(input("Veuillez entrer l'extension des fichiers, ne pas mettre de point (ex:txt):"))
    
    print(f"-- Extension selectionné: .{extension}\n")
    
    while True:
        confirmation_user = confirmation(str(input(f"Confirmez-vous avoir sélectioné l'extension '.{extension}'? o/n: ")))
        if confirmation_user == "Erreur":
            print("Veillez entrer une des deux valeurs demandés")
            continue
        break
    
    if confirmation_user == "Non valide":
        continue
    
    break


print("--Extension des fichiers confirmé\n")


print("--Début de création des fichiers\n")


ignore = 0
creation = 0


for nombre in range(1,nbFichiers+1):
    
    # Format à changer ici si nécessaire
    if extension:
        nomFichier = f"{nom}{nombre}.{extension}"
    else:
        nomFichier = f"{nom}{nombre}"
        
    chemin_nom = join(chemin, nomFichier)
    
    if nomFichier in elementsDossier:
        print("(ignorée) '%s' existe déjà dans '%s'" %(nomFichier, chemin))
        ignore += 1
    else:
        f = open(chemin_nom, "w")
        f.close()
        print("(création) '%s' creé dans '%s'" %(nomFichier, chemin))
        creation += 1


# Retour pour la fin
print("\nL'opération est finie avec succés!")

if creation and ignore:
    print(f"{creation} fichiers créés.\n{ignore} fichiers ignorés")
elif creation:
    print(f"--{creation} fichiers créés.")
elif ignore:
    print(f"--{ignore} fichiers ignorés")
else:
    print("--Aucun fichier n'a été créé, assurez-vous d'avoir rempli les paramétres correctement")

str(input("Appuyer sur entrée pour fermer le programme"))
exit()
