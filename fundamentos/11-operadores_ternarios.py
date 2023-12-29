# Operadores Ternários
'''
Os operadores ternários são uma forma compacta de escrever
expressões condicionais. Eles são usados para retornar
um valor diferente com base em uma condição.

A sintaxe de um operador ternário é a seguinte:

<condição> ? <valor_verdadeiro> : <valor_falso>

O operador ternário é avaliado da esquerda para a direita. 
A condição é avaliada primeiro.
Se a condição for verdadeira, o valor_verdadeiro é retornado. 
Caso contrário, o valor_falso é retornado.
'''
# Exemplos
'''
Aqui estão alguns exemplos de como usar
operadores ternários em Python:
'''
# Exemplo 1
# O seguinte código verifica se um número é maior que 10:
numero = 11
mensagem = "O Número é maior que 10" if numero > 10 else "O número não é maior que 10"
# Este código irá imprimir o seguinte: O número é maior que 10
print(mensagem)
# Exemplo 2
'''
O seguinte código atribui o valor "par" ou "ímpar"
a uma variável, dependendo do resto da divisão do número por 2:
'''
numero = 15

paridade = "par" if numero % 2 == 0 else "ímpar"
# Este código irá imprimir o seguinte: impar
print(paridade)

'''
A condição numero % 2 == 0 é avaliada primeiro. Se a condição for verdadeira, o valor "par" é retornado. Caso contrário, o valor "ímpar" é retornado.

No exemplo, o valor de numero é 15. O resto da divisão de 15 por 2 é 1, o que significa que o número não é divisível por 2 sem resto. Portanto, a condição numero % 2 == 0 é falsa e o valor "ímpar" é retornado.

Para obter o resultado "par", o valor de numero deve ser alterado para um número divisível por 2 sem resto. Por exemplo, se numero fosse alterado para 10, o resto da divisão por 2 seria 0 e a condição numero % 2 == 0 seria verdadeira. Portanto, o valor "par" seria retornado.
'''
numero = 10

paridade = "par" if numero % 2 == 0 else "ímpar"
# Este código irá imprimir o seguinte: par
print(paridade)
