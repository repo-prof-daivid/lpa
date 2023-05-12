# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    valor_do_usuario = input("Digite a nota 1: ")
    n1 = float(valor_do_usuario)

    valor_do_usuario = input("Digite a nota 2: ")
    n2 = float(valor_do_usuario)

    valor_do_usuario = input("Digite a nota final: ")
    nf = float(valor_do_usuario)

    media = (n1 + n2 + nf) / 3

    print("A média do aluno foi: " + str(media))

    if media >= 7:
        print("Aluno aprovado!")
    else:
        print("Aluno vai pra a final!")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
