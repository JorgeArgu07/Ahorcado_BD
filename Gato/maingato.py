import pygame, sys
from pygame.locals import *
from Button import Button
from Gato import Gato
from Tablero import Tablero


class maingato:
    def initMenu(self):

        pygame.init()
        display = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Gato")
        colorMagenta = (103, 58, 183)
        colorVerde = (138, 183, 58)
        font = pygame.font.SysFont('Arial', 50)
        titulo = font.render("GATO X / O", 1, (0, 0, 0))
        btnJugar = Button(colorMagenta, 70, 100, 100, 50, "Jugar")
        btnSalir = Button(colorVerde, 70, 170, 100, 50, "Salir")
        imgGatito = pygame.image.load("src/gatito.png")

        enJuego = True
        while True:
            # dibujar menu
            display.fill((255, 255, 255))
            btnJugar.draw(display, 1)
            btnSalir.draw(display, 1)
            display.blit(imgGatito, (50, 50))
            display.blit(titulo, (100, 20))
            pygame.display.update()
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if btnJugar.isOver(pos):
                        tablero = Tablero()
                        gato = Gato()
                        gato.iniciar(tablero)
                    if btnSalir.isOver(pos):
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    if btnJugar.isOver(pos):
                        btnJugar.color = (72, 40, 128)
                    elif btnSalir.isOver(pos):
                        btnSalir.color = (96, 128, 40)
                    else:
                        btnJugar.color = (103, 58, 183)
                        btnSalir.color = (138, 183, 58)

mainGato = maingato()
mainGato.initMenu()
