from pico2d import *
import shop


class Pet:
    Image_init = None
    TIME_PER_ACTION = 0.2
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    def __init__(self):
        self.x = 150
        self.y = 240
        self.frame = 0.0
        self.total_frames = 0.0
        self.state = "Run"

        if Pet.Image_init == None:
            self.run_chestnut_pet = load_image('Image\\chestnut_pet.png')
            self.run_wafer_pet = load_image('Image\\wafer_pet.png')
            self.run_dog_pet = load_image('Image\\dog_pet.png')

        self.dir = "Right"

    def update(self, frame_time):
        self.total_frames += Pet.FRAMES_PER_ACTION * Pet.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 6


    def draw(self, x, y):

        if shop.pet == "chestnut":
            self.run_chestnut_pet.draw(x - 70, y + 30)

        elif shop.pet == "dog":
            self.run_dog_pet.draw(x - 70, y + 30)

        elif shop.pet == "wafer":
            self.run_wafer_pet.draw(x - 70, y + 30)


class Pet_second:
    Image_init = None
    TIME_PER_ACTION = 0.2
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    def __init__(self):
        self.x = 530
        self.y = 170
        self.frame = 0.0
        self.total_frames = 0.0
        self.state = "Run"

        if Pet.Image_init == None:
            self.run_chestnut_pet = load_image('Image\\chestnut_pet2.png')
            self.run_wafer_pet = load_image('Image\\wafer_pet2.png')
            self.run_dog_pet = load_image('Image\\dog_pet2.png')

        self.dir = "Right"

    def update(self, frame_time):
        self.total_frames += Pet.FRAMES_PER_ACTION * Pet.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 6


    def draw(self, x, y):

        if shop.pet == "chestnut":
            self.run_chestnut_pet.draw(x - 30, y - 70)

        elif shop.pet == "dog":
            self.run_dog_pet.draw(x - 30, y - 70)

        elif shop.pet == "wafer":
            self.run_wafer_pet.draw(x - 30, y - 70)

