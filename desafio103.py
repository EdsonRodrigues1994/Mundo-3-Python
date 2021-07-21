'''Faça um programa que tenha yma função chamada ficha(), que receba dois parâmetros opcionais: onome de um jogador e quantos gols ele marcou.
O programa devera ser capaz de mostrar a ficja do jogador, mesmo que algum dado não tenha sido informado corretamente.'''


def ficha(nome, gols):

    if nome == "":
        nome = "<desconhecido>"
        print(f"O jogador {nome}", end="")
    else:
        print(f"O jogador {nome}", end="")
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if gols == "":
        gols = 0
        print(f" fez {gols} gol(s) no campeonato.")
    else:
        print(f" fez {gols} gol(s) no campeonato.")




nome = str(input("Nome do jogador: ").strip().title())
gols = str(input("Número de gols: ").strip())

ficha(nome, gols)





