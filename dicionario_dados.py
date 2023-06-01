if __name__ == '__main__':
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    endereco = input("Digite seu endereço: ")
    sexo = input("Digite seu sexo: ")
    d = {
        "idade": idade,
        "endereco": endereco,
        "nome": nome,
        "sexo": sexo
    }
    print(d)