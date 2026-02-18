def computador_escolhe_jogada(n, m):
    for retirada in range(1, m + 1):
        if (n - retirada) % (m + 1) == 0:
            return retirada
    return min(m, n)

def usuario_escolhe_jogada(n, m):
    while True:
        try:
            retirada = int(input(f"Quantas peças você quer retirar? (1 a {min(m, n)}): "))
            if 1 <= retirada <= m and retirada <= n:
                return retirada
            else:
                print(f"Jogada inválida! Você deve escolher entre 1 e {min(m, n)} peças.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

def partida():
    # Solicita valores iniciais
    while True:
        try:
            n = int(input("Informe o número total de peças: "))
            m = int(input("Informe o número máximo de peças por jogada: "))
            if n > 0 and m > 0:
                break
            else:
                print("Os valores devem ser maiores que zero.")
        except ValueError:
            print("Digite apenas números inteiros válidos.")

    # Define quem começa
    if n % (m + 1) == 0:
        vez_computador = False
        print("\nVocê começa!\n")
    else:
        vez_computador = True
        print("\nComputador começa!\n")

    # Loop do jogo
    while n > 0:
        if vez_computador:
            retirada = computador_escolhe_jogada(n, m)
            print(f"O computador retirou {retirada} peça(s).")
        else:
            retirada = usuario_escolhe_jogada(n, m)
            print(f"Você retirou {retirada} peça(s).")

        n -= retirada

        if n > 0:
            print(f"Agora restam {n} peça(s) na mesa.\n")
        else:
            if vez_computador:
                print("O computador ganhou!\n")
                return "computador"
            else:
                print("Você ganhou!\n")
                return "usuario"

        vez_computador = not vez_computador

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato\n")

    while True:
        try:
            escolha = int(input("Digite 1 ou 2: "))
            if escolha == 1:
                print("\nVocê escolheu uma partida isolada!\n")
                partida()
                break
            elif escolha == 2:
                print("\nVocê escolheu um campeonato!\n")
                placar_usuario = 0
                placar_computador = 0
                for rodada in range(1, 4):
                    print(f"**** Rodada {rodada} ****\n")
                    vencedor = partida()
                    if vencedor == "usuario":
                        placar_usuario += 1
                    else:
                        placar_computador += 1
                print("**** Final do campeonato! ****\n")
                print(f"Placar: Você {placar_usuario} X {placar_computador} Computador\n")
                break
            else:
                print("Digite apenas 1 ou 2.\n")
        except ValueError:
            print("Digite apenas números inteiros válidos.\n")

# Inicia o jogo
main()
