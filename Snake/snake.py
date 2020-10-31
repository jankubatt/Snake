import pygame as pg

pg.init()
pg.display.set_caption('Snake') 
size = 800
screen = pg.display.set_mode((size, size))
done = False

while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                        done = True
        
        pg.draw.rect(screen, (255,255,255), (100, 100, 50, 50))
        pg.display.flip()