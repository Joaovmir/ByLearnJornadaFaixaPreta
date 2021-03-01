import pygame

from variables import AMARELO, PRETO, VERMELHO, AZUL, BRANCO, CIANO, LARANJA, ROSA, VERDE, VELOCIDADE
from options import LIFES, GHOSTS

pygame.init()

screen = pygame.display.set_mode((800,580), 0)
font_style = pygame.font.SysFont('arial', 32, True, False)

from pac import Pacman
from scene import Scene
from ghost import Ghost


if __name__ == '__main__':

    size = 600 // 30
    
    lifes = LIFES
    pacman = Pacman(size)
    ghost1 = Ghost(VERMELHO, size)
    ghost2 = Ghost(CIANO, size)
    ghost3 = Ghost(LARANJA, size)
    ghost4 = Ghost(ROSA, size)
    if GHOSTS >= 5:
        ghost5 = Ghost(VERDE, size)
    if GHOSTS == 6:
        ghost6 = Ghost(AMARELO, size)
    scene = Scene(size, pacman, font_style, lifes)
    scene.add_movables(pacman)
    scene.add_movables(ghost1)
    scene.add_movables(ghost2)
    scene.add_movables(ghost3)
    scene.add_movables(ghost4)
    if GHOSTS >= 5:
        scene.add_movables(ghost5)
    if GHOSTS == 6:
        scene.add_movables(ghost6)
    
    while True:
        
        pacman.calculate()
        ghost1.calculate()
        ghost2.calculate()
        ghost3.calculate()
        ghost4.calculate()
        if GHOSTS >= 5:
            ghost5.calculate()
        if GHOSTS == 6:
            ghost6.calculate()
        scene.calculate()

        screen.fill(PRETO)
        scene.paint(screen)
        pacman.paint(screen)
        ghost1.paint(screen)
        ghost2.paint(screen)
        ghost3.paint(screen)
        ghost4.paint(screen)
        if GHOSTS >= 5:
            ghost5.paint(screen)
        if GHOSTS == 6:
            ghost6.paint(screen)
        pygame.display.update()
        pygame.time.delay(100)

        events = pygame.event.get()
        pacman.proccess_events(events)
        scene.proccess_events(events)
