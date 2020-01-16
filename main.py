from Modele.messageModel import *



if __name__ == "__main__":
    show = View() 
    show.show_message()
    User_choice = ""


    while User_choice not in ["v", "r", "w"]:
        User_choice = input("Choisissez entre Voir(v), Lire(r) et Écrire(w) :")
        Choice = Model()
        if User_choice == "v":
            show.show_message()
            User_choice = input("Choisissez entre Voir(v), Lire(r) et Écrire(w) :")
        if User_choice == "r":

        if User_choice == "w":