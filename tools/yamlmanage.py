import yaml

class YamlManage:

    @staticmethod
    def getyaml(filepath):

        try:
            with open(filepath) as json_file:
                yamliste = yaml.load(json_file, Loader=yaml.FullLoader)

            json_file.close()

        except (FileNotFoundError, IOError):
            print('Error on opening file')

        return yamliste

    @staticmethod
    def saveyaml(filepath,objecttosave):

        try:
            with open(filepath, 'w') as outfile:
                yaml.dump(objecttosave, outfile, default_flow_style=False)
        except (FileNotFoundError, IOError):
            print('Error on saving file')
