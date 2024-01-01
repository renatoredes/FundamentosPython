# Esse código realiza a leitura de um arquivo CSV
'''
abertura do arquivo
leitura e armazena na var. dados
fecha o arquivo após a leitura
Divide a string dados em linhas usando splitlines() 
e itera sobre cada linha. Cada linha representa um registro 
no arquivo CSV.

Para cada registro, divide a linha usando split(',') para separar os valores no CSV. 
Em seguida, utiliza o método format para imprimir os valores formatados. 
O *registro.split(',') desempacota os valores do registro.

Supondo que cada linha do CSV tenha dois 
campos (código e nome), a saída seria 

Esse código assume que o arquivo "fundos_imobiliarios.csv" 
contém linhas onde os valores estão separados por vírgula

Adicionei encoding='utf-8' ao abrir o arquivo 
indicando que a codificação a ser usada é UTF-8. 
Isso ajuda resolver problema de decodificação 
de caracteres especiais. 

'''
arquivo = open('fundos_imobiliarios_v1.csv', encoding='utf-8')
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
    print('codigo: {}, nome: {}'.format(*registro.split(',')))
