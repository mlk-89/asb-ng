import commande as cm


class SystemType(cm.Commande):
    def __init__(self,mycmd=None):
        super().__init__(self)
        self.mycmd = "uname -o"
        self.logger.info('Starting main process')

    def getCmd(self):
        return self.mycmd
