'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final coloque em ordem sabendo que o vencedor tirou o maior número no dado'''

from random import randint
from time import sleep
from operator import itemgetter

jogadores = dict()
ranking = list()
rank = dict()

print("Valores sorteados: ")
sleep(1)
for i in range(1,5):
    dado = randint(1, 6)
    jogadores['Jogador'] = i
    jogadores['Dado'] = dado
    ranking.append(jogadores.copy())
    sleep(1)
    print(f"O jogador {jogadores['Jogador']} tirou {jogadores['Dado']}.")

