# Exemplo utilizando if elif else for
def nota_conceito():
    # Solicita ao usuário que informe a nota
    valor_informado = input('Digite a nota do aluno: ')

    # Converte a entrada para float
    nota = float(valor_informado)

    # Verifica se a nota está no intervalo válido
    if nota < 0 or nota > 10:
        return 'Nota inválida: A nota deve estar no intervalo de 0 a 10'
    
    # Caso especial: nota igual a 0
    if nota == 0:
        return 'Conceito E-'
    
    # Dicionário para mapear limites para conceitos
    conceitos = {10: 'A', 9.1: 'A-', 8.1: 'B', 7.1: 'B-', 6.1: 'C', 5.1: 'C-', 4.1: 'D', 3.1: 'D-', 2.1: 'E-', 1.1: 'E-'}
    
    # Verifica em qual intervalo a nota se encaixa
    for limite, conceito in conceitos.items():
        if nota >= limite:
            return f'Conceito {conceito}'

# Chama a função para execução
conceito_resultante = nota_conceito()

# Exibe o resultado
print(conceito_resultante)
