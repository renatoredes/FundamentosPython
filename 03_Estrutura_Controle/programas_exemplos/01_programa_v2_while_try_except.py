# Jogo de Números Aleatórios

from random import randint
'''
random
fornece funcionalidades para geração de números aleatórios. 
Dentro desse módulo, existem várias funções que podem ser utilizadas 
para diferentes propósitos relacionados a aleatoriedade.

Adicionei from random import randint para importar 
apenas a função randint do módulo random.

Usei um loop while True para permitir que o 
usuário continue tentando até acertar.

Adicionei um bloco try-except para garantir que o 
usuário insira um número válido.

Usei break para sair do loop quando o usuário acerta.
'''
# Utilizando módulo random
def sorteio():
   return randint(1, 6)

numero_sorteado = sorteio()
print('O Número sorteado foi: ' +str(numero_sorteado))

numero = 0
# Utiliza um loop while para pedir ao usuário para digitar um número até que ele acerte
while True:
    # Utiliza um bloco try-except para garantir que o usuário insira um número válido
 try:
    numero = int(input('Digite um número entre 1 e 6: '))
 except ValueError:
   print('Por favor, digite um número válido.')
   continue # Utiliza continue para reiniciar o loop
 # Verifica se o número digitado é igual ao número sorteado
 if numero == numero_sorteado:
   print('Você Acertou!')
   break # Utiliza break para sair do loop se o usuário acertar
 else:
   print('Você não acertou. Tente novamente.')
print('O Número sorteado foi: ' +str(numero_sorteado))