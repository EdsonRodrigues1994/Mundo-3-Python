'''Faça um programa que tenha uma função notas() que pode receber varias notas de alunos e vai retornar um dicionário com as seguintes informações:
QUANTIDADE DE NOTAS
A MAIOR NOTA
A MENOR NOTA
A MÉDIA DA TURMA
A SITUAÇÃO (OPCIONAL)'''


turma = list()
galera = dict()


def notas(*values, sit=False):
    '''

    :param values: Todos os valores de entrada que são recebidos.
    :param sit: Opcional, se verdadeira, traz a situação que o aluno se encontra referente sua média.
    :return: Dicionário com várias informações sobre a situação da turma.
    '''

    countmedia = 0
    menor = 0
    maior = 0
    total = 0
    if sit == False:
        for i in values:
            turma.append(i)
            countmedia += + 1
            total += i
            galera['Total: '] = countmedia
            if countmedia == 1:
                maior = i
                menor = i
            if i >= maior:
                maior = i
                galera['Maior: '] = maior
            if i <= menor:
                menor = i
                galera['Menor: '] = menor
            galera['media'] = total / countmedia
    else:
        for i in values:
            turma.append(i)
            countmedia += + 1
            total += i
            galera['Total: '] = countmedia
            if countmedia == 1:
                maior = i
                menor = i
            if i >= maior:
                maior = i
                galera['Maior: '] = maior
            if i <= menor:
                menor = i
                galera['Menor: '] = menor
            galera['media'] = total / countmedia
            if galera['media'] >= 7:
                galera['Situação: '] = "BOA"
            if galera['media'] < 7:
                galera['Situação: '] = "RAZOÁVEL"
            if galera['media'] < 5:
                galera['Situação: '] = "RUIM"

    print(galera)


notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
help(notas)

