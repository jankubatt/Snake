def run():
    import random
    import pygame as pg

    pg.init()
    size = 800
    done = False
    direction = 0
    random.seed()
    snakeLength = 1
    clock = pg.time.Clock()
    player = [size/2, size/2]
    pg.display.set_caption('Snake') 
    screen = pg.display.set_mode((size, size))
    food = [random.randint(1, 31), random.randint(1, 31)]
    gameArray = [[0 for i in range(32)] for j in range(32)]

    #if food is on player's position, generate new pos
    while player[0] == food[0] and player[1] == food[1]:
        food = [random.randint(1, 31), random.randint(1, 31)]

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

            #movement
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

        #borders
        if player[0] < 0:
            player[0] = 775

        if player[1] < 0:
            player[1] = 775

        if player[0] >= size:
            player[0] = 0

        if player[1] >= size:
            player[1] = 0

        #food detection
        if player[0]/25 == food[0] and player[1]/25 == food[1]:
            snakeLength += 1
            food = [random.randint(1, 31), random.randint(1, 31)]

            while gameArray[food[0]][food[1]] != 0:
                food = [random.randint(1, 31), random.randint(1, 31)]

        #tail collision and length of snake
        if player[0] == 775 and player[1] == 775:
            if gameArray[int(player[0]/25)][int(player[1]/25)] != 0:
                snakeLength = 1
                gameArray = [[0 for i in range(32)] for j in range(32)]

            gameArray[int(player[0]/25)][int(player[1]/25)] = snakeLength
            
        elif player[0] == 775:
            if gameArray[int(player[0]/25)][int(player[1]/25)] != 0:
                snakeLength = 1
                gameArray = [[0 for i in range(32)] for j in range(32)]

            gameArray[int(player[0]/25)][int(player[1]/25)] = snakeLength

        elif player[1] == 775:
            if gameArray[int(player[0]/25)][int(player[1]/25)] != 0:
                snakeLength = 1
                gameArray = [[0 for i in range(32)] for j in range(32)]

            gameArray[int(player[0]/25)][int(player[1]/25)] = snakeLength

        elif player[0] == 0:
            if gameArray[int(player[0]/25)][int(player[1]/25)] != 0:
                snakeLength = 1
                gameArray = [[0 for i in range(32)] for j in range(32)]

            gameArray[int(player[0]/25)][int(player[1]/25)] = snakeLength

        elif player[1] == 0:
            if gameArray[int(player[0]/25)][int(player[1]/25)] != 0:
                snakeLength = 1
                gameArray = [[0 for i in range(32)] for j in range(32)]

            gameArray[int(player[0]/25)][int(player[1]/25)] = snakeLength

        else:
            if gameArray[int(player[0]/25)][int(player[1]/25)] != 0:
                snakeLength = 1
                gameArray = [[0 for i in range(32)] for j in range(32)]

            gameArray[int(player[0]/25)][int(player[1]/25)] = snakeLength

        screen.fill((0,0,0))

        #grid
        for i in range(0, 32):
            for j in range(0,32):
                if i % 2 == 0 and j % 2 == 0:
                    pg.draw.rect(screen, (10,10,10), (25*i, 25*j, 25, 25))
                if i % 2 == 1 and j % 2 == 1:
                    pg.draw.rect(screen, (10,10,10), (25*i, 25*j, 25, 25)) 

        #draw player
        pg.draw.rect(screen, (255, 255, 255), (player[0], player[1], 25, 25))
        for i in range(0, 32):
            for j in range(0,32):
                if gameArray[i][j] != 0:
                    gameArray[i][j] -= 1
                    pg.draw.rect(screen, (255, 255, 255), (i* 25, j * 25, 25, 25))

        #draw food
        pg.draw.rect(screen, (255, 0, 0), ((food[0]*25, food[1]*25, 25, 25)))
        pg.display.update()
        clock.tick(10)