import paramiko
import logging

class RemoteControl:
    def __init__(self):

        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self, address, username, password):
        self.client.connect(hostname=address,username=username,password=password)
        self.channel = self.client.invoke_shell()

    def launchCmd(self,mycmd):
        result = {}
        for name, command in mycmd.items():
            stdin, stdout, stderr = self.client.exec_command(command)
            result[name] = stdout.readlines()
            #for line in result[name]:
            #    print(line)
        return result


    def disconnect(self):
        self.client.close()
