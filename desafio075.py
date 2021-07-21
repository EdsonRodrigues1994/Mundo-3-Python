'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final mostre:
A) QUANTAS VEZES APARECEU O VALOR 9
B) EM QUE POSICAO FOI DIGITADO O PRIMEIRO VALOR 3
C) QUAIS FORAM OS NUMEROS PARES'''


num = (int(input("Digite um número: ")),
int(input("Digite um número: ")),
int(input("Digite um número: ")),
int(input("Digite um número: ")))

print(f"O valor 9 apareceu {num.count(9)}x.")

if 3 in num:
      print(f"O primeiro valor 3 foi digitado na {num.index(3) + 1}ª posição.")
      print("Os valores pares são: ")
else:
      print("O número 3 não foi digitado nenhuma vez!")
for i in num:
      if i %  2 == 0:
            print(i , end=" ")

