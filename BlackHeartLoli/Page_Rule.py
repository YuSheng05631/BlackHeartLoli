import pygame

class Page_Rule:
    def __init__(self, display):
        self.display = display
        self.clock = pygame.time.Clock()
        self.ruleIndex = 0

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
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        self.ruleIndex += 1
                        if not self.ruleIndex < 2:
                            self.ruleIndex = 0
                            return -1   # 回到主畫面
            # 顯示
            self.display.displayPageRule(self.ruleIndex)
            pygame.display.update()
            self.clock.tick(60)
