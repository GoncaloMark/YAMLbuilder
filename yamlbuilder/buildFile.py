try:
    import yaml
    from os import path
except ImportError as e:
    print("Some modules could not be imported from stdlib('yaml')")

class GetInput:
    def __init__(self, type):
        self.__type = type
        self._url = None
        self.__hops = None
        self.__tags= None
        self.__attrs = None
        self.__selecs = None
        self.__ID = None
        self._yaml_dict = None

        if self.__type == "cli":
            self._input = self.__getInputCLI()

        elif self.__type == "web":
            self._input = self.__getInputWeb()

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
        print("Selectors?")
        self.__selecs = list(input().strip().split())
        if "id" in self.__selecs:
            print("ID value(s)?")
            self.__ID = list(input().strip().split())
        print("Classes?")
        self.__classes = list(input().strip().split())

        if self.__ID == None:
            self._yaml_dict = self.__buildDict(self._url, self.__hops, self.__tags, self.__attrs, self.__selecs, self.__classes)
        else:
            self._yaml_dict = self.__buildDict(self._url, self.__hops, self.__tags, self.__attrs, self.__selecs, self.__ID, self.__classes)

    def __buildDict(self, *args):
        if self.__ID == None:
            dict = {
                'url': args[0],
                'hops': args[1],
                'tags': args[2], 
                'attrs': args[3],
                'selectors': args[4],
                'classes': args[5]
            }
        else:
            dict = {
                'url': args[0],
                'hops': args[1],
                'tags': args[2], 
                'attrs': args[3],
                'selectors': args[4],
                'IDv': args[5],
                'classes': args[6]
            }
        
        return dict

    def show_dict(self):
        return self._yaml_dict


class BuildFile(GetInput):
    def __init__(self, type):
        super().__init__(type=type)
        self.__createFile()

    def __createFile(self):
        if path.exists(rf'yamlfiles/cobweb_config{self._url}.yaml') == False:
            with open(rf'yamlfiles/cobweb_config{self._url}.yaml', 'w') as file:
                yaml.dump(self._yaml_dict, file)

if __name__ == "__main__":
    x = BuildFile(type="cli") #this is a test!
    pass
