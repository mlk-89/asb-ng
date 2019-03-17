import cmd
import scenario.system_info as systemInfoScenario
import tools.asbexception as ta
import tools.remote_control as remoteControl
import tools.dns as td
import tools.os as to
import scenario

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
        for i in self.serverlist:
            print(i.description())

    def do_init(self,servername):
        if servername:
            for server in self.serverlist:
                if server.name == servername:
                    if not server.ip:
                        try:
                            server.ip = td.DNSmanage().getip(server.name)
                        except(ta.DNSresolveERROR):
                            print("Cant resolve " + server.name)
                    if not server.os:
                        server.os = to.Os(server).getos()
        else:
            for server in self.serverlist:
                if not server.ip:
                    try:
                        server.ip = td.DNSmanage().getip(server.name)
                    except(ta.DNSresolveERROR):
                        print("Cant resolve " + server.name)
                if not server.os:
                    server.os = to.Os(server).getos()

    def do_sethostname(self, servername):
        myaction = scenario.scdebug.ScenarioDebug().getScenario()


    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass

    def do_quit(self, args):
        return True
