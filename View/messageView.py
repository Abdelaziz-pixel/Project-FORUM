from Modele.Model import *

class View():
    """class for display all message """
    
    def __init__(self):
        self.model = messageModel()

    def show_message(self):
        """display all messages """
        # get the messages from the model
        messages = self.model.display_message()
        print('hello this is all message : ')
        if messages:
            for row in messages:
                print("\nmessage {} : {}".format(row['id'], row['content']))
                print("Posté par {} le {} à {}".format(
                    row['author'],
                    row['publishing_date'].strftime("%d/%m/%Y"),
                    row['publishing_date'].strftime("%H:%M")
                ))
                print("\n------------------------------")

        else:
            print("no message actually")