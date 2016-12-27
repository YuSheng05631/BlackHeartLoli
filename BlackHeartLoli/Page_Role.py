import pygame

class Page_Role:
    def __init__(self, display):
        self.display = display
        self.clock = pygame.time.Clock()
        self.id1 = 0
        self.id2 = 4
        self.dbIndex = 0
        
    def start(self):
        while True:
            # 操作事件
            for event in pygame.event.get():
                # 離開
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # 按鍵按下
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.id1 -= 1
                    elif event.key == pygame.K_d:
                        self.id1 += 1
                    elif event.key == pygame.K_LEFT:
                        self.id2 -= 1
                    elif event.key == pygame.K_RIGHT:
                        self.id2 += 1
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.dbIndex -= 1
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.dbIndex += 1
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        return self.id1, self.id2, self.dbIndex     # 進入遊戲畫面
                    if self.id1 < 0:
                        self.id1 = 4
                    elif self.id1 > 4:
                        self.id1 = 0
                    if self.id2 < 0:
                        self.id2 = 4
                    elif self.id2 > 4:
                        self.id2 = 0
                    if self.dbIndex < 0:
                        self.dbIndex = 2
                    elif self.dbIndex > 2:
                        self.dbIndex = 0
                    
            # 顯示
            self.display.displayPageRole(self.id1, self.id2, self.dbIndex)
            pygame.display.update()
            self.clock.tick(60)
