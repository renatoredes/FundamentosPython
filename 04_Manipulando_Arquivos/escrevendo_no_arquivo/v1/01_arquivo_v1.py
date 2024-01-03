# Esse código realiza a escreita de um arquivo a partir da leitura
#  de um arquivo CSV
# as associa a variavel ao arquivo exemplo: arquivo_fundo.txt
# file = saida  faz a escrita dentro do arquivo
# fundos = registro.strip().split(','): Remove espaços em branco no início e no final da linha (strip())
# em seguida, divide a linha em colunas usando a vírgula como delimitador (split(',')).

with open('fundos_imobiliarios_v1.csv', encoding='utf-8') as arquivo:
    with open('fiis.txt', 'w', encoding='utf-8') as saida:
        for registro in arquivo:
            fundos = registro.strip().split(',')
            print('codigo: {}, nome: {}'.format(*fundos), file=saida)

if (arquivo.close):
    print('Arquivo já foi fechado!')
