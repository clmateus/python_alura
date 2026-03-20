# csv - Biblioteca que contém ferramentas para manipulação de arquivos .csv
import csv

with open('dados.csv', mode='w', encoding='utf8') as fp:
    escritor = csv.writer(fp)
    escritor.writerow(['nome', 'idade'])
    escritor.writerow(['Maria', '20'])