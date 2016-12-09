import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, id, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Pictures/Ball{}.png".format(id))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # self.image = pygame.transform.rotate(self.img, 60)
        self.startSpeed = -20
        self.fallingSpeed = 0.5
        self.x_Speed = 0
        self.y_Speed = -0

    def update(self):
        if self.y_Speed < 20:            
            self.y_Speed += self.fallingSpeed
        self.rect.y += self.y_Speed
        self.rect.x += self.x_Speed
