import pygame, sys
from pygame.locals import *
import random
from Jugador import Jugador
from maingato import maingato
from Button import Button


class Gato:
    def iniciar(self, tablero):
        pygame.init()
        display = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Gato")
        font = pygame.font.SysFont('Arial', 40)
        txtEmpate = font.render("EMPATE!", 1, (255, 255, 255))
        txtEmpate = font.render("GANADOR!", 1, (255, 255, 255))
        imgGatito = pygame.image.load("src/gatito.png")
        btnAceptar = Button((138, 183, 58), 135, 135, 100, 50, "Aceptar")

        ficha = "X"
        jnombre = ""
        jugador = Jugador(jnombre, ficha);
        turno = True
        running = True

        while running:
            display.fill((255, 255, 255))
            display.blit(imgGatito, (50, 50))
            tablero.dibujarTablero(display)

            if tablero.verificarGanador(ficha):
                pygame.draw.rect(display, (103, 58, 183), (60, 60, 250, 150), 0)
                display.blit(txtEmpate, (115, 75))
                btnAceptar.draw(display, 1)

            if tablero.verificarEmpate():
                pygame.draw.rect(display, (103, 58, 183), (60, 60, 250, 150), 0)
                display.blit(txtEmpate, (115, 75))
                btnAceptar.draw(display, 1)

            pygame.display.update()
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if turno:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for boton in tablero.botones:
                            if boton.isOver(pos):
                                tablero.setPosicion(boton.text, ficha)
                                turno = False

                        if btnAceptar.isOver(pos):
                            tablero.resetTablero()
                            reset = maingato()
                            reset.initMenu()
                            pygame.quit()
                            sys.exit()
                else:
                    tablero.setPosicion(tablero.botones[random.randint(0, 8)].text, "O")
                    turno = False
        else:
            pass
