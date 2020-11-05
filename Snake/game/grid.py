import pygame as pg
pg.init()

def draw(screen, size):
    for i in range(0, 32):
        for j in range(0,32):
            if i % 2 == 0 and j % 2 == 0:
                pg.draw.rect(screen, (10,10,10), (25*i, 25*j, 25, 25))
            if i % 2 == 1 and j % 2 == 1:
                pg.draw.rect(screen, (10,10,10), (25*i, 25*j, 25, 25))