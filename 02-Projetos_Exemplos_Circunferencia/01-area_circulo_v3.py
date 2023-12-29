'''
Aqui, estamos importando apenas a constante 
do módulo math. Isso significa que podemos usar diretamente pi 
ao invés de math.pi no restante do código.
'''
from math import pi

# Utilizando função
'''
Esta é a definição de uma função chamada circulo. 
A função aceita um parâmetro chamado raio. 
Dentro da função, calculamos a área do círculo usando a fórmula 
π × raio2 π × raio 2 e imprimimos a mensagem.
'''
def circulo(raio):
# Imprimo me explique esse pedaço de código
    print('Área do círculo', pi * float(raio) **2)
# Recebendo dados do usuário
raio = input('Informe o raio: ')
'''
Finalmente, chamamos a função circulo passando o raio informado
pelo usuário como argumento. 
Isso executa a função, que calcula a área do círculo e 
imprime a mensagem com o resultado.
'''
circulo(raio)
