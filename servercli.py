import cmd
import scenario.system_info as systemInfoScenario
import tools.remote_control as remoteControl
import tools.password as tp
import tools.asbexception as ta

class ServerCli(cmd.Cmd):

    intro = ""

    def __init__(self, serverlist):
        cmd.Cmd.__init__(self)
        self.prompt = ""
        self.serverlist = serverlist

    def do_getSystem(self,args):
        myaction = systemInfoScenario.SystemInfo().getScenario()

        for server in self.serverlist:
            myp = tp.Password().getpass(server.name)

            if server.ip:
                myadd = server.ip
            else:
                myadd = server.name

            rem = remoteControl.RemoteControl()
            try:
                rem.connect(myadd,server.admin,myp)
                res = rem.launchCmd(myaction)
                print(''.join(res['os']))
                rem.disconnect()
            except(ta.RemoteConError):
                print('Cant connect to remote ' + myadd)

    def do_list(self,args):
        for i in self.serverlist:
            print(i.description())

    def do_EOF(self, line):
        return True

    def do_quit(self, args):
        return True
