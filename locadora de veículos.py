lista_clientes = []

while True: #Inicio de código, onde ele pede os dados dos clientes.
    nome = input("\nInforme seu nome: ")

    while True:
        sexo = input("Informe o sexo[F/M]: ")
        if sexo.upper() == 'F' or sexo.upper() == 'M':
            break
        else:
            print("Informação invalida, tente novamente.\n")

    placa_carro = input("Informe a placa do veiculo contratado: ")
    qts_km = int(input("Quantidade de KMs a ser rodados: "))
    qts_dias = int(input("Dias de contratação: "))

    print("\nCADASTRO REALIZADO COM SUCESSO!")

    clientes = {
        "Nome": nome,
        "Sexo": sexo,
        "Placa do carro": placa_carro,
        "Quant. de dias": qts_dias,
        "Quant. de Kms": qts_km
    }

    print('-=-'*30)
    lista_clientes.append(clientes)
    sistema = input("Dejesa alocar mais um cliente? \nSe sim, digite 'SIM' para continuar. \nCaso contrario digite 'NÃO'")
    print('-=-'*30)

    if sistema == 'Não' or sistema == 'não' or sistema == 'n':
        break
    else:
        continue

preco_total = 0
km_total = 0
for clientes in lista_clientes:
    km_total += int(clientes["Quant. de Kms"])
    preco_total = int(clientes["Quant. de dias"] * 70) + float(clientes["Quant. de Kms"] * 0.10) 
    print(' ')
    print(f'Nome: {(clientes["Nome"])}'
          f'\nSexo: {(clientes["Sexo"])}'
          f'\nPlaca de carro: {(clientes["Placa do carro"])}'
          f'\nDias contratados: {(clientes["Quant. de dias"])} dias'
          f'\nKms à rodar: {(clientes["Quant. de Kms"])} KM'
          f'\n\nValor total quer irá ser pago: {preco_total:.2f}')

for clientes in lista_clientes:
    if clientes["Sexo"].upper() == 'F' and clientes["Quant. de dias"] > 7:
        print(f'\nA cliente {(clientes["Nome"])} solicitou {(clientes["Quant. de dias"])} dias de contratação')



media = km_total / len(lista_clientes)
print(f'\nA média de Kms cadastrados foi de: {media:.2f} Kms')
