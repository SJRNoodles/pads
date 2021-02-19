import pygame
from playsound import playsound


selectedSong = "test"
thesong = "Songs/" + selectedSong

pygame.init()
window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pads")

barImg = pygame.image.load('img/pad.png')
barpressImg = pygame.image.load('img/pad_press.png')
indImg = pygame.image.load('img/ind.png')
bg = pygame.image.load('img/playfield.png')
barX = 250
barY = 480

score = 0
direction = "0"
gameTick = 0
index = 0
hit = "-"
hitPlayed = 0

font = pygame.font.Font('freesansbold.ttf',32)

running = True

def pads(dir):
    # first bar
    if dir == "0":
        window.blit(barpressImg,(barX,barY))
    else:
        window.blit(barImg,(barX,barY))
    # second bar
    if dir == "1":
        window.blit(barpressImg,(barX + 200,barY))
    else:
        window.blit(barImg,(barX + 200,barY))
    

def score_show(inp):
    st = font.render(str(inp),True, (255,255,255))
    window.blit(st,(50,10))

def indicate(dir):
    if dir == "1":
        window.blit(indImg,(barX,300))
    if dir == "0":
        window.blit(indImg,(barX + 200,300))

def bgShow():
    window.blit(bg,(0,0))
def gameStart():
  selectedSong = "test"
  from song import songData
  clock = pygame.time.Clock()
  #reference variables
  running = True
  barImg = pygame.image.load('img/pad.png')
  barpressImg = pygame.image.load('img/pad_press.png')
  indImg = pygame.image.load('img/ind.png')
  bg = pygame.image.load('img/playfield.png')
  barX = 250
  barY = 480

  score = 0
  direction = "0"
  gameTick = 0
  index = 0
  hit = "-"
  hitPlayed = 0
  font = pygame.font.Font('freesansbold.ttf',32)
  
  while running:

      window.fill((0,0,0))
      from song import BPM
      BPMS = BPM / 60
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            running = False
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_LEFT:
                  direction = "0"
                  print("left")
              if event.key == pygame.K_RIGHT:
                  direction = "1"
                  print("right")
    
      if direction == hit:
          score=score+300
          if hitPlayed == 0:
              hitPlayed = 1
              playsound('snd/hitSnd.wav')
      

      bgShow()
      pads(direction)
      score_show(score)
      if index < len(songData):
         if songData[index] != direction:
            if songData[index] != "-":
                indicate(direction)
                print("bruh") 
      pygame.display.update()
  
      gameTick=gameTick+1
      if gameTick >= BPMS:
          print("dir" + direction)
          if index < len(songData):
              print(songData[index])
              hitNote = songData[index]
              hit = hitNote
              gameTick = 0
              index = index+1
            
      if gameTick == 15:
          hit = 0
          hitPlayed = 0
        
      clock.tick(30)

def title():
    logo = pygame.image.load('img/logo.png')
    bg = pygame.image.load('img/playfield.png')

    running = True
    while running:
        window.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    
                    gameStart()
                    print("start game")
        window.blit(bg,(0,0))
        window.blit(logo,(300,200))
        pygame.display.update()
title() # start running the game
pygame.quit()
