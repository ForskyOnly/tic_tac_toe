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

board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    print_board(board)
    print(f"Turn for {turn}. Move on which space?")
    move = input()
    board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print_board(board)


   
