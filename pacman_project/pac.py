from variables import AMARELO, PRETO, VERMELHO, AZUL, BRANCO, VELOCIDADE

import pygame

from game_element import GameElement
from movable import Movable

class Pacman(GameElement, Movable):
    def __init__(self, size):
        self.column = 1
        self.row = 1
        self.center_x = 400
        self.center_y = 300
        self.size = size
        self.radius = int(self.size/2)
        self.vel_x = 0
        self.vel_y = 0
        self.right = True
        self.row_intent = self.row
        self.column_intent = self.column
        self.mouth_opening = 0
        self.mouth_opening_vel = 3

    def calculate(self):

        self.column_intent = self.column + self.vel_x
        self.row_intent = self.row + self.vel_y
        self.center_x = int(self.column * self.size + self.radius)
        self.center_y = int(self.row * self.size + self.radius)
       
        if self.vel_x >= 0:
            self.right = True
        else:
            self.right = False


    def paint(self, tela):

        center = (self.center_x, self.center_y)
        
        # Pacman body
        pygame.draw.circle(tela, AMARELO, center, self.radius, 0)

        self.mouth_opening += self.mouth_opening_vel
        if self.mouth_opening > self.radius:
            self.mouth_opening_vel = -3
        if self.mouth_opening <= 0:
            self.mouth_opening_vel = 3

        if self.right:
            # Pacman mouth
            side = (self.center_x + self.radius, self.center_y + self.mouth_opening)
            off = (self.center_x + self.radius, self.center_y - self.mouth_opening)

            # Pacman eye
            eye_center_x = int(self.center_x + self.radius/4)
        else:
            side = (self.center_x - self.radius, self.center_y + self.mouth_opening)
            off = (self.center_x - self.radius, self.center_y - self.mouth_opening)

            eye_center_x = int(self.center_x - self.radius/4)
            
        points = (center, side, off)
        pygame.draw.polygon(tela, PRETO, points, 0)
        
        eye_center_y = int(self.center_y - self.radius/2)
        eye_center = (eye_center_x, eye_center_y)
        eye_radius = int(self.radius/6)
        pygame.draw.circle(tela, PRETO, eye_center, eye_radius, 0)

    def proccess_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = VELOCIDADE
                elif e.key == pygame.K_LEFT:
                    self.vel_x = -VELOCIDADE
                elif e.key == pygame.K_UP:
                    self.vel_y = -VELOCIDADE
                elif e.key == pygame.K_DOWN:
                    self.vel_y = VELOCIDADE
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = 0
                elif e.key == pygame.K_LEFT:
                    self.vel_x = 0
                elif e.key == pygame.K_UP:
                    self.vel_y = 0
                elif e.key == pygame.K_DOWN:
                    self.vel_y = 0
        
    def movement_accepted(self):
        self.row = self.row_intent
        self.column = self.column_intent

    def movement_refused(self, dir):
        self.row_intent = self.row
        self.column_intent = self.column

    def corner(self, dir):
        pass
