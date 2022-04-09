import json

class JsonLocalStorage:
    @staticmethod
    def saveLatest(data):
        JsonLocalStorage.save('latest.json', data)

    @staticmethod
    def loadLatest():
        return JsonLocalStorage.load('latest.json')

    @staticmethod
    def save(fileName, data):
        try:
            with open(fileName, "w") as p:
                json.dump(data, p)
        except IOError:
            print('IOError when trying to open a file named', fileName)

    @staticmethod
    def load(fileName):
        try:
            with open(fileName, "r") as read_it:
                data = json.load(read_it)
                return data
        except IOError:
            print('IOError when trying to open a file named', fileName)