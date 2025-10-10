import time

def timer_with_args(func):
    def wrapper(a, b):
        start = time.time()
        func(a, b)
        end = time.time()
        print(f'Время выполнения функции: {end - start:.5f} секунд\n')
    return wrapper


def timer_no_args(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Время выполнения функции: {end - start:.5f} секунд\n')
    return wrapper


def sum_numbers(a, b):
    print(f'Сумма чисел {a} и {b} равна {a + b}')


def sum_from_file():
    f = open('tasks/task5/input.txt', 'r', encoding='utf-8')
    text = f.read().split()
    f.close()

    a = float(text[0])
    b = float(text[1])
    result = a + b

    print(f'Прочитано из файла: {a} и {b}')
    print(f'Сумма равна: {result}')

    f = open('tasks/task5/output.txt', 'w', encoding='utf-8')
    f.write(str(result))
    f.close()

    print('Результат записан в файл output.txt')


timed_sum = timer_with_args(sum_numbers)
timed_sum(5, 10)

timed_sum_file = timer_no_args(sum_from_file)
timed_sum_file()

