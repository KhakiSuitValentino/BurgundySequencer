import pygame
import os

#Globals:
WIDTH, HEIGHT = 922, 692
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BURGUNDY SEQUENCER")

FPS = 10
BUTTON_CLICKBOX = 40, 40

#Images:
BACKGROUND_IMG = pygame.image.load(os.path.join('assets', 'layout.png'))
BUTTON = pygame.image.load(os.path.join('assets', "button.png"))

def draw_window():
     pygame.display.update()
     WIN.blit(BACKGROUND_IMG, (0, 0))
     WIN.blit(BUTTON, (277, 24))
     WIN.blit(BUTTON, (347, 64))


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