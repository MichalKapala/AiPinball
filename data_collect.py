"""" Geting data from pinball game, needed to build AI model """

import pinball
import pygame
import numpy as np

pinball.GAME_MODE = pinball.GAME_MODE['AIvAI']

plik = open('ruch.data', 'a')

CRASH = False
point1, point2 = 0, 0

while not CRASH:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CRASH = True

    pinball.run_game(event)
    poz_r_y = pinball.Rect1.y + pinball.Rect1.height / 2
    poz_r_x = pinball.Rect1.x = pinball.Rect1.width
    poz_ball_x = pinball.PlayBall.x
    poz_ball_y = pinball.PlayBall.y

    odl_x = np.fabs(poz_ball_x - poz_r_x)
    odl_y = poz_r_y - poz_ball_y
    ruch = pinball.Rect1.get_vec(event)
    plik = open('ruch.data', 'a')
    if pinball.PlayBall.vx < 0 and ruch != 0 and odl_y * ruch < 0:
        save_str = str(odl_y) + " " + str(odl_x) + " " + str(pinball.PlayBall.vy)
        plik.write(save_str + ' ' + str(ruch) + '\n')
