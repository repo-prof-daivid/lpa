def fatorial(valor):
    """4! = 4 * 3 * 2 * 1"""
    result = 1
    for i in range(valor, 0, -1):
        result = result * i
    return result


if __name__ == '__main__':
    fatorial_de_3 = fatorial(10)
    print(fatorial_de_3)
