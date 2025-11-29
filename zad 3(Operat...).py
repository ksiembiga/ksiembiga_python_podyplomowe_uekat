#Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w parametrze jest parzysta
##i zwróci tą informację jako typ logiczny bool (True/False). Należy uruchomić funkcję,
##wynik wykonania zapisać do zmiennej,
##a następnie wykorzystując warunek logiczny wyświetlić
##prawidłowy tekst "Liczba parzysta" / "Liczba nieparzysta"
import random

liczba = random.randint(1, 100)

def czy_parzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False

parzystosc = czy_parzysta(liczba)

if parzystosc is True :
    print("Liczba parzysta")
elif parzystosc is False:
    print("Liczba nieparzysta")