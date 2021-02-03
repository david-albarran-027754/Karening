from Settings_Karen import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, dest_x, dest_y, n):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "playeridle.png")).convert()
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.image.set_colorkey(white)

        noMob = n
        
        #ESTABLISH RECT, STARTING POSITION
        self.rect = self.image.get_rect()
        self.rect.left = start_x
        self.rect.bottom = start_y

        #MAKE STARTING POINT MORE ACCURATE
        self.floating_point_x = start_x
        self.floating_point_y = start_y

        #DIFFERENCE BTW START AND DEST PTS
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        #APPLY VELOCITY
        self.speedx = 5
        self.change_x = math.cos(angle) * self.speedx
        self.change_y = math.sin(angle) * self.speedx 

    def enemyPos(self):
        return (self.rect.centerx, self.rect.centery)

    def setDest(self, dest):
        self.rect.x = dest.x
        self.rect.y = dest.y

    def update(self):
        # The floating point x and y hold our more accurate location.
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x
 
        # The rect.x and rect.y are converted to integers.
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)

        if self.rect.left == 0:
            self.kill()

        if self.rect.right == width:
            self.kill()

        if self.rect.top == 0:
            self.kill()
 
        if self.rect.bottom == height:
            self.kill()




        #DELETE LASER ONCE OFF SCREEN
        # If the bullet flies of the screen, get rid of it.
       # if self.rect.x < 0 or self.rect.x > WIDTH or self.rect.y < 0 or self.rect.y > HEIGHT:
       #     self.kill()

            
