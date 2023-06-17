from os import walk
import pygame

#Import the boards into the game
def import_boards():
    boards = []
    path = "assets/images/board"
    for __, ___, img_files in walk(path):
        for img in img_files:
            full_path = path+"/"+img
            image = pygame.image.load(full_path).convert_alpha()
            image = pygame.transform.scale(image, (512, 512))
            boards.append(image)
    
    return boards

#Import pieces into the game
def import_pieces(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = surface.get_size()[0] // 16
    tile_num_y = surface.get_size()[1] // 16

    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * 16 #cordinate for image
            y = row * 16 #coordinate for image
            new_surf = pygame.Surface((16, 16), flags=pygame.SRCALPHA)#creating a image
            new_surf.blit(surface, (0, 0), pygame.Rect(x, y, 16, 16))
            cut_tiles.append(new_surf)
    return cut_tiles
