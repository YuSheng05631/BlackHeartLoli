import pygame, time

class Display:
    def __init__(self):
        self.width = 1024
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.image.load("Pictures/Backgound.jpg")
        self.menuButtons = [pygame.image.load("Pictures/Page_Menu_Buttons1.png"), pygame.image.load("Pictures/Page_Menu_Buttons2.png"), pygame.image.load("Pictures/Page_Menu_Buttons3.png")]
        self.ruleImages = [pygame.image.load("Pictures/rule1.png"), pygame.image.load("Pictures/rule2.png")]
        self.playerImages = self.generatePlayerImages()
        self.boxImages = [pygame.image.load("Pictures/box1.png"), pygame.image.load("Pictures/box2.png")]
        pygame.display.set_caption("Black Heart Loli")
        self.keepTextTitle = self.displayText("Black Heart Loli", x=100, y=100, size=100, italic=True)
        self.keepTextGameOver = self.displayText("Game Over", x=100, y=100, size=100)
        self.keepTextPlayerWin = [self.displayText("Player 2 Win!", x=200, y=200, size=100), self.displayText("Player 1 Win!", x=200, y=200, size=100)]

    def generatePlayerImages(self):
        playerImages = list()
        for i in range(1, 6):
            playerImages.append(pygame.image.load("Pictures/Player{}.png".format(i)))
        for i in range(0, 5):
            playerImages.append(pygame.transform.flip(playerImages[i], True, False))
        return playerImages

    def displayPageGame(self, balls, floors, players, win1, win2, startTime, passTime, bestTime, isOver):
        self.screen.blit(self.background, (0, 0))
        balls.draw(self.screen)
        floors.draw(self.screen)
        players.draw(self.screen)
        self.displayText("Player 1 Win: {} Times".format(win1), x=10, y=10, size=20)
        self.displayText("Player 2 Win: {} Times".format(win2), x=10, y=40, size=20)
        self.displayText("Pass Time: {} Sec".format(int(passTime - startTime)), x=820, y=10, size=20)
        self.displayText("Best Time: {} Sec".format(bestTime), x=820, y=40, size=20)
        if isOver != -1:
            self.displayKeepText(self.keepTextGameOver)
            self.displayKeepText(self.keepTextPlayerWin[isOver])

    def displayPageMenu(self, mbIndex):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.menuButtons[mbIndex], (100, 300))
        self.displayKeepText(self.keepTextTitle)

    def displayPageRole(self, id1, id2):
        self.screen.blit(self.background, (0, 0))
        ct = 0
        for x in range(400, 1000, 120):
            self.screen.blit(self.playerImages[ct], (x, 460))
            ct += 1
        for x in range(50, 650, 120):
            self.screen.blit(self.playerImages[ct], (x, 220))
            ct += 1
        self.displayText("Choose Role", x=20, y=20, size=80)
        self.displayText("Player 1", x=50, y=120, size=50)
        self.displayText("Player 2", x=760, y=360, size=50)
        self.screen.blit(self.boxImages[0], (15 + id1 * 120, 180))
        self.screen.blit(self.boxImages[1], (365 + id2 * 120, 420))

    def displayPageRule(self, ruleIndex):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.ruleImages[ruleIndex], (0, 0))

    def displayText(self, text, x, y, size, color=(0, 0, 0), bold=False, italic=False):
        font = pygame.font.Font("Fonts/freesansbold.ttf", size)
        font.set_bold(bold)
        font.set_italic(italic)
        textSurf = font.render(text, True, color)
        textRect = textSurf.get_rect()
        textRect.x = x
        textRect.y = y
        self.screen.blit(textSurf, textRect)
        return textSurf, textRect

    def displayKeepText(self, keepText:tuple):
        self.screen.blit(keepText[0], keepText[1])
