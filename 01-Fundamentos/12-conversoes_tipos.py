# Conversão de Tipos
'''
Em Python, a conversão de tipos (também conhecida como "type
casting") é a maneira de alterar o tipo de uma variável de um tipo para outro.
Exemplos comuns de conversão de tipos em Python:
'''
# 1. Conversão para Inteiro (int):
# Convertendo uma string para inteiro
numero_texto = '123'
numero_inteiro = int(numero_texto)
print(numero_inteiro) #Saida 123

# Convertendo um número de ponto flutuante para inteiro
numero_ponto_flutuante = 5.7
numero_inteiro = int(numero_ponto_flutuante)
print(numero_inteiro)  # Saída: 5

# 2. Conversão para Ponto Flutuante (float):
# Convertendo um inteiro para ponto flutuante
numero_inteiro = 42
numero_ponto_flutuante = float(numero_inteiro)
print(numero_ponto_flutuante)  # Saída: 42.0

# 3. Conversão para String (str):
# Convertendo um inteiro para string
numero_inteiro = 123
numero_texto = str(numero_inteiro)
print(numero_texto)  # Saída: "123"

# Convertendo um ponto flutuante para string
numero_ponto_flutuante = 3.14
numero_texto = str(numero_ponto_flutuante)
print(numero_texto)  # Saída: "3.14"

# 4. Conversão ou Coerção Automática:
# Em algumas situações, a conversão pode ocorrer 
# automaticamente, por exemplo, durante operações mistas:
# Conversão automática de inteiro para ponto flutuante
resultado = 5 * 2.0
print(resultado)  # Saída: 10.0

# 5. Conversão de Tipos Compostos:
# Em listas, tuplas e dicionários, você pode converter 
# Entre esses tipos  usando as funções list(), tuple() e dict():

# Convertendo uma lista para tupla
lista = [1, 2, 3]
tupla = tuple(lista)
print(tupla)  # Saída: (1, 2, 3)

# Convertendo uma tupla para lista
tupla = (4, 5, 6)
lista = list(tupla)
print(lista)  # Saída: [4, 5, 6]
