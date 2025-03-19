import pygame
import sys


from const import *
from game import Game

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Copy Chess')
        self.game = Game()


    def mainLoop(self):
        
        while True:
            self.game.show_bg(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(1)
                    sys.exit(1)
        
            pygame.display.update() # last line of code


main = Main()
main.mainLoop()