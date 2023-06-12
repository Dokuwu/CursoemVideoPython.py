import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
'''from pygame.locals import*
img = pygame.image.load('oi.jpg')

white = (255, 64, 64)
w = 430
h = 544
screen = pygame.display.set_mode((w, h))
screen.fill((white))
running = 1

while running:
    screen.fill((white))
    screen.blit(img,(0,0))
    pygame.display.flip()'''
pygame.event.wait()
pygame.quit()