from Settings_Karen import *


print(".")
class Platform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        '''
        car = [pygame.image.load(os.path.join(img_folder, "cars0.png")).convert(),
               pygame.image.load(os.path.join(img_folder, "cars1.png")).convert(),
               pygame.image.load(os.path.join(img_folder, "cars2.png")).convert(),
               pygame.image.load(os.path.join(img_folder, "cars3.png")).convert()]


        
        image = random.choice(car[])
        '''
        self.image = pygame.image.load(os.path.join(img_folder, "cars0.png")).convert()
        self.image = pygame.transform.scale(self.image, (300, 125))
        self.image.set_colorkey(black)
        print(".")
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = height - 130
        
        print(".")
    def update(self):
        self.rect.x += -10

        if self.rect.right < 0:
            self.kill()
