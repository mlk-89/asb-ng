import cmd
import os
import glob
import servercli
import model.server as ms
import model.allserver as mall
import tools.yamlmanage as ty

class Cli(cmd.Cmd):

    prompt = '> '
    intro = "Welcome to interactive Building console"
    serverlist = []

    def __init__(self):
        super().__init__()
        self.servers = mall.AllServer()
        self.aliases = {'ls': self.do_list
                         }

    def do_load(self, line):

        self.servers.clearList()

        yserverlist = ty.YamlManage.getyaml(filepath=line)
        for yserver in yserverlist['server']:
            self.servers.addServer(mydict=yserver)


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

        if not self.servers.isServerlistEmpty():
            yserver = {'server': self.servers.getAllServerDict()}
            ty.YamlManage.saveyaml(filepath=filename, objecttosave=yserver)

    def do_list(self,args):
        print(self.servers)

    def do_clearlist(self,args):
        self.servers.clearList()

    def do_addlist(self, servername):
        self.servers.addServer(servername=servername)

    def do_removelist(self,servername):
        self.servers.removeServer(servername)

    def complete_removelist(self, text, line, begidx, endidx):
        completion = []
        if text:
            if not self.servers.isServerlistEmpty():
                completion = self.servers.getServerStartWithName(text)
        else:
            if len(self.servers) < 20:
                completion = self.servers.getAllServerName(text)
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
        if self.servers.isServerlistEmpty() or not self.servers.isServerExist(servername):
            self.servers.addServer(servername)

        self.servers.setServerSelectedStartWith(servername)

        self.servers.sublist = mall.AllServer(self.servers.getServerStartWith(servername))
        scli = servercli.ServerCli(self.servers.sublist)
        scli.prompt = '(' + servername + ')> '
        scli.cmdloop()

    def complete_select(self, text, line, begidx, endidx):
        completion = []
        if text:
            completion = self.servers.getServerContainsName(text)
        else:
            if len(self.serverlist) < 20:
                completion = self.servers.getAllServerName()

        return completion

    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass

    def do_quit(self, args):
        """Quits the program."""
        print ("Quitting.")
        raise SystemExit

    def default(self, line):
        cmd, arg, line = self.parseline(line)
        if cmd in self.aliases:
            self.aliases[cmd](arg)
        else:
            print("*** Unknown syntax: %s" % line)
