# While True:

# função responsavel por gerar um valor aleatorio inteiro
from random import randint
numero_informado = -1
numero_secreto = randint(0,9)

#quando encontrar o valor secredo essa expressão passa a ser falsa
while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o número: '))
print('Numero secreto {} foi encontrado!'.format(numero_secreto))