from Modele.messageModel import *

class View():
    """class for display all message """

    def __init__(self):
        self.model = Model()

    def show_message(self):
        """display all messages """
        # get the messages from the model
        messages = self.model.model_message()
        print('hello this is all message : ')
        if messages:
            for row in messages:
                print("Posté par {} le {} à {}".format(
                row['author'],
                row['publishing_date'].strftime("%d/%m/%Y"),
                row['publishing_date'].strftime("%H:%M")
                ))
                print("\nmessage {} : {}".format(row['id'], row['content']))
                print("\n------------------------------")

        else:
            print("no message actually")