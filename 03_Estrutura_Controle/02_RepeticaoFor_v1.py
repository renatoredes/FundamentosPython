# Exemplo: FOR
'''
Em Python, o laço de repetição for é utilizado para iterar sobre uma 
sequência (como uma lista, uma tupla, uma string, etc.) 
ou outro objeto iterável. O formato básico do laço for é o seguinte:

Exemplo de estrutura for:

for variavel in sequencia:
    Corpo do loop
    Código a ser executado em cada iteração

variavel: A variável que assume o valor de cada elemento na sequência a cada iteração.
sequencia: A sequência (ou objeto iterável) sobre a qual você está iterando.
Corpo do loop: O bloco de código que é executado para cada item na sequência.    
'''
print('') #Espaço no código
# Exemplo 1: Iterando sobre uma Lista
frutas = ['maçã', 'banana', 'laranja']

for fruta in frutas:
    print(fruta) #Este código imprimirá cada elemento da lista frutas em linhas separadas.

'''
Você também pode usar a função range para gerar uma sequência numérica 
e iterar sobre ela. Por exemplo:
'''
print('') #Espaço entre um exemplo e outro
for numero in range(5):# exime de 0 até 4
    print(numero)