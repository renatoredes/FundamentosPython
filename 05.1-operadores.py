# Mais exemplos de operadores dessa vez
# Operador de Membro e Identidade
'''

Em Python, os operadores de membro (in e not in) 
e os operadores de identidade (is e is not) 
são usados para testar a associação entre objetos 
e para verificar se dois objetos têm a mesma identidade.
Exemplos de como esses operadores podem ser utilizados:
'''
# Operador de Membro (in e not in):
# Tradução em porgutguês:
# in siguinifica: in (pertence a)
# not in siguinifica not in (não pertence a)

# 1 Exemplo utilizando Listas:

# Verifica se um elemento está presente em uma lista
lista = [1, 2, 3, 4, 5]
# O número 3 está presente na lista ?
print(3 in lista)   # True
# O número 6 não está presente na lista
print(6 not in lista)   # True

# 2 Exemplo utilizando Strings:

# Verifica se uma substring está presente em uma string
texto = "Python é uma linguagem de programação"
# Python Está presente na substring ?
print("Python" in texto)   # True
# Java Não Está presente na substring ?
print("Java" not in texto)   # True
# Java Está presente na substring ?
print("Java" in texto)   # True

# Operador de Identidade (is e is not):
# is (é)
# is not (não é):

# 3 Exemplo Comparação de Objetos:
# Verifica se dois objetos têm a mesma identidade
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print('objetos: ')
print(x is y)   # False (são objetos diferentes)
print(x is z)   # True (mesma identidade porque z recebe o mesmo objeto)
print(x is not y)   # True (objetos diferentes)

# 4 Exemplo Comparação de Variáveis Nulas (None):

# Verifica se uma variável é None
variavel = None
print(variavel is None)   # True
print(variavel is not None)   # False

# Observação
'''
O operador is verifica a identidade dos objetos, enquanto o operador ==
verifica a igualdade dos valores. Use is com cuidado e geralmente prefira ==
para comparar valores, a menos que você tenha um motivo específico
para verificar a identidade dos objetos.
'''
