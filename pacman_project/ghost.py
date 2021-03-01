from variables import AMARELO, PRETO, VERMELHO, AZUL, BRANCO, VELOCIDADE, CIMA, BAIXO, DIREITA, ESQUERDA

import pygame
from random import choice

from game_element import GameElement
from movable import Movable

class Ghost(GameElement, Movable):

    def __init__(self, color, size):
        self.row = 15.0
        self.column = 13.0
        self.row_intent = self.row
        self.column_intent = self.column
        self.speed = 1
        self.direction = 0
        self.size = size
        self.color = color

    def paint(self, screen):
        piece = self.size // 8
        px = int(self.column * self.size)
        py = int(self.row * self.size)
        borders = [(px, py + self.size),
                  (px + piece, py + piece * 2), 
                  (px + piece * 2, py + piece // 2),
                  (px + piece * 3, py),
                  (px + piece * 5, py),
                  (px + piece * 6, py + piece //2),
                  (px + piece * 7, py + piece * 2),
                  (px + self.size, py + self.size)]
        pygame.draw.polygon(screen, self.color, borders, 0)

        ext_eye_radius = piece
        int_eye_radius = piece // 2

        left_eye_x = int(px + piece * 2.5)
        left_eye_y = int(py + piece * 2.5)

        right_eye_x = int(px + piece * 5.5)
        right_eye_y = int(py + piece * 2.5)

        pygame.draw.circle(screen, BRANCO, (left_eye_x, left_eye_y), ext_eye_radius, 0)
        pygame.draw.circle(screen, PRETO, (left_eye_x, left_eye_y), int_eye_radius, 0)
        pygame.draw.circle(screen, BRANCO, (right_eye_x, right_eye_y), ext_eye_radius, 0)
        pygame.draw.circle(screen, PRETO, (right_eye_x, right_eye_y), int_eye_radius, 0)

    def proccess_events(self, event):
        pass

    def calculate(self):
        if self.direction == CIMA:
            self.row_intent -= self.speed
        elif self.direction == BAIXO:
            self.row_intent += self.speed
        elif self.direction == ESQUERDA:
            self.column_intent -= self.speed
        elif self.direction == DIREITA:
            self.column_intent += self.speed

    def change_direction(self, dir):
        self.direction = choice(dir)

    def corner(self, dir):
        self.change_direction(dir)

    def movement_accepted(self):
        self.row = self.row_intent
        self.column = self.column_intent

    def movement_refused(self, dir):
        self.row_intent = self.row
        self.column_intent = self.column
        self.change_direction(dir)

    def change_position(self, row, column):
        self.row = row
        self.column = column
        self.row_intent = row
        self.column_intent = column
