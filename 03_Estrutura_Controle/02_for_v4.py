# mais exemplos com for

# Percorrer uma lista de nomes e imprimi no console
nomes = ['Renato','Patricia','Lucas','Beatriz']
for nome in nomes:
    print(nome)

# Este código utiliza o enumerate para iterar sobre uma 
#lista de nomes e imprimir cada nome junto com a sua posição na lista.
nomes = ['Renato','Patricia','Lucas','Beatriz']
for posicao, nome_ in enumerate(nomes):
    print(f'{posicao + 1})', nome_)
'''
nomes é uma lista que contém os nomes 'Renato', 'Patricia', 'Lucas' e 'Beatriz'.

O loop for utiliza a função enumerate para iterar sobre os elementos da lista nomes. 
A função enumerate retorna uma tupla contendo a posição (índice) e o valor do 
elemento atual na iteração.

posicao e nome_ são as variáveis que recebem a posição e o valor de cada 
elemento na lista, respectivamente.

Dentro do loop, a instrução print exibe a posição 
(índice + 1 para começar a contagem a partir de 1) e o nome associado a essa posição.

Neste código, utilizei uma f-string para formatar a saída da impressão. 
f-string permite incorporar expressões Python dentro de strings, tornando a 
formatação mais clara e concisa.

O resultado é a impressão de cada nome junto com a sua posição na lista:

1) Renato
2) Patricia
3) Lucas
4) Beatriz
'''