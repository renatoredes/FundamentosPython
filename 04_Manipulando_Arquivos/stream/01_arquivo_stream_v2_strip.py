# Leitura de arquivo utilizando estratégia Stream
arquivo = open('fundos_imobiliarios_v1.csv', encoding='utf-8')

# Itera sobre cada linha do arquivo
for registro in arquivo:
    # Remove espaços em branco extras do final de cada registro
    registro = registro.rstrip()
    # Divide a linha em colunas usando a vírgula como delimitador
    # remove espaços em branco extras e imprime os dados formatados
    colunas = [coluna.strip() for coluna in registro.split(',')]
    # Imprime os dados sem adicionar uma nova linha ao final
    print('codigo: {}, nome: {}'.format(*colunas), end='')

# Fecha o arquivo
arquivo.close()
