# mode='w' - Write - Modo de escrita de arquivos. Se o arquivo não existir ele é criado, se já existe é sobreescrito.
with open('arquivo.txt', mode='w', encoding='utf8') as fp:
    fp.write('Olá mundo!')

# mode='r' - Read - Modo de leitura de arquivos. 
with open('arquivo.txt', mode='r', encoding='utf8') as fp:
    print(fp.read())