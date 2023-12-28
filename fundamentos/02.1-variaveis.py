'''
Para declarar uma variável em Python, basta atribuir um valor
a ela utilizando o operador de atribuição =.
Por exemplo, para declarar uma variável
chamada idade e atribuir o valor 25, escrevemos:
'''
idade = 25

# A sintaxe de declaração de variáveis é a seguinte:
# <nome_da_variável> = <valor_da_variável>
'''
O nome da variável deve começar com uma letra
(maiúscula ou minúscula) ou com o caractere de sublinhado (_).
O nome da variável pode conter letras, números e o caractere de sublinhado.
'''
# Exemplos:

# 1 Declaração de Variáveis:
# Variável inteira
idade = 35
print(idade)
# Variável de ponto flutuante
altura = 1.70
print(altura)
# Variável de texto (string)
nome = "Renato"
print(nome)
# Variável booleana
tem_carro = True
print(tem_carro)

# 2 Operações com Variáveis:
# Operações matemáticas
soma = idade + 5
print(soma)
media = (idade + 30) / 2
print(media)
# Concatenação de strings
saudacao = "Olá, " + nome + "!"
print(saudacao)
# Alteração de variável booleana
tem_carro = False
print(tem_carro)


# Imprimindo variáveis
print("Idade:", idade)
print("Altura:", altura)
print("Nome:", nome)

# Saída formatada
print(f"{nome} tem {idade} anos.")
