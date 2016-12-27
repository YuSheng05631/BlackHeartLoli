import pygame, random

class Ball(pygame.sprite.Sprite):
    def __init__(self, id, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Pictures/Ball{}.png".format(id))
        self.imageRotated = self.generateImageRotated()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.startSpeed = -18
        self.fallingSpeed = 0.5
        self.x_Speed = random.randint(-3, 3)
        self.y_Speed = -15

    def generateImageRotated(self):
        imageRotated = list()
        for i in range(0, 360, 5):
            imageRotated.append(pygame.transform.rotate(self.image, i))
        return imageRotated

    def rotate(self):
        self.image = random.choice(self.imageRotated)

    def update(self):
        if self.y_Speed < 20:
            self.y_Speed += self.fallingSpeed
        self.rect.y += self.y_Speed
        self.rect.x += self.x_Speed
