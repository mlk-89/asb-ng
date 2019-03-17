import paramiko
import logging
import tools.password as tp
import tools.asbexception as ta


class RemoteControl:

    def __init__(self):

        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self, address, username, password):
        try:
            self.client.connect(hostname=address,username=username,password=password)
            self.channel = self.client.invoke_shell()
        except(Exception):
            raise ta.RemoteConError("Connexion error")


    def launchCmd(self,mycmd):
        result = {}
        for name, command in mycmd.items():
            stdin, stdout, stderr = self.client.exec_command(command)
            result[name] = stdout.readlines()
            #for line in result[name]:
            #    print(line)
        return result

    def launchCompleteCmd(self, server, myaction):
        myp = tp.Password().getpass(server.name)
        if server.ip:
            myadd = server.ip
        else:
            myadd = server.name

        try:
            self.connect(myadd, server.admin, myp)
            res = self.launchCmd(myaction)
            self.disconnect()
            response = ""
            for i in res:
                response+= "".join(res[i]).replace('"','')
            return response
        except(ta.RemoteConError):
            print('Cant connect to remote ' + myadd)


    def disconnect(self):
        self.client.close()
