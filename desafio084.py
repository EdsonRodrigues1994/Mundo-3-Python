'''Faça um programa que leia nome  e peso de várias pessoas guardando tudo em uma lista. No final mostre:
A)QUANTAS PESSOAS FORAM CADASTRADAS
B) UMA LISTAGEM COM AS PESSOAS MAIS PESADAS
C) UMA LISTAGEM COM AS PESSOAS MAIS LEVES.'''


pessoas = list()
dados = list()
maior = menor = count = 0
pessoaMais = " "
pessoaMenos = " "

while True:
    dados.append(str(input("Nome: ")).title())
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    count += + 1
    continuar = str(input("Quer continuar? [S / N]: ").upper()[0])
    while continuar not in "SN":
        print("Dado incorreto!")
        continuar = str(input("Quer continuar? [S / N]: ").upper()[0])
    if continuar == "N":
        print("Saindo ...")
        break




print(f"Foram cadastradas {count} pessoa(s).")
print(f"O maior peso cadastrado é {maior:.2f} kg. Peso de", end=" ")
for peso in pessoas:
    if peso[1] == maior:
        print(f"{peso[0]}", end=", ")
print(f"\nO menor peso cadastrado é {menor:.2f} kg. Peso de", end=" ")
for peso in pessoas:
    if peso[1] == menor:
        print(f"{peso[0]}", end=", ")
