import sys, pygame
from random import *

class MyBallClass(pygame.sprite.Sprite):
	def __init__(self, image_file, location, speed):
		pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location
		self.speed = speed

	def move(self):
		self.rect = self.rect.move(self.speed)
		if self.rect.left < 0 or self.rect.right > width:
			self.speed[0] = -self.speed[0]
		if self.rect.top < 0 or self.rect.bottom > height:
			self.speed[1] = -self.speed[1]

def animate(group):
	screen.fill([255, 255, 255])
	for ball in group:

		group.remove(ball)

		if python.sprite.spritecollide(ball, group, False):
			ball.speed[0] = -ball.speed[0]
			ball.speed[1] = -ball.speed[1]

		group.add(ball)

		ball.move()
		screen.blit(ball.image, ball.rect)
	pygame.display.flip()
	pygame.time.delay(20)