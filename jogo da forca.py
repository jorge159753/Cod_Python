def jogar_forca(palavra):
    tentativas = 3
    letras_corretas = []
    
    print("Jogo da Forca!")
    print("_ " * len(palavra))
    
    while tentativas > 0:
        letra = input("\nDigite uma letra: ").lower() #.lower() serve para transformar qualquer letra mesmo maiuscula em minuscula.
        
        if letra in palavra:
            letras_corretas.append(letra)
            print("Letra correta!")
        else:
            tentativas -= 1
            print(f"Letra incorreta! Você tem {tentativas} tentativas restantes.")
        
        palavra_mostrada = ""
        for letra_palavra in palavra:
            if letra_palavra in letras_corretas:
                palavra_mostrada += letra_palavra
            else:
                palavra_mostrada += "_ "
        
        print(palavra_mostrada)
        
        if palavra_mostrada == palavra:
            print("Parabéns! Você ganhou!")
            break
    
    if palavra_mostrada != palavra:
        print(f"\nVocê perdeu! A palavra era: {palavra}")

# Palavra a ser adivinhada
palavra_secreta = "python"

# Iniciar o jogo
jogar_forca(palavra_secreta)
