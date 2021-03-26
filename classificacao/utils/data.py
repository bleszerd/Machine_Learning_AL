import csv


def read_acesso():
    X = []
    Y = []

    file = open("../csv/acesso.csv", 'r')
    reader = csv.reader(file)

    reader.__next__()

    for home, como_funciona, contato, comprou in reader:
        X.append([int(home), int(como_funciona), int(contato)])
        Y.append(int(comprou))

    return X, Y


def read_buscas():
    X = []
    Y = []

    file = open("../csv/buscas.csv", 'r')
    reader = csv.reader(file)

    reader.__next__()

    for home, busca, logado, comprou in reader:
        X.append([int(home), busca, int(logado)])
        Y.append(int(comprou))

    return X, Y
