if __name__ == '__main__':
    nome = input("Digite seu nome: ")

    for i in range(1, len(nome)+1):
        print(nome[0:i])