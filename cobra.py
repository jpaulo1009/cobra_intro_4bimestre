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
from turtle import onscreenclick

from freegames import square, vector

# -------------------------
# Estado inicial do jogo
# -------------------------

comida = vector(0, 0)
cobra = [vector(10, 0)]
direcao = vector(0, -10)

jogador = ""
rodada = 1
# -------------------------
# Funções auxiliares
# -------------------------
def inicio_jogo():
    global jogador
    jogador = textinput("Novo jogador", "Digite seu nome: ")

def clique(x, y):
    cabeca = cobra[0]

    dx = x - cabeca.x
    dy = y - cabeca.y

    if abs(dx) > abs(dy):
        nova = vector(10, 0) if dx > 0 else vector(-10, 0)
    else:
        nova = vector(0, 10) if dy > 0 else vector(0, -10)

    direcao.x = nova.x
    direcao.y = nova.y



def mudar_direcao(x, y):
    """Altera a direção do movimento da cobra."""
    direcao.x = x
    direcao.y = y


def dentro_limites(cabeca):
    """Retorna True se a cabeça estiver dentro da área do jogo."""
    return -200 < cabeca.x < 190 and -200 < cabeca.y < 190

def salvar_jogador(jogador):
    with open("listinha_pae", "a") as f:
        f.write(jogador + "\n")
# -------------------------
# Lógica principal do jogo
# -------------------------
def posicao_comida():
    comida.x = randrange(-15, 15) * 10
    comida.y = randrange(-15, 15) * 10
    ontimer(posicao_comida, 7000)

def mover():
    """Move a cobra um passo à frente."""
    global rodada
    
    cabeca = cobra[-1].copy()
    cabeca.move(direcao)

    if cabeca in cobra:
        square(cabeca.x, cabeca.y, 13, 'red')

    if not dentro_limites(cabeca):
        update()
        return

    cobra.append(cabeca)

    if cabeca == comida:
        print('Tamanho da cobra:', len(cobra))
        
        # Nova posição aleatória para a comida
        comida.x = randrange(-15, 15) * 10
        comida.y = randrange(-15, 15) * 10
    else:
        cobra.pop(0)
    
    clear()

    # Desenho da cobra
    for segmento in cobra:
        square(segmento.x, segmento.y, 13, 'black')

    # Desenho da comida
    square(comida.x, comida.y, 13, 'green')

    update()

    ontimer(mover, 70)

    salvar_jogador()


# -------------------------
# Configuração da janela
# -------------------------
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

inicio_jogo()

onkey(lambda: mudar_direcao(10, 0), 'Right')
onkey(lambda: mudar_direcao(-10, 0), 'Left')
onkey(lambda: mudar_direcao(0, 10), 'Up')
onkey(lambda: mudar_direcao(0, -10), 'Down')
onscreenclick(clique)

mover()
posicao_comida()

mainloop()