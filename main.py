#!/usr/bin/env python3

import pygame

from constants import FPS, DISPLAY, BACKGROUND
from cube import Cube


class CubeSimulation():
    def __init__(self):
        self._display = pygame.display.set_mode(DISPLAY.size)
        self._background = pygame.Surface(BACKGROUND.size)
        self._clock = pygame.time.Clock()
        self._cube = Cube()

    def start(self):
        while True:
            self._update()

    def _update(self):
        self._clock.tick(FPS)
        self._handle_input(pygame.key.get_pressed())
        self._cube.rotateX(0.5)
        self._cube.rotateY(0.5)
        self._cube.rotateZ(0.5)
        self._display.fill((0, 0, 0))
        self._cube.draw(self._display)
        pygame.display.update()

    def _handle_input(self, keys):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


if __name__ == '__main__':
    SIM = CubeSimulation()
    SIM.start()
