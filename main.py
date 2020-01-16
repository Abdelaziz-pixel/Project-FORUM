from Modele.messageModel import *
from View.messageView import *
import os 


if __name__ == "__main__":
    show = View() 
    show.show_message()
    User_choice = ""


    while User_choice not in ["v", "r", "w"]:
        User_choice = input("Choisissez entre Voir(v), Écrire(w) et Quitter(q) :")
        Choice = Model()
        if User_choice == "v":
            show.show_message()
            User_choice = input("Choisissez entre Voir(v), Écrire(w) et Quitter(q) :")
        if User_choice == "w":
            author = input("Entrez votre nom :")
            content = input ("Quel est votre message :")
            Choice.write_message(author, content)
            User_choice = input("Choisissez entre Voir(v), Écrire(w) et Quitter(q) :")
        if User_choice == "q":
            print("Bonne journée !")
            exit()