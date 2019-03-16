import paramiko

class RemoteControl:
    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self, address, username, password):
        self.client.connect(hostname=address,username=username,password=password)
        self.channel = self.client.invoke_shell()

    def launchCmd(self,mycmd):
        for command in mycmd:
            stdin, stdout, stderr = self.client.exec_command(command)
            for line in stdout.readlines():
                print(line)

    def disconnect(self):
        self.client.close()
