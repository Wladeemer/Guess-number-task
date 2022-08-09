"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число

        if number == predict_number:
            break  # выход из цикла если угадали
    #print(f"Алгоритм угадал число за количество иттераций: {count} ")
        
    return count


def algorithm_predict(number: int = 1) -> int:
    """Угадываем число, согласно алгоритма деления отрезка пополам

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    ''' начало отрезка а|---number--------|b конец отрезка'''
    a = 0
    b = 100

    while True:
        count += 1

        if number >= ((a + b) / 2):
            a = ((a + b) / 2)

        if number < ((a + b) / 2):
            b = ((a + b) / 2)

        if number == round(b):
            # print ('Вы загадали число:  ', round(b))
            break  # выход из цикла если угадали

        if number == round(a):
            # print ('Вы загадали число:  ', round(a))
            break  # выход из цикла если угадали

    return count


def score_game(func_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости

    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(func_predict(number))

    score = int(np.mean(count_ls))
    
    return print(f"Алгоритм угадывает число в среднем за количество иттераций: {score} ")






if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    score_game(algorithm_predict)
