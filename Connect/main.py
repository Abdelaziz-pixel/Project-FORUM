from createAccount import *
from connectAccount import *
import os


if __name__ == "__main__":

    newlog = NewAccount()
    log = Account()
    User_choice = ""

    while User_choice != "q":
        User_choice = input("Choisissez entre vous connecter(l), créer un compte(c) ou quitter(q) :")
        if User_choice == "l":
            log.connect_user()
        if User_choice == "c":
            newlog.create_user()
        if User_choice == "q":
            print("Bonne journée à bientot !")
            exit()