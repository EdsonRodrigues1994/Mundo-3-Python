'''Crie um programa que tenha uma função chamada maior(),que receba varios parametros
com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é maior.'''

from time import sleep

def maior(*num):
    count = 0
    maior = 0
    print("-=" * 35)
    print("Analisando os valores passados ...")
    sleep(1.5)
    for valor in num:
        sleep(0.3)
        print(f"{valor}", end=" ")
        sleep(0.5)
        if count == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        count += + 1

    print(f"Foram informados {count} valores ao todo.")
    print(f"O maior valor informado foi {maior}. ")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
