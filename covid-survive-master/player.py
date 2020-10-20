import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("img/baixo1.png")
        self.image = pygame.transform.scale(self.image, [45, 45])
        self.rect = pygame.Rect(540, 360, 45, 45)

        self.speed = 5

    def update(self, *args):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        elif keys[pygame.K_s]:
            self.rect.y += self.speed
        elif keys[pygame.K_a]:
            self.rect.x -= self.speed
        elif keys[pygame.K_d]:
            self.rect.x += self.speed

        if self.rect.top < 130:
            self.rect.top = 130
        elif self.rect.bottom > 680:
            self.rect.bottom = 680
        elif self.rect.left < 10:
            self.rect.left = 10
        elif self.rect.right > 1070:
            self.rect.right = 1070
