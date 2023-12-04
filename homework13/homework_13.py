import json


class DataStorage:
    def __init__(self, path):
        self.__path = path
        self.status = 'disconnected'
        self.content = None
        self._file = None

    @property
    def path(self):
        return self.__path

    def _create_storage(self):
        with open(f'{self.path}', 'w') as self._file:
            json.dump([], self._file)
            return self._file

    def connect(self):
        try:
            self._file = open(f'{self.path}', 'r')
            self.content = json.load(self._file)
            self.status = 'connected'
        except FileNotFoundError:
            self._create_storage()
            self._file = open(f'{self.path}', 'r')
            self.content = json.load(self._file)
            self.status = 'connected'

    def disconnect(self):
        if self.status == 'connected':
            self._file.close()
            self.status = 'disconnected'
            print(f'File {self.path} is closed now')
        else:
            print(f'File {self.path} is not open')


class DataStorageWrite(DataStorage):
    def connect(self):
        if self.status == 'disconnected':
            try:
                with open(f'{self.path}', 'r') as self._file:
                    self.content = json.load(self._file)
                self._file = open(f'{self.path}', 'w')
                self.status = 'connected'
            except FileNotFoundError:
                self._create_storage()
                with open(f'{self.path}', 'r') as self._file:
                    self.content = json.load(self._file)
                self._file = open(f'{self.path}', 'w')
                self.status = 'connected'
        else:
            print('File is connected. Before connect again please use disconnect')

    def append(self, string_to_append):
        if self.status == 'connected':
            self.content.append(string_to_append)
        else:
            print('File is disconnected. before append new string please use connect')

    def disconnect(self):
        json.dump(self.content, self._file)
        super().disconnect()


storage1 = DataStorageWrite('s1.json')
storage1.connect()
print(storage1.content)
storage1.append('hi')
storage1.append('how')
storage1.append('are')
storage1.append('you')
storage1.disconnect()
storage1.connect()
print(storage1.content)
storage1.disconnect()
storage1.connect()
storage1.append('i')
storage1.append('am')
storage1.append('fine')
storage1.append('thanks')
storage1.disconnect()
