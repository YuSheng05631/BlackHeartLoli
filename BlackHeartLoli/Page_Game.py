import pygame, time
from Ball import Ball
from Floor import Floor
from Player import Player

class Page_Game:
    def __init__(self, display):
        self.display = display
        self.clock = pygame.time.Clock()
        self.ballList = None
        self.floorList = None
        self.playerList = None
        self.ballGroup = None
        self.floorGroup = None
        self.playerGroup = None

    def initObject(self):   # 物件初始化
        self.ballList = [Ball(1, 100, 200), Ball(2, 858, 200)]
        self.floorList = [Floor(106, 560), Floor(412, 560), Floor(718, 560)]
        # self.floorList = [Floor(100, 560), Floor(300, 560), Floor(500, 560), Floor(700, 560)]
        self.playerList = [Player(2, 100, 460, True), Player(5, 824, 460, False)]
        self.ballGroup = pygame.sprite.Group()
        self.floorGroup = pygame.sprite.Group()
        self.playerGroup = pygame.sprite.Group()
        self.ballGroup.add(self.ballList)
        self.floorGroup.add(self.floorList)
        self.playerGroup.add(self.playerList)
        self.startTime = time.time()
        self.passTime = time.time()
        self.bestTime = self.readBestTime()
        self.isOver = -1
        self.startCounting = False
        self.startCountingTime = 0

    def writeBestTime(self, bestTime):
        with open("record.data", "wt") as f:
            f.write(str(bestTime))

    def readBestTime(self):
        try:
            with open("record.data", "rt") as f:
                return int(f.read())
        except:
            self.writeBestTime(0)
            return 0

    def keyEvent(self):     # 按鍵事件
        for event in pygame.event.get():
            # 離開
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # 按鍵按下
            if event.type == pygame.KEYDOWN:
                # 1P 移動
                if event.key == pygame.K_w:
                    self.playerList[0].movingUp = True
                elif event.key == pygame.K_a:
                    self.playerList[0].movingLeft = True
                elif event.key == pygame.K_d:
                    self.playerList[0].movingRight = True
                # 2P 移動
                elif event.key == pygame.K_UP:
                    self.playerList[1].movingUp = True
                elif event.key == pygame.K_LEFT:
                    self.playerList[1].movingLeft = True
                elif event.key == pygame.K_RIGHT:
                    self.playerList[1].movingRight = True
                # 離開
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    return True
            # 按鍵放開
            if event.type == pygame.KEYUP:
                # 1P 移動
                if event.key == pygame.K_w:
                    self.playerList[0].movingUp = False
                elif event.key == pygame.K_a:
                    self.playerList[0].movingLeft = False
                elif event.key == pygame.K_d:
                    self.playerList[0].movingRight = False
                # 2P 移動
                elif event.key == pygame.K_UP:
                    self.playerList[1].movingUp = False
                elif event.key == pygame.K_LEFT:
                    self.playerList[1].movingLeft = False
                elif event.key == pygame.K_RIGHT:
                    self.playerList[1].movingRight = False

    def collisionBallToBall(self):          # 球碰球
        pass

    def collisionBallToBoundary(self):      # 球碰邊界
        for ball in self.ballList:
            if ball.rect.right >= self.display.width:
                ball.x_Speed *= -1
            elif ball.rect.left <= 0:
                ball.x_Speed *= -1

    def collisionBallToFloor(self):         # 球碰地板
        d = pygame.sprite.groupcollide(self.ballGroup, self.floorGroup, False, False)
        if d:
            for ball, floorList in d.items():
                for floor in floorList:
                    if ball.rect.top < floor.rect.bottom and ball.rect.bottom > floor.rect.top and ball.rect.center[0] - 30 > floor.rect.right:
                         ball.x_Speed *= -1 # 向左
                    elif ball.rect.top < floor.rect.bottom and ball.rect.bottom > floor.rect.top and ball.rect.center[0] + 30 < floor.rect.left:
                         ball.x_Speed *= -1 # 向右
                    elif ball.rect.right > floor.rect.left and ball.rect.left < floor.rect.right and ball.rect.center[1] > floor.rect.bottom:
                         ball.y_Speed = 0 # 向上
                    elif ball.rect.right > floor.rect.left and ball.rect.left < floor.rect.right and ball.rect.center[1] < floor.rect.top:
                         ball.y_Speed = ball.startSpeed # 向下

    def collisionPlayerToBall(self):        # 玩家碰球
        pass

    def collisionPlayerToBoundary(self):    # 玩家碰邊界
        for player in self.playerList:
            if player.rect.right >= self.display.width:
                player.rect.right = self.display.width
            elif player.rect.left <= 0:
                player.rect.left = 0

    def collisionPlayerToFloor(self):       # 玩家碰地板
        d = pygame.sprite.groupcollide(self.playerGroup, self.floorGroup, False, False)
        if d:
            for player, floorList in d.items():
                for floor in floorList:
                    if player.rect.top < floor.rect.bottom and player.rect.bottom > floor.rect.top and player.rect.center[0] - 30 > floor.rect.right:
                        player.rect.left = floor.rect.right # 向左
                    elif player.rect.top < floor.rect.bottom and player.rect.bottom > floor.rect.top and player.rect.center[0] + 30 < floor.rect.left:
                        player.rect.right = floor.rect.left # 向右
                    elif player.rect.right > floor.rect.left and player.rect.left < floor.rect.right and player.rect.center[1] > floor.rect.bottom:
                        player.rect.top = floor.rect.bottom # 向上
                    elif player.rect.right > floor.rect.left and player.rect.left < floor.rect.right and player.rect.center[1] < floor.rect.top:
                        player.rect.bottom = floor.rect.top # 向下
            return d.keys() # stepOnFloor

    def collisionPlayerToPlayer(self):      # 玩家碰玩家
        c = pygame.sprite.collide_rect(self.playerList[0], self.playerList[1])
        if c:
            if self.playerList[0].rect.top < self.playerList[1].rect.bottom and self.playerList[0].rect.bottom > self.playerList[1].rect.top and self.playerList[0].rect.center[0] > self.playerList[1].rect.right:
                # 0右1左
                if self.playerList[0].movingLeft and self.playerList[1].movingRight:
                    self.playerList[0].rect.x += 5
                    self.playerList[1].rect.x -= 5
                elif self.playerList[0].movingLeft or self.playerList[1].movingRight:
                    self.playerList[0].rect.x += 2.5
                    self.playerList[1].rect.x -= 2.5
            elif self.playerList[0].rect.top < self.playerList[1].rect.bottom and self.playerList[0].rect.bottom > self.playerList[1].rect.top and self.playerList[0].rect.center[0] < self.playerList[1].rect.left:
                # 0左1右
                if self.playerList[0].movingRight and self.playerList[1].movingLeft:
                    self.playerList[0].rect.x -= 5
                    self.playerList[1].rect.x += 5
                elif self.playerList[0].movingRight or self.playerList[1].movingLeft:
                    self.playerList[0].rect.x -= 2.5
                    self.playerList[1].rect.x += 2.5
            elif self.playerList[0].rect.right > self.playerList[1].rect.left and self.playerList[0].rect.left < self.playerList[1].rect.right and self.playerList[0].rect.center[1] > self.playerList[1].rect.bottom:
                # 0下1上
                self.playerList[1].rect.bottom = self.playerList[0].rect.top
                return self.playerList[1], self.playerList[0]   # stepOnPlayer, isSteped
            elif self.playerList[0].rect.right > self.playerList[1].rect.left and self.playerList[0].rect.left < self.playerList[1].rect.right and self.playerList[0].rect.center[1] < self.playerList[1].rect.top:
                # 0上1下
                self.playerList[0].rect.bottom = self.playerList[1].rect.top
                return self.playerList[0], self.playerList[1]   # stepOnPlayer, isSteped
        return None, None

    def gameOver(self):         # 遊戲結束
        if self.isOver == -1:
            self.isOver = self.detectGameOver()
        if self.isOver != -1 and not self.startCounting:
            self.startCounting = True
            self.startCountingTime = time.time()
        if self.startCounting:
            if self.passTime - self.startCountingTime > 5:   # 倒數五秒
                if self.readBestTime() < self.bestTime:
                    self.writeBestTime(self.bestTime)
                self.initObject()

    def detectGameOver(self):   # 偵測玩家與球是否掉下邊界
        ct = 0
        for player in self.playerList:
            if player.rect.top >= self.display.height:
                return ct
            ct += 1
        ct = 0
        for ball in self.ballList:
            if ball.rect.top >= self.display.height:
                return ct
            ct += 1
        return -1

    def start(self):
        # 物件初始化
        self.initObject()
        while True:
            # 按鍵事件
            if self.keyEvent():
                return -1

            # 碰撞事件
            self.collisionBallToBall()                      # 球碰球
            self.collisionBallToBoundary()                  # 球碰邊界
            self.collisionBallToFloor()                     # 球碰地板
            self.collisionPlayerToBall()                    # 玩家碰球
            self.collisionPlayerToBoundary()                # 玩家碰邊界
            stepOnFloor = self.collisionPlayerToFloor()     # 玩家碰地板
            stepOnPlayer, isSteped = self.collisionPlayerToPlayer()   # 玩家碰玩家

            # 更新位置
            self.ballGroup.update()
            self.playerGroup.update(stepOnFloor, stepOnPlayer, isSteped)

            # 計時
            self.passTime = time.time()
            if self.bestTime < self.passTime - self.startTime:
                self.bestTime = int(self.passTime - self.startTime)

            # 遊戲結束
            self.gameOver()

            # 顯示
            self.display.displayPageGame(self.ballGroup, self.floorGroup, self.playerGroup, self.startTime, self.passTime, self.bestTime, self.isOver)
            pygame.display.update()
            self.clock.tick(60)
