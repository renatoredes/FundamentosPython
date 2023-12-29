'''
Os operadores lógicos AND, OR e NOT
têm os mesmos significados em português que em inglês.
'''
# Exemplo AND, OR, NOT
'''
AND: Retorna True se ambos os operandos forem True.
Em português, isso significa E. Por exemplo, o seguinte
código retorna True porque ambos os operandos são True:
'''
a = True
b = True

print(a and b)  # True

"""
OR: Retorna True se pelo menos um dos operandos for True.
Em português, isso significa Ou. Por exemplo,
o seguinte código retorna True porque pelo menos
um dos operandos é True:
"""
a = True
b = False

print(a or b)  # True
'''
NOT: Retorna o valor lógico oposto do operando.
Em português, isso significa Não. Por exemplo,
o seguinte código retorna False porque o operando é True:
'''
a = True

print(not a)  # False
