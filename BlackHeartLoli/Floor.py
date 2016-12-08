import pygame

class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Pictures/floor.jpg")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        pass
