'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso mostre:
A)QUANTOS NUMEROS FORAM DIGITADOS
B)A LISTA DE VALORES, ORDENADAS DE FORMA DECRESCENTE.
C) SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA.'''

lista = list()

while True:
    lista.append(int(input("Digite um número: ")))
    continuar = str(input("Deseja continuar? [S/ N]: ").upper()[0])
    while continuar not in "SN":
        print("Opção inválida digite [S / N] para prosseguir: ")
        continuar = str(input("Deseja continuar? [S/ N]: ").upper()[0])
    if continuar == "N":
        print("Saindo ...")
        break
lista.sort(reverse=True)
print(f"Foram digitados {len(lista)} números para sua lista.")
print(f"A lista em ordem decrescente é: {lista}")
if 5 in lista:
    print(f"O número 5 apareceu {lista.count(5)} x na lista na {lista.index(5) + 1}ª posição.")
else:
    print("O número 5 não apareceu nenhuma vez!")