import os
import random

jogarNovamente= "s"
jogadas = 0
jogadas += 1
quemJoga= 2
maxJogadas= 9
vit= "n"
velha=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]

]

def tela():
    global velha
    global jogadas
    os.system("cls")
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("0:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("0:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print(f'Jogadas: {jogadas}')

def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas

    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            l = int(input("Linha: "))
            c = int(input("Coluna: "))

            if velha[l][c] == " ":
                velha[l][c] = "X"
                quemJoga = 1
                jogadas += 1
            else:
                print("Essa posição já está ocupada. Tente novamente.")
        except ValueError:
            print("Linha e(ou) coluna inválida")

def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas

    if quemJoga == 1 and jogadas < maxJogadas:
        while True:
            l = random.randrange(0,3)
            c = random.randrange(0,3)

            if velha[l][c] == " ":
                velha[l][c] = "O"
                quemJoga = 2
                jogadas += 1
                break

def vitoria():
    for i in range(3):
        if velha[i][0] == velha[i][1] == velha[i][2] != " ":
            return True
        if velha[0][i] == velha[1][i] == velha[2][i] != " ":
            return True
    if velha[0][0] == velha[1][1] == velha[2][2] != " ":
            return True
    if velha[0][2] == velha[1][1] == velha[2][0] != " ":
            return True
    
    if jogadas == maxJogadas:
        return "Empate"
    
    return False

while jogarNovamente == 's':
    tela()
    jogadorJoga()
    if vitoria():
        print("Jogador venceu!" if vit == "X" else "CPU venceu!" if vit == "O" else "Empate!")
        break

    tela()
    cpuJoga()
    if vitoria():
        print("Jogador venceu!" if vit == "X" else "CPU venceu!" if vit == "O" else "Empate!")
        break

tela()
