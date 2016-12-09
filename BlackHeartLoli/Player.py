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

    def update(self, stepOnFloor, stepOnPlayer, isSteped):
        self.movingDown = True
        # 偵測玩家是否在地板上
        if stepOnFloor is not None:
            if self in stepOnFloor:
                stepOnFloor = True
        # 偵測玩家是否在玩家上
        if stepOnPlayer is not None:
            if self is stepOnPlayer:
                stepOnPlayer = True
        # 偵測玩家是否被踩在玩家下
        if isSteped is not None:
            if self is isSteped:
                isSteped = True
        # 轉向
        if self.flip and self.movingLeft:
            self.flip = False
            self.image = pygame.transform.flip(self.image, True, False)
        if not self.flip and self.movingRight:
            self.flip = True
            self.image = pygame.transform.flip(self.image, True, False)
        # 跳躍
        if self.movingUp and (stepOnFloor is True or stepOnPlayer is True):
            self.isJumping = True
            self.jumpingHeight = 32
        if self.isJumping:
            self.jumpingHeight -= 1
            self.rect.y -= self.jumpingHeight
            if self.jumpingHeight < 0:          # 正在下降
                if stepOnPlayer is True:        # 踩人
                    self.jumpingHeight = 15
                if isSteped is True:            # 被踩
                    self.jumpingHeight = 0
                if stepOnFloor is True:         # 踩地板
                    self.isJumping = False
        # 下左右
        if self.movingDown:
            self.rect.y += 8
        if self.movingLeft:
            self.rect.x -= 5
        if self.movingRight:
            self.rect.x += 5
