if __name__ == '__main__':
    userInfo = input("Digite o que você quer escrever no arquivo: ")
    arq = open("escrita_do_usuario.txt", "w")
    arq.write(userInfo)
    arq.close()

    arq = open("escrita_do_usuario.txt", "r")
    print(arq.read())
    arq.close()