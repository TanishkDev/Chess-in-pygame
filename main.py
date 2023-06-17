import pygame
import sys
from setting import *
from board import Board, Square
from pieces import *


pygame.init()

# Main game
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.board = Board(self.screen)
        self.selected_or_not = False
        self.selected_piece = None
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
        self.squares = self.generate_square()
        self.setup_board()
        self.turn = 1

    def generate_square(self):
        output = []
        for y in range(8):
            for x in range(8):
                col = white if (x+y) % 2 == 0 else black
                output.append(Square(x, y, col))

        return output

    def get_square_pos(self, pos):
        for square in self.squares:
            if (square.x, square.y) == (pos[0], pos[1]):
                return square

    def get_piece_from_pos(self, pos):
        return self.get_square_pos(pos).occupied_piece
        
    def setup_board(self):
        for row_ind, row in enumerate(self.pieces_map):
            for col_ind, val in enumerate(row):
                x = col_ind * size
                y = row_ind * size
                pos = [x, y]
                square = self.get_square_pos([col_ind, row_ind])
                if val == 1:
                    pawn = Pawn("w", pos)
                    self.white_pawn.append(pawn)
                    square.occupied_piece = pawn
                if val == 2:
                    rook = Rook("w", pos)
                    self.white_rook.append(rook)
                    square.occupied_piece = rook
                if val == 3:
                    knight = Knight("w", pos)
                    self.white_knight.append(knight)
                    square.occupied_piece = knight
                if val == 4:
                    bishop = Bishop("w", pos)
                    self.white_bishop.append(bishop)
                    square.occupied_piece = bishop
                if val == 5:
                    self.white_queen = Queen("w", pos)
                    square.occupied_piece = self.white_queen
                if val == 6:
                    self.white_king = King("w", pos)
                    square.occupied_piece = self.white_king
                if val == 11:
                    pawn = Pawn("b", pos)
                    self.black_pawn.append(pawn)
                    square.occupied_piece = pawn
                if val == 12:
                    rook = Rook("b", pos)
                    self.black_rook.append(rook)
                    square.occupied_piece = rook
                if val == 13:
                    knight = Knight("b", pos)
                    self.black_knight.append(knight)
                    square.occupied_piece = knight
                if val == 14:
                    bishop = Bishop("b", pos)
                    self.black_bishop.append(bishop)
                    square.occupied_piece = bishop
                if val == 16:
                    self.black_king = King("b", pos)
                    square.occupied_piece = self.black_king
                if val == 15:
                    self.black_queen = Queen("b", pos)
                    square.occupied_piece = self.black_queen

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

    # def select_piece(self):
    #     for row_ind, row in enumerate(self.pieces_map):
    #         for col_ind, val in enumerate(row):
    #             # x = col_ind * size + 128
    #             # y = row_ind * size + 64
    #             x = col_ind * size
    #             y = row_ind * size

    #             if self.mouse_pos == [col_ind, row_ind]:
    #                 # white pieces select
    #                 for piece in self.white_pawn:
    #                     if piece.rect.x == x and piece.rect.y == y:
    #                         self.selected_or_not = True
    #                         self.selected_piece = {
    #                             "p": piece, "name": "w_p", "pos": (x, y)}
    #                 for piece in self.white_rook:
    #                     if piece.rect.x == x and piece.rect.y == y:
    #                         self.selected_or_not = True
    #                         self.selected_piece = {
    #                             "p": piece, "name": "w_r", "pos": (x, y)}
    #                 for piece in self.white_knight:
    #                     if piece.rect.x == x and piece.rect.y == y:
    #                         self.selected_or_not = True
    #                         self.selected_piece = {
    #                             "p": piece, "name": "w_k", "pos": (x, y)}
    #                 for piece in self.white_bishop:
    #                     if piece.rect.x == x and piece.rect.y == y:
    #                         self.selected_or_not = True
    #                         self.selected_piece = {
    #                             "p": piece, "name": "w_b", "pos": (x, y)}
    #                 if self.white_king.rect.x == x and self.white_king.rect.y == y:
    #                     piece = self.white_king
    #                     self.selected_or_not = True
    #                     self.selected_piece = {
    #                         "p": piece, "name": "w_king", "pos": (x, y)}
    #                 if self.white_queen.rect.x == x and self.white_queen.rect.y == y:
    #                     piece = self.white_queen
    #                     self.selected_or_not = True
    #                     self.selected_piece = {
    #                         "p": piece, "name": "w_queen", "pos": (x, y)}

    #                 # black pieces select
    #                 for piece in self.black_pawn:
    #                     if piece.rect.x == x and piece.rect.y == y:
    #                         self.selected_or_not = True
    #                         self.selected_piece = {
    #                             "p": piece, "name": "b_p", "pos": (x, y)}
    #                 for piece in self.black_rook:
    #                     if piece.rect.x == x and piece.rect.y == y:
    #                         self.selected_or_not = True
    #                         self.selected_piece = {
    #                             "p": piece, "name": "b_r", "pos": (x, y)}
    #                 for piece in self.black_bishop:
    #                     if piece.rect.x == x and piece.rect.y == y:
    #                         self.selected_or_not = True
    #                         self.selected_piece = {
    #                             "p": piece, "name": "b_b", "pos": (x, y)}
    #                 for piece in self.black_knight:
    #                     if piece.rect.x == x and piece.rect.y == y:
    #                         self.selected_or_not = True
    #                         self.selected_piece = {
    #                             "p": piece, "name": "b_k", "pos": (x, y)}
    #                 if self.black_king.rect.x == x and self.black_king.rect.y == y:
    #                     piece = self.black_king
    #                     self.selected_or_not = True
    #                     self.selected_piece = {
    #                         "p": piece, "name": "b_king", "pos": (x, y)}
    #                 if self.black_queen.rect.x == x and self.black_queen.rect.y == y:
    #                     piece = self.black_queen
    #                     self.selected_or_not = True
    #                     self.selected_piece = {
    #                         "p": piece, "name": "b_queen", "pos": (x, y)}
    def handle_click(self):
        clicked_square = self.get_square_pos(self.mouse_pos)
        print(clicked_square.occupied_piece)
        if self.selected_piece is None:
            if clicked_square.occupied_piece is not None:
                if clicked_square.occupied_piece.color == self.turn:
                    self.selected_piece = clicked_square.occupied_piece
        elif self.move_pieces([clicked_square.x, clicked_square.y]):
            self.turn = 0 if self.turn == 1 else 1
        elif clicked_square.occupied_piece is not None:
            if clicked_square.occupied_piece.color==self.turn:
                self.selected_piece = clicked_square.occupied_piece

    def move_pieces(self, pos):
        self.change_occupying_piece(self,pos)
        self.selected_piece.pos = [pos[0]*size, pos[1]*size]
        self.selected_or_not = False
        self.selected_piece = None
        return True
    
    def change_occupying_piece(self,pos):
        swaped = False
        for square in self.squares:
            if square.x==self.selected_piece.pos[0] and square.y==self.selected_piece.pos[1]:
                square.occupied_piece=None
                swaped=False         
            if swaped==True and square.x==pos[0] and square.y==pos[1]:
                square.occupied_piece = self.selected_piece
                swaped=False 

    # send mouse to pos to select piece
    def get_mouse_pos(self, mouse_pos):
        self.mouse_pos = mouse_pos
        self.handle_click()
        # self.select_piece()

    def run(self):
        self.board.draw()
        # self.highlight_piece()
        self.draw_peices()


screen = pygame.display.set_mode((widht, height))


clock = pygame.time.Clock()

game = Game(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if not game.selected_or_not:
                mouse_pos = pygame.mouse.get_pos()
                x_pos = (mouse_pos[0])//64
                y_pos = (mouse_pos[1])//64

                game.get_mouse_pos([x_pos, y_pos])

            elif game.selected_or_not:
                mouse_pos = pygame.mouse.get_pos()
                x_pos = (mouse_pos[0])//64
                y_pos = (mouse_pos[1])//64
                game.move_pieces((x_pos, y_pos))

    screen.fill((43, 46, 51))
    game.run()
    pygame.display.update()
    clock.tick(60)

