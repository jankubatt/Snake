#       _               _  __     _           _   
#      | |             | |/ /    | |         | |  
#      | | __ _ _ __   | ' /_   _| |__   __ _| |_ 
#  _   | |/ _` | '_ \  |  <| | | | '_ \ / _` | __|
# | |__| | |_| | | | | | . \ |_| | |_| | |_| | |_ 
#  \____/ \__,_|_| |_| |_|\_\__,_|_.__/ \__,_|\__|

import pygame as pg
import random

pg.init()
random.seed()
clock = pg.time.Clock()
pg.display.set_caption('Snake') 
size = 800
screen = pg.display.set_mode((size, size))
player = [size/2, size/2]
direction = 0
done = False
gameArray = [[" " for i in range(32)] for j in range(32)]
food = [random.randint(0, 32), random.randint(0, 32)]

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
                            
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and direction != 1:
                direction = 3
            if event.key == pg.K_s and direction != 3:
                direction = 1
            if event.key == pg.K_a and direction != 0:
                direction = 2
            if event.key == pg.K_d and direction != 2:
                direction = 0
            
    if (direction == 0):
        player[0]+=25

    if (direction == 1):
        player[1]+=25

    if (direction == 2):
        player[0]-=25

    if (direction == 3):
        player[1]-=25

    if player[0] < 0:
        player[0] = size

    if player[1] < 0:
        player[1] = size

    if player[0] > size:
        player[0] = 0

    if player[1] > size:
        player[1] = 0

    if player[0]/25 == food[0] and player[1]/25 == food[1]:
        food = [random.randint(0, 32), random.randint(0, 32)]
                
    screen.fill((0,0,0))
  
    for i in range(0, 32):
        for j in range(0,32):
            if i % 2 == 0 and j % 2 == 0:
                pg.draw.rect(screen, (10,10,10), (25*i, 25*j, 25, 25))
            if i % 2 == 1 and j % 2 == 1:
                pg.draw.rect(screen, (10,10,10), (25*i, 25*j, 25, 25))
        
    gameArray = [[" " for i in range(32)] for j in range(32)] 
    if player[0] == 800:
        gameArray[int(player[1]/25)][31] = "S"
            
    elif player[1] == 800:
        gameArray[31][int(player[0]/25)] = "S"

    else:
        gameArray[int(player[1]/25)][int(player[0]/25)] = "S"
        gameArray[food[1]][food[0]] = "F"

    pg.draw.rect(screen, (255, 255, 255), (int(player[0]), int(player[1]), 25, 25))
    pg.draw.rect(screen, (255, 0, 0), (food[0]*25, food[1]*25, 25, 25))
    pg.display.update()
    clock.tick(10)

