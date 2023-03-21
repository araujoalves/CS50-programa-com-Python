# Palavra secreta para o jogo da forca
palavra = 'python'

# Cria uma lista para armazenar as letras adivinhadas
letras_adivinhadas = ['_'] * len(palavra)

# Loop principal do jogo
tentativas = 0
while True:
    # Imprime a palavra atualizada com as letras adivinhadas
    print(' '.join(letras_adivinhadas))

    # Lê uma letra do jogador
    letra = input('Digite uma letra: ').lower()

    # Verifica se a letra já foi adivinhada antes
    if letra in letras_adivinhadas:
        print('Você já tentou essa letra. Tente outra.')
    else:
        # Verifica se a letra está na palavra
        acertou = False
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_adivinhadas[i] = letra
                acertou = True

        # A letra não está na palavra
        if not acertou:
            print('Essa letra não está na palavra.')
            tentativas += 1

            # Verifica se o jogador excedeu o número máximo de tentativas
            if tentativas == 6:
                print('Game over. A palavra era:', palavra)
                break

        # Verifica se o jogador adivinhou todas as letras da palavra
        if '_' not in letras_adivinhadas:
            print('Parabéns, você ganhou!')
            break


