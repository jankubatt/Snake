def run():
    import pygame as pg
    from game import grid

    pg.init()
    clock = pg.time.Clock()
    pg.display.set_caption('Snake') 
    size = 800
    screen = pg.display.set_mode((size, size))
    x = size/2
    y = size/2
    direction = 0
    done = False

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
                x+=25

            if (direction == 1):
                y+=25

            if (direction == 2):
                x-=25

            if (direction == 3):
                y-=25

            if x < 0:
                x = size

            if y < 0:
                y = size

            if x > size:
                x = 0

            if y > size:
                y = 0
                
            screen.fill((0,0,0))
            grid.draw(screen, 800)
            pg.draw.rect(screen, (255, 255, 255), (x, y, 25, 25))
            pg.display.update()
            clock.tick(10)