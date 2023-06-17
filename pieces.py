import pygame
from support import import_pieces
from setting import *

class Pieces:
    def __init__(self):
        super(Pieces, self).__init__()
        self.white_imgs = import_pieces("assets/images/16x16 pieces/WhitePieces.png")
        self.black_imgs = import_pieces("assets/images/16x16 pieces/BlackPieces.png")

    def draw(self,screen):
        screen.blit(self.image,self.image.get_rect(topleft=(self.pos)))

class Pawn(Pieces):
    def __init__(self,color,pos):
        super().__init__()
        if color=="w":
            self.image = self.white_imgs[0]
        else:
            self.image = self.black_imgs[0]
    
        self.color = 1 if color=="w" else 0
        self.pos = pos
        self.image = pygame.transform.scale(self.image,(size,size))
        self.rect = self.image.get_rect(topleft = (self.pos))

class Knight(Pieces):
    def __init__(self,color,pos):
        super().__init__()
        if color=="w":  self.image = self.white_imgs[1]     
        else:   self.image = self.black_imgs[1]
        self.color = 1 if color=="w" else 0
        self.pos = pos
        self.image = pygame.transform.scale(self.image,(size,size))
        self.rect = self.image.get_rect(topleft = (self.pos))

class Rook(Pieces):
    def __init__(self,color,pos):
        super().__init__()
        if color=="w":  self.image = self.white_imgs[2]     
        else:   self.image = self.black_imgs[2]
        self.color = 1 if color=="w" else 0
        self.pos = pos
        self.image = pygame.transform.scale(self.image,(size,size))
        self.rect = self.image.get_rect(topleft = (self.pos))

class Bishop(Pieces):
    def __init__(self,color,pos):
        super().__init__()
        if color=="w":  self.image = self.white_imgs[3]     
        else:   self.image = self.black_imgs[3]
        self.color = 1 if color=="w" else 0
        self.pos = pos
        self.image = pygame.transform.scale(self.image,(size,size))
        self.rect = self.image.get_rect(topleft = (self.pos))

class Queen(Pieces):
    def __init__(self,color,pos):
        super().__init__()
        if color=="w":  self.image = self.white_imgs[4]     
        else:   self.image = self.black_imgs[4]
        self.color = 1 if color=="w" else 0
        self.pos=pos
        self.image = pygame.transform.scale(self.image,(size,size))
        self.rect = self.image.get_rect(topleft = (self.pos))

class King(Pieces):
    def __init__(self,color,pos):
        super().__init__()
        if color=="w":  self.image = self.white_imgs[5]     
        else:   self.image = self.black_imgs[5]
        self.color = 1 if color=="w" else 0
        self.pos=pos
        self.image = pygame.transform.scale(self.image,(size,size))
        self.rect = self.image.get_rect(topleft = (self.pos))
