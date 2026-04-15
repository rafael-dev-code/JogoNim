# Jogo do NIM em Python

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/status-Concluído-brightgreen)
![License](https://img.shields.io/badge/license-Free-lightgrey)

Implementação do clássico Jogo do NIM em Python, com suporte a partida única ou campeonato de 3 rodadas contra o computador.

## Sobre o Projeto

O Jogo do NIM é um jogo matemático de estratégia em que dois jogadores alternam turnos removendo peças de uma única pilha.

Este projeto foi desenvolvido com foco em:

- aplicação de lógica matemática
- estruturas de repetição e decisão
- validação de entrada do usuário
- organização do código em funções
- simulação de estratégia computacional

## Regras do Jogo

- O jogo inicia com `n` peças na mesa.
- Cada jogador pode remover entre `1` e `m` peças por turno.
- O jogador que retirar a última peça vence.

## Funcionalidades

- validação de entradas do usuário
- partida única
- campeonato com 3 rodadas
- controle automático de placar
- alternância automática de turnos
- estratégia matemática implementada

## Requisitos

- Python 3.x

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/akakecendo-creator/JogoNim.git
```

2. Acesse a pasta do projeto:

```bash
cd JogoNim
```

3. Execute o jogo:

```bash
python Jogo_do_NIM.py
```

No Windows, se necessário, você também pode usar:

```bash
py Jogo_do_NIM.py
```

## Como Jogar

Ao iniciar o programa, você escolhe entre:

- `1` para jogar uma partida isolada
- `2` para jogar um campeonato com 3 rodadas

Depois disso, o jogo solicita:

- o número total de peças
- o número máximo de peças que podem ser retiradas por jogada

Durante a partida, o jogador e o computador se alternam até que todas as peças sejam removidas.

## Exemplo de Execução

```text
Bem-vindo ao jogo do NIM! Escolha:

1 - para jogar uma partida isolada
2 - para jogar um campeonato

Digite 1 ou 2: 1

Você escolheu uma partida isolada!

Informe o número total de peças: 13
Informe o número máximo de peças por jogada: 3

Computador começa!
```

## Objetivos de Aprendizado

Este projeto é adequado para praticar:

- funções em Python
- estruturas condicionais e de repetição
- validação de dados de entrada
- decomposição de problemas
- lógica de jogos

## Licença

Este projeto está disponível para fins de estudo e prática.
