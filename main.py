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

pygame.mixer.set_num_channels(20)



# Events
next_sequence_event = pygame.USEREVENT + 1
pygame.time.set_timer(next_sequence_event, 150)
isPlaying = False


# Sequences
sequence1 = []

#Classes
class Button():
     def __init__(self, x, y, width, height, timing=0, onClickFunction=None, onePress=False, isOn = False, color = '#EF0096'):
          self.x = x
          self.y = y
          self.width = width
          self.height = height
          self.onClickFunction = onClickFunction
          self.onePress = onePress
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


# Buttons
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


#THE GAME LOOP:
def main():

     run = True
     clock = pygame.time.Clock()

     playButtonIndex = 0
     sequenceCounter = 0
     isPlaying = False

     btnindex = 0

     while run:
               

          clock.tick(FPS)
          for event in pygame.event.get():
               draw_window()

               if event.type == pygame.QUIT:
                    run = False

               elif event.type == pygame.KEYDOWN and isPlaying == False:
                    isPlaying = True

               elif event.type == pygame.KEYDOWN and isPlaying == True:
                    isPlaying = False

               if isPlaying == True:
                    event.type == next_sequence_event
                    print(sequenceCounter)
                    if sequenceCounter == 1:
                         if buttons[0].color == '#ffffff':
                              pygame.mixer.Channel(0).play(pygame.mixer.Sound(kick))
                         if buttons[16].color == '#ffffff':
                              pygame.mixer.Channel(1).play(pygame.mixer.Sound(clap))
                         if buttons[32].color == '#ffffff':
                              pygame.mixer.Channel(2).play(pygame.mixer.Sound(snare))
                         if buttons[48].color == '#ffffff':
                              pygame.mixer.Channel(3).play(pygame.mixer.Sound(c_hat))
                         if buttons[64].color == '#ffffff':
                              pygame.mixer.Channel(4).play(pygame.mixer.Sound(o_hat))
                         if buttons[80].color == '#ffffff':
                              pygame.mixer.Channel(5).play(pygame.mixer.Sound(tom))
                         if buttons[96].color == '#ffffff':
                              pygame.mixer.Channel(6).play(pygame.mixer.Sound(efx1))
                         if buttons[112].color == '#ffffff':
                              pygame.mixer.Channel(7).play(pygame.mixer.Sound(efx2))
                         if buttons[128].color == '#ffffff':
                              pygame.mixer.Channel(8).play(pygame.mixer.Sound(chord1))
                         if buttons[144].color == '#ffffff':
                              pygame.mixer.Channel(9).play(pygame.mixer.Sound(chord2))
                         if buttons[160].color == '#ffffff':
                              pygame.mixer.Channel(10).play(pygame.mixer.Sound(chord3))
                         if buttons[176].color == '#ffffff':
                              pygame.mixer.Channel(11).play(pygame.mixer.Sound(bass1))
                         if buttons[192].color == '#ffffff':
                              pygame.mixer.Channel(12).play(pygame.mixer.Sound(bass2))
                         if buttons[208].color == '#ffffff':
                              pygame.mixer.Channel(13).play(pygame.mixer.Sound(bass3))
                    
                    if sequenceCounter == 2:
                           if buttons[1].color == '#ffffff':
                              pygame.mixer.Channel(0).play(pygame.mixer.Sound(kick))
                           if buttons[17].color == '#ffffff':
                              pygame.mixer.Channel(1).play(pygame.mixer.Sound(clap))
                           if buttons[33].color == '#ffffff':
                              pygame.mixer.Channel(2).play(pygame.mixer.Sound(snare))
                           if buttons[49].color == '#ffffff':
                              pygame.mixer.Channel(3).play(pygame.mixer.Sound(c_hat))
                           if buttons[65].color == '#ffffff':
                              pygame.mixer.Channel(4).play(pygame.mixer.Sound(o_hat))
                           if buttons[81].color == '#ffffff':
                              pygame.mixer.Channel(5).play(pygame.mixer.Sound(tom))
                           if buttons[97].color == '#ffffff':
                              pygame.mixer.Channel(6).play(pygame.mixer.Sound(efx1))
                           if buttons[113].color == '#ffffff':
                              pygame.mixer.Channel(7).play(pygame.mixer.Sound(efx2))
                           if buttons[129].color == '#ffffff':
                              pygame.mixer.Channel(8).play(pygame.mixer.Sound(chord1))
                           if buttons[145].color == '#ffffff':
                              pygame.mixer.Channel(9).play(pygame.mixer.Sound(chord2))
                           if buttons[161].color == '#ffffff':
                              pygame.mixer.Channel(10).play(pygame.mixer.Sound(chord3))
                           if buttons[177].color == '#ffffff':
                              pygame.mixer.Channel(11).play(pygame.mixer.Sound(bass1))
                           if buttons[193].color == '#ffffff':
                              pygame.mixer.Channel(12).play(pygame.mixer.Sound(bass2))
                           if buttons[209].color == '#ffffff':
                              pygame.mixer.Channel(13).play(pygame.mixer.Sound(bass3))

                    if sequenceCounter == 3:
                           if buttons[2].color == '#ffffff':
                              pygame.mixer.Channel(0).play(pygame.mixer.Sound(kick))
                           if buttons[18].color == '#ffffff':
                              pygame.mixer.Channel(1).play(pygame.mixer.Sound(clap))
                           if buttons[34].color == '#ffffff':
                              pygame.mixer.Channel(2).play(pygame.mixer.Sound(snare))
                           if buttons[50].color == '#ffffff':
                              pygame.mixer.Channel(3).play(pygame.mixer.Sound(c_hat))
                           if buttons[66].color == '#ffffff':
                              pygame.mixer.Channel(4).play(pygame.mixer.Sound(o_hat))
                           if buttons[82].color == '#ffffff':
                              pygame.mixer.Channel(5).play(pygame.mixer.Sound(tom))
                           if buttons[98].color == '#ffffff':
                              pygame.mixer.Channel(6).play(pygame.mixer.Sound(efx1))
                           if buttons[114].color == '#ffffff':
                              pygame.mixer.Channel(7).play(pygame.mixer.Sound(efx2))
                           if buttons[130].color == '#ffffff':
                              pygame.mixer.Channel(8).play(pygame.mixer.Sound(chord1))
                           if buttons[146].color == '#ffffff':
                              pygame.mixer.Channel(9).play(pygame.mixer.Sound(chord2))
                           if buttons[162].color == '#ffffff':
                              pygame.mixer.Channel(10).play(pygame.mixer.Sound(chord3))
                           if buttons[178].color == '#ffffff':
                              pygame.mixer.Channel(11).play(pygame.mixer.Sound(bass1))
                           if buttons[194].color == '#ffffff':
                              pygame.mixer.Channel(12).play(pygame.mixer.Sound(bass2))
                           if buttons[210].color == '#ffffff':
                              pygame.mixer.Channel(13).play(pygame.mixer.Sound(bass3))
                 
                    if sequenceCounter == 4:
                           if buttons[3].color == '#ffffff':
                              pygame.mixer.Channel(0).play(pygame.mixer.Sound(kick))
                           if buttons[19].color == '#ffffff':
                              pygame.mixer.Channel(1).play(pygame.mixer.Sound(clap))
                           if buttons[35].color == '#ffffff':
                              pygame.mixer.Channel(2).play(pygame.mixer.Sound(snare))
                           if buttons[51].color == '#ffffff':
                              pygame.mixer.Channel(3).play(pygame.mixer.Sound(c_hat))
                           if buttons[67].color == '#ffffff':
                              pygame.mixer.Channel(4).play(pygame.mixer.Sound(o_hat))
                           if buttons[83].color == '#ffffff':
                              pygame.mixer.Channel(5).play(pygame.mixer.Sound(tom))
                           if buttons[99].color == '#ffffff':
                              pygame.mixer.Channel(6).play(pygame.mixer.Sound(efx1))
                           if buttons[115].color == '#ffffff':
                              pygame.mixer.Channel(7).play(pygame.mixer.Sound(efx2))
                           if buttons[131].color == '#ffffff':
                              pygame.mixer.Channel(8).play(pygame.mixer.Sound(chord1))
                           if buttons[147].color == '#ffffff':
                              pygame.mixer.Channel(9).play(pygame.mixer.Sound(chord2))
                           if buttons[163].color == '#ffffff':
                              pygame.mixer.Channel(10).play(pygame.mixer.Sound(chord3))
                           if buttons[179].color == '#ffffff':
                              pygame.mixer.Channel(11).play(pygame.mixer.Sound(bass1))
                           if buttons[195].color == '#ffffff':
                              pygame.mixer.Channel(12).play(pygame.mixer.Sound(bass2))
                           if buttons[211].color == '#ffffff':
                              pygame.mixer.Channel(13).play(pygame.mixer.Sound(bass3))

                    if sequenceCounter == 5:
                           if buttons[4].color == '#ffffff':
                              pygame.mixer.Channel(0).play(pygame.mixer.Sound(kick))
                           if buttons[20].color == '#ffffff':
                              pygame.mixer.Channel(1).play(pygame.mixer.Sound(clap))
                           if buttons[36].color == '#ffffff':
                              pygame.mixer.Channel(2).play(pygame.mixer.Sound(snare))
                           if buttons[52].color == '#ffffff':
                              pygame.mixer.Channel(3).play(pygame.mixer.Sound(c_hat))
                           if buttons[68].color == '#ffffff':
                              pygame.mixer.Channel(4).play(pygame.mixer.Sound(o_hat))
                           if buttons[84].color == '#ffffff':
                              pygame.mixer.Channel(5).play(pygame.mixer.Sound(tom))
                           if buttons[100].color == '#ffffff':
                              pygame.mixer.Channel(6).play(pygame.mixer.Sound(efx1))
                           if buttons[116].color == '#ffffff':
                              pygame.mixer.Channel(7).play(pygame.mixer.Sound(efx2))
                           if buttons[132].color == '#ffffff':
                              pygame.mixer.Channel(8).play(pygame.mixer.Sound(chord1))
                           if buttons[148].color == '#ffffff':
                              pygame.mixer.Channel(9).play(pygame.mixer.Sound(chord2))
                           if buttons[164].color == '#ffffff':
                              pygame.mixer.Channel(10).play(pygame.mixer.Sound(chord3))
                           if buttons[180].color == '#ffffff':
                              pygame.mixer.Channel(11).play(pygame.mixer.Sound(bass1))
                           if buttons[196].color == '#ffffff':
                              pygame.mixer.Channel(12).play(pygame.mixer.Sound(bass2))
                           if buttons[212].color == '#ffffff':
                              pygame.mixer.Channel(13).play(pygame.mixer.Sound(bass3))

                    if sequenceCounter == 6:
                           if buttons[5].color == '#ffffff':
                              pygame.mixer.Channel(0).play(pygame.mixer.Sound(kick))
                           if buttons[21].color == '#ffffff':
                              pygame.mixer.Channel(1).play(pygame.mixer.Sound(clap))
                           if buttons[37].color == '#ffffff':
                              pygame.mixer.Channel(2).play(pygame.mixer.Sound(snare))
                           if buttons[53].color == '#ffffff':
                              pygame.mixer.Channel(3).play(pygame.mixer.Sound(c_hat))
                           if buttons[69].color == '#ffffff':
                              pygame.mixer.Channel(4).play(pygame.mixer.Sound(o_hat))
                           if buttons[85].color == '#ffffff':
                              pygame.mixer.Channel(5).play(pygame.mixer.Sound(tom))
                           if buttons[101].color == '#ffffff':
                              pygame.mixer.Channel(6).play(pygame.mixer.Sound(efx1))
                           if buttons[117].color == '#ffffff':
                              pygame.mixer.Channel(7).play(pygame.mixer.Sound(efx2))
                           if buttons[133].color == '#ffffff':
                              pygame.mixer.Channel(8).play(pygame.mixer.Sound(chord1))
                           if buttons[149].color == '#ffffff':
                              pygame.mixer.Channel(9).play(pygame.mixer.Sound(chord2))
                           if buttons[165].color == '#ffffff':
                              pygame.mixer.Channel(10).play(pygame.mixer.Sound(chord3))
                           if buttons[181].color == '#ffffff':
                              pygame.mixer.Channel(11).play(pygame.mixer.Sound(bass1))
                           if buttons[197].color == '#ffffff':
                              pygame.mixer.Channel(12).play(pygame.mixer.Sound(bass2))
                           if buttons[213].color == '#ffffff':
                              pygame.mixer.Channel(13).play(pygame.mixer.Sound(bass3))

                    if sequenceCounter == 7:
                           if buttons[6].color == '#ffffff':
                              pygame.mixer.Channel(0).play(pygame.mixer.Sound(kick))
                           if buttons[22].color == '#ffffff':
                              pygame.mixer.Channel(1).play(pygame.mixer.Sound(clap))
                           if buttons[38].color == '#ffffff':
                              pygame.mixer.Channel(2).play(pygame.mixer.Sound(snare))
                           if buttons[54].color == '#ffffff':
                              pygame.mixer.Channel(3).play(pygame.mixer.Sound(c_hat))
                           if buttons[70].color == '#ffffff':
                              pygame.mixer.Channel(4).play(pygame.mixer.Sound(o_hat))
                           if buttons[86].color == '#ffffff':
                              pygame.mixer.Channel(5).play(pygame.mixer.Sound(tom))
                           if buttons[102].color == '#ffffff':
                              pygame.mixer.Channel(6).play(pygame.mixer.Sound(efx1))
                           if buttons[118].color == '#ffffff':
                              pygame.mixer.Channel(7).play(pygame.mixer.Sound(efx2))
                           if buttons[134].color == '#ffffff':
                              pygame.mixer.Channel(8).play(pygame.mixer.Sound(chord1))
                           if buttons[150].color == '#ffffff':
                              pygame.mixer.Channel(9).play(pygame.mixer.Sound(chord2))
                           if buttons[166].color == '#ffffff':
                              pygame.mixer.Channel(10).play(pygame.mixer.Sound(chord3))
                           if buttons[182].color == '#ffffff':
                              pygame.mixer.Channel(11).play(pygame.mixer.Sound(bass1))
                           if buttons[198].color == '#ffffff':
                              pygame.mixer.Channel(12).play(pygame.mixer.Sound(bass2))
                           if buttons[214].color == '#ffffff':
                              pygame.mixer.Channel(13).play(pygame.mixer.Sound(bass3))

                    if sequenceCounter == 8:
                           if buttons[7].color == '#ffffff':
                              pygame.mixer.Channel(0).play(pygame.mixer.Sound(kick))
                           if buttons[23].color == '#ffffff':
                              pygame.mixer.Channel(1).play(pygame.mixer.Sound(clap))
                           if buttons[39].color == '#ffffff':
                              pygame.mixer.Channel(2).play(pygame.mixer.Sound(snare))
                           if buttons[55].color == '#ffffff':
                              pygame.mixer.Channel(3).play(pygame.mixer.Sound(c_hat))
                           if buttons[71].color == '#ffffff':
                              pygame.mixer.Channel(4).play(pygame.mixer.Sound(o_hat))
                           if buttons[87].color == '#ffffff':
                              pygame.mixer.Channel(5).play(pygame.mixer.Sound(tom))
                           if buttons[103].color == '#ffffff':
                              pygame.mixer.Channel(6).play(pygame.mixer.Sound(efx1))
                           if buttons[119].color == '#ffffff':
                              pygame.mixer.Channel(7).play(pygame.mixer.Sound(efx2))
                           if buttons[135].color == '#ffffff':
                              pygame.mixer.Channel(8).play(pygame.mixer.Sound(chord1))
                           if buttons[151].color == '#ffffff':
                              pygame.mixer.Channel(9).play(pygame.mixer.Sound(chord2))
                           if buttons[167].color == '#ffffff':
                              pygame.mixer.Channel(10).play(pygame.mixer.Sound(chord3))
                           if buttons[183].color == '#ffffff':
                              pygame.mixer.Channel(11).play(pygame.mixer.Sound(bass1))
                           if buttons[199].color == '#ffffff':
                              pygame.mixer.Channel(12).play(pygame.mixer.Sound(bass2))
                           if buttons[215].color == '#ffffff':
                              pygame.mixer.Channel(13).play(pygame.mixer.Sound(bass3))

                    if sequenceCounter == 9:
                           if buttons[8].color == '#ffffff':
                              pygame.mixer.Channel(0).play(pygame.mixer.Sound(kick))
                           if buttons[24].color == '#ffffff':
                              pygame.mixer.Channel(1).play(pygame.mixer.Sound(clap))
                           if buttons[40].color == '#ffffff':
                              pygame.mixer.Channel(2).play(pygame.mixer.Sound(snare))
                           if buttons[56].color == '#ffffff':
                              pygame.mixer.Channel(3).play(pygame.mixer.Sound(c_hat))
                           if buttons[72].color == '#ffffff':
                              pygame.mixer.Channel(4).play(pygame.mixer.Sound(o_hat))
                           if buttons[88].color == '#ffffff':
                              pygame.mixer.Channel(5).play(pygame.mixer.Sound(tom))
                           if buttons[104].color == '#ffffff':
                              pygame.mixer.Channel(6).play(pygame.mixer.Sound(efx1))
                           if buttons[120].color == '#ffffff':
                              pygame.mixer.Channel(7).play(pygame.mixer.Sound(efx2))
                           if buttons[136].color == '#ffffff':
                              pygame.mixer.Channel(8).play(pygame.mixer.Sound(chord1))
                           if buttons[152].color == '#ffffff':
                              pygame.mixer.Channel(9).play(pygame.mixer.Sound(chord2))
                           if buttons[168].color == '#ffffff':
                              pygame.mixer.Channel(10).play(pygame.mixer.Sound(chord3))
                           if buttons[184].color == '#ffffff':
                              pygame.mixer.Channel(11).play(pygame.mixer.Sound(bass1))
                           if buttons[200].color == '#ffffff':
                              pygame.mixer.Channel(12).play(pygame.mixer.Sound(bass2))
                           if buttons[216].color == '#ffffff':
                              pygame.mixer.Channel(13).play(pygame.mixer.Sound(bass3))

                    if sequenceCounter == 10:
                           if buttons[9].color == '#ffffff':
                              pygame.mixer.Channel(0).play(pygame.mixer.Sound(kick))
                           if buttons[25].color == '#ffffff':
                              pygame.mixer.Channel(1).play(pygame.mixer.Sound(clap))
                           if buttons[41].color == '#ffffff':
                              pygame.mixer.Channel(2).play(pygame.mixer.Sound(snare))
                           if buttons[57].color == '#ffffff':
                              pygame.mixer.Channel(3).play(pygame.mixer.Sound(c_hat))
                           if buttons[73].color == '#ffffff':
                              pygame.mixer.Channel(4).play(pygame.mixer.Sound(o_hat))
                           if buttons[89].color == '#ffffff':
                              pygame.mixer.Channel(5).play(pygame.mixer.Sound(tom))
                           if buttons[105].color == '#ffffff':
                              pygame.mixer.Channel(6).play(pygame.mixer.Sound(efx1))
                           if buttons[121].color == '#ffffff':
                              pygame.mixer.Channel(7).play(pygame.mixer.Sound(efx2))
                           if buttons[137].color == '#ffffff':
                              pygame.mixer.Channel(8).play(pygame.mixer.Sound(chord1))
                           if buttons[153].color == '#ffffff':
                              pygame.mixer.Channel(9).play(pygame.mixer.Sound(chord2))
                           if buttons[169].color == '#ffffff':
                              pygame.mixer.Channel(10).play(pygame.mixer.Sound(chord3))
                           if buttons[185].color == '#ffffff':
                              pygame.mixer.Channel(11).play(pygame.mixer.Sound(bass1))
                           if buttons[201].color == '#ffffff':
                              pygame.mixer.Channel(12).play(pygame.mixer.Sound(bass2))
                           if buttons[217].color == '#ffffff':
                              pygame.mixer.Channel(13).play(pygame.mixer.Sound(bass3))

                    if sequenceCounter == 11:
                           if buttons[10].color == '#ffffff':
                              pygame.mixer.Channel(0).play(pygame.mixer.Sound(kick))
                           if buttons[26].color == '#ffffff':
                              pygame.mixer.Channel(1).play(pygame.mixer.Sound(clap))
                           if buttons[42].color == '#ffffff':
                              pygame.mixer.Channel(2).play(pygame.mixer.Sound(snare))
                           if buttons[58].color == '#ffffff':
                              pygame.mixer.Channel(3).play(pygame.mixer.Sound(c_hat))
                           if buttons[74].color == '#ffffff':
                              pygame.mixer.Channel(4).play(pygame.mixer.Sound(o_hat))
                           if buttons[90].color == '#ffffff':
                              pygame.mixer.Channel(5).play(pygame.mixer.Sound(tom))
                           if buttons[106].color == '#ffffff':
                              pygame.mixer.Channel(6).play(pygame.mixer.Sound(efx1))
                           if buttons[122].color == '#ffffff':
                              pygame.mixer.Channel(7).play(pygame.mixer.Sound(efx2))
                           if buttons[138].color == '#ffffff':
                              pygame.mixer.Channel(8).play(pygame.mixer.Sound(chord1))
                           if buttons[154].color == '#ffffff':
                              pygame.mixer.Channel(9).play(pygame.mixer.Sound(chord2))
                           if buttons[170].color == '#ffffff':
                              pygame.mixer.Channel(10).play(pygame.mixer.Sound(chord3))
                           if buttons[186].color == '#ffffff':
                              pygame.mixer.Channel(11).play(pygame.mixer.Sound(bass1))
                           if buttons[202].color == '#ffffff':
                              pygame.mixer.Channel(12).play(pygame.mixer.Sound(bass2))
                           if buttons[218].color == '#ffffff':
                              pygame.mixer.Channel(13).play(pygame.mixer.Sound(bass3))

                    if sequenceCounter == 12:
                           if buttons[11].color == '#ffffff':
                              pygame.mixer.Channel(0).play(pygame.mixer.Sound(kick))
                           if buttons[27].color == '#ffffff':
                              pygame.mixer.Channel(1).play(pygame.mixer.Sound(clap))
                           if buttons[43].color == '#ffffff':
                              pygame.mixer.Channel(2).play(pygame.mixer.Sound(snare))
                           if buttons[59].color == '#ffffff':
                              pygame.mixer.Channel(3).play(pygame.mixer.Sound(c_hat))
                           if buttons[75].color == '#ffffff':
                              pygame.mixer.Channel(4).play(pygame.mixer.Sound(o_hat))
                           if buttons[91].color == '#ffffff':
                              pygame.mixer.Channel(5).play(pygame.mixer.Sound(tom))
                           if buttons[107].color == '#ffffff':
                              pygame.mixer.Channel(6).play(pygame.mixer.Sound(efx1))
                           if buttons[123].color == '#ffffff':
                              pygame.mixer.Channel(7).play(pygame.mixer.Sound(efx2))
                           if buttons[139].color == '#ffffff':
                              pygame.mixer.Channel(8).play(pygame.mixer.Sound(chord1))
                           if buttons[155].color == '#ffffff':
                              pygame.mixer.Channel(9).play(pygame.mixer.Sound(chord2))
                           if buttons[171].color == '#ffffff':
                              pygame.mixer.Channel(10).play(pygame.mixer.Sound(chord3))
                           if buttons[187].color == '#ffffff':
                              pygame.mixer.Channel(11).play(pygame.mixer.Sound(bass1))
                           if buttons[203].color == '#ffffff':
                              pygame.mixer.Channel(12).play(pygame.mixer.Sound(bass2))
                           if buttons[219].color == '#ffffff':
                              pygame.mixer.Channel(13).play(pygame.mixer.Sound(bass3))

                    if sequenceCounter == 13:
                           if buttons[12].color == '#ffffff':
                              pygame.mixer.Channel(0).play(pygame.mixer.Sound(kick))
                           if buttons[28].color == '#ffffff':
                              pygame.mixer.Channel(1).play(pygame.mixer.Sound(clap))
                           if buttons[44].color == '#ffffff':
                              pygame.mixer.Channel(2).play(pygame.mixer.Sound(snare))
                           if buttons[60].color == '#ffffff':
                              pygame.mixer.Channel(3).play(pygame.mixer.Sound(c_hat))
                           if buttons[76].color == '#ffffff':
                              pygame.mixer.Channel(4).play(pygame.mixer.Sound(o_hat))
                           if buttons[92].color == '#ffffff':
                              pygame.mixer.Channel(5).play(pygame.mixer.Sound(tom))
                           if buttons[108].color == '#ffffff':
                              pygame.mixer.Channel(6).play(pygame.mixer.Sound(efx1))
                           if buttons[124].color == '#ffffff':
                              pygame.mixer.Channel(7).play(pygame.mixer.Sound(efx2))
                           if buttons[140].color == '#ffffff':
                              pygame.mixer.Channel(8).play(pygame.mixer.Sound(chord1))
                           if buttons[156].color == '#ffffff':
                              pygame.mixer.Channel(9).play(pygame.mixer.Sound(chord2))
                           if buttons[172].color == '#ffffff':
                              pygame.mixer.Channel(10).play(pygame.mixer.Sound(chord3))
                           if buttons[188].color == '#ffffff':
                              pygame.mixer.Channel(11).play(pygame.mixer.Sound(bass1))
                           if buttons[204].color == '#ffffff':
                              pygame.mixer.Channel(12).play(pygame.mixer.Sound(bass2))
                           if buttons[220].color == '#ffffff':
                              pygame.mixer.Channel(13).play(pygame.mixer.Sound(bass3))

                    if sequenceCounter == 14:
                           if buttons[13].color == '#ffffff':
                              pygame.mixer.Channel(0).play(pygame.mixer.Sound(kick))
                           if buttons[29].color == '#ffffff':
                              pygame.mixer.Channel(1).play(pygame.mixer.Sound(clap))
                           if buttons[45].color == '#ffffff':
                              pygame.mixer.Channel(2).play(pygame.mixer.Sound(snare))
                           if buttons[61].color == '#ffffff':
                              pygame.mixer.Channel(3).play(pygame.mixer.Sound(c_hat))
                           if buttons[77].color == '#ffffff':
                              pygame.mixer.Channel(4).play(pygame.mixer.Sound(o_hat))
                           if buttons[93].color == '#ffffff':
                              pygame.mixer.Channel(5).play(pygame.mixer.Sound(tom))
                           if buttons[109].color == '#ffffff':
                              pygame.mixer.Channel(6).play(pygame.mixer.Sound(efx1))
                           if buttons[125].color == '#ffffff':
                              pygame.mixer.Channel(7).play(pygame.mixer.Sound(efx2))
                           if buttons[141].color == '#ffffff':
                              pygame.mixer.Channel(8).play(pygame.mixer.Sound(chord1))
                           if buttons[157].color == '#ffffff':
                              pygame.mixer.Channel(9).play(pygame.mixer.Sound(chord2))
                           if buttons[173].color == '#ffffff':
                              pygame.mixer.Channel(10).play(pygame.mixer.Sound(chord3))
                           if buttons[189].color == '#ffffff':
                              pygame.mixer.Channel(11).play(pygame.mixer.Sound(bass1))
                           if buttons[205].color == '#ffffff':
                              pygame.mixer.Channel(12).play(pygame.mixer.Sound(bass2))
                           if buttons[221].color == '#ffffff':
                              pygame.mixer.Channel(13).play(pygame.mixer.Sound(bass3))

                    if sequenceCounter == 15:
                           if buttons[14].color == '#ffffff':
                              pygame.mixer.Channel(0).play(pygame.mixer.Sound(kick))
                           if buttons[30].color == '#ffffff':
                              pygame.mixer.Channel(1).play(pygame.mixer.Sound(clap))
                           if buttons[46].color == '#ffffff':
                              pygame.mixer.Channel(2).play(pygame.mixer.Sound(snare))
                           if buttons[62].color == '#ffffff':
                              pygame.mixer.Channel(3).play(pygame.mixer.Sound(c_hat))
                           if buttons[78].color == '#ffffff':
                              pygame.mixer.Channel(4).play(pygame.mixer.Sound(o_hat))
                           if buttons[94].color == '#ffffff':
                              pygame.mixer.Channel(5).play(pygame.mixer.Sound(tom))
                           if buttons[110].color == '#ffffff':
                              pygame.mixer.Channel(6).play(pygame.mixer.Sound(efx1))
                           if buttons[126].color == '#ffffff':
                              pygame.mixer.Channel(7).play(pygame.mixer.Sound(efx2))
                           if buttons[142].color == '#ffffff':
                              pygame.mixer.Channel(8).play(pygame.mixer.Sound(chord1))
                           if buttons[158].color == '#ffffff':
                              pygame.mixer.Channel(9).play(pygame.mixer.Sound(chord2))
                           if buttons[174].color == '#ffffff':
                              pygame.mixer.Channel(10).play(pygame.mixer.Sound(chord3))
                           if buttons[190].color == '#ffffff':
                              pygame.mixer.Channel(11).play(pygame.mixer.Sound(bass1))
                           if buttons[206].color == '#ffffff':
                              pygame.mixer.Channel(12).play(pygame.mixer.Sound(bass2))
                           if buttons[222].color == '#ffffff':
                              pygame.mixer.Channel(13).play(pygame.mixer.Sound(bass3))

                    if sequenceCounter == 16:
                           if buttons[15].color == '#ffffff':
                              pygame.mixer.Channel(0).play(pygame.mixer.Sound(kick))
                           if buttons[31].color == '#ffffff':
                              pygame.mixer.Channel(1).play(pygame.mixer.Sound(clap))
                           if buttons[47].color == '#ffffff':
                              pygame.mixer.Channel(2).play(pygame.mixer.Sound(snare))
                           if buttons[63].color == '#ffffff':
                              pygame.mixer.Channel(3).play(pygame.mixer.Sound(c_hat))
                           if buttons[79].color == '#ffffff':
                              pygame.mixer.Channel(4).play(pygame.mixer.Sound(o_hat))
                           if buttons[95].color == '#ffffff':
                              pygame.mixer.Channel(5).play(pygame.mixer.Sound(tom))
                           if buttons[111].color == '#ffffff':
                              pygame.mixer.Channel(6).play(pygame.mixer.Sound(efx1))
                           if buttons[127].color == '#ffffff':
                              pygame.mixer.Channel(7).play(pygame.mixer.Sound(efx2))
                           if buttons[143].color == '#ffffff':
                              pygame.mixer.Channel(8).play(pygame.mixer.Sound(chord1))
                           if buttons[159].color == '#ffffff':
                              pygame.mixer.Channel(9).play(pygame.mixer.Sound(chord2))
                           if buttons[175].color == '#ffffff':
                              pygame.mixer.Channel(10).play(pygame.mixer.Sound(chord3))
                           if buttons[191].color == '#ffffff':
                              pygame.mixer.Channel(11).play(pygame.mixer.Sound(bass1))
                           if buttons[207].color == '#ffffff':
                              pygame.mixer.Channel(12).play(pygame.mixer.Sound(bass2))
                           if buttons[223].color == '#ffffff':
                              pygame.mixer.Channel(13).play(pygame.mixer.Sound(bass3))



                    # Play Button Hughlighting Logic
                    if(sequenceCounter == 15):
                         playButtons[15].color = '#FFAFAF'
                         playButtons[14].color = '#1C0020'

                         sequenceCounter = 0
                         break
                    else:
                         if (sequenceCounter == 0):
                              playButtons[sequenceCounter].color = '#FFAFAF'
                              playButtons[15].color = '#1C0020'

                         else:
                              playButtons[sequenceCounter].color = '#FFAFAF'
                              playButtons[sequenceCounter-1].color = '#1C0020'

                         
                    sequenceCounter+=1



     pygame.quit()

if __name__ == "__main__":
     main()