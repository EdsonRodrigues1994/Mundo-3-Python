'''Faça um programa que tenha a função chamada escreva(), que receba um texto qualquer como parametro
e mostre yma mensagem com tamanho adaptável'''

def escreva(msg):
    linha = len(msg)
    print("~" * linha)
    print(msg)
    print("~" * linha)

escreva("Olá mundo!!!!")
escreva("testando tamanhooooo")