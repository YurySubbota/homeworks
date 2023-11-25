# Homework8


def addition(a, b):  # сложение
    return int(a) + int(b)


def subtraction(a, b):  # вычитане
    return int(a) - int(b)


def multiplication(a, b):  # умножение
    return int(a) * int(b)


def division(a, b):  # деление
    try:
        result = int(a) / int(b)
    except ZeroDivisionError:
        print('can not divide by zero')
        result = None
    return result


def exponentiation(a, b):  # возведение в степень
    return int(a) ** int(b)


def is_number(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def input_control(number):
    if number == 'exit':
        quit()
    if is_number(number):
        return number
    print('you can input exit or numbers ONLY')


def app():
    operation = None
    operations = {'1': addition, '2': subtraction, '3': multiplication, '4': division, '5': exponentiation}
    operations_list = {'1': 'addition', '2': 'subtraction', '3': 'multiplication', '4': 'division',
                       '5': 'exponentiation'}
    while True:
        print('to exit enter exit instead of any number')
        a = input_control(input('enter first number\n'))
        b = input_control(input('enter second number\n'))
        operation_number = input_control(input(f'enter operation number\n{operations_list}\n'))
        try:
            operation = operations[operation_number]
        except KeyError:
            print('operation does not exist')
        if a and b and operation:
            print('result = ', operation(a, b))
        else:
            print('your input incorrect')
        print('try again')


app()
