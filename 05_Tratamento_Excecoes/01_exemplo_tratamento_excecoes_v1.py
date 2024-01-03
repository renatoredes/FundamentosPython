def calcular_retorno_investimento():
    try:
        # Recebe do usuário o valor investido
        valor_investido = float(input("Digite o valor investido: "))

        # Recebe do usuário o valor da ação
        valor_acao = float(input("Digite o valor da ação: "))

        # Calcula a quantidade de ações compradas
        quantidade_acoes = valor_investido / valor_acao

        # Exibe o resultado 2f: Isso faz parte da formatação de strings em Python,
        print(f"\nVocê comprou {quantidade_acoes:.2f} ações com o valor investido de R${
              valor_investido:.2f}.")

    except ValueError:   # Exceção que pode ocorrer quando o usuário insere um valor que não pode ser convertido para um número.
        print("Erro: Por favor, digite valores numéricos válidos.")

    except ZeroDivisionError:
        print("Erro: O valor da ação não pode ser zero.")

    except Exception as e:
        print(f"Erro inesperado: {e}")

    finally:
        print("Obrigado por utilizar o calculador de retorno de investimento.")


# Chama a função principal
calcular_retorno_investimento()
