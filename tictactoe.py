# dico = {
#     "A" : ["_","_","_"],
#     "B" : ["_","_","_"],
#     "C" : ["_","_","_"]
# }


# def afficher_la_grille():
#     """
#     fonction qui affiche une grille crée avec un dictionnaire auparavant
#     et qui fais la mise en forme des elements, séparés d'un "|", avec un retour
#     à la ligne, aprés chaque element de la clé du dictionnaire.    
#     """
#     for cle in dico:
#         for elt in dico [cle]:
#             print(" ", elt, " |", end = "")
#         print("\n")
    
# afficher_la_grille()

# def jouer_un_coup():
#     val_user = (input("choisissez votre position : "))
#     if val_user[0] in ["A","B","C"] and (val_user[1]) in [1,2,3] :
#         if dico[val_user[0]][(val_user[1])] == "_" :
#             return(dico[val_user[0]][(val_user[1])] == "x")
        
            
         

            
            
#         #     for key, value in dico(afficher_la_grille) :
#         #       key == val_user[0]
#         #       value == val_user[1]
#         #       print("X" in dico(afficher_la_grille))
#         # else : print("mauvaise valeur" + val_user)
    
       
# jouer_un_coup()


   
plateau = {
    "A" :[None for _ in range(3)],
    "B" :[None for _ in range(3)],
    "C" :[None for _ in range(3)]
}

def afficher_la_grille(plateau:dict) -> None:
    """fonction qui affiche la grille"""
   
    for cle in plateau:
        for elt in plateau [cle]:
            print(" ", elt, " |", end = "")
        print("\n")
    
afficher_la_grille(plateau)
        
            
            