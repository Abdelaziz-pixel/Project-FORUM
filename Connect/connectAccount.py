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
        raws = self.choice.cursor.fectall()

        
