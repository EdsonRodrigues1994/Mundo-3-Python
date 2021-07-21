'''Faça um programa que tenha uma fução chamada area(),
que receba dimensoes de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''


def area(l, c):
    '''
    Função : Calculo de área
    :param l: largura
    :param c: comprimento
    :return: total
    Criado por Edson Rodrigues
    '''
    total = l * c
    print(f"A área do seu terreno {l} x {c} é de {total}m²")

print("Controle de terrenos")
print("-" * 30)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))

area(l, c)
help(area)