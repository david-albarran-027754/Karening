from Settings_Karen import *

class Exp(pygame.sprite.Sprite):
    def __init__(self, e):

        pygame.sprite.Sprite.__init__(self)

        self.expo = [pygame.image.load(os.path.join(img_folder, "SHINY_EXP0.png")).convert(),
                     pygame.image.load(os.path.join(img_folder, "SHINY_EXP1.png")).convert(),
                     pygame.image.load(os.path.join(img_folder, "SHINY_EXP2.png")).convert(),
                     pygame.image.load(os.path.join(img_folder, "SHINY_EXP3.png")).convert(),
                     pygame.image.load(os.path.join(img_folder, "SHINY_EXP4.png")).convert(),
                     pygame.image.load(os.path.join(img_folder, "SHINY_EXP5.png")).convert(),
                     ]


        self.expoMarker = 0

        self.image = self.expo[self.expoMarker]


        
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 0
        self.exp = 0

        self.lever = 0



    def getExp(self):
        return self.expoMarker

    def useExp(self, e):
        self.exp += e
        if self.exp == 25:
            self.expoMarker = 1
        elif self.exp == 50:
            self.expoMarker = 2
        elif self.exp == 75:
            self.expoMarker = 3
        elif self.exp == 100:
            self.expoMarker = 4
        elif self.exp == 125:
            self.expoMarker = 5
        elif self.exp == 150:
            self.expoMarker = 6
        elif self.exp == 175:
            self.expoMarker -= 6
            self.exp -= 175
            self.lever += 1

    def level(self):
        return self.lever
            
        

    def update(self):
        
        self.image = self.expo[self.expoMarker]
        if self.expoMarker == 6:
            self.expoMarker = 0
        self.image = pygame.transform.scale(self.image, (200, 140))
        self.image.set_colorkey(white)


        
