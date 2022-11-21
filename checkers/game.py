import pygame
from .constants import RED, WHITE, GREY, YELLOW, BLACK;
from checkers.board import Board


class Game:
    def __init__(self, win):
        self.win = win
        self._init()

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
            if not result:
                self.selected = None
                self.select (row, col)

        else:

            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        
        return False


    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            # skipped = self.valid_moves
            return False

        return True

    def change_turn(self):
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
