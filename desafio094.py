'''Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de casa pessoa em um
dicionario e todos os dicionarios em uma lista. No final mostre:
A) QUANTAS PESSOAS FORAM CADASTRADAS
B)A MEDIA DE IDADE DO GRUPO
C)UMA LISTA COM TODAS AS MULHERES
D) UMA LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MEDIA.'''

pessoas = dict()
grupo = list()
mulheres = list()
acimaMedia = list()
countPessoas = 0
somaIdade = 0
mediaIdade = 0


while True:
    pessoas['Nome'] = str(input("Nome: ").title())
    pessoas['Sexo'] = str(input("Sexo [M / F]: ").upper()[0])
    if pessoas['Sexo'] == "F":
        mulheres.append(pessoas['Nome'])
    while pessoas['Sexo'] not in "MF":
        print("Dado inserido inválido!")
        pessoas['Sexo'] = str(input("Sexo [M / F]: ").upper()[0])
    pessoas['Idade'] = int(input("Idade: "))
    grupo.append(pessoas.copy())
    countPessoas += + 1
    somaIdade += pessoas['Idade']
    mediaIdade = somaIdade / countPessoas
    continuar = str(input("Deseja continuar? [S / N]: ").upper()[0])
    while continuar not in "SN":
        print("Dado inserido inválido!")
        continuar = str(input("Deseja continuar? [S / N]: ").upper()[0])
    if continuar == "N":
        break
print(f"{countPessoas} pessoa(s) foram cadastradas")
print(f"A média de idade do grupo é de {mediaIdade:.2f} ano(s)")
print(f"As mulheres cadastradas são: {mulheres}")
if pessoas['Idade'] > mediaIdade:
    acimaMedia.append(pessoas['Nome'])
    acimaMedia.append(pessoas['Sexo'])
    acimaMedia.append(pessoas['Idade'])
print(f"As pessoas cadastradas com idade acima da média são: {acimaMedia}")



