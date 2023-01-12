dico = {
    "A" : ["_","_","_"],
    "B" : ["_","_","_"],
    "C" : ["_","_","_"]
}


def afficher_la_grille():
    """
    fonction qui affiche une grille crée avec un dictionnaire auparavant
    et qui fais la mise en forme des elements, séparés d'un "|", avec un retour
    à la ligne, aprés chaque element de la clé du dictionnaire.    
    """
    for cle in dico:
        for elt in dico [cle]:
            print(" ", elt, " |", end = "")
        print("\n")
    
afficher_la_grille()

def jouer_un_coup():
    val_user = (input("choisissez votre position : "))
    if val_user[0] in ["A","B","C"] and (val_user[1]) in [1,2,3] :
        if dico[val_user[0]][(val_user[1])] == "_" :
   
   
