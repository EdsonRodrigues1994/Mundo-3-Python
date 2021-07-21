'''Crie um programa onde o usuário possa digitar cinco valores numericos e cadastre-o em uma lista, ja na posição correta de inserção.
sem usar o sort.
No final mostre a lista ordenada na tela.'''

lista = list()

for count in range(0 , 5):
    num = int(input("Digite um valor: "))
    if count == 0:
        lista.append(num)
    elif num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f"Adicionado na posição {pos} da lista.")
                break
            pos += 1
print(f"Os valores digitados em ordem foram {lista}")




