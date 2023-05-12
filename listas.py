if __name__ == '__main__':
    listaPalavras = ["banana", "maçã", "abacaxi"]

    # listaPalavrasTamanho = [len(i) for i in listaPalavras if i == "banana"]
    listaPalavrasTamanho = []
    for fruta in listaPalavras:
        if fruta == "banana":
            listaPalavrasTamanho.append(len(fruta))
    print(listaPalavrasTamanho)