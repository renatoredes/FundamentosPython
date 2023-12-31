# Exemplo For utilizando dicionario
produto = {'MXRF11':10.57, 'ALZR11':117.64,'BTLG11':103.87,'HGLG11':161.99,'KNRI11':165.50,'KNCR11':104.55,'XPLG11':108.90,'XPML11':117.12}
 
for chave in produto.keys():
    print(chave)

for valor in produto.values():
    print(valor)

print('___________________')

#intera os itens do produto
for ticket, valor in produto.items():
    print(ticket,'=', valor)
'''
Resultado consolte

MXRF11 = 10.57
ALZR11 = 117.64
BTLG11 = 103.87
HGLG11 = 161.99
KNRI11 = 165.5
KNCR11 = 104.55
XPLG11 = 108.9
XPML11 = 117.12
'''