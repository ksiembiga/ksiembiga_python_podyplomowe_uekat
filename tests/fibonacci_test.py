import pytest

def fibonacci_test(numbers):
    numbers = [0, 1, 5, 10, -1]

    for number in numbers:
        assert number > 0, ValueError
        liczba = 0
        for i in range(number):
            liczba += i

        if number > 0:
            print(f' {number}: {liczba}')