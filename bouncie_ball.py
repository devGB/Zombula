import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load('enderman.png')
#beach_ball.png')
x = 50
y = 50
x_speed = 10
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.time.delay(20)
    pygame.draw.rect(screen, [255,255,255], [x,  y, 70, 188], 0)
    x = x + x_speed
    y = y + x_speed
    if x > screen.get_width() - 90 or x < 0:
        x_speed = - x_speed
    if y > screen.get_height() - 90 or y < 0:
    	y = - x_speed
    screen.blit(my_ball,[x, y])
    pygame.display.flip()
