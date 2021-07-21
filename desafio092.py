'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os com idade
em um idcionário, se por acasoa  CPTS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar'''


from datetime import datetime

funcionario = dict()



funcionario['Nome'] = str(input("Nome: ").title())
funcionario['Nascimento'] = int(input("Ano de Nascimento: "))
dtAtual = datetime.now().year - funcionario['Nascimento']
funcionario['CTPS'] = int(input("Carteira de trabalho (0 não tem): "))
if funcionario['CTPS'] != 0:
    funcionario['Contratacao'] = int(input("Ano de contratação: "))
    funcionario['Salario'] = float(input("Salário: "))
    funcionario['aposentadoria'] = dtAtual + ((funcionario['Contratacao'] + 35) - datetime.now().year)
    print(f"Nome tem o valor {funcionario['Nome']}")
    print(f"Idade tem o valor {dtAtual}")
    print(f"Ctps tem o valor {funcionario['CTPS']}")
    print(f"Contratação tem o valor {funcionario['Contratacao']}")
    print(f"Salário tem o valor {funcionario['Salario']:.2f}")
    print(f"Aposentadoria tem o valor {funcionario['aposentadoria']}")
else:
    print(f"Nome tem o valor {funcionario['Nome']}")
    print(f"Idade tem o valor {dtAtual}")
    print(f"Ctps tem o valor {funcionario['CTPS']}")
















