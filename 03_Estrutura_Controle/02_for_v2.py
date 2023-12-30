# Laço de Repetição utilizando for
#Exemplo 1: Iterando sobre uma Lista
frutas = ['maçã', 'banana', 'laranja']

for fruta in frutas:
    print(fruta)

# Exemplo 2: Calculando a Soma dos Números em uma Lista
'''
Neste exemplo, o código usa um laço for para percorrer cada número na lista 
numeros e calcular a soma total.
'''
numeros = [1,2,3,4,5]
soma = 0

for numero in numeros:
    soma += numero
print(f'A soma dos números é: {soma}')

#Exemplo 3: Iterando sobre uma String
mensagem = "Python é incrível!"

for caractere in mensagem:
    print(caractere)
'''
Neste exemplo, o código utiliza o método items() para iterar 
obre as chaves e valores de um dicionário.
'''
#Exemplo 5: Iterando sobre Dicionário
pessoa = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}
for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')