# Exemplo utilizando if elif else

def nota_coceito(valor):
    nota = float(valor)
    if nota < 0 or nota >10:
        return 'Nota inválida: A nota deve estar no intervalo de 0 a 10'
    elif nota >9.1:
        return 'Conceito A'
    elif nota >=8.1:
        return 'Conceito A-'
    elif nota >=7.1:
        return 'Conceito B'
    elif nota >=6.1:
        return 'Conceito B-'
    elif nota >=5.1:
        return 'Conceito C'
    elif nota >=4.1:
        return 'Conceito C-'
    elif nota >=3.1:
        return 'Conceito D'
    elif nota >=2.1:
        return 'Conceito D-'  
    elif nota >=1.1:
        return 'Conceito E-'
    elif nota ==0:
        return 'Conceito E-'
    else:
        return 'Nota inválida'

if __name__ == '__main__':
    valor_informado = input('Nota do Aluno: ')
    conceito = nota_coceito(valor_informado)
    print(conceito)
