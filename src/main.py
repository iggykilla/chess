import pygame
import sys


from const import *


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Copy Chess')


    def mainLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(1)
                    sys.exit(1)
        
            pygame.display.update() # last line of code


main = Main()
main.mainLoop()