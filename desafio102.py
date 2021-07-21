'''Crie um programa que tenha uma função fatorial() qye receba dois parametros:
o primeiro que indique o numero a calcular, e o segundo chamado show, que será
um valor lógico(opcional) indicando se será mostrado ou nao na tela o processo de cálculo fatorial'''

import math

def fatorial(num, show=False):

    print("-" * 25)
    fat = 1
    for count in range(num, 0, -1):
        if show:
            print(count, end="")
            if count > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        fat *= count
    return fat


print(fatorial(5, show=True))

