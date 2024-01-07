# Trabalhando com escrita de arquivos
# len verifica se o arquivo tem 2 elementos a expectativa é que cada linha do arquivo CSV
# contenha dois elementos (um para o código e outro para o nome).

import csv


def processar_arquivo_csv(entrada, saida):
    try:
        with open(entrada, mode='r', encoding='utf-8') as arquivo_csv, open(saida, mode='w', encoding='utf-8', newline='') as arquivo_saida:
            leitor_csv = csv.reader(arquivo_csv)
            escritor_csv = csv.writer(arquivo_saida)

            # Escreve cabeçalho
            escritor_csv.writerow(['codigo', 'nome'])

            for linha in leitor_csv:
                # Verifica se a linha tem exatamente dois elementos
                if len(linha) == 2:
                    codigo, nome = linha
                    # Escreve a linha processada no arquivo de saída
                    escritor_csv.writerow([codigo, nome])
                else:
                    print(f'Linha ignorada: {linha}')

        print('Arquivo processado com sucesso!')

    except FileNotFoundError:
        print(f'O arquivo "{entrada}" não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')


# Chama a função com os nomes dos arquivos desejados
processar_arquivo_csv('fundos_imobiliarios_v1.csv',
                      'fundos_imobiliarios_2023.txt')
