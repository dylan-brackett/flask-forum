class Post:

    def __init__(self, message, id_num):
        self.message = message
        self.id_num = id_num
    
    def get_message(self):
        return self.message
    
    def set_message(self, message):
        self.message = message

    def get_id_num(self):
        return self.id_num
    
    def set_id_num(self, id_num):
        self.id_num = id_num
        