import pygame, sys, random, time

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([0,0,0])

pygame.draw.circle(screen, [255,0,0],[100,100], 39, 0)
pygame.draw.circle(screen, [0,255,0],[100,100], 29, 0)

pygame.draw.circle(screen, [255,0,0],[540,100], 69, 0)
pygame.draw.circle(screen, [0,255,0],[540,100], 50, 0)

pygame.draw.arc(screen,[0,255,0],(100,300,400,100),3.14,0,3)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()









