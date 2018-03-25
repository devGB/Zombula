import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load('steve.png')
#beach_ball.png')
x = 70
y = 97
x_speed = 6
y_speed = 6
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.time.delay(20)
    pygame.draw.rect(screen, [255,255,255], [x,  y, 120, 192], 0)
    y = y + y_speed
    x = x + x_speed
    if x > screen.get_width() - 110 or x < 0:
        x = 0
    if y > screen.get_height() - 172 or y < 0:
    	y = 0
    screen.blit(my_ball,[x, y])
    pygame.display.flip()
