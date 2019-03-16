class Server:

    def __init__(self, name='',ip='',os='', admin='root', dict={}):

        self._name = name
        self._ip = ip
        self._os = os
        self._admin = admin

        if dict:
            for k,v in dict.items():
                self._name = k
                if v is not None:
                    if 'ip' in v:
                        self._ip = v['ip']
                    if 'os' in v:
                        self._os = v['os']

    def extract_from_yaml(self, name, yamlliste):
        if yamlliste:
            for server in yamlliste:
                for k,v in server:
                    if k == name:
                        self._name = k
                        self._ip = v['ip']
                        self._os = v['os']

    @property
    def name(self):
        return self._name

    @property
    def ip(self):
        return self._ip

    @property
    def os(self):
        return self._os

    @property
    def admin(self):
        return self._admin

    def description(self):
        mystr = "\n" + self._name

        if self._ip:
            mystr += "\n\tip: {}".format(self._ip)

        if self._os:
            mystr += "\n\tos: {}".format(self._os)

        return mystr

    def __str__(self):
        return self._name
