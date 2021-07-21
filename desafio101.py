'''Crie um programa que tenha uma funcao chamada voto() que vai receber como parametro o ano de nascimento
deuma pessoa, retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL OU OBRIGATORIO nas eleições.'''

from datetime import datetime


def voto(nasc):
    '''

    :param nasc: Recebe o resultado do input externo
    :return: Sem retorno
    '''

    ano = datetime.now().year - nasc

    if ano < 16:
        return f"Com {ano} anos: NÃO VOTA."
    elif ano < 18:
        return f"Com {ano} anos: VOTO OPCIONAL."
    elif ano < 65:
        return f"Com {ano} anos: VOTO OBRIGATÓRIO."
    else:
        return f"Com {ano} anos: VOTO OPCIONAL."


print("-" * 25)
nascimento = int(input("Em que ano você nasceu?"))
print(voto(nascimento))

