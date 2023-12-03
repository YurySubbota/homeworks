import json


class DataStorage:
    def __init__(self, path):
        self.__path = path
        self.status = 'disconnected'
        self.content = None
        self.__file = None

    @property
    def path(self):
        return self.__path

    def _create_storage(self):
        with open(f'{self.path}', 'w') as self.__file:
            json.dump([], self.__file)
            return self.__file

    def connect(self):
        try:
            self.__file = open(f'{self.path}', 'r')
            self.content = json.load(self.__file)
            self.status = 'connected'
        except FileNotFoundError:
            self._create_storage()
            self.connect()

    def disconnect(self):
        if self.status == 'connected':
            self.__file.close()
            self.status = 'disconnected'
            print(f'File {self.path} is closed now')
        else:
            print(f'File {self.path} is not open')


class DataStorageWrite(DataStorage):
    def connect(self):
        if self.status == 'disconnected':
            try:
                with open(f'{self.path}', 'r') as self.__file:
                    self.content = json.load(self.__file)
                self.__file = open(f'{self.path}', 'w')
                self.status = 'connected'
            except FileNotFoundError:
                self._create_storage()
                self.connect()
        else:
            print('File is connected. Before connect again please use disconnect')

    def append_string(self, string_to_append):
        if self.status == 'connected':
            self.content.append(string_to_append)
            print(self.content)
            json.dump(self.content, self.__file)
        else:
            print('File is disconnected. before append new string please use connect')


storage1 = DataStorageWrite('s1.json')
storage1.connect()
print(storage1.content)
storage1.append_string('hi')
storage1.append_string('how')
storage1.append_string('are')
storage1.append_string('you')
storage1.disconnect()
storage1.connect()
print(storage1.content)
storage1.disconnect()