'''Faça um programa que tenha uma funcao chamada contador(), que receba tres parametros:
inicio, fim e passo e realize a contagem.
Seu programa tem que realizar tres contagens através da função criada:
A) DE 1 ATÉ 10, DE 1 EM 1
B) DE 10 ATÉ 0, DE 2 EM2
C) UMA CONTAGEM PERSONALIZADA'''

from time import sleep

def contador():
    print("-=" * 25)
    print("Contagem, de 1 até 10 de 1 em 1")
    sleep(1)
    for i in range(1, 11):
        sleep(0.5)
        print(i, end=" ")
    sleep(0.5)
    print("FIM!", end="")
    print("")
    print("-=" * 25)
    print("Contagem de 10 até 10 de 2 em 2")
    for i in range(10, -2, -2):
        sleep(0.5)
        print(i, end=" ")
    sleep(0.5)
    print("FIM!", end="")
    print("")
    print("-=" * 25)
    sleep(0.5)
    print("Agora é a sua vez de personalizar a contagem!")
    inicio = int(input("Início: "))
    fim = int(input("Fim: "))
    passo = int(input("Passo: "))

    if inicio < fim:
        if passo > 0:
            for i in range(inicio, fim + 1, passo):
                sleep(0.5)
                print(i, end=" ")
            sleep(0.5)
            print("FIM!", end="")
            print("")
            print("-=" * 25)
    if inicio > fim:
        if passo > 0:
            for i in range(inicio, fim - 1, - passo):
                sleep(0.5)
                print(i, end=" ")
            sleep(0.5)
            print("FIM!", end="")
            print("")
            print("-=" * 25)
    if inicio > fim:
        if passo < 0:
            for i in range(inicio, fim - 1, passo):
                sleep(0.5)
                print(i, end=" ")
            sleep(0.5)
            print("FIM!", end="")
            print("")
            print("-=" * 25)
    if inicio < fim:
        if passo == 0:
            passo = 1
            for i in range(inicio, fim + 1, passo):
                sleep(0.5)
                print(i, end=" ")
            sleep(0.5)
            print("FIM!", end="")
            print("")
            print("-=" * 25)
    if inicio > fim:
        if passo == 0:
            passo = 1
            for i in range(inicio, fim - 1, - passo):
                sleep(0.5)
                print(i, end=" ")
            sleep(0.5)
            print("FIM!", end="")
            print("")
            print("-=" * 25)

contador()