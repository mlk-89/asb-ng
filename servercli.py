import cmd
import scenario.system_info as systemInfoScenario
import tools.asbexception as ta
import tools.remote_control as remoteControl
import tools.dns as td
import tools.os as to
import model.allserver as mall

class ServerCli(cmd.Cmd):

    intro = ""

    def __init__(self, serverlist):
        cmd.Cmd.__init__(self)
        self.serverlist = serverlist

    def do_getSystem(self,args):
        myaction = systemInfoScenario.SystemInfo().getScenario()

        for server in self.serverlist:
            print(remoteControl.RemoteControl().launchCompleteCmd(server,myaction))

    def do_list(self,args):
        print(self.serverlist)

    def do_init(self,servername):
        if servername:

            try:
                ip = td.DNSmanage().getip(servername)
            except(ta.DNSresolveERROR):
                print("Cant resolve " + servername)

            print()
            os = to.Os(self.serverlist.getServer(servername)).getos()
            print(os)
            self.serverlist.modifyServer(servername=servername, ip=ip, os=os)

        else:
            for server in self.serverlist:
                if not server.ip:
                    try:
                        server.ip = td.DNSmanage().getip(server.name)
                    except(ta.DNSresolveERROR):
                        print("Cant resolve " + server.name)
                if not server.os:
                    server.os = to.Os(server).getos()



    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass

    def do_quit(self, args):
        return True
