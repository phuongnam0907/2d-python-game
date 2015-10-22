import random
import json
import os

from pico2d import *
from datetime import *

import time
import game_framework
import title_state
import main_state1



name = "MainState"

cookie = None
ground = None
second_background = None
font = None

class Second_Background:
    def __init__(self):
        self.X = 400
        self.Y = 400
        self.Speed = 5
        self.frame = 0
        self.image = load_image('Image\\Fourth_Background.png')
        self.image2 = load_image('Image\\Fourth_Background2.png')


    def update(self):
        self.Y = self.Y + self.Speed
        self.frame = self.frame + 1
        if self.frame % 10 == 0:
            self.Speed += 0.1
        if self.Y == 1200:
            self.Y = 400

    def draw(self):
        self.image.draw(self.X, self.Y)
        self.image2.draw(self.X, self.Y - 800)

class Second_ground:
    def __init__(self):
        self.ground_X = 400
        self.ground_Y = 400
        self.scroll_Y = 400
        self.Speed = 15
        self.frame = 0
        self.First_ground_1 = load_image('Image\\Fourth_ground.png')
        self.First_ground_2 = load_image('Image\\Fourth_ground2.png')
        self.First_ground_3 = load_image('Image\\Fourth_ground3.png')
        self.First_ground_4 = load_image('Image\\Fourth_ground4.png')
        self.First_ground_5 = load_image('Image\\Fourth_ground5.png')
        self.First_ground_6 = load_image('Image\\Fourth_ground6.png')

    def update(self):
        self.ground_Y = self.ground_Y + self.Speed
        self.frame = self.frame + 1
        if self.frame % 10 == 0:
            self.Speed += 0.1
        if self.ground_Y >= (self.scroll_Y * (12)) + 5:
            self.ground_Y = 400

    def draw(self):
        self.First_ground_1.draw(self.ground_X, self.ground_Y)
        self.First_ground_2.draw(self.ground_X, self.ground_Y - (self.scroll_Y * 2))
        self.First_ground_3.draw(self.ground_X, self.ground_Y - (self.scroll_Y * 4))
        self.First_ground_4.draw(self.ground_X, self.ground_Y - (self.scroll_Y * 6))
        self.First_ground_5.draw(self.ground_X, self.ground_Y - (self.scroll_Y * 8))
        self.First_ground_6.draw(self.ground_X, self.ground_Y - (self.scroll_Y * 10))


class Cookie:
    def __init__(self):
        self.X, self.Y = 240, 560
        self.frame = 0
        self.state = "Run"
        self.image = load_image('Image\\cookie_run4.png')
        self.slide_image = load_image('Image\\cookie_run_slide4.png')
        self.jump_image = load_image('Image\\cookie_run_jump2_4.png')
        self.jump_image2 = load_image('Image\\cookie_run_jump_4.png')
        self.dir = 0
        self.gravityX = 0

    def gravity(self):
        if (self.X + 45 + self.gravityX) > 285:
            self.gravityX -= 4
            self.X += self.gravityX
        else:
            self.X = 240
            self.gravityX = 0

    def update(self):
        self.gravity()
        if self.state == "Run":
            self.frame = (self.frame + 1) % 6
        elif self.state == "Jump" and self.state == "Slide":
            self.frame = 0
        elif self.state == "Jump" and self.X <= 250:
            self.state = "Run"
        '''self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1'''

    def draw(self):
        if self.state == "Run":
            self.image.clip_draw(0, self.frame * 75, 87, 75, self.X, self.Y)
        elif self.state == "Slide":
            self.slide_image.draw(self.X - 17, self.Y)
        elif self.state == "Jump":
            if self.dir % 2 == 1:
                self.jump_image.draw(self.X, self.Y)
            elif self.dir % 2 == 0:
                self.jump_image2.draw(self.X, self.Y)

def enter():
    global cookie, ground, second_background
    cookie = Cookie()
    ground = Second_ground()
    second_background = Second_Background()


def exit():
    global cookie, ground, second_background
    del(cookie)
    del(ground)
    del(second_background)


def pause():
    pass


def resume():
    pass


def handle_events():
    global jump
    global cookie
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_DOWN:
                cookie.state = "Slide"
            elif event.key == SDLK_UP:
                cookie.state = "Jump"
                cookie.dir += 1
                if (cookie.X + 45) == 285:
                    cookie.gravityX = 35
            elif event.key == SDLK_1:
                game_framework.change_state(main_state1)

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_DOWN:
                cookie.state = "Run"
            '''elif event.key == SDLK_UP:
                cookie.state = "Run"'''

        '''elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            if (cookie.Y - 45) == 195:
                cookie.gravityY = -35'''
                # cookie.state = cookie.JUMP



def update():
    second_background.update()
    ground.update()
    cookie.update()


def draw():
    clear_canvas()
    second_background.draw()
    ground.draw()
    cookie.draw()
    update_canvas()
    delay(0.03)





