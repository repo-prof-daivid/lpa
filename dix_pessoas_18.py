if __name__ == '__main__':
    pessoas = {}
    while True:
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        cpf = input("Digite seu cpf: ")
        pessoas[cpf] = {
            "nome" : nome,
            "idade": idade
        }
        encerrar = input("Deseja inserir uma nova pessoa?")
        if encerrar != "sim":
            break
    pessoas_menor_18 = {}
    pessoas_maior_igual_18 = {}
    for cpf, pessoa in pessoas.items():
        """ cpf = 0
        pessoa = {'nome': 'daivid', 'idade': '30'} """
        if pessoa["idade"] < 18:
            pessoas_menor_18[cpf] = pessoa
        else:
            pessoas_maior_igual_18[cpf] = pessoa

    print("Pessoas 18+", pessoas_maior_igual_18)
    print()
    print("Pessoas 17-", pessoas_menor_18)
