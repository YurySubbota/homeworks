from random import randint


class NotEnoughMoney(Exception):
    def __init__(self, some_to_buy):
        self.some_to_buy = some_to_buy

    def __str__(self):
        return f"Not enough money to buy {self.some_to_buy}"


class ChattelFirst(Exception):
    def __str__(self):
        return "You must buy chattel before buy estate"


class Property:
    def __init__(self, price, name):
        self.__price = price
        self.__name = name

    @property
    def price(self):
        return self.__price

    def __repr__(self):
        return f"{self.__name} - {self.price}"


class Chattel(Property):
    @property
    def type_of_property(self):
        return 'chattel'


class Estate(Property):
    @property
    def type_of_property(self):
        return 'estate'


class Human:
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.property = []

    def __repr__(self):
        return f"{self.name} - {self.money}, {self.property}"

    def is_chattel_in_property(self):
        for property in self.property:
            if property.type_of_property == 'chattel':
                return True

    def work(self):
        self.money += randint(5, 10)

    def buy(self, some_property):
        if some_property.type_of_property == 'estate':
            if self.is_chattel_in_property():
                if some_property.price > self.money:
                    print(f'Sorry, you do not have enough money to buy {some_property}')
                    return
                self.property.append(some_property)
                self.money -= some_property.price
                print(f'Congratulations! You have buy {some_property}')
            else:
                print('You must buy chattel before buy estate')
        else:
            if some_property.price > self.money:
                print(f'Sorry, you do not have enough money to buy {some_property}')
                return
            self.property.append(some_property)
            self.money -= some_property.price
            print(f'Congratulations! You have buy {some_property}')

    def sell(self, some_property):
        for i in range(len(self.property) - 1):
            if some_property == self.property[i]:
                self.property.pop(i)
                self.money += some_property.price
                print(f'You have sell {some_property}')
                return
            else:
                print(f'You do not have {some_property}')

def app():
    john = Human("John")
    car = Chattel(40, 'car')
    house = Estate(100, 'house')
    print(john)
    john.buy(house)
    john.work()
    john.work()
    john.buy(car)
    john.work()
    john.work()
    john.sell(house)
    print(john)
    john.work()
    john.work()
    john.work()
    john.work()
    john.buy(house)
    print(john)
    john.work()
    john.work()
    john.work()
    john.buy(car)
    print(john)
    john.work()
    john.work()
    john.buy(house)
    print(john)
    for _ in range(0, 10):
        john.work()
    john.buy(house)
    print(john)
    john.work()
    john.work()
    john.work()
    john.work()
    john.work()
    john.buy(house)
    print(john)
    john.sell(car)
    print(john)


app()
