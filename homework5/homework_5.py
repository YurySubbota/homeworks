from random import randint


def range_and_random_numbers():
    while True:
        range_of_numbers = []
        for i in 'first', 'second':
            range_of_numbers.append(int(input(f"input {i} number in range 5 - 30 numbers ")))
        if 4 < range_of_numbers[1] - range_of_numbers[0] + 1 < 31:
            break
        else:
            print('incorrect range. try again')
    random_numbers = set()
    while len(random_numbers) < 3:
        random_numbers.add(randint(range_of_numbers[0], range_of_numbers[1]))
    return range_of_numbers, list(random_numbers)


def user_numbers_and_guessed(range_of_numbers, random_numbers):
    list_of_numbers = [i for i in range(range_of_numbers[0], range_of_numbers[1] + 1)]
    while True:
        print('You have this list of numbers\n', list_of_numbers)
        user_numbers = []
        for i in 'first', 'second', 'third':
            user_numbers.append(input(f'Please try to guessed {i} number from the list '))
            if 'exit' in user_numbers:
                quit()
        if len(set(user_numbers)) != 3:
            print('Do not cheating. Try again.')
        else:
            break

    guessed = 0
    for i in user_numbers:
        if int(i) in random_numbers:
            guessed += 1
    return guessed


def main_function():
    range_of_numbers, random_numbers = range_and_random_numbers()
    while True:
        guessed = user_numbers_and_guessed(range_of_numbers, random_numbers)
        print(f'You guessed {guessed} numbers')
        if guessed == 3:
            print('You Win')
            quit()
        print('try again')


main_function()