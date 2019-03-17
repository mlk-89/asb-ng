import socket
import tools.asbexception as ta

class DNSmanage:

    def getip(self, hostname):
        try:
            return socket.gethostbyname(hostname)
        except:
            raise ta.DNSresoleERROR("Cant resolve to IP")
