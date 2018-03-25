def animate(group):
	screen.fill([255,255,255])
	for ball in group:
		ball.move()
	for ball in group:
		group.remove(ball)

		if pygame.sprite.spritecollide(ball, group, False):
			ball.speed[0] = -ball.speed[0]
			ball.speed[1] = -ball.speed[1]

		group.app(ball)

		screen.blit(ball.image, ball.rect)
	pygame.display.flip()
	pygame.time.delay(20)