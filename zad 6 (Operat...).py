def szescian(lista1, lista2):
    lista3 = lista1 + lista2
    lista3 = list(set(lista3))
    lista3 = [x ** 3 for x in lista3]
    return lista3
