'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade de digitação de um número
de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''


def leiaInt(msg):

    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("Por favor, digite um número inteiro válido.")
            continue
        except (KeyboardInterrupt):
            print("Usuário preferiu não digitar esse número.")
            return 0
        else:
            return n


def leiaFloat(msg):

    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print("Por favor, digite um número inteiro válido.")
            continue
        except (KeyboardInterrupt):
            print("Usuário preferiu não digitar esse número.")
            return 0
        else:
            return n


n1 = leiaInt("Digite um Inteiro: ")
n2 = leiaFloat("Digite um Real: ")
print(f"O valor inteiro digitado foi {n1} e o real {n2}")