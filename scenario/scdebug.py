import scenario as sc
from commande import system_hostname as csh


class ScenarioDebug(sc.Scenario):
    def __init__(self, server):
        super().__init__()
        self.logger.info('Debug')
        self.server = server

    def getScenario(self):
        action = {}

        action.update(csh.SystemHostname(self.server.os,self.server.name,self.server.domain).getCmd())

        return action
