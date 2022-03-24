import random

def sortear_jogadores(lista):
    lista = random.sample(lista, 4)
    return len(lista)

if __name__ == '__main__':
    sortear_jogadores([1,2,3,4])