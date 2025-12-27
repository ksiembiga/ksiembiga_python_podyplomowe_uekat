import random


liczba = random.randint(1, 100)


def czy_parzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False


parzystosc = czy_parzysta(liczba)

if parzystosc is True:
    print("Liczba parzysta")
elif parzystosc is False:
    print("Liczba nieparzysta")
