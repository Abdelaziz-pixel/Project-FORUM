from connection import *

class NewAccount():

    def __init__(self):
        self.choice = connection()
        self.name = None
        self.firstname = None
        self.pseudo = None
        self.email = None
        self.age = None
        self.password = None

    def create_user(self):
        print("-----------------------------------------------------------------")
        print("Bienvenu sur le forum, nous allons procéder à votre inscription !")
        print("-----------------------------------------------------------------")
        self.name = input("Quel est votre nom ? ")
        self.firstname = input("Quel est ton prénom ? ")
        self.pseudo = input("Sous quel pseudo souhaitez-vous apparaitre ? ")
        self.email = input("Quel est votre E-mail ? ")
        self.age = int(input("Quel est votre age ? "))
        self.password = input("Entrez votre Mot de passe : ")
        self.choice.initialize_connection()
        self.choice.cursor.execute("INSERT INTO Users(name,firstname,pseudo,email,age,password) VALUES (%s,%s,%s,%s,%s,%s);",(self.name,self.firstname,self.pseudo,self.email,self.age,self.password))
        self.choice.connection.commit()
        self.choice.close_connection()
