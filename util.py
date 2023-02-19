import pygame
from data import *   #імпорти
from math import *
#класс гравця
class Player(pygame.Rect):
    def __init__(self, x, y, image1,image2, image3, speed, width = 60,height = 120):
       super().__init__(x, y, width, height)
       self.MOVE = {"UP": False, "DOWN": False, "LEFT": False, "RIGHT": False}
       self.IMAGE = image1
       self.IMAGE_LIST = [image2, image1, image3]
       self.MOVE_IMAGE = 0
       self.SPEED = speed
       self.IMAGE_NOW = self.IMAGE
       self.TEST = [False, False, False, False]
       self.X = x
       self.Y = y
       self.SHOT = False
       self.BULLET = []
    #алгоритм анімації
    def moves (self, value, coff):
        if value % coff == 0:
            return 1
        return 0
    #рух для гравця
    def move(self, x, y):
        if self.MOVE["UP"] and self.y > 0 + 15:
            self.y -= self.SPEED
            self.MOVE_IMAGE += 1
        if self.MOVE["DOWN"] and self.y < set_win["HEIGHT"] - 80:
            self.y += self.SPEED
            self.MOVE_IMAGE += 1
        if self.MOVE["LEFT"] and self.x > 0:
           self.x -= self.SPEED
           self.MOVE_IMAGE += 1
           if not self.TEST[2]:
               self.IMAGE_NOW = pygame.transform.flip(self.IMAGE, True, False)
               self.TEST = [False, False, True, False]
           self.MOVE_IMAGE += 1
        if self.MOVE["RIGHT"] and self.x < set_win["WIDTH"] - 40:
           self.x += self.SPEED
           self.MOVE_IMAGE += 1
           if not self.TEST[3]:
               self.IMAGE_NOW = pygame.transform.rotate(self.IMAGE, 0)
               self.TEST = [False, False, False, True]
        #анімація
        if self.MOVE_IMAGE == 8:
           self.MOVE_IMAGE = 0
        self.IMAGE = self.IMAGE_LIST[self.moves(self.MOVE_IMAGE, 7)]
#клас бота
class Bot(pygame.Rect):
    def __init__(self, x, y, width, height, image1, image2, image3, speed):
        super().__init__(x, y, width, height)
        self.IMAGE1 = image1
        self.IMAGE_LIST = [image1, image2, image3]
        self.IMAGE_NOW = self.IMAGE1
        self.SPEED = speed
        self.MOVE_IMAGE = 0
        self.X = x
        self.Y = y
    #рух зомбіка
    def move_bot(self, value, coff):
        if value % coff == 0:
            return 1
        return 0
        #кут для зомбіка
    def angle(self, enemy):
        x = self.x - enemy.x
        d = (((abs(self.x -enemy.x) ** 2) + (abs(self.y -enemy.y) ** 2)) ** 0.5)
        if d == 0:
            d+=1
        sinx = abs(x) / d
        degree = asin(sinx) / 3.1415 * 180
        triang_x = enemy.x - self.x
        triang_y = enemy.y - self.y
        #четверті
        if triang_x < 0 and triang_y <= 0:
            return 180 + degree
        elif triang_x >= 0 and triang_y < 0:
            return 180 - (90 + degree) + 90
        elif triang_x > 0 and triang_y >= 0:
            return degree
        elif triang_x <= 0 and triang_y > 0:
            return 360 - (270 + degree) + 270
        return degree
    #рух бота
    def step(self,enemy):
        degree = self.angle(enemy)

        y = cos(radians(degree)) * self.SPEED
        #x = ((self.STEP  2 - y * 2) ** 0.5)
        x = cos(radians(90 - degree)) * self.SPEED
        
        self.X += x
        self.Y += y  
        self.x = self.X
        self.y = self.Y
        self.MOVE_IMAGE += 1
        #aнімація бота
        if self.MOVE_IMAGE == 8:
            self.MOVE_IMAGE = 0
        self.IMAGE1 = self.IMAGE_LIST[self.move_bot(self.MOVE_IMAGE, 7)]

class Bullet(pygame.Rect):
    def __init__(self,x, y, w, h):
        super().__init__(x, y, w, h)
        self.IMAGE = bullet_image
        self.X = 0
        self.Y = 0
        self.STEP = 8

    def make_angle(self, x, y, heroX, heroY):
        leg = abs(x  - heroX)
        hypotenuse = (leg ** 2 + abs(y - heroY) ** 2) ** 0.5
        if hypotenuse == 0:
            hypotenuse += 1
        sin = leg / hypotenuse
        degree = asin(sin) / 3.1415 * 180
        triang_x = heroX - x
        triang_y = heroY - y
        if triang_x < 0 and triang_y <= 0:
            self.X = cos(radians(180 - 90- degree)) * self.STEP
            self.Y = cos(radians(degree)) * self.STEP
            degree += 270
        elif triang_x >= 0 and triang_y < 0:
            self.X = cos(radians(180 - 90- degree)) * self.STEP * -1
            self.Y = cos(radians(degree)) * self.STEP
            degree = 180 + (90 - degree)
        elif triang_x > 0 and triang_y >= 0:
            self.X = cos(radians(180 - 90- degree)) * self.STEP * -1
            self.Y = cos(radians(degree)) * self.STEP *-1
            degree += 90
        elif triang_x <= 0 and triang_y > 0:
            self.X = cos(radians(180 - 90- degree)) * self.STEP
            self.Y = cos(radians(degree)) * self.STEP *-1
            degree = 90 - degree
        self.IMAGE = pygame.transform.rotate(self.IMAGE, degree)




























