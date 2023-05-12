if __name__ == '__main__':
    saque = int(input("Quanl o valor do saque? "))
    notas = [200, 100, 50, 20, 10, 5, 2, 1]
    for i in notas:
        print("Número de notas de R$ " + str(i) + ": " + str(int(saque/i)))
        saque = saque % i