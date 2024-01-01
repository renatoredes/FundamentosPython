import pandas as pd

arquivo = pd.read_excel('fundos_imobiliarios_v1.xlsx')

# Lê os dados do arquivo Excel
dados = arquivo

# Acessa a coluna "codigo"
codigos = dados['Codigo']

# Acessa a coluna "Nome"
nomes = dados['Nome']

# Imprime os códigos e nomes
for codigo, nome in zip(codigos, nomes):
    print(f'Codigo: {codigo}, Nome: {nome}')


# Observação o Github não suporta arquivo com extensão .xlsx por esse motivo não realizei deploy
# Para esse código funcionar na pasta xlsx renomei a extensão do arquivo csv para xlsx

# Ou faça o passo a passo abaixo
'''
Passos para esse código funcionar 

1° No seu notebook/pc abra uma planilha excel/ arquivo .xlsx
2° Adicione na planilha essas informações

Codigo	Nome
MXRF11	Alianza Trust Renda Imobiliaria Fundo Investimento Imobiliario
ALZR11	BTG PACTUAL LOGÍSTICA FUNDO DE INVESTIMENTO IMOBILIÁRIO
BTLG11	CSHG LOGÍSTICA FDO INV IMOB - FII
HGLG11	Kinea Renda Imobiliaria FII
KNRI11	Kinea Rendimentos Imobiliários Fundo de Investimento Imobiliário
KNCR11	Kinea Rendimentos Imobiliários Fundo de Investimento Imobiliário
XPLG11	XP LOG FUNDO DE INVESTIMENTO IMOBILIÁRIO
XPML11	XP Malls FII

3° Passo salve o arquivo com nome fundos_imobiliarios_v1.xlsx
4° Salvar no diretorio do projeto com o nome xlsx
5° Execulte esse codigo  e funcionará
'''
