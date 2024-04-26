def confirmation (lettre):
    
    valide = ("o", "O")
    non_valide = ("n", "N")
    
   
    if lettre in valide:
        return ("Valide")
    
    elif lettre in non_valide:
        return ("Non valide")
    
    else:
        return ("Erreur")