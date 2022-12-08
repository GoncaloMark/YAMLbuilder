from urllib.parse import urlparse


try:
    import yaml
    from os import path
except ImportError as e:
    print("Some modules could not be imported from stdlib('yaml')")

class GetInput:
    def __init__(self):
        self._url = None
        self.__hops = None
        self.__tags= None
        self.__attrs = None
        self.__selecs = None
        self.__ID = None
        self._yaml_dict = None
        self.__attrsv = None

        self.__getInputCLI()

    def __getInputCLI(self):
        print("Config File Setup! What's the URL?")
        self._url = input()
        if self._url == '':
            raise ValueError
        print("Maximum number of hops?")
        self.__hops = int(input())
        print("Tags to scrape?")
        self.__tags = list(input().strip().split())
        print("Any attributes?")
        self.__attrs = list(input().strip().split())
        print("Attribute(s) value(s)?")
        self.__attrsv = list(input().strip().split())
        print("Selectors?")
        self.__selecs = list(input().strip().split())
        if "id" in self.__selecs or "id" in self.__attrs:
            print("ID value(s)?")
            self.__ID = list(input().strip().split())
        print("Classes?")
        self.__classes = list(input().strip().split())
        self._yaml_dict = self.__buildDict(self._url, self.__hops, self.__tags, self.__attrs, self.__attrsv, self.__selecs,self.__ID, self.__classes)

    def __buildDict(self, *args):
        dict = {
                'url': args[0],
                'hops': args[1],
                'tags': args[2], 
                'attrs': args[3],
                'attrV':args[4],
                'selectors': args[5],
                'IDv': args[6],
                'classes': args[7]
            }
        
        return dict

    def show_dict(self):
        return self._yaml_dict


class BuildFile(GetInput):
    def __init__(self):
        super().__init__()
        self.__createFile()

    def __createFile(self):
        identifier = urlparse(self._url).netloc[4:]
        if path.exists(rf'yamlfiles/cobweb_{identifier}_config.yaml') == False:
            with open(rf'yamlfiles/cobweb_{identifier}_config.yaml', 'w') as file:
                yaml.dump(self._yaml_dict, file)

if __name__ == "__main__":
    x = BuildFile() #this is a test!
    pass
