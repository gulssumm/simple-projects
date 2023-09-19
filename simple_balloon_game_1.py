import pygame
import random

pygame.init()
window = pygame.display.set_mode((900, 700))
pygame.display.set_caption('BALLOON GAME')


class Balloon(pygame.sprite.Sprite):
	def __init__(self, x, y, scale, speed):
		self.speed = speed
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('hot-air-balloon.png')
		self.img = pygame.transform.scale(img, (int(img.get_width()), int(img.get_height())))
		self.rect = self.img.get_rect()
		self.rect.center = (x, y)

	def move(self, moving_down):
		dy = 0
		if moving_down:
			dy = -self.speed
		self.rect.y -= dy

	def draw(self):
		window.blit(self.img, self.rect)


balloon_1 = Balloon(50, 70, 3, 4)
balloon_2 = Balloon(200, 50, 3, 4)
balloon_3 = Balloon(300, 100, 3, 4)
balloon_4 = Balloon(450, 50, 3, 4)
balloon_5 = Balloon(550, 10, 3, 4)
balloon_6 = Balloon(650, 150, 3, 4)
balloon_7 = Balloon(700, 10, 3, 4)
balloon_8 = Balloon(750, 100, 3, 4)
balloon_9 = Balloon(850, 70, 3, 4)

timer = pygame.time.Clock()
x = 20
y = 20
speedy = 150
score_keep = 0
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)
white = (255, 255, 255)

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render("SCORE: {score}".format(score=score_keep), True, green, white)
textRect = text.get_rect(center=(800, 680))

game_over_font = pygame.font.Font('freesansbold.ttf', 64)
game_over_text = game_over_font.render("GAME OVER", True, red)
game_over_text_rect = game_over_text.get_rect(center=(450, 350))
game_over = False

img_target = pygame.image.load('target.png')
img_bomb = pygame.image.load('bomb.png')
pygame.mouse.set_visible(False)
cursor_img_rect = img_target.get_rect()

moving_down = True
running = True
while running:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			print("x = {}, y = {}".format(pos[0], pos[1]))  # get positions
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False

	# CURSOR
	cursor_position = pygame.mouse.get_pos()  # update position
	cursor_img_rect.center = cursor_position
	window.blit(img_target, cursor_img_rect)  # draw the cursor


	def is_point_inside_rect(point, rect):
		return rect.left < point[0] < rect.right and rect.top < point[1] < rect.bottom

	# BOMBS
	x_bomb = random.randint(0, 850)
	y_bomb = random.randint(0, 650)
	window.blit(img_bomb, (x_bomb, y_bomb))

	# BALLOONS
	if not game_over:
		for balloon in [balloon_1, balloon_2, balloon_3, balloon_4, balloon_5, balloon_6, balloon_7, balloon_8, balloon_9]:
			balloon.draw()
			if is_point_inside_rect(cursor_position, balloon.rect):
				score_keep += 1
				text = font.render("SCORE: {score}".format(score=score_keep), True, green, white)
				balloon.rect.center = (random.randint(0, 900), 700)
			if is_point_inside_rect(cursor_position, pygame.Rect(x_bomb, y_bomb, img_bomb.get_width(), img_bomb.get_height())):
				running = False
			if is_point_inside_rect(cursor_position, pygame.Rect(x_bomb, y_bomb, img_bomb.get_width(), img_bomb.get_height())):
				game_over = True  # Set game over state if cursor hits a bomb
		for balloon in [balloon_1, balloon_2, balloon_3, balloon_4, balloon_5, balloon_6, balloon_7, balloon_8, balloon_9]:
			balloon.move(moving_down)

	if game_over:
		window.blit(game_over_text, game_over_text_rect)
		pygame.display.update()  # Update the display
		pygame.time.delay(2000)
		running = False  # End the game after the delay

	window.blit(text, textRect)
	pygame.display.flip()  # paint screen one time

	window.fill(white)
	timer.tick(20)
	pygame.display.update()

pygame.quit()