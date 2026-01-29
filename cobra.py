"""
Snake, jogo clássico de arcade.

Este jogo está parcialmente implementado.
Seu objetivo é compreender o funcionamento do código
e completar ou melhorar os trechos indicados com TODO,
para que fique funcionalmente semelhante ao jogo
presente no pacote freegames.

Depois, você deverá resolver os desafios propostos abaixo:

1. Como tornar a cobra mais rápida ou mais lenta?
2. Como fazer a cobra atravessar as bordas da tela?
3. Como fazer a comida se mover?
4. Alterar o jogo para que a cobra responda a cliques do mouse.
5. Exibir a pontuação na tela para o jogador, conforme a cobra come
as comidas.
6. Identificar jogador em cada rodada. Qual o nome do jogador que vai iniciar um jogo?
7. Armazenar jogador e suas pontuações em arquivo. Ao final do jogo, armazenar em arquivo
o nome do jogador que jogou e sua respectiva pontuação na rodada.
8. Listar jogadores e suas pontuações. Exibir no terminal uma lista de todos os jogadores
que jogaram o jogo com suas respectivas pontuações.

Leia o código com atenção antes de começar.
"""


from random import randrange
from turtle import *

from freegames import square, vector

# -------------------------
# Estado inicial do jogo
# -------------------------

comida = vector(0, 0)
cobra = [vector(10, 0)]
direcao = vector(0, -10)

# -------------------------
# Funções auxiliares
# -------------------------

def mudar_direcao(x, y):
    """Altera a direção do movimento da cobra."""
    direcao.x = x
    direcao.y = y

def dentro_limites(cabeca):
    """Retorna True se a cabeça estiver dentro da área do jogo."""
    return -200 < cabeca.x < 190 and -200 < cabeca.y < 190


# -------------------------
# Lógica principal do jogo
# -------------------------
def posicao_comida():
    comida.x = randrange(-15, 15) * 10
    comida.y = randrange(-15, 15) * 10
    ontimer(posicao_comida, 7000)
    
def mover():
    """Move a cobra um passo à frente."""
    cabeca = cobra[-1].copy()
    cabeca.move(direcao)

    # TODO: 
    # Extraia `cabeca in cobra` para uma função
    if not dentro_limites(cabeca) or cabeca in cobra:
        square(cabeca.x, cabeca.y, 9, 'red')
        update()
        return

    cobra.append(cabeca)

    if cabeca == comida:
        cobra.append(cabeca)
        print('Tamanho da cobra:', len(cobra))
        
        # Nova posição aleatória para a comida
        comida.x = randrange(-15, 15) * 10
        comida.y = randrange(-15, 15) * 10
    else:
        # TODO:
        for segmento in cobra:
            cobra.pop(0)

    clear()

    # Desenho da cobra
    for segmento in cobra:
        square(segmento.x, segmento.y, 13, 'black')

    # Desenho da comida
    square(comida.x, comida.y, 13, 'green')

    update()

    ontimer(mover, 70)


# -------------------------
# Configuração da janela
# -------------------------

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

onkey(lambda: mudar_direcao(10, 0), 'Right')
onkey(lambda: mudar_direcao(-10, 0), 'Left')
onkey(lambda: mudar_direcao(0, 10), 'Up')
onkey(lambda: mudar_direcao(0, -10), 'Down')

mover()
posicao_comida()

mainloop()