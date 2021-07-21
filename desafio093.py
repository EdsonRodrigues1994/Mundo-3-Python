'''Crieum programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''


jogador = dict()
gols = list()
i = 0
totGols = 0
jogos = 0

jogador['Nome'] = str(input("Nome: ").title())
partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
jogador['Gols'] = gols
numPart = partidas

while i < partidas:
    golpartida = int(input(f"Quantos gols na partida {i + 1} ?"))
    totGols += golpartida
    gols.append(golpartida)
    jogador['Total'] = totGols
    i += + 1

print("-=" * 30)
print(jogador)
print("-=" * 30)

print(f"O campo nome tem o valor {jogador['Nome']}")
print(f"O campo gols tem o valor {jogador['Gols']}")
print(f"O campo total tem o valor {jogador['Total']}")

print("-=" * 30)

print(f"O jogador {jogador['Nome']} jogou {partidas} partidas.")
while jogos < partidas:
    for p in jogador['Gols']:
        print(f"    => Na partida {jogos + 1}, fez {p} gol(s). ")
        p += + 1
        jogos += + 1
print(f"Foi um total de {jogador['Total']} gols.")

print("-=" * 30)