import pygame
from Display import Display
from Page_Game import Page_Game
from Page_Menu import Page_Menu
from Page_Rule import Page_Rule

pygame.init()
pygame.mixer.init()

class main:
    def __init__(self):
        self.display = Display()
        self.pageGame = Page_Game(self.display)
        self.pageMenu = Page_Menu(self.display)
        self.pageRule = Page_Rule(self.display)
        self.mbIndex = -1
        pygame.mixer.music.load("Music/Daydream cafe (Instrumental).mp3")
        pygame.mixer.music.play(loops=-1)
        self.start()

    def start(self):
        while True:
            if self.mbIndex == -1:
                self.mbIndex = self.pageMenu.start()    # 主畫面
            elif self.mbIndex == 0:
                self.mbIndex = self.pageGame.start()    # 遊戲畫面
            elif self.mbIndex == 1:
                self.mbIndex = self.pageRule.start()    # 規則畫面
            elif self.mbIndex == 2:
                break   # 離開
        pygame.quit()
        quit()

if __name__ == '__main__':
    main()
