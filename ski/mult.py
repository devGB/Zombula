import sys , pygame

class MyBallClass(pygame.sprite.Srite):
	def __init__(self, image_file, location):
		pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location

size = width, height = 640, 480
sccreen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
img_file = "beach_ball.png"
balls = []
for row in range (0, 3):
	for column in range (0, 3):
		location = [column * 180 + 10, row * 180 + 10]
		ball = MyBallClass(img_file, location)
		balls.append(ball)
for ball in balls:
	screen.blit(ball.image, ball.rect)
pygame.display.flip()
