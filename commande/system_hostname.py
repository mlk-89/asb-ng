import commande as cm


class SystemHostname(cm.Commande):

    def __init__(self, os, hostname, domain):
        super().__init__()
        self.logger.info('Setting Remote hostname')
        self.hostname = hostname
        self.domain = domain

        if os in 'centos':
            self.setcentos()


    def setcentos(self):
        self.mycmd['hostname'] = "hostnamectl set-hostname " + '.'.join(self.hostname,self.domain)
