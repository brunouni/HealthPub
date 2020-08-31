import pygame
from random import randint
pygame.init()
# posições
x = 540
y = 360
covid_x = 0
covid_y = 360
covid2_x = 540
covid2_y = 720
covid3_x = 1080
covid3_y = 360
velocidade = 2.5
velocidade_covid = 2
# imagens
fundo = pygame.image.load('Mapa.png')
covid = pygame.image.load('covid.png')
covid = pygame.transform.scale(covid, (45, 45))
covid2 = pygame.image.load('covid2.png')
covid2 = pygame.transform.scale(covid2, (45, 45))
covid3 = pygame.image.load('covid3.png')
covid3 = pygame.transform.scale(covid3, (45, 45))
medico = pygame.image.load('sprite.png')
medico = pygame.transform.scale(medico, (45, 45))
janela = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("HealthPub")

janela_aberta = True
while janela_aberta :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_w] and y>= 130:
            y-= velocidade
        if comandos[pygame.K_s] and y<= 630:
            y+= velocidade
        if comandos[pygame.K_d] and x<= 1010:
            x+= velocidade
        if comandos[pygame.K_a] and x>= 30:
            x-= velocidade

        # colisão
        if ((x - 20 < covid_x and y + 20 > covid_y)):
            y = 1000

        #if ((x - 30 < covid2_x and y - 30 < covid2_y)):
#            y = 1000

 #       if ((x - 30 > covid3_x and y + 30 > covid3_y)):
  #          y = 1000

        if(covid_x >= 1150):
            covid_x = (0)
        if (covid2_y <= 0):
            covid2_y = (720)
        if (covid3_x <= 0):
            covid3_x = (1080)

        covid_x += velocidade_covid
        covid2_y -= velocidade_covid
        covid3_x -= velocidade_covid

        janela.blit(fundo,(0,0))
        janela.blit(medico, (x, y))
        janela.blit(covid, (covid_x, covid_y))
        janela.blit(covid2, (covid2_x, covid2_y))
        janela.blit(covid3, (covid3_x, covid3_y))

        pygame.display.update()

pygame.quit()
