from pico2d import *

import random
import json
import os
import title_state

hurdle_data_file = open('MapData\\FirstMap_hurdle1.txt', 'r')
hurdle_data = json.load(hurdle_data_file)
hurdle_data_file.close()

hurdle_len_file = open('MapData\\TypeOfHurdle.txt', 'r')
len_data = json.load(hurdle_len_file)
hurdle_len_file.close()

#####################################################################

hurdle_data_file2 = open('MapData\\FirstMap_hurdle2.txt', 'r')
hurdle_data2 = json.load(hurdle_data_file2)
hurdle_data_file2.close()

hurdle_len_file2 = open('MapData\\TypeOfHurdle2.txt', 'r')
len_data2 = json.load(hurdle_len_file2)
hurdle_len_file2.close()



class Hurdle:
    global hurdle_data

    #Image_init = None
    STAND = 0

    def hurdle_move(self):
        self.x -= self.speed

    hurdle_state = {
        STAND: hurdle_move
    }
    def __init__(self, HurdleType, num):
        self.x = hurdle_data[HurdleType][num * 2]
        self.y = hurdle_data[HurdleType][num * 2 + 1]
        self.speed = 10
        self.name = 'noname'
        self.image = None

        if HurdleType == len_data['PORK']['num'] :
            self.image = load_image(len_data['PORK']['dir'])
        elif HurdleType == len_data['THORN']['num']:
            self.image = load_image(len_data['THORN']['dir'])

    def create(self, num):

        hurdle = []
        for i in range(2):
            self.name = "택수"
            self.x = hurdle_data[i]['x']
            self.y = hurdle_data[i]['y']
            hurdle.append(self)

        return hurdle


    def update(self):
        self.hurdle_move()

    def draw(self):
        self.image.draw(self.x, self.y)


class Hurdle2:
    global hurdle_data2

    #Image_init = None
    STAND = 0

    def hurdle_move(self):
        self.x -= self.speed

    hurdle_state = {
        STAND: hurdle_move
    }
    def __init__(self, HurdleType, num):
        self.x = hurdle_data2[HurdleType][num * 2]
        self.y = hurdle_data2[HurdleType][num * 2 + 1]
        self.speed = 10
        self.name = 'noname'
        self.image = None

        if HurdleType == len_data2['PORK']['num'] :
            self.image = load_image(len_data2['PORK']['dir'])

    def create(self, num):

        hurdle2 = []
        for i in range(2):
            self.name = "택수"
            self.x = hurdle_data2[i]['x']
            self.y = hurdle_data2[i]['y']
            hurdle2.append(self)

        return hurdle2


    def update(self):
        self.hurdle_move()

    def draw(self):
        self.image.draw(self.x, self.y)