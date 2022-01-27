import pygame
import sys
from setting import widht, height, chess_board_x, chess_board_y
from board import Board
from pieces import *

pygame.init()

# Main game


class Game:
    def __init__(self):
        self.board = Board(screen)
        self.setup_board()

    def add_group_pieces(self, pieces, no_of_pieces=None):
        sprite_group = pygame.sprite.Group()
        if pieces == "white_pawn":
            for i in range(no_of_pieces):
                pos = [128+64*i, 64+64*1]
                sprite = Pawn("w", pos)
                sprite_group.add(sprite)

        if pieces == "black_pawn":
            for i in range(no_of_pieces):
                pos = [128+64*i, 64+64*6]
                sprite = Pawn("b", pos)
                sprite_group.add(sprite)

        if pieces == "white_knight":
            for i in range(no_of_pieces):
                if i == 0:
                    pos = [128+64*1, 64+64*0]
                if i == 1:
                    pos = [128+64*6, 64+64*0]
                sprite = Knight("w", pos)
                sprite_group.add(sprite)

        if pieces == "black_knight":
            for i in range(no_of_pieces):
                if i == 0:
                    pos = [128+64*1, 64+64*7]
                if i == 1:
                    pos = [128+64*6, 64+64*7]
                sprite = Knight("b", pos)
                sprite_group.add(sprite)

        if pieces == "white_rook":
            for i in range(no_of_pieces):
                if i == 0:
                    pos = [128+64*0, 64+64*0]
                if i == 1:
                    pos = [128+64*7, 64+64*0]
                sprite = Rook("w", pos)
                sprite_group.add(sprite)

        if pieces == "black_rook":
            for i in range(no_of_pieces):
                if i == 0:
                    pos = [128+64*0, 64+64*7]
                if i == 1:
                    pos = [128+64*7, 64+64*7]
                sprite = Rook("b", pos)
                sprite_group.add(sprite)

        if pieces == "white_bishop":
            for i in range(no_of_pieces):
                if i == 0:
                    pos = [128+64*2, 64+64*0]
                if i == 1:
                    pos = [128+64*5, 64+64*0]
                sprite = Bishop("w", pos)
                sprite_group.add(sprite)

        if pieces == "black_bishop":
            for i in range(no_of_pieces):
                if i == 0:
                    pos = [128+64*2, 64+64*7]
                if i == 1:
                    pos = [128+64*5, 64+64*7]
                sprite = Bishop("b", pos)
                sprite_group.add(sprite)

        if pieces == "white_queen":
            pos = [128+64*3, 64+64*0]
            sprite = Queen("w", pos)
            sprite_group.add(sprite)

        if pieces == "black_queen":
            pos = [128+64*3, 64+64*7]
            sprite = Queen("b", pos)
            sprite_group.add(sprite)

        if pieces == "white_king":
            pos = [128+64*4, 64+64*0]
            sprite = King("w", pos)
            sprite_group.add(sprite)

        if pieces == "black_king":
            pos = [128+64*4, 64+64*7]
            sprite = King("b", pos)
            sprite_group.add(sprite)

        return sprite_group

    def setup_board(self):
        self.white_pieces = {0: self.add_group_pieces("white_pawn", 8),
                             1: self.add_group_pieces("white_knight", 2),
                             2: self.add_group_pieces("white_bishop", 2),
                             3: self.add_group_pieces("white_rook", 2),
                             4: self.add_group_pieces("white_queen"),
                             5: self.add_group_pieces("white_king")}

        self.black_pieces = {0: self.add_group_pieces("black_pawn", 8),
                             1: self.add_group_pieces("black_knight", 2),
                             2: self.add_group_pieces("black_bishop", 2),
                             3: self.add_group_pieces("black_rook", 2),
                             4: self.add_group_pieces("black_queen"),
                             5: self.add_group_pieces("black_king")}

    def draw(self):
        # use dict comprehension once all sprite are completed
        for i in range(6):
            self.white_pieces[i].draw(screen)
            self.black_pieces[i].draw(screen)

    def run(self):
        self.board.draw()
        self.draw()


screen = pygame.display.set_mode((widht, height))


clock = pygame.time.Clock()

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((43, 46, 51))
    game.run()
    pygame.display.update()
    clock.tick(60)

    screen.fill((43, 46, 51))
    game.run()
    pygame.display.update()
    clock.tick(60)
