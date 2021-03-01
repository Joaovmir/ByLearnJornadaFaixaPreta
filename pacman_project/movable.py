from variables import AMARELO, PRETO, VERMELHO, AZUL, BRANCO, VELOCIDADE
from abc import ABCMeta, abstractmethod

import pygame

class Movable(metaclass = ABCMeta):

    @abstractmethod
    def movement_accepted(self):
        pass

    @abstractmethod
    def movement_refused(self, dir):
        pass

    @abstractmethod
    def corner(self, dir):
        pass

    