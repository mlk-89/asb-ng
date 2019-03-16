import commande as cm


class SystemType(cm.Commande):
    def __init__(self,mycmd=None):
        super().__init__()
        self.mycmd = "uname -o"
        self.logger.info('Retrieving remote OS')

    def getCmd(self):
        return self.mycmd
