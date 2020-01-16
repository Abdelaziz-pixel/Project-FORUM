from connection import *

class NewAccount():

    def __init__(self):
        self.Choice = connection()
        self.name = None
        self.pseudo = None
        self.email = None
        self.age = None
        self.password = None

    def create_user(self):
        print("-------------------------------")
        print("Bienvenu sur le forum, nous allons procéder à votre inscription !")
        print("-------------------------------")
        self.name = input("Quel est votre nom ? ")
        self.pseudo = input("Sous quel pseudo souhaitez-vous apparaitre ? ")
        self.email = input("Quel est votre E-mail ? ")
        self.age = int(input("Quel est votre age ? "))
        self.password = input("Entrez votre Mot de passe : ")

    def verify_age(self):
        if age >= 18:
            return self.create_user()
        if age < 18:
            print("Le forum est réservé au majeur, désoler !")

    def verify_email(self,admail,email):
        import smtplib
        smtp = smtplib.SMTP(self.email)
        res = smtp.verify(admail)
        smtp.quit()
        return res
    