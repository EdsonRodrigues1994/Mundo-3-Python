'''Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobrar() e metade().
Faça tambem um programa que importe sse módulo e use algumas dessas funções.'''

from ex107 import moeda


p = float(input("Digite o preço: R$ "))
print(f"A metade de {p} é: {moeda.metade(p)}")
print(f"O dobro de {p} é: {moeda.dobro(p)}")
print(f"Aumentando 10%, temos: {moeda.aumentar(p)}")
print(f"Reduzindo 13% temos: {moeda.reduzindo(p)}")