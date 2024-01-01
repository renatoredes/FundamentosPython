# Esse código realiza a leitura de um arquivo CSV
def ler_e_imprimir_arquivo():
    arquivo = open('fundos_imobiliarios_v1.csv', encoding='utf-8')
    dados = arquivo.read()
    arquivo.close()
    for registro in dados.splitlines():
        print('codigo: {}, nome: {}'.format(*registro.split(',')))


print(ler_e_imprimir_arquivo())
