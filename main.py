import pygame

pygame.init()
relogio = pygame.time.Clock()

tamanho = (1200, 500)
tela = pygame.display.set_mode(tamanho)

pygame.display.set_caption("Homeless Walker")
dt = 0

# Carrega a spritesheet para nosso projeto
folhaSpritesIdle = pygame.image.load("assets/Homeless_1/Idle_2.png").convert_alpha()
folhaSpritesWalk = pygame.image.load("assets/Homeless_1/Walk.png").convert_alpha()
folhaSpritesJump = pygame.image.load("assets/Homeless_1/Jump.png").convert_alpha()

# Define os frames
framesIdle = []
framesWalk = []
framesJump = []

for i in range(11):
    frame = folhaSpritesIdle.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    framesIdle.append(frame)

for i in range(8):
    frame = folhaSpritesWalk.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    framesWalk.append(frame)

for i in range(16):
    frame = folhaSpritesJump.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    framesJump.append(frame)

# Variaveis da animação do personagem parado
indexFrameIdle = 0
tempoAnimacaoIdle = 0.0
velocidadeAnimacaoIdle = 5

# Variaveis da animação do personagem andando
indexFrameWalk = 0
tempoAnimacaoWalk = 0.0
velocidadeAnimacaoWalk = 10

# Variaveis da animação do personagem pulando
indexFrameJump = 0
tempoAnimacaoJump = 0.0
velocidadeAnimacaoJump = 10

# Retangulo do personagem
personagemRect = framesIdle[0].get_rect(midbottom=(100, 480))

gravidade = 1
direcaoPersonagem = 1
estaAndando = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    tela.fill((255, 255, 255))

    # Atualiza a animação do personagem parado
    tempoAnimacaoIdle += dt

    # Verifica se o tempo de animação do personagem parado é maior ou igual ao tempo de animação
    if tempoAnimacaoIdle >= 1 / velocidadeAnimacaoIdle:
        # Atualiza o frame do personagem parado
        indexFrameIdle = (indexFrameIdle + 1) % len(framesIdle)
        tempoAnimacaoIdle = 0.0

    # Atualiza a animação do personagem andando
    tempoAnimacaoWalk += dt
    
    # Verifica se o tempo de animação do personagem andando é maior ou igual ao tempo de animação
    if tempoAnimacaoWalk >= 1 / velocidadeAnimacaoWalk:
        # Atualiza o frame do personagem andando
        indexFrameWalk = (indexFrameWalk + 1) % len(framesWalk)
        tempoAnimacaoWalk = 0.0

    # Atualiza a animação do personagem pulando
    tempoAnimacaoJump += dt

    # Verifica se o tempo de animação do personagem pulando é maior ou igual ao tempo de animação
    if tempoAnimacaoJump >= 1 / velocidadeAnimacaoJump:
        # Atualiza o frame do personagem pulando
        indexFrameJump = (indexFrameJump + 1) % len(framesJump)
        tempoAnimacaoJump = 0.0

    # Verifica se o personagem está andando
    estaAndando = False

    # Movimenta o personagem no eixo X
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        personagemRect.x -= 200 * dt # Movimenta o personagem para a esquerda
        direcaoPersonagem = -1
        estaAndando = True
    if teclas[pygame.K_RIGHT]:
        personagemRect.x += 200 * dt # Movimenta o personagem para a direita
        direcaoPersonagem = 1
        estaAndando = True
    if teclas[pygame.K_SPACE]:
        if personagemRect.centery == 330:
            gravidade = -50

    # Gravidade Aumenta
    gravidade += 3

    personagemRect.y += gravidade

    if personagemRect.centery >= 330:
        personagemRect.centery = 330

    # Desenha o personagem
    if gravidade < 0:
        tela.blit(framesJump[indexFrameJump], personagemRect)
    else:
        if estaAndando:
            if direcaoPersonagem == 1:
                tela.blit(framesWalk[indexFrameWalk], personagemRect)
            else:
                tela.blit(pygame.transform.flip(framesWalk[indexFrameWalk], True, False), personagemRect)
        else:
            if direcaoPersonagem == 1:
                tela.blit(framesIdle[indexFrameIdle], personagemRect)
            else:
                tela.blit(pygame.transform.flip(framesIdle[indexFrameIdle], True, False), personagemRect)

    pygame.display.update()
    dt = relogio.tick(60) / 1000