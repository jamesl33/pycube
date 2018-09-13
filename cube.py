#!/usr/bin/env python3

import pygame
import numpy as np


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
        for index in range(len(self._points)):
            self._points[index] = np.matmul(matrix, self._points[index])

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
                               (int(point[0] + surface.get_size()[0] / 2),
                                int(point[1] + surface.get_size()[1] / 2)),
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
                         (a[0] + surface.get_size()[0] / 2, a[1] + surface.get_size()[1] / 2),
                         (b[0] + surface.get_size()[0] / 2, b[1] + surface.get_size()[1] / 2))
