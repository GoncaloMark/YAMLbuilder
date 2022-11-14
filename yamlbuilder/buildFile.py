try:
    import os
except ImportError as e:
    print("Some modules could not be imported from stdlib('os')")

class GetInput:
    def __init__(self, type):
        self.__type = type
        self.__url = None
        self.__hops = None
        self.__tags= None
        self.__attrs = None
        self.__yaml_dict = None

        if self.__type == "cli":
            self._input = self.__getInputCLI()

        elif self.__type == "web":
            self._input = self.__getInputWeb()

    def __getInputCLI(self):
        print("Config File Setup! What's the URL?")
        self.__url = input()
        print("Maximum number of hops?")
        self.__hops = input()
        print("Tags to scrape?")
        self.__tags = list(input().strip().split())
        print("Any attributes?")
        self.__attrs = list(input().strip().split())
        print("Classes?")
        self.__classes = list(input().strip().split())

        self.__yaml_dict = self.__buildDict(self.__url, self.__hops, self.__tags, self.__attrs, self.__classes)
        return self.__yaml_dict

    def __getInputWeb(self):
        pass

    def __buildDict(self, *args):
        dict = [{
            'url': args[0],
            'hops': args[1],
            'tags': args[2],
            'attrs': args[3],
            'classes': args[4]
        }]
        
        return dict

    def show_dict(self):
        return self.__yaml_dict


class BuildFile(GetInput):
    def __init__(self, type):
        super().__init__(type=type)
        self.__createFile()

    def __createFile(self):
        pass

if __name__ == "__main__":
    x = GetInput(type="cli")
    print(x.show_dict())
