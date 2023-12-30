# Exemplos utilizando for
for i in range(1, 11):
    print('i = {}'.format(i))
print('....')

for j in range(11):
    print(f'j = {j}')

print('....')

# for encadeados explique esse código
'''
Este código utiliza dois loops for encadeados para imprimir a tabuada de 
multiplicação de 1 a 10. Vamos explicar passo a passo:
'''
#O primeiro loop for (for x in range(1, 11):) itera sobre os números 
#de 1 a 10, atribuindo cada valor a variável x.

#Dentro desse primeiro loop, há um segundo loop for (for y in range(1, 11):) 
#que itera novamente sobre os números de 1 a 10, atribuindo cada valor 
#a variável y.

#Dentro do segundo loop, há uma instrução print que imprime a multiplicação 
#de x e y junto com a expressão formatada.

for x in range(1, 11):
    for y in range(1, 11):
        print(f'{x} * {y} = {x * y}')

'''
O resultado é uma tabela de multiplicação de 1 a 10, onde cada linha 
representa uma multiplicação específica. Por exemplo, a primeira iteração 
do loop externo (x = 1) resultará nas seguintes linhas impressas:

1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
...
1 * 10 = 10
Esse processo se repete para cada valor de x de 1 a 10, gerando a tabela 
completa de multiplicação.

O uso de loops encadeados é comum quando você precisa percorrer 
todas as combinações possíveis de elementos de duas ou mais sequências. 
Neste caso, estamos gerando a tabela de multiplicação, onde cada elemento 
é o resultado de multiplicar um valor de x por um valor de y.
'''