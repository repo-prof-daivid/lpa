if __name__ == '__main__':
    inputDoUsuario = input("Digite o primeiro número: ")
    n1 = float(inputDoUsuario)

    inputDoUsuario = input("Digite o segundo número: ")
    n2 = float(inputDoUsuario)

    dif = 0

    if n1 > n2:
        dif = n1 - n2
    else:
        dif = n2 - n1

    print("A diferença entre eles é: " + str(dif))