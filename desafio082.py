'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final mostre oconteúdo das três listas geradas'''

lista = list()
impar = list()
par = list()

while True:
    lista.append(int(input("Digite um número: ")))
    continuar = str(input("Deseja continuar? [S / N]").upper()[0])
    while continuar not in "SN":
        print("Opção inválida, informe [S / N] para continuar: ")
        continuar = str(input("Deseja continuar? [S / N]").upper()[0])
    if continuar == "N":
        print("Saindo ...")
        break
for count in lista:
    if count % 2 == 0:
        par.append(count)
    else:
        impar.append(count)
print(f"A sua lista é: {sorted(lista)}")
print(f"A sua lista composta apenas por números pares: {sorted(par)}")
print(f"A sua lista composta apenas por números ímpares: {sorted(impar)}")