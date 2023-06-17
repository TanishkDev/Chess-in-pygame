from support import import_boards
from setting import *
import pygame
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
# Square
class Square:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color 
        self.abs_x = chess_board_x + (size*self.x)
        self.abs_y = chess_board_y + (size*self.y)
        self.highlighted = False
        self.occupied_piece = None
        self.rect = pygame.Rect(self.abs_x,self.abs_y,size,size)
    
    def get_coord(self):
        return self.x, self.y
