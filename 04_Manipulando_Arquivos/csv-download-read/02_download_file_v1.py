import os
import csv
from urllib import request


def download_and_read_file(url, local_path):
    try:
        # Cria a pasta local se não existir
        if not os.path.exists(local_path):
            os.makedirs(local_path)

        # Obtém o nome do arquivo a partir da URL
        file_name = os.path.join(local_path, url.split('/')[-1])

        # Baixa o arquivo e salva localmente
        with request.urlopen(url) as entrada, open(file_name, 'wb') as saida:
            print(f'Baixando o arquivo {file_name}...')
            saida.write(entrada.read())

        print(f'O arquivo foi baixado e salvo em {file_name}')

        # Lê o conteúdo do arquivo usando decode('latin1') e imprime
        with open(file_name, 'r', encoding='latin1') as arquivo:
            conteudo = arquivo.read()
            print(f'Conteúdo do arquivo:\n{conteudo}')

        # Utiliza csv.reader para processar o conteúdo do arquivo
        with open(file_name, 'r', encoding='latin1') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            for linha in leitor_csv:
                print(linha)

    except Exception as e:
        print(f'Ocorreu um erro: {e}')


if __name__ == '__main__':
    # URL do arquivo que você deseja baixar
    url = 'https://www12.senado.leg.br/transparencia/prestacao-de-contas/paginas/old-acoes-de-supervisao-controle-e-de-correicao-1/teste.csv/@@download/file/teste.csv'

    # Pasta local onde o arquivo será salvo
    local_path = './pasta_local'

    # Chama a função para realizar o download e processar o conteúdo com decode('latin1')
    download_and_read_file(url, local_path)
