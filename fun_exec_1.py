def produtoTresElementos(valor1, valor2, valor3):
    resultado = valor1 * valor2 * valor3
    return resultado

def inputFloat(numero):
    valor = float(input("Digite o valor {}: ".format(numero)))
    return valor


if __name__ == '__main__':
    valor1 = inputFloat(1)
    valor2 = inputFloat(2)
    valor3 = inputFloat(3)
    produto = produtoTresElementos(valor1, valor2, valor3)
    print(produto)