'''
O padrão de projeto Facade é um padrão estrutural que fornece uma 
interface simplificada para um conjunto mais complexo de classes
bibliotecas ou subsistemas. Ele atua como uma fachada (fachada) 
que oculta a complexidade subjacente e fornece uma interface única 
e simplificada para o cliente.
'''
# Acessando multiplos pacotes ou pasta
# Padrão de projetos facade
from pacote_03 import soma, subtracao

print('Soma: ', soma(3000, 700))
print('Subtração: ', subtracao(200, 50))


# Explicação do uso de facade

'''
A pacote_03 pode ser uma coleção de módulos ou classes que implementam 
funcionalidades relacionadas à soma e subtração. O padrão Facade é aplicado porque 
você está importando essas funcionalidades diretamente do pacote pacote_03 em
vez de interagir diretamente com os módulos internos desse pacote. Isso fornece uma 
interface mais simplificada para o cliente (seu código) e oculta a complexidade interna do pacote.

Por exemplo, você não precisa se preocupar com a implementação específica de 
soma e subtracao em pacote_03; você apenas usa essas funções conforme 
necessário.

'''
