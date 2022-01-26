import pygame
from support import import_pieces
from setting import *

class Pieces(pygame.sprite.Sprite):
    def __init__(self):
        super(Pieces, self).__init__()
        self.pieces_img = {"white":import_pieces("assets/images/16x16 pieces/WhitePieces.png"),
                            "black":import_pieces("assets/images/16x16 pieces/BlackPieces.png")}
        self.white_imgs = import_pieces("assets/images/16x16 pieces/WhitePieces.png")
        self.black_imgs = import_pieces("assets/images/16x16 pieces/BlackPieces.png")

class Pawn(Pieces):
    def __init__(self,color,pos):
        super().__init__()
        if color=="w":
            self.image = self.white_imgs[0]
        else:
            self.image = self.black_imgs[0]
        
        self.image = pygame.transform.scale(self.image,(size,size))
        self.rect = self.image.get_rect(topleft = (pos))