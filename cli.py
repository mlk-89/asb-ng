import cmd
import os
import glob
import yaml
import servercli
import model.server as ms

class Cli(cmd.Cmd):

    prompt = '> '
    intro = "Welcome to interactive Building console"
    serverlist = []

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

    def do_save(self, filename):
        if not filename:
            filename = 'asb_serverfile.yaml'
        if self.serverlist:
            yserver = {'server': []}
            for server in self.serverlist:
                yserver['server'].append(server.getdict())

            try:
                with open(filename, 'w') as outfile:
                    yaml.dump(yserver, outfile, default_flow_style=False)
            except (FileNotFoundError, IOError):
                print('Error on saving file')

    def do_list(self,args):
        for i in self.serverlist:
            print(i.description())

    def do_clearlist(self,args):
        self.serverlist = []

    def do_addlist(self, servername):
        self.serverlist.append(ms.Server(name=servername))

    def do_removelist(self,servername):
        for server in self.serverlist:
            if servername == server.name:
                self.serverlist.remove(server)

    def complete_removelist(self, text, line, begidx, endidx):
        completion = []
        if text:
            if self.serverlist:
                for server in self.serverlist:
                    if text in server.name:
                        completion.append(server.name)
        else:
            if len(self.serverlist) < 20:
                for server in self.serverlist:
                    completion.append(server.name)
        return completion

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

    def do_select(self,servername):
        selected = []

        if not self.serverlist:
            self.serverlist.append(ms.Server(name=servername))

        for server in self.serverlist:
            if server.name.startswith(servername):
                selected.append(server)

        if not selected:
            selected.append(ms.Server(name=servername))

        scli = servercli.ServerCli(selected)
        scli.prompt = servername + '> '
        scli.cmdloop()

    def complete_select(self, text, line, begidx, endidx):
        completion = []
        if text:
            if self.serverlist:
                for server in self.serverlist:
                    if text in server.name:
                        completion.append(server.name)
        else:
            if len(self.serverlist) < 20:
                for server in self.serverlist:
                    completion.append(server.name)

        return completion

    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass

    def do_quit(self, args):
        """Quits the program."""
        print ("Quitting.")
        raise SystemExit
