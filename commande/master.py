import logging


class Commande:

    def __init__(self,mycmd=None):
        self.logger = logging.getLogger('Command')

        if mycmd:
            self.mycmd = mycmd

    def getCmd(self):
        return self.mycmd
