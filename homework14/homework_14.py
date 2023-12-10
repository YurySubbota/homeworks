import json


class IsNotList(Exception):
    def __str__(self):
        print('this json file format is not supported')


class BaseHandler:
    def __init__(self, path):
        self.__path = path
        self.content = None
        self._file = None
        
    @property
    def path(self):
        return self.__path

    def read(self):
        raise NotImplementedError

    def append(self, new_string):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError


class JsonHandler(BaseHandler):
    def __init__(self, path):
        super().__init__(path)
        try:
            with open(self.path, 'r') as self._file:
                self.content = json.load(self._file)
            raise IsNotList if not isinstance(self.content, list) else ...
            quit() if not isinstance(self.content, list) else ...
        except FileNotFoundError:
            pass

    def read(self):
        try:
            with open(self.path, 'r') as self._file:
                self.content = json.load(self._file)
        except FileNotFoundError:
            with open(self.path, 'w') as self._file:
                json.dump([], self._file)
            with open(self.path, 'r') as self._file:
                self.content = json.load(self._file)
        print('JsonHandler.read()')
        return self.content

    def append(self, new_string):
        self.content.append(new_string)
        print(f'JsonHandler.append(){new_string}')


    def close(self):
        with open(self.path, 'w') as self._file:
            json.dump(self.content, self._file)        
        print('JsonHandler.close()')


class TxtHandler(BaseHandler):
    def read(self):
        try:
            with open(self.path, 'r') as self._file:
                self.content = self._file.read()
        except FileNotFoundError:
            with open(self.path, 'w'):
                pass
            with open(self.path, 'r') as self._file:
                self.content = self._file.read()
        print('TxtHandler.read()')

    def append(self, new_string):
        self.content += str(new_string)
        print(f'TxtHandler.append(){new_string}')

    def close(self):
        if self.content is not None:
            with open(self.path, 'w') as self._file:
                self._file.write(self.content)
        else:
            print('you must read before close')
            
        print('TxtHandler.close()')


class FileWorker(BaseHandler):
    def __init__(self, path):
        super().__init__(path)
        self.handler = self.type_of_file()(self.path)

    def type_of_file(self):
        if self.path.lower().endswith('.json'):  # if end of string .json
            return JsonHandler
        elif self.path.lower().endswith('.txt'):
            return TxtHandler
        quit('Can not open this file. Please try to open .json or .txt file only')

    def read(self):
        self.handler.read()

    def append(self, new_string):
        self.handler.append(new_string)

    def close(self):
        self.handler.close()


def app():
    fw = FileWorker('path_to_file.json')
    content = fw.read()
    fw.append('obj1')
    fw.append('obj2')
    fw.close()


app()

