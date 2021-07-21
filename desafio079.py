'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores unicos, digitados em ordem crescente.'''

numeros = list()

while True:
    numeros.append(int(input("Digite um número: ")))
    numeros.sort()
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Deseja continuar? [S / N]: ").upper()[0])
    if continuar == "N":
        print("Processando ...")
        break
print(sorted(set(numeros)))


