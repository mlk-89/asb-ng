import cmd
import os
import glob
import yaml
import scenario.system_info as systemInfoScenario
import tools.remote_control as remoteControl
import servercli

class Cli(cmd.Cmd):

    prompt = '> '
    intro = "Welcome to interactive Building console"
    serverlist = ""


    def do_load(self, line):
        try:
            with open(line) as json_file:
                self.serverlist = yaml.load(json_file, Loader=yaml.FullLoader)

            print(self.serverlist)
        except (FileNotFoundError, IOError):
            print('Error on opening file')


    def complete_load(self, text, line, begidx, endidx):
        before_arg = line.rfind(" ", 0, begidx)
        if before_arg == -1:
            return  # arg not found

        fixed = line[before_arg + 1:begidx]  # fixed portion of the arg
        arg = line[before_arg + 1:endidx]
        pattern = arg + '*'

        completions = []
        for path in glob.glob(pattern):
            if path and os.path.isdir(path) and path[-1] != os.sep:
                pathshow = path + os.sep
                completions.append(pathshow.replace(fixed, "", 1))
            elif path.endswith('.json'):
                completions.append(path.replace(fixed, "", 1))

        return completions

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
        res = rem.launchCmd(myaction)

        print(''.join(res['os']))
        rem.disconnect()

    def do_select(self,servername):
        scli = servercli.ServerCli()
        scli.prompt = servername + '> '
        scli.cmdloop()

    def do_EOF(self, line):
        return True

    def do_quit(self, args):
        """Quits the program."""
        print ("Quitting.")
        raise SystemExit
