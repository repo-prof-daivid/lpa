from random import *

if __name__ == '__main__':
    """ exercício 1 
    Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.
    """

    print("Exercício 1: ")
    # se quiser ler os numeros a partir do usuário
    # lista = []
    # for i in range(0, 5):
    #     lista_reais.append(float(input("digite um número real: ")))
    lista = [randint(-1000, 1000) for i in range(0, 5)] # compressão de lista
    for i in range(0, len(lista)):
        print("O elemento é {} e a sua posição na lista é {}.".format(lista[i], i))

    """ exercício 2 """
    print("Exercício 2: ")
    # se quiser ler os numeros a partir do usuário
    # lista_reais = []
    # for i in range(0, 10):
    #     lista_reais.append(float(input("digite um número real: ")))
    lista_reais = [random() for i in range(0,10)] # Compressão de lista criando números aleatórios
    print(lista_reais)
    ultima_posicao_lista = len(lista_reais)-1
    for i in range(ultima_posicao_lista, -1, -1):
        print(lista_reais[i])

    """ exercício 3 """
    print("Exercício 3: ")
    # se quiser ler as notas a partir do usuário
    # lista_notas = []
    # for i in range(1, 5):
    #     lista_notas.append(float(input("digite a nota {}: ".format(i))))
    lista_notas = [randint(1, 10) for i in range(0, 4)]
    media = sum(lista_notas) / len(lista_notas)
    print(lista_notas)
    print(media)

    """ exercício 4 """
    print("Exercício 4: ")
    lista_idades = [randint(0, 100) for i in range(0,20)]
    print(lista_idades)
    print(max(lista_idades))
    print(min(lista_idades))
