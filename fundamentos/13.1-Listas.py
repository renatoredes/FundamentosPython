# Continuando com exemplo de lista
'''
No arquivo 13-ListasTuplas.py temos a lista: historico_transacoes
Aqui teremos exemplos de adicionar, atualizar e remover dados 
Da lista historico_transacoes
'''
# Lista historico_transacoes
historico_transacoes = [
    {"data": "2023-01-15", "descricao": "Depósito", "valor": 1000.00},
    {"data": "2023-01-20", "descricao": "Retirada", "valor": -500.00},
    {"data": "2023-02-02", "descricao": "Pagamento", "valor": -200.00},
]
print('Vai imprimir a lista historico_transacoes:')
print(' ')
print(historico_transacoes)
# Exemplos:
# Adicionando uma nova transação à lista
'''
Aqui eu criei uma lista mais também pode ser uma tupla
para adicionar os novos dados dentro da lista 
historico_transacoes.
'''
nova_transacao = ["2023-02-10", "Depósito", 800.00]
print('Vai imprimir a lista nova_transacao...')
print(' ')
print(nova_transacao)
print(' ')
print('Vai adicionar a lista nova_transacao dentro da lista historico_transacoes...')
print(' ')
historico_transacoes.append(nova_transacao)
print('Dados Adicionado..')
print(' ')
print('Agora vai imprimir os dados com a nova transação...')
print(' ')
print(historico_transacoes)
print(' ')