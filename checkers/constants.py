import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# Colors are in RGB 

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128 )

#call image from assets
#method from pygame to resize image
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (45, 25))
