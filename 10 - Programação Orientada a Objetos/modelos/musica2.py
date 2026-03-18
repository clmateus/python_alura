class Musica():
    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'A música {self.nome} da banda {self.artista} tem duração de {self.duracao}'
    
    def listar_musicas():
        for i in Musica.musicas:
            print(f'{i}')

south_of_heaven = Musica('South of Heaven', 'Slayer', 298)
crystal_mountain = Musica('Crystal Mountain', 'Death', 307)
nutshell = Musica('Nutshell', 'Alice in Chains', 259)

Musica.listar_musicas()