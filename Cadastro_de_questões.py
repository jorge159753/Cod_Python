questoes_obj = []
print("Insira abaixo as questões que dejesa e seuas respectivas respostas:: ")

i = 0
while True:
    i += 1
    
    questao = input(f'{i} - Questão: ')
    respostas = input("Respostas: ")
    resp_corrreta = input("Informe a respsota certa: ")
    print("= ="*30)


    questoes = {
        "Questões add": questao,
        "Respostas": respostas,
        "Resposta_certa": resp_corrreta
    }
    
    questoes_obj.append(questoes)
    
    sistema = input("Dejesa adicionar mais uma questão? \nCaso não queria, basta digitar 'NÃO'")
    print("= ="*30)
    if sistema == 'Não' or sistema == 'n':
        break
    else:
        continue

print("Qual a resposta para a/as perguntas a seguir:")
print("-"*30)

acertos = 0
erros = 0
for questoes in questoes_obj:
    print(f'f{(questoes["Questões add"])}')
    print(f'Qual a resposta? \n{(questoes["Respostas"])}')
    resposta_usuario = input("-> ")
    print("-=-" *30)
    if questoes["Resposta_certa"].upper() == resposta_usuario:
        acertos += 1
    else:
        erros += 1

print(f'Você acertou um total de {acertos}\n'
      f'E errou um total de {erros}.')
