import pygame
import sys
from setting import *
from board import Board
from pieces import *
from mouse import Mouse

pygame.init()

# Main game

"""
USE A TILE MAP
[[2,3,4,5,6,4,3,2],
[1,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]
[11,11,11,11,11,11,11,11],
12,13,14,15,16,14,13,12],
]

MOUSE POS
x_index = (mouse_x-offset)//row_widht
y_index = (mouse_y-offset)//col_height
piece would be at board [x_index][y_index]
"""


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.board = Board(self.screen)

        self.pieces_map = [[2, 3, 4, 5, 6, 4, 3, 2],
                           [1, 1, 1, 1, 1, 1, 1, 1],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [11, 11, 11, 11, 11, 11, 11, 11],
                           [12, 13, 14, 15, 16, 14, 13, 12]]
        self.white_pawn = []
        self.white_rook = []
        self.white_knight = []
        self.white_bishop = []
        self.white_queen = None
        self.white_king = None
        self.black_pawn = []
        self.black_rook = []
        self.black_knight = []
        self.black_bishop = []
        self.black_queen = None
        self.black_king = None
        self.setup_board()

    def setup_board(self):
        for row_ind, row in enumerate(self.pieces_map):
            for col_ind, val in enumerate(row):
                x = col_ind * size + 128
                y = row_ind * size + 64

                pos = [x, y]

                if val == 1:
                    pawn = Pawn("w", pos)
                    self.white_pawn.append(pawn)
                if val == 2:
                    rook = Rook("w", pos)
                    self.white_rook.append(rook)
                if val == 3:
                    knight = Knight("w", pos)
                    self.white_knight.append(knight)
                if val == 4:
                    bishop = Bishop("w", pos)
                    self.white_bishop.append(bishop)
                if val == 5:
                    self.white_queen = Queen("w", pos)
                if val == 6:
                    self.white_king = King("w", pos)

                if val == 11:
                    pawn = Pawn("b", pos)
                    self.black_pawn.append(pawn)
                if val == 12:
                    rook = Rook("b", pos)
                    self.black_rook.append(rook)
                if val == 13:
                    knight = Knight("b", pos)
                    self.black_knight.append(knight)
                if val == 14:
                    bishop = Bishop("b", pos)
                    self.black_bishop.append(bishop)
                if val == 16:
                    self.black_king = King("b", pos)
                if val == 15:
                    self.black_queen = Queen("b", pos)   


    def draw_peices(self):
        for piece in self.white_pawn:
            piece.draw(self.screen)
        for piece in self.white_rook:
            piece.draw(self.screen)
        for piece in self.white_knight:
            piece.draw(self.screen)
        for piece in self.white_bishop:
            piece.draw(self.screen)

        self.white_king.draw(self.screen)
        self.white_queen.draw(self.screen)

        for piece in self.black_pawn:
            piece.draw(self.screen)
        for piece in self.black_rook:
            piece.draw(self.screen)
        for piece in self.black_knight:
            piece.draw(self.screen)
        for piece in self.black_bishop:
            piece.draw(self.screen)
        
        self.black_king.draw(self.screen)
        self.black_queen.draw(self.screen)

    def run(self):
        self.board.draw()
        self.draw_peices()


screen = pygame.display.set_mode((widht, height))


clock = pygame.time.Clock()

game = Game(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((43, 46, 51))
    game.run()
    pygame.display.update()
    clock.tick(60)
