from variables import AMARELO, PRETO, VERMELHO, AZUL, BRANCO, VELOCIDADE
from abc import ABCMeta, abstractmethod

import pygame

class GameElement(metaclass = ABCMeta):

    @abstractmethod
    def paint(self):
        pass
    
    @abstractmethod
    def calculate(self):
        pass

    @abstractmethod
    def proccess_events(self, events):
        pass
