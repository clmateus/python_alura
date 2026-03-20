import csv

with open('dados.csv', newline='') as fp:
    leitor = csv.reader(fp)
    for linha in leitor:
        print(linha)