'''
Se você estiver lidando com um arquivo muito grande 
e quiser ler o conteúdo em partes 
para evitar carregar todo o arquivo na memória de uma vez
podemos usar um loop para ler o arquivo em blocos (chunks). 

 a leitura em blocos é uma estratégia eficiente para 
 lidar com arquivos grandes.

"tamanho do bloco" refere-se à quantidade de dados que 
são lidos a cada iteração do loop. 
Em vez de ler o arquivo inteiro de uma vez, você lê uma parte 
(um bloco) de cada vez.

'''

# Exemplo ler arquivo em blocos de 4096 bytes
# Para partir a leitura em (bloco) a cada loop
nome_arquivo = 'fundos_imobiliarios_v1.csv'


def ler_arquivo_em_partes(nome_arquivo, tamanho_em_bloco=4096):
    try:
        with open(nome_arquivo, encoding='utf-8') as arquivo:
            while True:
                # Lê um bloco do arquivo
                bloco = arquivo.read(tamanho_em_bloco)

                # Se o bloco estiver vazio, chegamos ao final do arquivo
                if not bloco:
                    break
                # Processa o bloco (nesse exemplo, apenas imprime)
                print(bloco)
    except FileExistsError:
        print(f'O arquivo "{nome_arquivo}" não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')


# Chama a função arquivo desejado
ler_arquivo_em_partes(nome_arquivo)
