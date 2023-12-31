from random import randint
'''
random
fornece funcionalidades para geração de números aleatórios. 
Dentro desse módulo, existem várias funções que podem ser utilizadas 
para diferentes propósitos relacionados a aleatoriedade.
'''
# Utilizando módulo random
def sorteio():
    return randint(1, 6)

for n in range(1, 7):
    if n % 2 == 1:
        print(n)
        continue
    if sorteio() == n: # verifica se o resultado da função sorteio é igual a n
        print('ACERTOU', n)
        break
else:
    print('Não acertou o número!')

