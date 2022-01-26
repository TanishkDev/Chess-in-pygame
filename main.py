import pygame
import sys
from setting import widht, height, chess_board_x, chess_board_y
from board import Board
from pieces import Pawn

pygame.init()

# Main game


class Game:
    def __init__(self):
        self.board = Board(screen)
        self.setup_board()

    def add_group_pieces(self, piece,no_of_pieces):
        sprite_group = pygame.sprite.GroupSingle()
        if pieces == "white_pawn":
            for i in range(no_of_pieces-1):
                pos = [128+64*i,64+64*1]
                sprite = Pawn("w", pos)
                sprite_group.add(sprite)
            
        if pieces == "black_pawn":
            for i in range(no_of_pieces-1):   
                pos = [128+64*i,64+64*6]
                sprite = Pawn("b", pos)
                sprite_group.add(sprite)
            
        return sprite_group

    def setup_board(self):  
        self.white_pieces = {0: self.add_group_pieces("white_pawn",8)}
        print(self.white_pieces[0].sprite.rect)
        self.black_pieces = {0: self.add_group_pieces("black_pawn",8)}

    def draw(self):
        self.white_pieces[0].draw(screen)
        self.black_pieces[0].draw(screen)

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
