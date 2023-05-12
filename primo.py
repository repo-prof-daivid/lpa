if __name__ == '__main__':
    numero = 0
    primos = 0
    while True:
        divisores = 0
        numero += 1
        for c in range(2, numero):
            if numero % c == 0:
                divisores += 1
        if divisores == 0:
            print('{} é primo'.format(numero))
            primos += 1
        if primos == 15:
            break