# mode='a' - Append - Modo de adição de informações a arquivos. Esse modo necessita que o arquivo já exista e ele não o deleta como o modo write
with open('arquivo.txt', mode='a', encoding='utf8') as fp:
    fp.write('\nOutra linha')