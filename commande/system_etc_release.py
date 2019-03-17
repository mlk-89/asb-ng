import commande as cm


class SystemEtcRelease(cm.Commande):
    def __init__(self,mycmd=None):
        super().__init__()
        self.logger.info('Retrieving remote OS')
        self.mycmd['osname'] = "grep -iE '^id=' /etc/os-release|cut -d'=' -f2"
        self.mycmd['osversion'] = "grep -i '^version=' /etc/os-release|cut -d'=' -f2"

