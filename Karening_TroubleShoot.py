from Settings_Karen import *

class NoMob(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join(img_folder, "Background.png")).convert()
        self.rect = self.image.get_rect()

        self.rect.x = 750
        self.rect.y = 750

        self.image = pygame.transform.scale(self.image, (50, 50))

    def update(self):

        mouse_pos = pygame.mouse.get_pos()
        print(mouse_pos)
        mouseState = pygame.mouse.get_pressed()

        if mouse_pos >= (750, 750):
            if mouseState[0] == 1:
                print("new mob")
                noMob(1)

                newMob(400, 50)
