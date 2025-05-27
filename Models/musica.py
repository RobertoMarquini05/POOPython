class Musica():
    musicas = []
    def __init__(self, nome, artista, duracao):
        self.Nome = nome
        self.Artista = artista
        self.Duracao = duracao
        Musica.musicas.append(self)
    def listar_musicas():
        for musicaAtual in Musica.musicas:
            print(musicaAtual.Nome)

musica_pop = Musica("Psycho", "PostMalone", 3.57)
musica_trap = Musica("Mi'adama", "Sidoka", 4.29)

Musica.listar_musicas()