import os
import pygame
import time
import random
import math
print("imports done")

width = 800
height = 800
fps = 30



#Colors
white = (255,255,255)
yellow = (255, 255, 0) 
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
l_blue = (0, 255, 255)


#Asset Folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
snd_folder = os.path.join(game_folder, "snd")
print("Asset Folders done")
#Player Constants




pygame.init()
pygame.mixer.init()

#Sounds
bullet_sound = pygame.mixer.Sound(os.path.join(snd_folder, "pew_noise2.wav"))
pygame.mixer.music.load(os.path.join(snd_folder, "bg_song1.wav"))
pygame.mixer.music.set_volume(0.4)
print("Sounds done")

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
protag = pygame.sprite.Group()

from Karening_Bullet import *
from Karening_Exp import *
from Karening_Level import *

from Karening_Health import *
from Karening_Enemy import *
from Karening_Platform import *
from Karening_Player import *
from Karening_TroubleShoot import *
print("File Imports done")


