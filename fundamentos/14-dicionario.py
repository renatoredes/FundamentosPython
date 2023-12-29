# Dicionario
'''
Em Python, um dicionário (dict) é uma estrutura de dados que armazena pares chave-valor
Permitindo que você associe um valor a uma chave específica. Dicionários são úteis 
para armazenar e acessar dados de maneira eficiente, especialmente quando a identificação 
dos dados é feita por meio de chaves exclusivas.
'''
# Características principais de um dicionário em Python:
'''
Mutabilidade: Os dicionários são mutáveis, o que significa que 
você pode adicionar, modificar ou remover itens após sua criação.

Chaves Únicas: As chaves em um dicionário devem ser únicas. 
Cada chave é associada a um único valor.

Chaves e Valores de Diferentes Tipos: 
As chaves e os valores podem ser de diferentes tipos.
'''
# Exemplos:
'''
Aqui, o dicionário usuario armazena informações 
sobre um usuário, incluindo um sub-dicionário para o endereço.
'''
# Dicionário de informações de usuário
usuario = {
    "nome": "Alice",
    "idade": 28,
    "email": "alice@email.com",
    "endereco": {
        "rua": "Rua XYZ",
        "cidade": "São Paulo",
        "cep": "01234-567"
    }
}
print(usuario)

# Exemplo:Mapeamento de códigos de produtos para seus nomes
'''
Neste exemplo, o dicionário codigo_para_nome é utilizado 
para mapear códigos de produtos aos seus respectivos nomes.
'''
codigo_para_nome = {
    101: "Laptop",
    202: "Smartphone",
    303: "Fones de Ouvido",
    # ...
}

print(codigo_para_nome)