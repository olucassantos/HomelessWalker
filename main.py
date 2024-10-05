import pygame

pygame.init()
relogio = pygame.time.Clock()

tamanho = (1200, 500)
tela = pygame.display.set_mode(tamanho)

pygame.display.set_caption("Homeless Walker")
dt = 0

# Carrega a spritesheet para nosso projeto
folhaSpritesIdle = pygame.image.load("assets/Homeless_1/Idle.png").convert_alpha()
folhaSpritesWalk = pygame.image.load("assets/Homeless_1/Walk.png").convert_alpha()

# Define os frames
framesIdle = []

for i in range(6):
    frame = folhaSpritesIdle.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    framesIdle.append(frame)

# Variaveis da animação do personagem parado
indexFrameIdle = 0
tempoAnimacaoIdle = 0.0
velocidadeAnimacaoIdle = 10

# Retangulo do personagem
personagemRect = framesIdle[0].get_rect(midbottom=(100, 480))

gravidade = 1

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

    # Movimenta o personagem no eixo X
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        personagemRect.x -= 200 * dt # Movimenta o personagem para a esquerda
    if teclas[pygame.K_RIGHT]:
        personagemRect.x += 200 * dt # Movimenta o personagem para a direita
    if teclas[pygame.K_SPACE]:
        if personagemRect.centery == 330:
            gravidade = -30
            
    # Gravidade Aumenta
    gravidade += 3

    personagemRect.y += gravidade

    if personagemRect.centery >= 330:
        personagemRect.centery = 330

    # Desenha o personagem
    tela.blit(framesIdle[indexFrameIdle], personagemRect)

    # Desenha um retangulo em volta do personagem
    pygame.draw.rect(tela, (0, 0, 0), personagemRect, 2)

    pygame.display.update()
    dt = relogio.tick(60) / 1000