voluntarios = []

while True:
    voluntario = input('Digite o nome do voluntário (ou "sair" para encerrar): ')
    
    if voluntario.lower() == 'sair':
        print(f'Voluntários registrados: {voluntarios}')
        break

    voluntarios.append(voluntario)