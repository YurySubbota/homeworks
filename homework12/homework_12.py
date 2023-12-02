class Moving:
    def __init__(self, name):
        name = name
    def move(self):
        raise NotImplementedError('I do not understand this')


class Animal(Moving):
    def voice(self):
        raise NotImplementedError('I do not understand this')


class Transport(Moving):
    def launch(self):
        raise NotImplementedError('I do not understand this')


class Duck(Animal):
    def voice(self):
        print('cria')

    def move(self):
        print('swim')


class Tiger(Animal):
    def voice(self):
        print('r-rrr')

    def move(self):
        print('run')


class Car(Transport):
    def __init__(self, name):
        self.engine_is_work = False
        super().__init__(name)

    def move(self):
        if self.engine_is_work:
            print('car is going')
        else:
            print('car is standing')

    def launch(self):
        print('start engine')
        self.engine_is_work = True


duck1 = Duck('duck')
tiger1 = Tiger('tiger')
car1 = Car('car')
duck1.move()
duck1.voice()
tiger1.voice()
tiger1.move()
car1.move()
car1.launch()
car1.move()