if __name__ == '__main__':
    lista = [i for i in range(16)]
    print(lista)
    print(lista[1:10])
    print(lista[8:14])
    print([i for i in lista if i % 2 == 0])
    print([i for i in lista if i % 2 != 0])
    print([i for i in lista if i % 2 == 0 or i % 3 == 0 or i % 4 == 0])
    lista2 = lista[:]
    lista2.sort(reverse=True)
    print(lista2)
    print(sum(lista[10:])/sum(lista[3:10]))
