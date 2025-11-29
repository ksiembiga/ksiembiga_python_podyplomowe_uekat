
#Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
#(rekomendowane wykorzystanie funkcji range), a następnie wyświetli co drugi element.


lista = []
##def co_drugi():
for i in range(10):
    lista.append(i)
for i, element in enumerate(lista):
    if i % 2 == 0:
        print(element)






