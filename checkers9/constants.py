import pygame

WIDTH, HEIGHT = 900, 900
ROWS, COLS = 9, 9
SQUARE_SIZE = WIDTH//COLS

RED = (255, 0 ,0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
BROWN = (205,133,63)

CROWN = pygame.transform.scale(pygame.image.load('checkers9/assets/crown512.png'), (WIDTH//COLS//3, HEIGHT//ROWS//3))
