import commande.system_type as systemTypeCmd
import scenario as sc


class SystemInfo(sc.Scenario):

    def __init__(self):
        super().__init__()
        self.logger.info('Gathering OS info')

    def getScenario(self):
        action = {}
        action.update(systemTypeCmd.SystemType().getCmd())

        return action
