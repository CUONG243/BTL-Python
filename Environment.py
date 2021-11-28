import os
import pygame

class Environment:
	# define some variables
	screen = None
	size = None

	def __init__(self, screen):
		self.screen = screen
		self.img = pygame.image.load('themes/background.png')	
		self.screen.fill((0, 0, 0))  
		self.screen.blit(self.img, (0, 0))  
		# Initialise font support
		pygame.font.init()
		# Disable mouse
		pygame.mouse.set_visible(False)
	
		pygame.display.update()

	def getPath(self):
		return os.path.dirname(os.path.abspath(__file__))
