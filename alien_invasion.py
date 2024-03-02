import sys
import pygame

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen =pygame.display.set_mode((800,600))
        pygame.display.set_caption("alien invasion game")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            self.clock.tick(60)

if __name__=='__main__':
    ai = AlienInvasion()
    ai.run_game()
