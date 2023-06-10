def reajuste(salario_atual):

    if salario_atual <= 280:
        valor_reajuste = salario_atual * 0.2
        print(f"Percentual aplicado foi de 20%\n"
              f"O Valor do aumento foi de: R$56 a mais.\n"
              f"Seu novo salario é de: R${salario_atual + valor_reajuste}")

    elif salario_atual <= 700:
        valor_reajuste = salario_atual * 0.15
        print(f"Percentual aplicado foi de 15%\n"
              f"O Valor do aumento foi de: R${valor_reajuste} a mais.\n"
              f"Seu novo salario é de: R${salario_atual + valor_reajuste}")

    elif salario_atual <= 1500:
        valor_reajuste = salario_atual * 0.10
        print(f"Percentual aplicado foi de 10%\n"
              f"O Valor do aumento foi de: R${valor_reajuste} a mais.\n"
              f"Seu novo salario é de: R${salario_atual + valor_reajuste}")

    elif salario_atual > 1500:
        valor_reajuste = salario_atual * 0.05
        print(f"Percentual aplicado foi de 5%\n"
              f"O Valor do aumento foi de: R${valor_reajuste} a mais.\n"
              f"Seu novo salario é de: R${salario_atual + valor_reajuste}")


salario_atual = float(input("Informe seu salario atual: "))

print(f"\nSeu salario atual era: R${salario_atual}")
print('='*20)

salario_reajuste = reajuste(salario_atual)