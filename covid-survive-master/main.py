import pygame
from player import Player
from enemy import Enemy
from enemy import Enemy2
from enemy import Enemy3
from shot import Shot
from shot import Shot2
from shot import Shot3
from shot import Shot4
import random
import os

# iniciar o jogo
pygame.init()
display = pygame.display.set_mode([1080, 720])
pygame.display.set_caption("COVID SURVIVE")

os.environ['SDL_VIDEO_CENTERED'] = '1'

branco = (255, 255, 255)
preto = (0, 0, 0)

#menu
click = False
def menu():
    menum.play(-1)
    pygame.mixer.Sound.set_volume(menum, 0.1)
    global gameLoop, fimdejogo
    while True:

        display.blit(menuimg, (0,0))
        display.blit(logo, (390, 120))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(220, 450, 200, 50)
        button_2 = pygame.Rect(660, 450, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                fimdejogo = False
                main()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()

        display.blit(botao, (220, 450))
        display.blit(botao, (660, 450))
        textob('Jogar', preto, 30)
        textob2('Sair', preto, 30)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        pygame.time.Clock()

def texto(msg, cor, tam,):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    display.blit(texto1, [42, 300])
def texto2(msg, cor, tam,):
    font = pygame.font.SysFont(None, tam)
    texto3 = font.render(msg, True, cor)
    display.blit(texto3, [35, 40])
def textop(msg, cor, tam,):
    font = pygame.font.SysFont(None, tam)
    textop2 = font.render(msg, True, cor)
    display.blit(textop2, [320, 150])
def textomenu(msg, cor, tam,):
    font = pygame.font.SysFont(None, tam)
    textomenuu = font.render(msg, True, cor)
    display.blit(textomenuu, [400, 187])
def textob(msg, cor, tam,):
    font = pygame.font.SysFont(None, tam)
    textob1 = font.render(msg, True, cor)
    display.blit(textob1, [290, 465])
def textob2(msg, cor, tam,):
    font = pygame.font.SysFont(None, tam)
    textobt2 = font.render(msg, True, cor)
    display.blit(textobt2, [740, 465])


# objetos

objectGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
enemy2Group = pygame.sprite.Group()
enemy3Group = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()
shot2Group = pygame.sprite.Group()
shot3Group = pygame.sprite.Group()
shot4Group = pygame.sprite.Group()

# background

bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("img/Mapa.png")
bg.image = pygame.transform.scale(bg.image, [1080, 720])
bg.rect = bg.image.get_rect()
menuimg = pygame.image.load("img/menu.png")
menuimg = pygame.transform.scale(menuimg, [1080, 720])
logo = pygame.image.load("img/logo.png")
botao = pygame.image.load("img/botao.png")
botao = pygame.transform.scale(botao, [200, 50])
player = Player(objectGroup)

XY = (1080, 720)
fimdejogo = False
pontos = 0
gameLoop = True
timer = 0
clock = pygame.time.Clock()

#música
pygame.mixer.music.load("sounds/música.mp3")
pygame.mixer.music.set_volume(0.1)
ready = pygame.mixer.Sound("sounds/ready.ogg")
pygame.mixer.Sound.set_volume(ready, 0.1)
menum = pygame.mixer.Sound("sounds/menu.wav")

#sons
shoot = pygame.mixer.Sound("sounds/somseringa.ogg")
pygame.mixer.Sound.set_volume(ready, 0.3 )
gameover = pygame.mixer.Sound("sounds/game_over.ogg")
pygame.mixer.Sound.set_volume(gameover, 0.1)

def main():
    global objectGroup, enemyGroup, enemy2Group, enemy3Group, shotGroup, shot2Group, shot3Group, shot4Group, gameLoop, fimdejogo, pontos, XY, timer, clock, shoot, gameover, ready, newEnemy, bg, player, display
    ready.play(0)
    pygame.mixer.music.play(-1)
    menum.stop()
    while gameLoop:
        clock.tick(60)
        while fimdejogo:
            fim = pygame.transform.scale(pygame.image.load("img/Mapafim.png").convert_alpha(), XY)
            display.blit(fim, (0, 0))
            texto("Fim de jogo, você foi infectado!! Pressione a tecla ESC para sair e ESPAÇO para jogar novamente", (branco), 32)
            textop("Sua pontuação foi de: " +str(pontos), (branco), 52)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    newShot = Shot(objectGroup, shotGroup)
                    newShot.rect.center = player.rect.center
                    shoot.play()
                elif event.key == pygame.K_LEFT:
                    newShot = Shot2(objectGroup, shot2Group)
                    newShot.rect.center = player.rect.center
                    shoot.play()
                elif event.key == pygame.K_DOWN:
                    newShot = Shot3(objectGroup, shot3Group)
                    newShot.rect.center = player.rect.center
                    shoot.play()
                elif event.key == pygame.K_UP:
                    newShot = Shot4(objectGroup, shot4Group)
                    newShot.rect.center = player.rect.center
                    shoot.play()

        # update logic
        objectGroup.update()

        timer += 1
        if timer > 30:
            timer = 0
            if random.random() < 0.35:
                newEnemy = Enemy(objectGroup, enemyGroup)
            if pontos > 200:
                if random.random() < 0.35:
                    newEnemy = Enemy(objectGroup, enemyGroup)
                    newEnemy = Enemy2(objectGroup, enemy2Group)
            if pontos > 500:
                if random.random() < 0.35:
                    newEnemy = Enemy(objectGroup, enemyGroup)
                    newEnemy = Enemy2(objectGroup, enemy2Group)
                    newEnemy = Enemy3(objectGroup, enemy3Group)


        collisions = pygame.sprite.spritecollide(player, enemyGroup, False, pygame.sprite.collide_mask)
        collisions2 = pygame.sprite.spritecollide(player, enemy2Group, False, pygame.sprite.collide_mask)
        collisions3 = pygame.sprite.spritecollide(player, enemy3Group, False, pygame.sprite.collide_mask)

        if collisions or collisions2 or collisions3:
            fimdejogo = True
            gameover.play(0)
            pygame.mixer.music.stop()

        hits = pygame.sprite.groupcollide(shotGroup, enemyGroup, True, True, pygame.sprite.collide_mask)
        hits2 = pygame.sprite.groupcollide(shotGroup, enemy2Group, True, True, pygame.sprite.collide_mask)
        hits3 = pygame.sprite.groupcollide(shotGroup, enemy3Group, True, True, pygame.sprite.collide_mask)
        hits4 = pygame.sprite.groupcollide(shot2Group, enemyGroup, True, True, pygame.sprite.collide_mask)
        hits5 = pygame.sprite.groupcollide(shot2Group, enemy2Group, True, True, pygame.sprite.collide_mask)
        hits6 = pygame.sprite.groupcollide(shot2Group, enemy3Group, True, True, pygame.sprite.collide_mask)
        hits7 = pygame.sprite.groupcollide(shot3Group, enemyGroup, True, True, pygame.sprite.collide_mask)
        hits8 = pygame.sprite.groupcollide(shot3Group, enemy2Group, True, True, pygame.sprite.collide_mask)
        hits9 = pygame.sprite.groupcollide(shot3Group, enemy3Group, True, True, pygame.sprite.collide_mask)
        hits10 = pygame.sprite.groupcollide(shot4Group, enemyGroup, True, True, pygame.sprite.collide_mask)
        hits11 = pygame.sprite.groupcollide(shot4Group, enemy2Group, True, True, pygame.sprite.collide_mask)
        hits12 = pygame.sprite.groupcollide(shot4Group, enemy3Group, True, True, pygame.sprite.collide_mask)

        if hits or hits4 or hits7 or hits10:
            pontos += 10
        if hits2 or hits5 or hits8 or hits11:
            pontos += 20
        if hits3 or hits6 or hits9 or hits12:
            pontos += 50

        # Draw
        objectGroup.draw(display)
        texto2("Pontuação: "+str(pontos), (preto), 36)
        pygame.display.update()
menu()
if __name__ == "__main__":
    main()