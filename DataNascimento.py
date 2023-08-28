def meses():
    mes_ano = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
    }
    return mes_ano

def dataNascimento(dia, mes, ano):
    mes_ano = meses()   #Puxa a função "def meses"
    nome_mes = mes_ano[mes] #A variavel "mes" esta sendo usado como chave para acessar o dicionario "mes_ano".
    saida = print(f'Você nasceu em {dia} de {nome_mes} de {ano}')
    return saida

dia = int(input("Dia que nasceu: "))
mes = int(input("Mês que nasceu, em sequência númerica: "))
ano = int(input("Ano que nasceu: "))

dataNascimento(dia, mes, ano)
