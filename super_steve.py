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
    x = x + x_speed
    y = y + y_speed
    if x > screen.get_width() - 120 or x < 0:
        x_speed = -x_speed
    if y > screen.get_height() - 192 or y < 0:
    	y_speed = -y_speed
    screen.blit(my_ball,[x, y])
    pygame.display.flip()
