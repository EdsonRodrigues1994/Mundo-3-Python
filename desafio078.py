'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.'''



num = (int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")),
int(input("Digite um número: ")),int(input("Digite um número: ")))

print(f"Você digitou {num}")
print(f"O menor valor digitado foi {min(num)} na {num.index(min(num)) + 1}ª posição e o maior número foi {max(num)} na {num.index(max(num)) + 1}ª posição.")

