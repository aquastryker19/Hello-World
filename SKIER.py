# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 19:11:58 2016

@author: pi
"""
#MADE BY SKYE THE AMAZING :) ch 10
import pygame, sys, random
import os
os.chdir('skier')
skier_images = ['skier_down.png', 'skier_right1.png', 'skier_right2.png', 'skier_left2.png', 'skier_left1.png']

class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('skier_down.png')
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.angle = 0

def turn(self, direction):
    self.angle = self.angle + direction
    if self.angle < -2: self.angle  = -2
    if self.angle > 2: self.angle = 2
    center = self.rect.center
    self.image = pygame.image.load(skier_images[self.angle])
    self.rect = self.image.get_rect()
    self.rect.center = center
    speed = [self.angle, 6 - abs(self.angle) * 2]
    return speed

def move(self, speed):
    self.rect.centerx = self.rect.centerx + speed[0]
    if self.rect.centerx < 20: self.rect.centerx = 20
    if self.rect.centerx > 620: self.rect.centerx = 620

class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, type):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.location = location
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type
        self.passed = False

    def scroll(self, t_ptr):
        self.rect.centery = self.location[1] - t_ptr

def create_map(start, end):
    obstacles = pygame.sprite.Group()
    gates = pygame.sprite.Group()
    locations = []
    for i in range(10):
        row = randint(start, end)
        co1 = random.randint(0, 9)
        location = [co1 * 64 + 20, row * 64 + 20]
        if not (location in locations):
            locations.append(location)
            type = random.choice(['tree', 'flag'])
            if type == 'tree': img = 'skier_tree.png'
            elif type =='flag': img = 'skier_flag.png'
            obstacle = ObstacleClass(img, location, type)
            obstacles.add(obstacle)
    return obstacles
def animate():
    screen.fill([255, 255, 255])
    pygame.display.update(obstacles.draw(screen))
    screen.blit(skier.image, skier.rect)
    screen.blit(score_text, [10, 10])
    pygame.display.flip()

def updateObstacleGroup(map0, map1):
    obstacles = pygame.sprite.Group()
    for ob in map0: obstacles.add(ob)
    for ob in map1: obstacles.add(ob)
    return obstacles
import pdb as db
from pdb import set_trace as st

#st()
os.chdir('/home/pi/skye/Hello-World/skier')
pygame.init()
screen = pygame.display.set_mode([640,640])
clock = pygame.time.Clock()
skier = SkierClass()
speed = [0, 6]
map_position = 0
points = 0
map0 = create_map(20, 29)
map1 = create_map(10, 19)
activeMap = 0
obstacles = updateObstacleGroup(map0, map1)
font = pygame.font.Font(None, 50)



while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = skier.turn(-1)
            elif event.key == pygame.K_RIGHT:
                speed = skier.turn(1)
    skier.move(speed)
    map_position += speed[1]