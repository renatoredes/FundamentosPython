# Funções com parâmetros

'''
Em Python, você pode criar funções que aceitam parâmetros, que são valores 
fornecidos à função quando ela é chamada. Esses parâmetros são usados 
dentro da função para realizar operações ou retornar resultados.

Abaixo temos um exemplo simples de uma função que recebe dois parâmetros e 
retorna a soma deles:
'''

# Exemplo função somar recebendo 2 parametros


def somar(a, b):
    resultado = a + b
    return resultado


# Chamando a função e imprimindo o resultado
resultado_soma = somar(10, 20)  # arumento passado para os parâmetros
print(f"A soma é: {resultado_soma}")

# Podemos criar parâmetros de  diferentes tipos (inteiros, strings, listas, etc.)
