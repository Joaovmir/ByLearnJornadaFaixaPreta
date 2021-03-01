from variables import AMARELO, PRETO, VERMELHO, AZUL, BRANCO, VELOCIDADE, CIMA, BAIXO, DIREITA, ESQUERDA

import pygame
from random import choice

from game_element import GameElement
from pac import Pacman
from ghost import Ghost

class Scene(GameElement):

    def __init__(self, size, pac, font, lifes):
        self.pacman = pac
        self.movables = []
        self.size = size
        self.state = "PLAYING"
        self.score = 0
        self.lifes = lifes
        self.font = font
        self.matrix = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 5, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 6, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 5, 2, 0, 0, 0, 0, 0, 0, 2, 6, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]
    
    def add_movables(self, obj):
        self.movables.append(obj)

    def paint_score(self, screen):
        score_text = f'SCORE: {self.score}'
        lifes_text = f'LIFES: {self.lifes}'
        img_score_text = self.font.render(score_text, True, AMARELO)
        img_lifes = self.font.render(lifes_text, True, AMARELO)
        screen.blit(img_score_text, (590, 280))
        screen.blit(img_lifes, (600, 20))

    def paint_row(self, screen, row_number, row):
        for column_number, column in enumerate(row):
            x = column_number * self.size
            y = row_number * self.size
            half = self.size // 2

            color = PRETO
            if column == 2:
                color = AZUL

            pygame.draw.rect(screen, color, (x, y, self.size, self.size), 0)

            if column == 1:
                pygame.draw.circle(screen, AMARELO, (x + half, y + half), self.size // 10, 0)
            elif column == 5 or column == 6:
                pygame.draw.circle(screen, VERMELHO, (x + half, y + half), self.size // 3, 0)

    def paint_playing(self, screen):
        for row_number, row in enumerate(self.matrix):
            self.paint_row(screen, row_number, row)
        self.paint_score(screen)

    def paint_text(self, screen, text):
        img_text = self.font.render(text, True, AMARELO)
        text_x = (screen.get_width() - img_text.get_width()) // 2
        text_y = (screen.get_height() - img_text.get_height()) // 2
        screen.blit(img_text, (text_x, text_y))

    def paint_paused(self, screen):
        self.paint_text(screen, 'P A U S E D')

    def paint_gameover(self, screen):
        self.paint_text(screen, 'G A M E   O V E R')

    def paint_victory(self, screen):
        self.paint_text(screen, 'V I C T O R Y ! !')

    def paint(self, screen):
        if self.state == 'PLAYING':
            self.paint_playing(screen)
        elif self.state == 'PAUSED':
            self.paint_playing(screen)
            self.paint_paused(screen)
        elif self.state == 'GAMEOVER':
            self.paint_playing(screen)
            self.paint_gameover(screen)
        elif self.state == 'VICTORY':
            self.paint_playing(screen)
            self.paint_victory(screen)

    def get_directions(self, row, column):
        directions = []
        if self.matrix[int(row - 1)][int(column)] != 2:
            directions.append(CIMA)
        if self.matrix[int(row + 1)][int(column)] != 2:
            directions.append(BAIXO)
        if self.matrix[int(row)][int(column - 1)] != 2:
            directions.append(ESQUERDA)
        if self.matrix[int(row)][int(column + 1)] != 2:
            directions.append(DIREITA)
        return directions

    def calculate(self):
        if self.state == 'PLAYING':
            self.calculate_playing()
        elif self.state == 'PAUSED':
            self.calculate_paused()
        elif self.state == 'GAMEOVER':
            self.calculate_gameover()

    def calculate_gameover(self):
        pass
    
    def calculate_paused(self):
        pass

    def calculate_playing(self):

        for movable in self.movables:
            row = int(movable.row)
            column = int(movable.column)
            row_intent = int(movable.row_intent)
            column_intent = int(movable.column_intent)
            directions = self.get_directions(row, column)
            if len(directions) >= 3:
                movable.corner(directions)
            if isinstance(movable, Ghost) and movable.row == self.pacman.row and movable.column == self.pacman.column:
                self.lifes -= 1
                if self.lifes <= 0:
                    self.state = 'GAMEOVER'
                else:
                    self.pacman.row = 1
                    self.pacman.column = 1
            else:
                if 0 <= column_intent < 28 and 0 <= row_intent < 29 and self.matrix[row_intent][column_intent] != 2:
                    movable.movement_accepted()
                    if isinstance(movable, Pacman):
                        if self.matrix[row][column] == 1:
                            self.score += 5
                            self.matrix[row][column] = 0
                        elif self.matrix[row][column] == 5:
                            self.score += 25
                            self.matrix[row][column] = 0
                            gh = choice(self.movables[1:])
                            gh.change_position(1.0, 1.0)
                        elif self.matrix[row][column] == 6:
                            self.score += 25
                            self.matrix[row][column] = 0
                            gh = choice(self.movables[1:])
                            gh.change_position(1.0, 26.0)
                        if self.score >= 1650:
                            self.state = 'VICTORY'
                else:
                    movable.movement_refused(directions)

    def proccess_events(self, events):
        for e in events:
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p:
                    if self.state == 'PAUSED':
                        self.state = 'PLAYING'
                    elif self.state == 'PLAYING':
                        self.state = 'PAUSED'
