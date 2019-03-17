class RemoteConError (Exception):

    def __init__(self, message):
        self.message = message

class DNSresoleERROR (Exception):

    def __init__(self, message):
        self.message = message
