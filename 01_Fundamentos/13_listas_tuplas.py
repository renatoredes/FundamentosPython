# Listas e tuplas quais principais diferenças ?
'''
Listas e tuplas são duas estruturas de dados em Python 
que armazenam coleções de elementos. No entanto, existem 
Algumas diferenças fundamentais entre elas:
'''
# Lista (list):
'''
Mutabilidade:

1. Mutável: 
As listas são mutáveis, o que significa que você pode alterar.
Adicionar ou remover elementos após a criação da lista.

2. Sintaxe:
Utiliza colchetes [] para a criação: minha_lista = [1, 2, 3].

3. Métodos:
Oferece uma variedade de métodos embutidos para modificação 
como append(), extend(), insert(), remove(), e pop().

4. Uso:
Ideal quando você precisa de uma coleção de itens 
que pode ser alterada durante a execução do programa.
'''

# Tupla (tuple):
'''
1. Imutabilidade:
Imutável: As tuplas são imutáveis, ou seja, após a criação 
Não é possível adicionar, remover ou alterar elementos. 
Isso proporciona integridade aos dados.

2. Sintaxe:
Utiliza parênteses () para a criação: minha_tupla = (1, 2, 3).

3. Métodos:
Possui menos métodos embutidos em comparação com listas. 
pois não suporta operações que modificam os elementos.

4. Uso:
Indicada quando você tem uma coleção de itens que não precisa 
ser alterada, como coordenadas geográficas, valores constantes
Ou como uma forma de retornar múltiplos valores de uma função.
'''
# Exemplo Comparativo:
# Lista
minha_lista = [1, 2, 3]
minha_lista[0] = 4  # Lista é mutável
print(minha_lista)  # Saída: [4, 2, 3]

# Tupla
minha_tupla = (1, 2, 3)
# minha_tupla[0] = 4  # Isso resultaria em um erro, tupla é imutável
# Ou seja na posição [0] Eu não posso adicionar o valor 4
print(minha_tupla)  # Saída: (1, 2, 3)

# Quando Escolher Entre Lista e Tupla:
'''
Use Lista Quando:
 * Precisar de uma coleção mutável.
 * Planejar modificar, adicionar ou remover elementos 
   durante a execução do programa.

Use Tupla Quando:
 * Precisar de uma coleção imutável.  
 * Desejar garantir a integridade dos dados e evitar alterações
   inadvertidas.

'''
# Exemplo pratico contexto bancário
# Listas e tuplas podem ser aplicadas em diferentes situações
# Dependendo das necessidades específicas do sistema.

# Exemplos:

'''
Lista (list):
 Histórico de Transações:
 Em um sistema de gerenciamento de contas, você pode usar uma 
 lista para armazenar o histórico de transações de um cliente. 
 A lista seria atualizada sempre que ocorrer uma nova transação.
 '''
historico_transacoes = [
    {"data": "2023-01-15", "descricao": "Depósito", "valor": 1000.00},
    {"data": "2023-01-20", "descricao": "Retirada", "valor": -500.00},
    {"data": "2023-02-02", "descricao": "Pagamento", "valor": -200.00},
]
# Exibe mensagem no console a lista de historico_transacoes
print("--------------------------")
print(historico_transacoes) 

'''
Isso permite uma manipulação fácil dos dados de transações 
como adição, remoção ou consulta.
'''
# Lista de Contas Correntes:
'''
Você pode usar uma lista para armazenar informações sobre várias
contas correntes, incluindo dados do titular, saldo e status 
da conta.
'''
print("--------------------------")
contas_correntes = [
    {"titular": "João Silva", "saldo": 1500.00, "status": "Ativa"},
    {"titular": "Maria Oliveira", "saldo": 2500.00, "status": "Inativa"},
    # ...
]
'''
Isso permite uma gestão dinâmica da lista de contas
como adição de novas contas ou atualização de informações.
'''
# Exibe no console a lista contas_correntes
print(contas_correntes)
print("--------------------------")

# Tupla (tuple):
'''
Informações Fixas do Cliente:
 * Em situações em que as informações do cliente são fixas 
   e não devem ser alteradas, uma tupla pode ser apropriada.
'''
print("Essa tupla representa informações imutáveis do cliente.")
informacoes_cliente = ("João Silva", "123.456.789-00", "Rua XYZ, 123", "Cliente VIP")
print(informacoes_cliente)

# Dados de Câmbio Fixos:
'''
Se houver taxas de câmbio fixas que não devem ser modificadas 
durante a execução do programa, uma tupla pode ser usada.
'''
print('Isso garante que as taxas de câmbio permaneçam constantes.')
taxas_cambio = (("USD", "BRL", 5.50), ("EUR", "BRL", 6.30), ("JPY", "BRL", 0.048))
print(taxas_cambio)

# Considerações Gerais:
'''
Mutable vs. Immutable:

Ao escolher entre lista e tupla, considere se os dados devem ser 
modificáveis (lista) ou se devem permanecer constantes (tupla).

Desempenho:
Tuplas podem oferecer um desempenho ligeiramente melhor em certas 
situações devido à sua imutabilidade.

Semântica:
Use listas quando a ordem e a mutabilidade dos elementos 
são importantes. Use tuplas quando os dados devem ser imutáveis 
e representam uma única entidade.
'''

