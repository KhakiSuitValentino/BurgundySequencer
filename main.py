from math import fabs
from tkinter import W
import pygame
import os
import math

#Configuration:
pygame.init()
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

# objects = []

# def objects_test():
#      if objects != []:
#           print('objects array populated')


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
     def __init__(self, x, y, width, height, onClickFunction=None, onePress=False, isOn = False, color = '#EF0096'):
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

          self.pos = (self.x, self.y)


          self.buttonSurface = pygame.Surface((self.width, self.height))
          self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

          self.alreadyPressed = False

          # object.append(self)


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
for i in range(1,totalNumOfBtns):
     buttons.append(Button(x, y, 41,41))
     x+=35
     if(i % 16 == 0 and i != 0):
          x = 295
          y += 40




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
     # kick1Btn.draw()
     # kick2Btn.draw()
     # kick3Btn.draw()
     # kick4Btn.draw()
     # kick5Btn.draw()


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

     while run:
               

          clock.tick(FPS)
          for event in pygame.event.get():


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
               if event.type == pygame.QUIT:
                    run = False

          # for object in objects:
          #      object.process()

          draw_window()


     pygame.quit()

if __name__ == "__main__":
     main()