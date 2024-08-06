import pygame

PLAYER_TEXTURE_FILE = "images\\player.png"
PLAYER_SIDE_LENGTH = 64


class Player:
    def __init__(self):
        self.image = pygame.image.load(PLAYER_TEXTURE_FILE)
        self.image_rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.image_rect)
    def move(self, x, y):
        self.image_rect.x = x
        self.image_rect.y = y
