import cmd
import scenario.system_info as systemInfoScenario
import tools.remote_control as remoteControl

class Cli(cmd.Cmd):

    prompt = '> '
    intro = "Welcome to interactive Building console"

    def do_debug(self,args1):
        print("ok")

    def complete_debug(self, text, line, begidx, endidx):
        liste = ["cs1","cs2","cs3"]
        if text:
            completion = [f
                            for f in liste
                            if f.startswith(text)
                            ]
        return completion

    def do_getSystem(self,args):
        myaction = systemInfoScenario.SystemInfo().getScenario()
        rem = remoteControl.RemoteControl()
        rem.connect('192.168.122.89','root','totolitoto')
        rem.launchCmd(myaction)
        rem.disconnect()

    def do_quit(self, args):
        """Quits the program."""
        print ("Quitting.")
        raise SystemExit
