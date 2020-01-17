from connection import *

class Account():

    def __init__(self):
        self.choice = connection()
        self.peusdo = None
        self.password = None

    def connect_user(self):
        self.pseudo = input("Quel es votre pseudo ? ")
        self.password = (input("Votre mot de passe : "))
        self.choice.initialize_connection()
        self.choice.cursor.execute("SELECT pseudo, password FROM Users WHERE pseudo = %s AND password = %s;",(self.pseudo,self.password))
        raws = self.choice.cursor.fetchall()

        for raw in raws:
            if raw[0] == self.pseudo and raw[1] == self.password:
                login = True
                print(login)

        self.choice.close_connection()
