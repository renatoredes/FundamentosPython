# Exemplo utilizando if elif else range
# Exemplo range verifica se o intervalo está dentro do range
def nota_coceito(valor):
    nota = float(valor)
    if nota < 0 or nota >10:
        return 'Nota inválida: A nota deve estar no intervalo de 0 a 10'
    elif nota in range(6, 11):
        return 'APROVADO'
    elif nota in range(0, 3):
        return 'Reprovado'
    elif nota in range(4,5):
        return 'Recuperação'
    else:
        return 'Nota inválida'