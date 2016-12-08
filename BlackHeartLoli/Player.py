import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, id, x, y, flip:bool):
        pygame.sprite.Sprite.__init__(self)
        self.flip = flip
        self.image = pygame.image.load("Pictures/Player{}.png".format(id))
        self.image = pygame.transform.flip(self.image, self.flip, False)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.movingUp = False
        self.movingDown = False
        self.movingLeft = False
        self.movingRight = False
        self.isJumping = False
        self.jumpingHeight = 0

    def update(self, stepOnFloor):
        self.movingDown = True
        # 偵測玩家是否在地板上
        if stepOnFloor is not None:
            if self in stepOnFloor:
                stepOnFloor = True
        # 跳躍
        if self.movingUp and stepOnFloor is True:
            self.isJumping = True
            self.movingDown = False
            self.jumpingHeight = 32
        if self.isJumping:
            self.jumpingHeight -= 1
            self.rect.y -= self.jumpingHeight
            if stepOnFloor is True and self.jumpingHeight < 0:
                self.isJumping = False
        # 下左右
        if self.movingDown:
            self.rect.y += 8
        if self.movingLeft:
            self.rect.x -= 5
        if self.movingRight:
            self.rect.x += 5
