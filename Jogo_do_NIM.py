USUARIO = "usuario"
COMPUTADOR = "computador"
RODADAS_CAMPEONATO = 3


def ler_inteiro(mensagem, mensagem_erro):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print(mensagem_erro)


def ler_inteiro_positivo(mensagem):
    while True:
        valor = ler_inteiro(mensagem, "Digite apenas números inteiros válidos.")
        if valor > 0:
            return valor
        print("Os valores devem ser maiores que zero.")


def computador_escolhe_jogada(n, m):
    limite = min(m, n)
    for retirada in range(1, limite + 1):
        if (n - retirada) % (m + 1) == 0:
            return retirada
    return limite


def usuario_escolhe_jogada(n, m):
    limite = min(m, n)
    while True:
        retirada = ler_inteiro(
            f"Quantas peças você quer retirar? (1 a {limite}): ",
            "Por favor, digite um número inteiro válido.",
        )
        if 1 <= retirada <= limite:
            return retirada
        print(f"Jogada inválida! Você deve escolher entre 1 e {limite} peças.")


def obter_configuracao_partida():
    n = ler_inteiro_positivo("Informe o número total de peças: ")
    m = ler_inteiro_positivo("Informe o número máximo de peças por jogada: ")
    return n, m


def definir_primeiro_jogador(n, m):
    if n % (m + 1) == 0:
        return USUARIO
    return COMPUTADOR


def anunciar_inicio(jogador_inicial):
    if jogador_inicial == COMPUTADOR:
        print("\nComputador começa!\n")
    else:
        print("\nVocê começa!\n")


def executar_turno(n, m, jogador_atual):
    if jogador_atual == COMPUTADOR:
        retirada = computador_escolhe_jogada(n, m)
        print(f"O computador retirou {retirada} peça(s).")
    else:
        retirada = usuario_escolhe_jogada(n, m)
        print(f"Você retirou {retirada} peça(s).")
    return retirada


def alternar_jogador(jogador_atual):
    if jogador_atual == COMPUTADOR:
        return USUARIO
    return COMPUTADOR


def exibir_resultado_final(vencedor):
    if vencedor == COMPUTADOR:
        print("O computador ganhou!\n")
    else:
        print("Você ganhou!\n")


def partida():
    n, m = obter_configuracao_partida()
    jogador_atual = definir_primeiro_jogador(n, m)
    anunciar_inicio(jogador_atual)

    while n > 0:
        retirada = executar_turno(n, m, jogador_atual)
        n -= retirada

        if n == 0:
            exibir_resultado_final(jogador_atual)
            return jogador_atual

        print(f"Agora restam {n} peça(s) na mesa.\n")
        jogador_atual = alternar_jogador(jogador_atual)


def campeonato():
    placar_usuario = 0
    placar_computador = 0

    for rodada in range(1, RODADAS_CAMPEONATO + 1):
        print(f"**** Rodada {rodada} ****\n")
        vencedor = partida()
        if vencedor == USUARIO:
            placar_usuario += 1
        else:
            placar_computador += 1

    print("**** Final do campeonato! ****\n")
    print(f"Placar: Você {placar_usuario} X {placar_computador} Computador\n")


def escolher_modo_de_jogo():
    while True:
        escolha = ler_inteiro("Digite 1 ou 2: ", "Digite apenas números inteiros válidos.\n")
        if escolha in (1, 2):
            return escolha
        print("Digite apenas 1 ou 2.\n")


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato\n")

    escolha = escolher_modo_de_jogo()
    if escolha == 1:
        print("\nVocê escolheu uma partida isolada!\n")
        partida()
        return

    print("\nVocê escolheu um campeonato!\n")
    campeonato()


if __name__ == "__main__":
    main()
