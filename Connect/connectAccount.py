from connection import *

class Account():

    def __init__(self):
        self.choice = connection()
        self.peusdo = None
        self.password = None

    def connect_user(self):
        self.peusdo = input("Quel es votre pseudo ? ")
        self.password = (input("Votre mot de passe : "))