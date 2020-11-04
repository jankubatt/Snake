#       _               _  __     _           _   
#      | |             | |/ /    | |         | |  
#      | | __ _ _ __   | ' /_   _| |__   __ _| |_ 
#  _   | |/ _` | '_ \  |  <| | | | '_ \ / _` | __|
# | |__| | |_| | | | | | . \ |_| | |_| | |_| | |_ 
#  \____/ \__,_|_| |_| |_|\_\__,_|_.__/ \__,_|\__|


import pygame as pg
import random

random.seed()
pg.init()
clock = pg.time.Clock()
pg.display.set_caption('Snake') 
size = 800
screen = pg.display.set_mode((size, size))
x = 0
y = 0
direction = 0
done = False
eaten = False
generated = False

def is_collided_with(self, sprite):
    return self.rect.colliderect(sprite.rect)

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
            x+=5

        if (direction == 1):
            y+=5

        if (direction == 2):
            x-=5

        if (direction == 3):
            y-=5


        if x < 0:
            x = size

        if y < 0:
            y = size

        if x > size:
            x = 0

        if y > size:
            y = 0
            
        screen.fill((0,0,0))

        if eaten == False:
            if generated == False:
                xFood = random.randint(10, size - 10)
                yFood = random.randint(10, size - 10)
                generated = True
        else:
            generated = False
            eaten = False
        
        food = pg.draw.rect(screen, (255,0,0), (xFood, yFood, 20, 20))
        player = pg.draw.rect(screen, (255,255,255), (x, y, 25, 25))

        

        pg.draw.rect(screen, (255,0,0), (xFood, yFood, 20, 20))
        pg.draw.rect(screen, (255,255,255), (x, y, 25, 25))

        if player.colliderect(food):
            eaten = True

        pg.display.update()
        clock.tick(60)