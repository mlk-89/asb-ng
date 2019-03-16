import logging


class Commande:

    def __init__(self):
        self.logger = logging.getLogger('Command')
        self.mycmd = {}

    def getCmd(self):
        return self.mycmd
