import tools.remote_control as tr
import commande.system_type as cs
import commande.system_etc_release as cse

class Os:

    base = {
        'Linux/GNU': 'linux',
        'FreeBSD': 'FreeBSD',
    }

    def __init__(self, servername):
        self._servername = servername

    def getbase(self):
        return tr.RemoteControl().launchCompleteCmd(self._servername,cs.SystemType().getCmd())

    def getos(self):
        baseos = self.getbase()
        if 'Linux' in baseos:
            os_full = tr.RemoteControl().launchCompleteCmd(self._servername,cse.SystemEtcRelease().getCmd())
        else:
            os_full = baseos

        return os_full.replace('\n','')
