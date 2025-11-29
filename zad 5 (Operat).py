#Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list, a drugi typu int .
#Funkcja ma sprawdzić (zwracając typ logiczny bool),
#czy lista z parametru pierwszego zawiera taką wartość jaką przekazano w parametrze drugim.




def zgodnosc(lista: list, liczba: int):
    if lista == liczba:
        return True
    else:
        return False