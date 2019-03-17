class RemoteConError (Exception):

    def __init__(self, message):
        self.message = message


class DNSresolveERROR (Exception):

    def __init__(self, message):
        self.message = message


class ServerMissingInfo(Exception):
    def __init__(self, message):
        self.message = message
