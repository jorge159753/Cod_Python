def prestacoes(valor_total, parcelas):
    valor_por_prestacao = valor_total/parcelas

    return valor_por_prestacao

def multa(dias, valor_por_prestacao_juros):
    valor_por_prestacao_juros += valor_por_prestacao_juros * 0.3 + dias * 0.01
    valor_por_prestacao_juros = int(valor_por_prestacao_juros)
    return valor_por_prestacao_juros 

valor_total = int(input("Informe o valor original do produto: "))
parcelas = int(input("Informe em quantas parcelas quer dividir: "))

valor_da_prestacao_esperado = prestacoes(valor_total, parcelas)

qtdParcelas = parcelas

while qtdParcelas > 0:

    sistema = input("\nVocê atrasou na data de pagamento das prestações? [S/N]: ")
    if sistema == 'S':
        dias = int(input("* Quantos dias de atraso? "))
        if dias > 0:
            valor_por_prestacao_juros_esperado = multa(dias, valor_da_prestacao_esperado)
            print(f'O valor de cada prestação com essa multa fica R${valor_por_prestacao_juros_esperado}\n')

            while True:  
                valor_da_prestacao_pagar_juros = valor_por_prestacao_juros_esperado

                valor_da_prestacao_pagar = int(input(f' -> Valor a pagar nesta prestacção é R${valor_por_prestacao_juros_esperado}: '))
                if valor_da_prestacao_pagar == valor_da_prestacao_pagar_juros:
                    qtdParcelas -= 1
                    if qtdParcelas == 0:
                        print("-=" * 15)
                        print("Você pagou todas as prestações.")
                        print("-=" * 15)
                    else:
                        print("Pagamento aceito.")
                        break
                else:
                    print("!!! Valor informado não compativel com a prestação atual. !!!")
    else:
        valor_da_prestacao_esperado = prestacoes(valor_total, parcelas)

        valor_da_prestacao = int(input(f' -> Valor a pagar nesta prestacção é R${valor_da_prestacao_esperado}: '))

        if valor_da_prestacao == valor_da_prestacao_esperado:
            qtdParcelas -= 1
            if qtdParcelas == 0:
                print("-=" * 15)
                print("Você pagou todas as prestações.")
                print("-=" * 15)
        else:
            print("!!! Valor informado não compativel com a prestação atual. !!!")

print(" ")
print("-=-" * 15)
print(f'Valor total do produto foi de R${valor_total}\n\n')
print("-" * 15)
print(f'Valor de cada prestação foi de R${valor_da_prestacao_esperado}\n\n')
print("-" * 15)
print(f'Quantidades de prestações feitas pelo usúario: {parcelas} prestações')
