import pygame
import numpy as np
import math
import AI as bot

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GAME_MODE = {'test': 0,
             "1v1": 1,
             'AI': 2,
             "AIvAI": 3}

window_width, window_height = (800, 500)
game_display = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()



class Rectangle:

    def __init__(self, width, height, x, y, index):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.index = index


    def move_rec(self, vec):
        if vec < 0 and self.y >= 20:
            self.y += vec
        if vec > 0 and self.y <= 360:
            self.y += vec

    def get_vec(self, event):
        vec = 0
        if self.index == 2:
            if event.type == pygame.KEYDOWN:
                if event.key == 273:
                    vec = -10
                if event.key == 274:
                    vec = 10

        elif self.index == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == 119:
                    vec = -10
                if event.key == 115:
                    vec = 10
        return vec

    def draw(self):
        pygame.draw.rect(game_display, WHITE, [self.x, self.y, self.width, self.height])


class Ball:
    def __init__(self, x=390, y=240, rad=15):
        self.move = True
        self.x = x
        self.y = y
        self.rad = rad
        self.vx = 5
        self.vy = 5
        self.v_start = 50
        self.point_earned = False

    def move_ball(self):
        if self.move:
            self.x += self.vx
            self.y += self.vy

    def check_coll_wall(self):
        if self.y >= 490 or self.y <= 10:
            self.vy *= -1

    def check_coll_player(self, x, y, w, h):

        if x > 400 and self.vx > 0:
            if self.x + self.rad >= x and (self.y >= y and self.y <= y + h):
                oddalenie = 60 - math.fabs((y + h/2) - self.y) + 1
                print(oddalenie)
                if self.y > y and self.y < (y+ h/2):
                    self.vy = -5 * 30/(oddalenie + 5) - 2
                    self.vy = math.floor(self.vy)
                    print(self.vy)
                else:
                    self.vy = 5 * 30 / ( oddalenie + 5) + 2
                    self.vy = math.floor(self.vy)
                    print(self.vy)
                self.vx = -math.sqrt(self.v_start - self.vy ** 2)
                self.vx = math.floor(self.vx)  -5


        elif x < 400 and self.vx < 0:
            if self.x - self.rad <= x + w and (self.y >= y and self.y <= y + h):
                oddalenie = 60 -math.fabs((y + h / 2) - self.y) + 1
                print(oddalenie)
                if self.y > y and self.y < (y + h / 2):
                    self.vy = -5 * 30 / (oddalenie + 5)
                    self.vy = math.floor(self.vy)
                    print(self.vy)
                else:
                    self.vy = 5 * 30 / (oddalenie + 5)
                    self.vy = math.floor(self.vy)
                    print(self.vy)
                self.vx = math.sqrt(self.v_start - self.vy ** 2)
                self.vx = math.floor(self.vx) + 5

    def check_point(self):
        if self.x >= 790 or self.x <= 10:
            if GAME_MODE != 0:
                self.point_earned = True
                self.reset()
            else:
                self.vx *= -1



    def set_new_v(self):
        pass

    def reset(self):
        self.x = 390
        self.y = 240
        self.point_earned = False
        self.vy = self.v_start * np.random.choice([-1,1])
        self.vx = int(self.v_start) * np.random.choice([-1,1])


    def draw(self):
        pygame.draw.circle(game_display, WHITE, (self.x, self.y), self.rad)

    def ball_process(self):
        self.move_ball()
        self.check_coll_wall()
        self.check_point()
        self.draw()

Rect1 = Rectangle(30, 120, 10, window_height / 2 - 60, 1)
Rect2 = Rectangle(30, 120, 750, window_height / 2 - 60, 2)
PlayBall = Ball()

def run_game(event):

        pygame.display.update()
        game_display.fill(BLACK)
        Rect1.draw()
        Rect2.draw()
        if not GAME_MODE or GAME_MODE or GAME_MODE == 2:
            Rect1.move_rec(Rect1.get_vec(event))

        if GAME_MODE:
            Rect2.move_rec(Rect2.get_vec(event))

        if GAME_MODE == 2 or GAME_MODE == 3:
            Bot = bot.AI()
            if not Bot.fited:
                Bot.fit()
            poz_r_y = Rect2.y + Rect2.height / 2 - PlayBall.y
            poz_r_x = np.fabs(Rect2.x - PlayBall.x)
            ruch2 = Bot.predict(poz_r_y, poz_r_x, PlayBall.vy)
            Rect2.move_rec(ruch2)

        if GAME_MODE == 3:
            Bot = bot.AI('sgd')
            if not Bot.fited:
                Bot.fit()
            poz_r_y = Rect1.y + Rect1.height / 2 - PlayBall.y
            poz_r_x = np.fabs(Rect1.x - PlayBall.x)
            ruch1 = Bot.predict(poz_r_y, poz_r_x, PlayBall.vy)
            Rect1.move_rec(ruch1)

        PlayBall.check_coll_player(Rect1.x, Rect1.y, Rect1.width, Rect1.height)
        PlayBall.check_coll_player(Rect2.x, Rect2.y, Rect2.width, Rect2.height)
        PlayBall.ball_process()
        clock.tick(60)

