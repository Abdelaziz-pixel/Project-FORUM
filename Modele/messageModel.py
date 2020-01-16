class Model():

    def __init__(self):
        self.Choice = None 
        self.Choice = connection 

    def model_message(self):
        self.Choice.initialize_connection()
        self.Choice.cursor.execute("SELECT * FROM Messages;")
        view = self.Choice.cursor.fetchall()
        self.Choice.close_connection()
        return view

    def write_message():
        self.Choice.initialize_connection()
        self.Choice.cursor.execute("INSERT INTO Messages(content, publishing_date, author) VALUES (%s, NOW(), %s);",(content, author))
        self.Choice.connection.commit()
        self.Choice.close_connection()