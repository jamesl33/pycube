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
import numpy as np

from constants import DISPLAY


class Cube():
    def __init__(self):
        self._points = [
            np.array([-1, -1, -1]),
            np.array([1, -1, -1]),
            np.array([1, 1, -1]),
            np.array([-1, 1, -1]),
            np.array([-1, -1, 1]),
            np.array([1, -1, 1]),
            np.array([1, 1, 1]),
            np.array([-1, 1, 1]),
        ]

    def _rotate(self, matrix):
        for index, point in enumerate(self._points):
            self._points[index] = np.matmul(matrix, point)

    def rotateX(self, degree):
        theta = np.radians(degree)
        cos, sin = np.cos(theta), np.sin(theta)

        rotation_matrix = np.array([
            [1, 0, 0],
            [0, cos, sin],
            [0, -sin, cos]
        ])

        self._rotate(rotation_matrix)

    def rotateY(self, degree):
        theta = np.radians(degree)
        cos, sin = np.cos(theta), np.sin(theta)

        rotation_matrix = np.array([
            [cos, 0, -sin],
            [0, 1, 0],
            [sin, 0, cos]
        ])

        self._rotate(rotation_matrix)

    def rotateZ(self, degree):
        theta = np.radians(degree)
        cos, sin = np.cos(theta), np.sin(theta)

        rotation_matrix = np.array([
            [cos, sin, 0],
            [-sin, cos, 0],
            [0, 0, 1]
        ])

        self._rotate(rotation_matrix)

    def draw(self, surface):
        projection = np.array([
            [1, 0, 0],
            [0, 1, 0]
        ])

        projected = [np.matmul(projection, point) for point in self._points]

        for point in projected:
            point = point * 100
            pygame.draw.circle(surface,
                               (255, 255, 255),
                               (int(point[0] + DISPLAY[2] / 4),
                                int(point[1] + DISPLAY[3] / 2)),
                               10)

        for index in range(4):
            self._connect(index, (index + 1) % 4, surface)
            self._connect(index + 4, ((index + 1) % 4) + 4, surface)
            self._connect(index, index + 4, surface)

    def _connect(self, a, b, surface):
        a = self._points[a]
        b = self._points[b]
        a, b = a * 100, b * 100

        pygame.draw.line(surface,
                         (255, 255, 255),
                         (a[0] + DISPLAY[2] / 4, a[1] + DISPLAY[3] / 2),
                         (b[0] + DISPLAY[2] / 4, b[1] + DISPLAY[3] / 2))
