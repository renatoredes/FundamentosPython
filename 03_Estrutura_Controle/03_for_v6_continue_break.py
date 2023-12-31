# for utilizando break e continue em um loop

# Quebra de linha
print('Exemplo: 1')

# Este é um loop for que itera sobre números de 1 a 10 (inclusive)
for numero in range(1, 11):
    # Verifica se o número atual é par
    if numero % 2 == 0:
        # Se for par, utiliza o 'continue' para pular para a próxima iteração do loop
        continue
    # Se o número não for par, imprime o número
    print(numero)

# Quebra de linha
print()
# Quebra de linha
print('Exemplo: 2')

# Este é um loop for que itera sobre números de 1 a 10 (inclusive)
for numero in range(1, 11):
    # Verifica se o número atual é ímpar
    if numero % 2 != 0:
        # Se for ímpar, utiliza o 'continue' para pular para a próxima iteração do loop
        continue
    # Se o número não for ímpar (ou seja, se for par), imprime o número
    print(numero)

# Exemplo com break
print('Exemplo: 3')

# Inicia um loop que itera sobre números de 1 a 19
for numero in range(1, 20):
    # Verifica se o número atual é maior que 5
    if numero > 5:
        # Se for maior que 5, utiliza o 'break' para interromper o loop
        break
    # Imprime o número encontrado
    print(numero)
