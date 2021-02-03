from Settings_Karen import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,d):
        pygame.sprite.Sprite.__init__(self)
        print("1.1")
        self.pews = [
                    pygame.image.load(os.path.join(img_folder, "Disk0.png")).convert(),
                    pygame.image.load(os.path.join(img_folder, "Disk1.png")).convert(),
                    pygame.image.load(os.path.join(img_folder, "Disk2.png")).convert(),
                    pygame.image.load(os.path.join(img_folder, "Disk3.png")).convert()]
        print("1.2")
        
        self.pew_count = 0
        print("2")
        self.image = self.pews[self.pew_count]
        self.image.set_colorkey(black)
        
        self.direction = d
        
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x
        self.speed = 20

        print("3")
    def update(self):
        if self.direction == "RIGHT":
            self.rect.x += self.speed
        elif self.direction == "LEFT":
            self.rect.x -= self.speed
        elif self.direction == "UP":
            self.rect.y -= self.speed
        elif self.direction == "DOWN":
            self.rect.y += self.speed

        self.image = self.pews[self.pew_count]
        self.image.set_colorkey(black)

        self.pew_count += 1
        if self.pew_count > 3:
            self.pew_count = 0
        print(self.pew_count)
        
        if self.rect.left > width:
            self.kill()
        elif self.rect.right < 0:
            self.kill()
        elif self.rect.top > height:
            self.kill()
        elif self.rect.bottom < 0:
            self.kill()

        
