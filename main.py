import random

class Simulador():

    def __init__(self, numero_jogadores):
        self.numero_jogadores = numero_jogadores

    def sortear_jogadores(self):
        lista = [i+1 for i in range(self.numero_jogadores)]
        lista = random.sample(lista, self.numero_jogadores)
        return lista

if __name__ == '__main__':
    simulador = Simulador(numero_jogadores=4)
    print(Simulador.sortear_jogadores([1,2,3,4], tamanho=4))