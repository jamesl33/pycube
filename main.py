#!/usr/bin/env python3
"""
This file is part of pycube.

Copyright (C) 2019, James Lee <jamesl33info@gmail.com>.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import pygame

from constants import FPS, DISPLAY, BACKGROUND
from hypercube import Hypercube
from cube import Cube


class CubeSimulation():
    def __init__(self):
        self._display = pygame.display.set_mode(DISPLAY.size)
        self._background = pygame.Surface(BACKGROUND.size)
        self._clock = pygame.time.Clock()
        self._hypercube = Hypercube()
        self._cube = Cube()

    def start(self):
        while True:
            self._update()

    def _update(self):
        self._clock.tick(FPS)
        self._handle_input(pygame.key.get_pressed())
        self._display.fill((0, 0, 0))

        self._cube.rotateX(0.5)
        self._cube.rotateY(0.25)
        self._cube.draw(self._display)

        self._hypercube.rotateY(0.5)
        self._hypercube.rotateW(0.25)
        self._hypercube.draw(self._display)

        pygame.display.update()

    def _handle_input(self, keys):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


if __name__ == '__main__':
    SIM = CubeSimulation()
    SIM.start()
