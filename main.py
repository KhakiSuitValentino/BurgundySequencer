from math import fabs
from tkinter import W
import pygame
import os
import math
from pygame import mixer

# from parser import sequence2st

#Configuration:
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("BURGUNDY SEQUENCER")
pygame.mouse.set_visible(1)
WIDTH, HEIGHT = 922, 692
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
BUTTON_CLICKBOX = 40, 40
run = False
kick1_isOn = False
kick2_isOn = False

#Images:
BACKGROUND_IMG = pygame.image.load(os.path.join('assets', 'layout.png'))
BUTTON = pygame.image.load(os.path.join('assets', "button.png"))
HITBOX = pygame.image.load(os.path.join('assets', "hitbox.png"))


# Audio
kick = 'assets/audio/kick.wav'
clap = 'assets/audio/clap.wav'
snare = 'assets/audio/snare.wav'
c_hat = 'assets/audio/c_hat.wav'
o_hat = 'assets/audio/o_hat.wav'
tom = 'assets/audio/tom.wav'
efx1 = 'assets/audio/efx1.wav'
efx2 = 'assets/audio/efx2.wav'
chord1 = 'assets/audio/chord1.wav'
chord2 = 'assets/audio/chord2.wav'
chord3 = 'assets/audio/chord3.wav'
bass1 = 'assets/audio/bass1.wav'
bass2 = 'assets/audio/bass2.wav'
bass3 = 'assets/audio/bass3.wav'

# pygame.mixer.Channel(0).play(pygame.mixer.Sound(kick))



# Events
next_sequence_event = pygame.USEREVENT + 1
pygame.time.set_timer(next_sequence_event, 500)



# Sequences
sequence1 = []




# Functions:

# def lightswitch(self,button_name):
# global kick1_isOn
# global kick2_isOn     

# print(button_name)

# match button_name:
#      case 'kick1':
#           WIN.blit(BUTTON, (312, 24))
          
#      case 'kick2':
#           WIN.blit(BUTTON, (312, 24))

#Classes
class Button():
     def __init__(self, x, y, width, height, timing=0, onClickFunction=None, onePress=False, isOn = False, color = '#EF0096'):
          self.x = x
          self.y = y
          self.width = width
          self.height = height
          self.onClickFunction = onClickFunction
          self.onePress = onePress
          # self.button_name = button_name
          self.isOn = isOn
          self.pressed = False
          self.color = color 
          self.timing = timing

          self.pos = (self.x, self.y)


          self.buttonSurface = pygame.Surface((self.width, self.height))
          self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

          self.alreadyPressed = False


     def draw(self):
          self.buttonSurface.set_alpha(0)
          pygame.draw.circle(WIN, self.color, self.pos, 14)
          self.check_click()

     def check_click(self):
          x = pygame.mouse.get_pos()[0]
          y = pygame.mouse.get_pos()[1]

          sqx = (x - self.x)**2
          sqy = (y - self.y)**2

          if math.sqrt(sqx + sqy) < 14:
               if pygame.mouse.get_pressed()[0]:
                      self.pressed = True
               else:
                    if self.pressed == True:
                         if self.color == '#EF0096':
                              self.color = '#ffffff'
                              self.pressed = False
                         else:
                              self.color = '#EF0096'
                              self.pressed = False


          # if self.buttonRect.collidepoint(mousePos):
          #      if pygame.mouse.get_pressed()[0]:
          #           self.pressed = True
          #      else:
          #           if self.pressed == True:
          #                if self.color == '#EF0096':
          #                     self.color = '#ffffff'
          #                     self.pressed = False
          #                else:
          #                     self.color = '#EF0096'
          #                     self.pressed = False


                         




          # mousePos = pygame.mouse.get_pos()
          # # self.buttonSurface.blit(HITBOX, (0, 0))
          # self.buttonSurface.set_alpha(0)
          # if self.buttonRect.collidepoint(mousePos):
          #      if pygame.mouse.get_pressed()[0]:
          #           self.pressed = True
          #      else:
          #           if self.pressed == True:
          #                print('lit')
          #                self.pressed = False
          #           # if self.onePress:
          #           #      self.onClickFunction(self, self.button_name)

          #           # elif not self.alreadyPressed:
          #           #      self.onClickFunction()
          #           #      self.alreadyPressed = True

          #           # else:
          #           #      self.alreadyPressed = False

          #           WIN.blit(self.buttonSurface, self.buttonRect)



# def myFunction():
#      print('myFunction Button Pressed')




# Buttons
# kick1Btn = Button(277, 24, 41, 41)
x = 295
y = 45
buttons = []
totalNumOfBtns = 225
timing = 0
for i in range(1,totalNumOfBtns):
     buttons.append(Button(x, y, 41,41, timing))
     x+=35
     timing+=500 
     if(i % 16 == 0 and i != 0):
          timing = 0
          x = 295
          y += 40


playButtons = []
x = 295
y = 605
timing = 0
for i in range(16):
     playButtons.append(Button(x,y,41,41, timing, False, False, False, '#1C0020'))
     x+= 35
     timing+= 500




# kick1Btn = Button(295, 45, 41, 41)
# kick2Btn = Button(334, 45, 41, 41)
# kick3Btn = Button(368, 45, 41, 41)
# kick4Btn = Button(402, 45, 41, 41)
# kick5Btn = Button(436, 45, 41, 41)
# kick6Btn = Button(472, 45, 41, 41)
# kick57tn = Button(508, 45, 41, 41)




# kick4Btn = Button(295, 45, 41, 41)
# kick5Btn = Button(295, 45, 41, 41)
# kick6Btn = Button(295, 45, 41, 41)
# kick7Btn = Button(295, 45, 41, 41)
# kick8Btn = Button(295, 45, 41, 41)
# kick9Btn = Button(295, 45, 41, 41)
# kick10Btn = Button(295, 45, 41, 41)
# kick11Btn = Button(295, 45, 41, 41)
# kick12Btn = Button(295, 45, 41, 41)
# kick13Btn = Button(295, 45, 41, 41)
# kick14Btn = Button(295, 45, 41, 41)
# kick15Btn = Button(295, 45, 41, 41)
# kick16Btn = Button(295, 45, 41, 41)







# Runs inside game loop
def draw_window():
     pygame.display.update()
     WIN.blit(BACKGROUND_IMG, (0, 0))

     for i in range(224):
          buttons[i].draw()

     for i in range(16):
          playButtons[i].draw()
          

     sequence = {
          1: sequence1,
     }

     # for i in range(len(sequence[1])):
     #      pygame.mixer.Channel(i).play(pygame.mixer.Sound(kick))
     #      pygame.mixer.Channel(i).play(pygame.mixer.Sound(chord1))




     # WIN.blit(BUTTON, (347, 64))
     # WIN.blit(HITBOX, (277, 64))

     # kick1 = Button('kick1', 277, 24, 41, 41, lightswitch, myFunction)
     # kick2 = Button('kick2', 312, 24, 41, 41, lightswitch, myFunction)


#THE GAME LOOP:
def main():

     # kick1 = WIN.blit(HITBOX, (277, 24)) 
     # kick1_on = False

     

     run = True
     clock = pygame.time.Clock()

     playButtonIndex = 0
     sequenceCounter = 0

     while run:
               

          clock.tick(FPS)
          for event in pygame.event.get():
               draw_window()

               if event.type == pygame.QUIT:
                    run = False
               elif event.type == next_sequence_event:
                    if sequenceCounter == 0:
                         if buttons[0].color == '#ffffff':
                              pygame.mixer.Channel(0).play(pygame.mixer.Sound(kick))
                         if buttons[16].color == '#ffffff':
                              pygame.mixer.Channel(0).play(pygame.mixer.Sound(kick))
                    if (sequenceCounter > 15):
                         sequenceCounter = 0



                    # Play Button Hughlighting Logic
                    if(playButtonIndex == 15):
                         playButtons[playButtonIndex].color = '#FFAFAF'
                         playButtons[14].color = '#1C0020'

                         playButtonIndex = 0
                    else:
                         if (playButtonIndex == 0):
                              playButtons[playButtonIndex].color = '#FFAFAF'
                              playButtons[15].color = '#1C0020'

                         else:
                              playButtons[playButtonIndex].color = '#FFAFAF'
                              playButtons[playButtonIndex-1].color = '#1C0020'

                         playButtonIndex+=1
                         sequenceCounter+=1




               # #mouse click on button:
               # if event.type == pygame.MOUSEBUTTONDOWN:
               #      # pos = pygame.mouse.get_pos()
                         
               #      if kick1.collidepoint(pygame.mouse.get_pos()) and kick1 == WIN.blit(BUTTON, (277, 24)) and kick1_on == True:
               #           kick1_on = False
               #           kick1 = WIN.blit(HITBOX, (277, 24))
               #           print('kick1 clicked and kick1 true > false')
                    
               #      if kick1.collidepoint(pygame.mouse.get_pos()) and kick1 == WIN.blit(HITBOX, (277, 24)):
               #           kick1_on = True
               #           kick1 = WIN.blit(BUTTON, (277, 24)) 
               #           print('kick1 clicked and kick1 false > true')
                         
                    

               #to quit game:
              

          # for object in objects:
          #      object.process()



     pygame.quit()

if __name__ == "__main__":
     main()