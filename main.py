import pygame
import os

WIDTH, HEIGHT = 922, 692
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PYGAME SEQUENCER")

FPS = 60

BACKGROUND_IMG = pygame.image.load(os.path.join('assets', 'layout.png'))

def draw_window():
     pygame.display.update()
     WIN.blit(BACKGROUND_IMG, (0, 0))


#THE GAME LOOP:
def main():
     clock = pygame.time.Clock()
     # to turn game on and off
     run = True
     while run:
          clock.tick(FPS)
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    run = False

          draw_window()


     pygame.quit()

if __name__ == "__main__":
     main()