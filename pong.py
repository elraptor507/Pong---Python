#configuración inicial
import pygame
pygame.init()
ANCHO = 1378
ALTO = 775
pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("PONG")

#Reloj
reloj = pygame.time.Clock()

#Texto
fuente = pygame.font.Font(None, 250)

#Sonido
pygame.mixer.init()
sonido = pygame.mixer.Sound("Desktop/python/youtube/pong/pop.wav")

#bucle principal
bucle = True
jugador1 = 0
jugador2 = 0
tamaño = 100
espesor = 30
bolax = ANCHO//2
bolay = ALTO//2
bolavx = 0.5
bolavy = 0.5
radio = 20
puntaje = 0

while bucle:
    #boton de cerrar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bucle = False

    #Entrada del teclado
    teclado = pygame.key.get_pressed()
    if teclado[pygame.K_w]:
        jugador1 -= 1
        if jugador1 < 0:
            jugador1 = ALTO

    if teclado[pygame.K_s]:
        jugador1 += 1
        if jugador1 > ALTO:
            jugador1 = 0

    if teclado[pygame.K_UP]:
        jugador2 -= 1
        if jugador2 < 0:
            jugador2 = ALTO

    if teclado[pygame.K_DOWN]:
        jugador2 += 1
        if jugador2 > ALTO:
            jugador2 = 0

    #Regla del juego
    bolax += bolavx
    bolay += bolavy
    if bolax < radio or bolax + radio > ANCHO:
        bolavx *= -1
        puntaje -= 1
        sonido.play()
    if bolay < radio or bolay + radio > ALTO:
        bolavy *= -1
        sonido.play()
    if bolax == 30 + espesor + radio and ((bolay > jugador1 - radio and bolay < jugador1 + tamaño + radio) or (bolay > jugador1 - ALTO - radio and bolay < jugador1 - ALTO + tamaño + radio)):
        bolavx *= -1
        puntaje += 1
        sonido.play()
    if bolax == ANCHO - 30 - espesor - radio and ((bolay > jugador2 - radio and bolay < jugador2 + tamaño + radio) or (bolay > jugador2 - ALTO - radio and bolay < jugador2 - ALTO + tamaño + radio)):
        bolavx *= -1
        puntaje += 1
        sonido.play()

    #Gráficos
    pantalla.fill((15,15,15)) #Color de fondo
    texto = fuente.render(str(puntaje), True, (100,100,100))
    pantalla.blit(texto,(ANCHO//2-50, ALTO//2- 80))
    pygame.draw.rect(pantalla, (0,0,255),(30,jugador1,espesor,tamaño)) #Jugador 1
    pygame.draw.rect(pantalla, (0,0,255),(30,jugador1 - ALTO,espesor,tamaño)) #Jugador 1 COPIA
    pygame.draw.rect(pantalla, (0,0,255),(ANCHO - espesor - 30, jugador2, espesor, tamaño)) #Jugador 2
    pygame.draw.rect(pantalla, (0,0,255),(ANCHO - espesor - 30, jugador2 - ALTO, espesor, tamaño)) #Jugador 2 COPIA
    pygame.draw.circle(pantalla, (255,0,0), (bolax,bolay), radio) #PELOTA
    pygame.display.flip()
    reloj.tick(max(500, 900 + puntaje))
    

pygame.quit()