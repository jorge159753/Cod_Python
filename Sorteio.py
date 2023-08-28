import random

def sorteio():
    num_sorteados = random.sample(range(100), k=6)
    return num_sorteados


entrada = input('Dejesa sortear os números da Mega-Sena? [S/N]')
if entrada == 'S':
    numeros_mega_sena = sorteio()
    numeros_mega_sena = sorted(numeros_mega_sena)           #Essa função "sorted()", ela faz os números se ordenarem de forma crescente.
    print("Os números sorteados foi:", numeros_mega_sena)
else:
    print('FIM')
