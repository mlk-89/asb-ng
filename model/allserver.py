import model.server as ms


class AllServer:

    def __init__(self, serverlist=[]):
        self.serverlist = serverlist
        self.sublist = None

    def setServerList(self,serverlist):
        self.serverlist = serverlist

    def getServerlist(self):
        return self.serverlist

    def getServersublist(self):
        return self.sublist

    def isServerlistEmpty(self):
        if self.serverlist:
            return False
        else:
            return True

    def getAllServer(self):
        return list(server for server in self.serverlist)

    def getAllServerName(self):
        return list(server.name for server in self.serverlist)

    def getServer(self, servername):
        for server in self.serverlist:
            if servername == server.name:
                return server

    def getServerStartWith(self,servername):
        return list(server for server in self.serverlist if server.name.startswith(servername))

    def getServerStartWithName(self,servername):
        return list(server.name for server in self.serverlist if server.name.startswith(servername))

    def getServerContains(self, servername):
        return list(server for server in self.serverlist if servername in server.name)

    def getServerContainsName(self, servername):
        return list(server.name for server in self.serverlist if servername in server.name)

    def getServerSelected(self):
        return list(server for server in self.serverlist if server.selected)

    def setServerSelectedStartWith(self, servername):
        for server in self.getServerStartWith(servername):
            server.selected = True

    def isServerExist(self,servername):
        res = False
        if self.serverlist:
            for server in self.serverlist:
                if servername == server.name:
                    res = True

        return res

    def addServer(self,servername=None,ip=None,os=None,mydict=None):
        self.serverlist.append(ms.Server(name=servername,ip=ip,os=os,mydict=mydict))

    def modifyServer(self,servername,ip=None,os=None):
        server = self.getServer(servername)

        if ip:
            if not server.ip or ip != server.ip:
                server.ip = ip
        if os:
            if not server.os or os != server.os:
                server.os = os

    def removeServer(self, servername):
        for server in self.serverlist:
            if servername == server.name:
                self.serverlist.remove(server)

    def getAllServerDict(self):
        res = []
        for server in self.serverlist:
            res.append(server.getdict())

        return res

    def clearList(self):
        self.serverlist.clear()

    def __str__(self):
        return "".join(list(x.description() for x in self.serverlist))

    def __len__(self):
        return len(self.serverlist)
