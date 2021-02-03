from Settings_Karen import *

class Health(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        print("class")
        self.healthbar = [pygame.image.load(os.path.join(img_folder, "healthy0.png")).convert(),
                          pygame.image.load(os.path.join(img_folder, "healthy1.png")).convert(),
                          pygame.image.load(os.path.join(img_folder, "healthy2.png")).convert(),
                          pygame.image.load(os.path.join(img_folder, "healthy3.png")).convert(),
                          pygame.image.load(os.path.join(img_folder, "healthy4.png")).convert(),
                          pygame.image.load(os.path.join(img_folder, "healthy5.png")).convert(),
                          pygame.image.load(os.path.join(img_folder, "healthy5.png")).convert(),
                          ]
        print("class_image")
        self.healthbar_count = 0
        
        self.image = self.healthbar[self.healthbar_count]
        
        self.image = pygame.transform.scale(self.image, (200, 150))
        print("class_imageChoose")
        self.image.set_colorkey(black)
        
        self.rect = self.image.get_rect()
        
        self.rect.x = 10
        
        self.rect.y = 50
        
        print("__init__)")
    def getHealth(self):
        return self.healthbar_count
        print("getHealth")
    def setHealth(self, health):
        if health == 1: #Increase Health: Unless Health is at 0
            self.healthbar_count -= 1
            if self.healthbar_count < 0:
                self.healthbar_count = 0


        elif health == -1:#Decrease Health: Unless Health is at 5
            self.healthbar_count += 1
            if self.healtbar_count > 5:
                self.healthbar_count = 5
            if self.healthbar_count == 5:
                pygame.quit()
        print("setHealth")
    def update(self):

        self.image = self.healthbar[self.healthbar_count]
        self.image = pygame.transform.scale(self.image, (200, 140))
        self.image.set_colorkey(white)



        
