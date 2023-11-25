# 1. Выбрал Python по тому что это один из самых простых в изучении языков программирования с большим количеством
# фреймворков и хорошей поддержкой сообщества. Как следствие самый быстрый способ получить оффер и уже работая
# программистом продолжить изучать другие языки такие как JS, C++ и Java если они понадобятся в работе
# 2. В Python есть
#   неизменяемые типы данных такие как: int, float, bool, str и tupe и
#   изменяемые типы данных такие как: list, set, dict
#       list - список - упорядоченная изменяемая коллекция объектов произвольных типов
#           (почти как массив, но типы могут отличаться).
#           начинается с 0 элемента, -1 элемент это последний элемент списка
#           переменная = [элемент, элемент,...]
#           переменная.append(элемент) - добавить элемент в конец списка
#           переменная.pop() - удалить последний элемент из списка
#           переменная.pop(номер_элемента) - удалить нужный элемент
#           len(переменная) - длинна списка
#       set - множество уникальных элементов не упорядоченных
#           переменная = {данные, данные, ...} или переменная = set([данные, данные, ...])
#           или переменная=set() или переменная=set(переменная)
#           переменная.add(данные)
#           оператор in  например print(значение in переменная) или (значение not in переменная) выведет true или false
#       dict - неупорядоченные коллекции произвольных объектов с доступом по ключу. Их иногда ещё называют
#           ассоциативными массивами или хеш-таблицами.
#           переменная={ключ:значение,ключ:значение}
#           dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение,
#           а возвращает default (по умолчанию None).
#            dict.items() - возвращает пары (ключ, значение).
#
# 3.
input_data = 86400
days = int(input_data / 60 / 60 // 24)
minutes = int((input_data - days * 24 * 60 * 60) // 60)
seconds = input_data % 60
print(days, " days ,", minutes, " minutes ,", seconds, " seconds ")

# интересно было попробовать вариант который будет универсальным и будет выдавать в годах, месяцах, днях, часах и секундах
# вопрос насколько эта функия ущербно выглядит если её в коде увидит условный тимлид
def how_long_time(all_seconds):
    seconds = all_seconds % 60
    tempary_variable = all_seconds // 60
    minutes = tempary_variable % 60
    tempary_variable = tempary_variable // 60
    hours = tempary_variable % 24
    tempary_variable = tempary_variable // 24
    days = tempary_variable % 30
    tempary_variable = tempary_variable // 30
    months = tempary_variable % 12
    years = tempary_variable // 12
    return [years, months, days, hours, minutes, seconds]

print(how_long_time(input_data)[0], " years, ", how_long_time(input_data)[1],
      " months, ", how_long_time(input_data)[2], " days ,", how_long_time(input_data)[3],
      " hours ,",  how_long_time(input_data)[4], " minutes ,", how_long_time(input_data)[5], " seconds ")

all_seconds = (((((how_long_time(input_data)[0] * 12 + how_long_time(input_data)[1]) * 30 +
                  how_long_time(input_data)[2]) * 24 + how_long_time(input_data)[3]) * 60 +
                how_long_time(input_data)[4]) * 60 + how_long_time(input_data)[5])
assert all_seconds == input_data