class Contador:
    def __init__(self):
        self.Valor = 0
    def incrementar(self):
        self.Valor += 1 
    def __str__(self):
        return self.Valor
        