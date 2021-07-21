'''Aprimore o desafio anteiror mostrando no final:
A) A SOMA DE TODOS OS VALORES PARES DIGITADOS.
B)A SOMA DOS VALORES DA TERCEIRA COLUNA
C) O MAIOR VALOR DA SEGUNDA LINHA'''



matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = 0
somaCol = 0


for linha in range (0, 3):
    for coluna in range (0, 3):
        matriz[linha][coluna]= int(input(f"Digite um valor para [{linha}, {coluna}]: "))
for linha in range (0, 3):
    for coluna in range (0 ,3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")
        if matriz[linha][coluna] % 2 == 0:
            somaPar += matriz[linha][coluna]
    print()
print(f"A soma dos valores pares é: {somaPar}")
for linha in range (0, 3):
    somaCol += matriz[linha][2]
print(f"A soma da terceira coluna é: {somaCol}")

for coluna in range (0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f"O maior valor da segunda linha é: {maior}")

