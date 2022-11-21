import pygame
from .constants import RED, WHITE, GREY, YELLOW, BLACK;
from checkers.board import Board


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()
        
    def _init(self): # private
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def rest(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            results = self._move(row, col)

    def move(self, row, col):