from Settings_Karen import *

class Level(pygame.sprite.Sprite):
    def __init__(self, l):
        
        self.level = [pygame.image.load(os.path.join(img_folder, "level0.png")).convert(),
                      pygame.image.load(os.path.join(img_folder, "level1.png")).convert(),
                      pygame.image.load(os.path.join(img_folder, "level2.png")).convert(),]

        self.lever = 0

        
        self.image = self.level[self.lever]

        self.rect = self.image.get_rect()

        self.rect.x = 690
        self.rect.y = 10

    def update(self):
        self.image = self.level[self.lever]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image.set_colorkey(white)

        
            
            
            
                
        
