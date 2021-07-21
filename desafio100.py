'''Faça um programa que tenha uma lista chamada numeros e duas funções chamadas
sorteia() e somapar(). A primeira função vai sortear 5 numeros e vai colocá-los dentro de uma lista e a
segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''
import random
from time import sleep

numeros = list()
pares = list()

def sorteia():

    for i in range(0,5):
        aleatorios = random.randint(0, 10)
        numeros.append(aleatorios)
    print(f"Sorteando 5 valores da lista:", end=" ")
    sleep(0.5)
    for i in numeros:
        sleep(0.5)
        print(f"{i}", end=" ")
    sleep(0.5)
    print("PRONTO!")

def somaPar():
    total = 0
    for i in numeros:
        if i % 2 == 0:
            pares.append(i)
            total += i

    print(f"Somando os valores pares de {numeros}, temos {total}")


sorteia()
somaPar()
