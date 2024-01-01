'''
with é usado para garantir a execução segura de código associado a recursos, como arquivos. 
Garante que, independentemente do que aconteça dentro do bloco, o recurso será fechado corretamente.

as arquivo: Associa o objeto de arquivo aberto a uma variável chamada arquivo. 
Isso permite que você se refira ao arquivo usando o nome arquivo dentro do bloco with.

dados. Aqui, estamos assumindo que o conteúdo do arquivo pode ser lido completamente 
sem problemas. Se o arquivo for grande, pode ser mais eficiente ler o conteúdo em partes.
'''


def ler_e_imprimir_arquivo(nome_arquivo):
    try:
        # Leitura de arquivo
        with open(nome_arquivo, encoding='utf-8') as arquivo:
            dados = arquivo.read()

        # Itera sobre cada linha do arquivo
        for registro in dados.splitlines():
            # Divide a linha em colunas usando a vírgula como delimitador e imprime os dados formatados
            print('codigo: {}, nome: {}'.format(*registro.split(',')))

    except FileNotFoundError:
        print(f'O arquivo "{nome_arquivo}" não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')


# Chama a função com o nome do arquivo desejado
ler_e_imprimir_arquivo('fundos_imobiliarios_v1.csv')
