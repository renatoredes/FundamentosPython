from math import pi

# Utilizando função com retorno
def circulo(raio):
    return pi * float(raio) ** 2

# Solicitando ao usuário para inserir o raio
raio = input('Informe o raio: ')

# Calculando a área chamando a função circulo
area = circulo(raio)

# Exibindo a área calculada
print('Área do círculo:', area)
