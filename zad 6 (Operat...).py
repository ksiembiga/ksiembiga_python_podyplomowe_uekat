#Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu list.
#Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć duplikaty,
#każdy element podnieść do potęgi 3 stopnia, a następnie zwrócić powstałą listę.


def szescian (lista1, lista2):
    lista3 = lista1 + lista2
    lista3 = list(set(lista3))
    lista3 =  [x **3 for x in lista3]
    return lista3

