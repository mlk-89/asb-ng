import logging

class asblog:

    loglevel = {
        'CRITICAL': logging.CRITICAL,
        'WARNING': logging.WARNING,
        'INFO' : logging.INFO,
        'DEBUG': logging.DEBUG,
    }

    def config(self, filename, loglevel='INFO'):
        logging.basicConfig(filename=filename, level=self.loglevel[loglevel],
                            format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')

    def setlog(self,channel,message):
        logging.getLogger(channel)
        logging.info(message)

