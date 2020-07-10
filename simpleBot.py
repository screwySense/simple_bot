import sys


def greet(bot_name, bot_year):
    print(f'Hello! My name is {bot_name}.')
    print(f'I was created in {bot_year}.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print(f'What a great name you have, {name}!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())

    age = (num_1 * 70 + num_2 * 21 + num_3 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")


def count():
    print("Now I will prove to you that I can count to any number you want.")

    num = int(input())
    for i in range(num + 1):
        print(f'{i} !')


def test():
    print("""Let's test your programming  knowledge.
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")

    while True:
        i = int(input())
        if i == 2:
            end()
            break
        else:
            print('Please, try again.')
            continue


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')
remind_name()
guess_age()
count()
test()
