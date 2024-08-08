import pygame
import pygame as pg

w, h = 20, 20
tile = 6
clock = pg.time.Clock()

screen = pg.display.set_mode((w * tile, h * tile))

run = True

map_x = 0
map_y = 0

map_lvl1 = [
    [1, 1, 1, 0, 0, 0, ],
    [1, 0, 0, 0, 0, 0, ],
    [1, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 1, 0, 0, ],
    [0, 0, 1, 1, 1, 0, ],
    [0, 0, 0, 1, 0, 0, ],
]

map_lvl2 = [
    [1, 1, 1, 1, 1, 1, ],
    [1, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 1, ],
    [1, 1, 1, 1, 1, 1, ],
]



def Map(map):
    x = -w
    y = -h
    for i in map:
        y += h
        x = -w
        for j in i:
            x += w

            if j == 1:

                pg.draw.rect(screen, (255, 0, 0), (x, y, w, h), 1)


while run:
    for event in pg.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False

            if event.key == pygame.K_1:
                screen.fill((0, 0, 0))
                Map(map_lvl1)

            if event.key == pygame.K_2:
                screen.fill((0, 0, 0))
                Map(map_lvl2)


    pg.display.flip()
    clock.tick(60)
pg.quit()
