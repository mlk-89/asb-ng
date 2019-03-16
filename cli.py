import cmd
import os
import glob
import yaml
import scenario.system_info as systemInfoScenario
import tools.remote_control as remoteControl
import servercli
import model.server as ms

class Cli(cmd.Cmd):

    prompt = '> '
    intro = "Welcome to interactive Building console"

    def do_load(self, line):
        self.serverlist = []
        try:
            with open(line) as json_file:
                yserverlist = yaml.load(json_file, Loader=yaml.FullLoader)

                for yserver in yserverlist['server']:
                    self.serverlist.append(ms.Server(dict=yserver))

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
            elif path.endswith('.yaml'):
                completions.append(path.replace(fixed, "", 1))

        return completions

    def do_list(self,args):
        for i in self.serverlist:
            print(i)

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

    def complete_select(self, text, line, begidx, endidx):
        completion = []
        if text:
            if self.serverlist:
                for server in self.serverlist:
                    for key,value in server:
                        if key.startswith(text):
                            completion.append(key)
        return completion

    def do_EOF(self, line):
        return True

    def do_quit(self, args):
        """Quits the program."""
        print ("Quitting.")
        raise SystemExit
