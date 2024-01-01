# Leitura de arquivo utilizando estratégia Stream
arquivo = open('fundos_imobiliarios_v1.csv', encoding='utf-8')
# Itera sobre cada linha do arquivo
# Isso aproveita a capacidade de iterar
# diretamente sobre o objeto arquivo, o que é eficiente
# para grandes conjuntos de dados.
for registro in arquivo:
    # Divide a linha em colunas usando a vírgula como delimitador e imprime os dados formatados
    print('codigo: {}, nome: {}'.format(*registro.split(',')))
# Fecha o arquivo
arquivo.close()
