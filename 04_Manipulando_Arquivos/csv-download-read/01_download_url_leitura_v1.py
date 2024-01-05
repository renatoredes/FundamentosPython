import csv
from urllib import request


def read(url, num_linhas=10):
    with request.urlopen(url) as entrada:
        print('Baixando o CSV......')
        dados = entrada.read().decode('latin1')

        # Limita a visualização a um certo número de linhas
        print(f'Download realizado com sucesso!')
        for linha in dados.splitlines()[:num_linhas]:
            print(linha)

        # Pule uma linha para facilitar a visualização
        print('\n')

        # Mostra a interpretação dos dados
        for cidade in csv.reader(dados.splitlines(), delimiter='\t'):
            print(cidade)


if __name__ == '__main__':
    read('https://www12.senado.leg.br/transparencia/prestacao-de-contas/paginas/old-acoes-de-supervisao-controle-e-de-correicao-1/teste.csv/@@download/file/teste.csv')
