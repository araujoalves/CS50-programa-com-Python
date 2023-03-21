# Cria um tabuleiro vazio
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Imprime o tabuleiro atual
def imprime_tabuleiro():
    print("   1   2   3")
    print("1: {} | {} | {}".format(tabuleiro[0][0], tabuleiro[0][1], tabuleiro[0][2]))
    print("  ---+---+---")
    print("2: {} | {} | {}".format(tabuleiro[1][0], tabuleiro[1][1], tabuleiro[1][2]))
    print("  ---+---+---")
    print("3: {} | {} | {}".format(tabuleiro[2][0], tabuleiro[2][1], tabuleiro[2][2]))

# Verifica se o jogo terminou em empate
def empate():
    for linha in tabuleiro:
        for elemento in linha:
            if elemento == " ":
                return False
    return True

# Verifica se o jogo terminou com um vencedor
def vencedor(jogador):
    # Verifica as linhas
    for linha in tabuleiro:
        if linha == [jogador, jogador, jogador]:
            return True

    # Verifica as colunas
    for coluna in range(3):
        if [tabuleiro[0][coluna], tabuleiro[1][coluna], tabuleiro[2][coluna]] == [jogador, jogador, jogador]:
            return True

    # Verifica as diagonais
    if [tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2]] == [jogador, jogador, jogador]:
        return True
    if [tabuleiro[0][2], tabuleiro[1][1], tabuleiro[2][0]] == [jogador, jogador, jogador]:
        return True

    return False

# Loop principal do jogo
jogador_atual = "X"
while True:
    # Imprime o tabuleiro
    imprime_tabuleiro()

    # Lê a jogada do jogador
    jogada = input("Jogador {}, digite a linha e coluna da sua jogada (exemplo: 1,2): ".format(jogador_atual))

    # Verifica se a jogada é válida
    if len(jogada) != 3 or jogada[1] != ",":
        print("Jogada inválida. Digite a linha e coluna separadas por vírgula.")
        continue

    linha = int(jogada[0]) - 1
    coluna = int(jogada[2]) - 1

    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        print("Jogada inválida. As linhas e colunas devem ser 1, 2 ou 3.")
        continue

    if tabuleiro[linha][coluna] != " ":
        print("Jogada inválida. Essa posição já está ocupada.")
        continue

    # Faz a jogada do jogador atual
    tabuleiro[linha][coluna] = jogador_atual

    # Verifica se o jogador atual vence

