import commande.system_type as systemTypeCmd

class SystemInfo:
    def __init__(self):
        print("Retrieving system information")

    def getScenario(self):
        action = []
        action.append(systemTypeCmd.SystemType().getCmd())

        return action
