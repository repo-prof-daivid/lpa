if __name__ == '__main__':
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    endereco = input("Digite seu endereço: ")
    sexo = input("Digite seu sexo: ")
    d = {
        "nome": nome,
        "idade": idade,
        "endereco": endereco,
        "sexo": sexo
    }
    chaves = []
    print(chaves)
    print(d.keys())
    for key in d.keys():
        chaves.append(key)
    print(chaves)
    chaves.sort()
    print(chaves)
    for key in chaves:
        print(key, d[key])
