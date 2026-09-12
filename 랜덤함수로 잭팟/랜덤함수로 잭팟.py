import pygame
import random
import time
from pathlib import Path

pygame.init()

#화면 크기 설정
WIDTH = 1920
HEIGHT = 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("파칭코 게임")

#시작값 지정
RUN = True
phase= 1
start=0

#이미지 지정
BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "image"
MUSIC_DIR = BASE_DIR / "music"

background = pygame.image.load(IMAGE_DIR / "background.png")
background1 = pygame.image.load(IMAGE_DIR / "background1.png")
gb=pygame.image.load(IMAGE_DIR / "golden_banana.png")
gch=pygame.image.load(IMAGE_DIR / "golden_cherry.png")
gc=pygame.image.load(IMAGE_DIR / "golden_coin.png")
gw=pygame.image.load(IMAGE_DIR / "golden_watermelon.png")
sb=pygame.image.load(IMAGE_DIR / "silver_banana.png")
sch=pygame.image.load(IMAGE_DIR / "silver_cherry.png")
sc=pygame.image.load(IMAGE_DIR / "silver_coin.png")
sw=pygame.image.load(IMAGE_DIR / "silver_watermelon.png")
cb=pygame.image.load(IMAGE_DIR / "copper_banana.png")
cch=pygame.image.load(IMAGE_DIR / "copper_cherry.png")
cc=pygame.image.load(IMAGE_DIR / "copper_coin.png")
cw=pygame.image.load(IMAGE_DIR / "copper_watermelon.png")
jack=pygame.image.load(IMAGE_DIR / "jackpot.png")
poop=pygame.image.load(IMAGE_DIR / "poop.png")

#노래
button_click = pygame.mixer.Sound(MUSIC_DIR / "buttonclick.wav")

#모양별 값 지정
jackpot=0
silver_cherry = 1_1
silver_coin= 1_2
silver_banana= 1_3
silver_watermelon = 1_4
golden_cherry = 2_1
golden_coin=2_2
golden_banana=2_3
golden_watermelon=2_4
copper_cherry= 3_1
copper_coin=3_2
copper_banana=3_3
copper_watermelon=3_4
poop_im=4

#슬롯 값 지정
slot1=99
slot2=99
slot3=99
num1=0
num2=0
slot_set=1


#list
space = [0, 1, 1, 1, 1]
other = [silver_banana,silver_cherry, silver_coin, silver_watermelon, golden_banana, golden_cherry,golden_coin,golden_watermelon, copper_banana, copper_cherry, copper_coin, copper_watermelon, poop_im, silver_banana,silver_cherry, silver_coin, silver_watermelon, golden_banana, golden_cherry,golden_coin,golden_watermelon, copper_banana, copper_cherry, copper_coin, copper_watermelon]


#화면 구현
while RUN:

 if phase == 1:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

#슬롯마다 모양 지정하기
        if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            phase = 2
            for i in range(1,4):
                if i ==1:
                  num1=random.choice(space)
                  if num1==0:
                     slot1=0         
                  elif num1==1:
                     num2=random.choice(other)
                     slot1=num2
                     
                if i ==2:
                  num1=random.choice(space)
                  if num1==0:
                     slot2=0
                  elif num1==1:
                       num2=random.choice(other)
                       slot2=num2

                if i ==3:
                  num1=random.choice(space)
                  if num1==0:
                     slot3=0
                  elif num1==1:
                       num2=random.choice(other)
                       slot3=num2 

     #첫 화면 빌드       
     screen.blit(background, (0,0))


 if phase == 2:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            if 1<=slot_set<4:
               button_click.play()
               print(slot1, slot2, slot3)
            time.sleep(1)

            if slot_set<5:
               slot_set+=1
  
            
            if slot_set==5:
               slot_set=1
               phase = 1
               slot1=99
               slot2=99
               slot3=99
               num1=0
               num2=0
           
     screen.blit(background1, (0,0))

#슬롯 차례대로 보여주기
     if slot_set>=2 :
       if slot1 == 11:
         screen.blit(sch, (280,200))  
       if slot1 == 12:
         screen.blit(sc, (280,200))   
       if slot1 == 13:
         screen.blit(sb, (280,200))
       if slot1 == 14:
          screen.blit(sw, (280,200))   
       if slot1 == 21:
          screen.blit(gch, (280,200))   
       if slot1 == 22:
          screen.blit(gc, (280,200))   
       if slot1 == 23:
          screen.blit(gb, (280,200))   
       if slot1 == 24:
          screen.blit(gw, (280,200))  
       if slot1 ==0:
          screen.blit(jack, (280,200)) 
       if slot1 ==31:
          screen.blit(cch, (280,200)) 
       if slot1 ==32:   
          screen.blit(cc, (280,200) )
       if slot1 == 33:
          screen.blit(cb, (280,200))
       if slot1 == 34:
          screen.blit(cw,  (280,200))
       if slot1 == 4:
          screen.blit(poop, (280,200))

     if slot_set>=3:
       if slot2 == 11:
         screen.blit(sch, (735,200))  
       if slot2 == 12:
         screen.blit(sc, (735,200))   
       if slot2 == 13:
         screen.blit(sb, (735,200))   
       if slot2 == 14:
          screen.blit(sw, (735,200))   
       if slot2 == 21:
          screen.blit(gch, (735,200))   
       if slot2 == 22:
          screen.blit(gc, (735,200))   
       if slot2 == 23:
          screen.blit(gb, (735,200))   
       if slot2 == 24:
          screen.blit(gw, (735,200))
       if slot2 ==0:
          screen.blit(jack, (735,200))
       if slot2 ==31:
          screen.blit(cch, (735,200)) 
       if slot2 ==32:
          screen.blit(cc, (735,200) )
       if slot2 == 33:
          screen.blit(cb, (735,200))
       if slot2 == 34:
          screen.blit(cw,  (735,200))
       if slot2 == 4:
          screen.blit(poop, (735,200))
     
     if slot_set>=4:
       if slot3 == 11:
          screen.blit(sch, (1190,200))  
       if slot3 == 12:
          screen.blit(sc, (1190,200))   
       if slot3 == 13:
          screen.blit(sb, (1190,200))   
       if slot3 == 14:
          screen.blit(sw, (1190,200))   
       if slot3 == 21:
          screen.blit(gch, (1190,200))   
       if slot3 == 22:
          screen.blit(gc, (1190,200))   
       if slot3 == 23:
          screen.blit(gb, (1190,200))   
       if slot3 == 24:
          screen.blit(gw, (1190,200))
       if slot3 ==0:
          screen.blit(jack, (1190,200))
       if slot3 ==31:
          screen.blit(cch, (1190,200)) 
       if slot3 ==32:
          screen.blit(cc, (1190,200) )
       if slot3 == 33:
          screen.blit(cb, (1190,200))
       if slot3 == 34:
          screen.blit(cw,  (1190,200))
       if slot3 == 4:
          screen.blit(poop, (1190,200))


#화면 유지
 pygame.display.update()