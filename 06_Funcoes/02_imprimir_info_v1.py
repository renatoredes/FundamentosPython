# Funções com parâmetros

'''
Neste exemplo, a função imprimir_info tem três parâmetros, onde 
cidade tem um valor padrão definido como "Desconhecida". 
Isso significa que se você chamar a função sem fornecer um valor 
para cidade, ela usará o valor padrão.
'''


def imprimir_info(nome, idade, cidade="Desconhecida"):
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")


# Chamando a função com diferentes números de argumentos
imprimir_info("João", 35)
imprimir_info("Maria", 33, "Recife")
