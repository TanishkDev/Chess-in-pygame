import pygame
from support import import_boards
from setting import *

#Boards
class Board:
    def __init__(self, screen):
        self.screen = screen
        self.boards = import_boards()
        self.board_number = 0
        self.rect = self.boards[self.board_number].get_rect()
        

    #draw boards
    def draw(self):
        self.screen.blit(self.boards[self.board_number],(chess_board_x,chess_board_y))

