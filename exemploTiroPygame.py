import pygame

TAMANHO_TELA = (800, 600)
ALTURA_CHAO = 485

pygame.init()
relogio = pygame.time.Clock()
tela = pygame.display.set_mode(TAMANHO_TELA)
pygame.display.set_caption("Exemplo de tiro")
dt = 0

# Carrega a imagem do jogador
folhaSpritesIdle = pygame.image.load("assets/Homeless_1/Idle_2.png").convert_alpha()

listFramesIdle = []

# Cria os frames do personagem na lista de listFramesIdle
for i in range(11):
    # Pega um frame da folha de sprites na posição i * 0, 0 com tamanho 128x128
    frame = folhaSpritesIdle.subsurface(i * 128, 0, 128, 128)

    # Redimensiona o frame para 2 vezes o tamanho original
    frame = pygame.transform.scale2x(frame)

    # Adiciona o frame na lista de listFramesIdle
    listFramesIdle.append(frame)

# Variaveis da animação do personagem parado
indexFrameIdle = 0 # Controla qual imagem está sendo mostrada na tela
tempoAnimacaoIdle = 0.0 # Controla quanto tempo se passou desde a última troca de frame
velocidadeAnimacaoIdle = 5 # Controlar o tempo de animação em relação ao tempo real (1 / velocidadeAnimacaoIdle)

# Retangulo do personagem na tela para melhor controle e posicionamento do personagem
personagemRect = listFramesIdle[0].get_rect(midbottom=(250, 480))
personagemColisaoRect = pygame.Rect(personagemRect.x, personagemRect.y, 80, 120)

gravidade = 1 # Gravidade do jogo, valor que aumenta a cada frame
direcaoPersonagem = 1 # Direção que o personagem está olhando (1 = Direita, -1 = Esquerda)
estaAndando = False # Define se o personagem está andando ou não

# Importa as imagens do plano de fundo
listBgImages = [
    pygame.image.load("assets/Apocalipse/Apocalypce4/Bright/bg.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Apocalypce4/Bright/rail&wall.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Apocalypce4/Bright/train.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Apocalypce4/Bright/columns&floor.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Apocalypce4/Bright/infopost&wires.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Apocalypce4/Bright/wires.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Apocalypce4/Bright/floor&underfloor.png").convert_alpha(),
]

listaBgVelocidades = [1, 3, 7, 9, 10, 15, 20] # Velocidades de cada imagem do plano de fundo

listaBgPosicoes = [0 for _ in range(len(listBgImages))] # Posições de cada imagem do plano de fundo

# Loop que redimensiona as imagens do plano de fundo
for i in range(len(listBgImages)):
    listBgImages[i] = pygame.transform.scale(listBgImages[i], TAMANHO_TELA)

# LOOP PRINCIPAL
while True:
    # Loop que verifica todos os eventos que acontecem no jogo
    for event in pygame.event.get():

        # Verifica se o evento é de fechar a janela
        if event.type == pygame.QUIT:
            pygame.quit() # Fecha o jogo
            exit() # Fecha o programa

    tela.fill((255, 255, 255)) # Preenche a tela com a cor branca

    # Desenha o plano de fundo
    for i in range(len(listBgImages)):
        # Desenha a imagem do plano de fundo que está na tela
        tela.blit(listBgImages[i], (listaBgPosicoes[i], 0))

    # ANIMAÇÃO DO PERSONAGEM PARADO 
    # Soma o tempo que se passou desde o último frame
    tempoAnimacaoIdle += dt

    # Verifica se o tempo de animação do personagem parado é maior ou igual ao tempo de animação
    if tempoAnimacaoIdle >= 1 / velocidadeAnimacaoIdle:
        # Atualiza o frame do personagem parado de acordo com a lista de frames
        indexFrameIdle = (indexFrameIdle + 1) % len(listFramesIdle)
        tempoAnimacaoIdle = 0.0 # Reseta o tempo entre os frames

    # Pega as teclas que foram pressionadas
    listTeclas = pygame.key.get_pressed()


    # Gravidade Aumenta
    gravidade += 2

    # Atualiza a posição Y do personagem de acordo com a gravidade
    personagemRect.y += gravidade

    # Verifica se o personagem está no chão
    if personagemRect.centery >= ALTURA_CHAO:
        personagemRect.centery = ALTURA_CHAO

    personagemColisaoRect.midbottom = personagemRect.midbottom

    frame = listFramesIdle[indexFrameIdle]
    tela.blit(frame, personagemRect)
    
    pygame.display.update() # Atualiza a tela

    dt = relogio.tick(60) / 1000 # Define o tempo de cada frame em segundos