def saudacao(nome, saud="Olá", pontuacao="!!"):
    return saud + ", " + nome + pontuacao


if __name__ == '__main__':
    print(saudacao("Daivid"))
    print(saudacao("João", "Parabéns"))
    print(saudacao("João", "Parabéns", "."))