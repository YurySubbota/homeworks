import json


class JsonIsNotList(Exception):
    def __str__(self):
        return 'this json file format is not supported'


class IncorrectFileType(Exception):
    def __str__(self):
        return 'Can not open this file. Please try to open .json or .txt file only'


class BaseHandler:
    def __init__(self, path):
        self.__path = path
        self.content = None
        self._file = None
        try:
            with open(self.path):
                pass
        except FileNotFoundError:
            self.create_file()

    @property
    def path(self):
        return self.__path

    def create_file(self):
        with open(self.path, 'w'):
            pass

    def read(self):
        raise NotImplementedError

    def append(self, new_string):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError


class JsonHandler(BaseHandler):
    def __init__(self, path):
        super().__init__(path)
        with open(self.path, 'r') as file:
            content = json.load(file)
        if not isinstance(content, list):
            raise JsonIsNotList

    def create_file(self):
        with open(self.path, 'w') as file:
            file.write('[]')

    def read(self):
        with open(self.path, 'r') as self._file:
            self.content = json.load(self._file)
        return self.content

    def append(self, new_string):
        self.content.append(new_string)

    def close(self):
        with open(self.path, 'w') as self._file:
            json.dump(self.content, self._file)


class TxtHandler(BaseHandler):
    def read(self):
        with open(self.path, 'r') as self._file:
            self.content = self._file.read()
        return self.content

    def append(self, new_string):
        self.content += str(new_string)

    def close(self):
        if self.content is not None:
            with open(self.path, 'w') as self._file:
                self._file.write(self.content)
        else:
            print('you must read before close')


class FileWorker(BaseHandler):
    def __init__(self, path):
        self.file_type = {'json': JsonHandler, 'txt': TxtHandler}
        self.handler = self.define_handler(path)(path)

    def define_handler(self, path):
        try:
            return self.file_type[path.split('.')[-1].lower()]
        except KeyError:
            raise IncorrectFileType

    def read(self):
        content = self.handler.read()
        return content

    def append(self, new_string):
        self.handler.append(new_string)

    def close(self):
        self.handler.close()


def app():
    fw = FileWorker("path_to_file.json")
    content = fw.read()
    print(content)
    fw.append("Hello ")
    fw.append("how ")
    fw.append("are ")
    fw.append("you ")
    fw.close()
    print(fw.read())


app()
