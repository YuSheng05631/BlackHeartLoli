import pygame

class Page_Menu:
    def __init__(self, display):
        self.display = display
        self.clock = pygame.time.Clock()
        self.mbIndex = 0

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
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.mbIndex -= 1
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.mbIndex += 1
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        return self.mbIndex # 離開
                    if self.mbIndex < 0:
                        self.mbIndex = 2
                    elif self.mbIndex > 2:
                        self.mbIndex = 0
            # 顯示
            self.display.displayPageMenu(self.mbIndex)
            pygame.display.update()
            self.clock.tick(60)
