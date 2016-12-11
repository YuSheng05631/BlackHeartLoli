import pygame

class Page_Role:
    def __init__(self, display):
        self.display = display
        self.clock = pygame.time.Clock()
        self.id1 = 0
        self.id2 = 4
        
    def start(self):
        while True:
            # �ާ@�ƥ�
            for event in pygame.event.get():
                # ���}
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # ������U
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.id1 -= 1
                    elif event.key == pygame.K_d:
                        self.id1 += 1
                    elif event.key == pygame.K_LEFT:
                        self.id2 -= 1
                    elif event.key == pygame.K_RIGHT:
                        self.id2 += 1
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        return self.id1, self.id2   # �i�J�C���e��
                    if self.id1 < 0:
                        self.id1 = 4
                    elif self.id1 > 4:
                        self.id1 = 0
                    if self.id2 < 0:
                        self.id2 = 4
                    elif self.id2 > 4:
                        self.id2 = 0
            # ���
            self.display.displayPageRole(self.id1, self.id2)
            pygame.display.update()
            self.clock.tick(60)
