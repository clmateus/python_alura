import json

with open('dados.json', mode='r', encoding='utf8') as fp:
    print(json.load(fp))