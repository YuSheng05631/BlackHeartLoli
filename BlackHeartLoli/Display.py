import pygame

class Display:
    def __init__(self):
        self.width = 1024
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.image.load("Pictures/Backgound.jpg")
        self.menuButtons = [pygame.image.load("Pictures/Page_Menu_Buttons1.png"), pygame.image.load("Pictures/Page_Menu_Buttons2.png"), pygame.image.load("Pictures/Page_Menu_Buttons3.png")]
        pygame.display.set_caption("Black Heart Loli")

    def displayPageGame(self, balls, floors, players):
        self.screen.blit(self.background, (0, 0))
        balls.draw(self.screen)
        floors.draw(self.screen)
        players.draw(self.screen)

    def displayPageMenu(self, mbIndex):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.menuButtons[mbIndex], (100, 300))
        self.displayText("Black Heart Loli", x=100, y=100, size=100, italic=True)

    def displayPageRule(self):
        self.screen.blit(self.background, (0, 0))
        self.displayText("Rule ...", x=100, y=100, size=100)

    def displayText(self, text, x, y, size, color=(0, 0, 0), bold=False, italic=False):
        font = pygame.font.Font("Fonts/freesansbold.ttf", size)
        font.set_bold(bold)
        font.set_italic(italic)
        textSurf = font.render(text, True, color)
        textRect = textSurf.get_rect()
        textRect.x = x
        textRect.y = y
        self.screen.blit(textSurf, textRect)
