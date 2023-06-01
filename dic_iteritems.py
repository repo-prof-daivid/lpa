if __name__ == '__main__':
    dicionario = {
        "compra_maria": "morango",
        "compra_pedro": "maça",
        "compra_joao": "melancia",
        "compra_josé": "mamão"
    }
    print(dicionario.items())
    for key, value in dicionario.items():
        print(key, value)
