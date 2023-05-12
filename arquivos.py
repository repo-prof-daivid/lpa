import os


if __name__ == '__main__':
    print(os.getcwd())
    print(os.path.exists("./arquivostxt"))
    os.chdir("./arquivostxt")
    print(os.getcwd())
    arq = open("text.txt", "w")
    arq.write("Hello world!")
    arq.close()
