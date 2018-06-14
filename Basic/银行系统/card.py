

class Card(object):

    def __init__(self, id, passwd, money):
        self.id = id
        self.passwd = passwd
        self.money = int(money)
        self.lock = False
