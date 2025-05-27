from Models.Contador import Contador
from Models.avaliacao import Avaliacao
contador = Contador()
class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self._nome} | {self._categoria}"

    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            contador.incrementar()
            print(f"{contador.__str__()} - {restaurante._nome} | {restaurante._categoria} | {restaurante._ativo} | {restaurante.media_avaliacao}")

    @property
    def ativo(self):
        return "Ativo" if self._ativo else "Desativado"
    
    def alternar_estado(self):
        self._ativo = not self._ativo  

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota < 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_notas = len(self._avaliacao)
        media = round(soma_notas / qtd_notas, 1)
        return media            

