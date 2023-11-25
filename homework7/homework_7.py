import time


def how_much_time(some_function):
    def how_time():
        function_time = time.time()
        function_result = some_function()
        function_time = time.time() - function_time
        return function_result, function_time

    return how_time


@how_much_time
def time_test_function():
    delay = 10
    print("Before delay")
    time.sleep(delay)
    print('After delay')
    return f'delay {delay} seconds'


print(time_test_function())

"""
import time


def название_декоратора(какая_то_функция):
    def внутрянка_декоратора():
        код_до_запуска_функции
        какая_то_функция()
        код_после_запуска_функции
        return что_нибудь
    return внутрянка_декоратора


@название_декоратора
def функция_к_которой_применяем_декоратор():
    код_функции


print(функция_к_которой_применяем_декоратор())
"""
