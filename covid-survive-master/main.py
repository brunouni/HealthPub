import pygame
from player import Player
from enemy import Enemy
from enemy import Enemy2
from shot import Shot
from shot import Shot2
import random
import os

# iniciar o jogo
pygame.init()
display = pygame.display.set_mode([1080, 720])
pygame.display.set_caption("COVID SURVIVE")

os.environ['SDL_VIDEO_CENTERED'] = '1'

branco = (255, 255, 255)
preto = (0, 0, 0)

def texto(msg, cor, tam,):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    display.blit(texto1, [270, 300])
def texto2(msg, cor, tam,):
    font = pygame.font.SysFont(None, tam)
    texto3 = font.render(msg, True, cor)
    display.blit(texto3, [35, 40])
def textop(msg, cor, tam,):
    font = pygame.font.SysFont(None, tam)
    textop2 = font.render(msg, True, cor)
    display.blit(textop2, [320, 150])


# objetos

objectGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
enemy2Group = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()
shot2Group = pygame.sprite.Group()
# background

bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("img/Mapa.png")
bg.image = pygame.transform.scale(bg.image, [1080, 720])
bg.rect = bg.image.get_rect()

player = Player(objectGroup)

XY = (1080, 720)
fimdejogo = False
pontos = 0
gameLoop = True
timer = 0
clock = pygame.time.Clock()

#música
pygame.mixer.music.load("sounds/música.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
ready = pygame.mixer.Sound("sounds/ready.ogg")
pygame.mixer.Sound.set_volume(ready, 0.1)
ready.play(0)
#sons
shoot = pygame.mixer.Sound("sounds/somseringa.ogg")
pygame.mixer.Sound.set_volume(ready, 0.3 )
gameover = pygame.mixer.Sound("sounds/game_over.ogg")
pygame.mixer.Sound.set_volume(gameover, 0.1)
if __name__ == "__main__":
    while gameLoop:
        clock.tick(60)
        while fimdejogo:
            fim = pygame.transform.scale(pygame.image.load("img/Mapafim.png").convert_alpha(), XY)
            display.blit(fim, (0, 0))
            texto("Fim de jogo, pressione a tecla ESC para sair", (branco), 36)
            textop("Sua pontuação foi de: " +str(pontos), (branco), 52)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop = False
                    fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameLoop = False
                        fimdejogo = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    newShot = Shot(objectGroup, shotGroup)
                    newShot.rect.center = player.rect.center
                    shoot.play()
                elif event.key == pygame.K_LEFT:
                    newShot = Shot2(objectGroup, shot2Group)
                    newShot.rect.center = player.rect.center
                    shoot.play()

        # update logic
        objectGroup.update()

        timer += 1
        if timer > 30:
            timer = 0
            if random.random() < 0.5:
                newEnemy = Enemy(objectGroup, enemyGroup)
                newEnemy2 = Enemy2(objectGroup, enemy2Group)


        collisions = pygame.sprite.spritecollide(player, enemyGroup, False, pygame.sprite.collide_mask)
        collisions2 = pygame.sprite.spritecollide(player, enemy2Group, False, pygame.sprite.collide_mask)

        if collisions or collisions2:
            fimdejogo = True
            gameover.play(0)
            pygame.mixer.music.stop()


        hits = pygame.sprite.groupcollide(shotGroup, enemyGroup, True, True, pygame.sprite.collide_mask)
        hits2 = pygame.sprite.groupcollide(shotGroup, enemy2Group, True, True, pygame.sprite.collide_mask)
        hits3 = pygame.sprite.groupcollide(shot2Group, enemyGroup, True, True, pygame.sprite.collide_mask)
        hits4 = pygame.sprite.groupcollide(shot2Group, enemy2Group, True, True, pygame.sprite.collide_mask)

        if hits or hits2 or hits3 or hits4:
            pontos += 10
        # Draw
        objectGroup.draw(display)
        texto2("Pontuação: "+str(pontos), (preto), 36)
        pygame.display.update()
