# A linguagem de programação Python oferece três operadores lógicos:

# E - AND: Retorna True se ambos os operandos forem True.
# Ou - OR: Retorna True se pelo menos um dos operandos for True.
# NOT: Retorna o valor lógico oposto do operando.

# Aqui estão alguns exemplos de operadores lógicos em Python:
a = True
b = False

# AND que dizer E
print(a and b)  # False
print(not a and b)  # True

# OR que dizer Ou
print(a or b)  # True
print(not a or b)  # False

# NOT
print(not a)  # False
print(not b)  # True

# Os operadores lógicos podem ser usados para construir 
# expressões lógicas mais complexas. 
# Por exemplo, o seguinte código verifica 
# se um número é maior ou igual a 10 e menor ou igual a 20:
numero = 15
print(numero >= 10 and numero <= 20)  # True

# Os operadores lógicos também podem ser usados em estruturas condicionais, como if e elif. 
# Por exemplo, o seguinte código imprime "O número é maior que 10" se o número for maior que 10:
numero = 15

if numero > 10:
    print("O número é maior que 10")
