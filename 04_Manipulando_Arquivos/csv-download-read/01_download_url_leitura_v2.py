import csv
from urllib import request
from io import StringIO


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o CSV......')
        dados = entrada.read().decode('latin1')

        # Corrigir delimitador para ponto e vírgula
        arquivo_csv = csv.reader(
            StringIO(dados.replace(';;;;;', '')), delimiter=';')

        for linha in arquivo_csv:
            print(linha)


if __name__ == '__main__':
    read('https://www12.senado.leg.br/transparencia/prestacao-de-contas/paginas/old-acoes-de-supervisao-controle-e-de-correicao-1/teste.csv/@@download/file/teste.csv')
