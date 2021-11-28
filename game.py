import pygame, sys
from Environment import Environment
from Level import Level

#set kích thước khung hình và tên game
pygame.display.init()
pygame.display.set_caption("CARRIER")
screen = pygame.display.set_mode((800,600))

def drawLevel(matrix_to_draw):		#vẽ map
	wall = pygame.image.load(myEnvironment.getPath() + '/themes/wall.png').convert()
	box = pygame.image.load(myEnvironment.getPath() + '/themes/box.png').convert()
	box_on_target = pygame.image.load(myEnvironment.getPath() + '/themes/box_on_target.png').convert()
	space = pygame.image.load(myEnvironment.getPath() + '/themes/space.png').convert()
	target = pygame.image.load(myEnvironment.getPath() + '/themes/target.png').convert()
	player = pygame.image.load(myEnvironment.getPath() + '/themes/player.png').convert()
	brick=pygame.image.load(myEnvironment.getPath() + '/themes/abc.png').convert()
		
	#Dictionary để ánh xạ hình ảnh thành các ký tự được sử dụng trong thiết kế cấp độ
	images = {'#': wall, '_': space, '$': box, '.': target, '@': player, '*': box_on_target,' ':brick}

	# Nhận kích thước hình ảnh
	box_size = wall.get_width()
	
	for i in range (0,len(matrix_to_draw)):
		for c in range (0,len(matrix_to_draw[i])):
			myEnvironment.screen.blit(images[matrix_to_draw[i][c]], (c*box_size, i*box_size))

	pygame.display.update()
	
def movePlayer(direction,myLevel):	#thực hiện việc di chuyển của người chơi
	matrix = myLevel.getMatrix()	
	myLevel.addToHistory(matrix)	
	
	x = myLevel.getPlayerPosition()[0]
	y = myLevel.getPlayerPosition()[1]

	global target_found
	
	if direction == "L":
		print (" Moving Left ")
		
		# if is space
		if matrix[y][x-1] == "_":
			matrix[y][x-1] = "@"
			if target_found == True:
				matrix[y][x] = "."
				target_found = False
			else:
				matrix[y][x] = "_"
		
		# if is box
		elif matrix[y][x-1] == "$":
			if matrix[y][x-2] == "_":
				matrix[y][x-2] = "$"
				matrix[y][x-1] = "@"
				if target_found == True:
					matrix[y][x] = "."
					target_found = False
				else:
					matrix[y][x] = "_"
			elif matrix[y][x-2] == ".":
				matrix[y][x-2] = "*"
				matrix[y][x-1] = "@"
				if target_found == True:
					matrix[y][x] = "."
					target_found = False
				else:
					matrix[y][x] = "_"
							
		# if is box_on_target
		elif matrix[y][x-1] == "*":
			if matrix[y][x-2] == "_":
				matrix[y][x-2] = "$"
				matrix[y][x-1] = "@"
				if target_found == True:
					matrix[y][x] = "."
				else:
					matrix[y][x] = "_"
				target_found = True
				
			elif matrix[y][x-2] == ".":
				matrix[y][x-2] = "*"
				matrix[y][x-1] = "@"
				if target_found == True:
					matrix[y][x] = "."
				else:
					matrix[y][x] = "_"
				target_found = True
				
		# if is target
		elif matrix[y][x-1] == ".":
			print ("Target Found")
			matrix[y][x-1] = "@"
			if target_found == True:
				matrix[y][x] = "."
			else:
				matrix[y][x] = "_"
			target_found = True
		
	elif direction == "R":
		print (" Moving Right ")

		# if is space
		if matrix[y][x+1] == "_":
			matrix[y][x+1] = "@"
			if target_found == True:
				matrix[y][x] = "."
				target_found = False
			else:
				matrix[y][x] = "_"
		
		# if is box
		elif matrix[y][x+1] == "$":
			if matrix[y][x+2] == "_":
				matrix[y][x+2] = "$"
				matrix[y][x+1] = "@"
				if target_found == True:
					matrix[y][x] = "."
					target_found = False
				else:
					matrix[y][x] = "_"
			
			elif matrix[y][x+2] == ".":
				matrix[y][x+2] = "*"
				matrix[y][x+1] = "@"
				if target_found == True:
					matrix[y][x] = "."
					target_found = False
				else:
					matrix[y][x] = "_"				
		
		# if is box_on_target
		elif matrix[y][x+1] == "*":
			if matrix[y][x+2] == "_":
				matrix[y][x+2] = "$"
				matrix[y][x+1] = "@"
				if target_found == True:
					matrix[y][x] = "."
				else:
					matrix[y][x] = "_"
				target_found = True
				
			elif matrix[y][x+2] == ".":
				matrix[y][x+2] = "*"
				matrix[y][x+1] = "@"
				if target_found == True:
					matrix[y][x] = "."
				else:
					matrix[y][x] = "_"
				target_found = True
			
		# if is target
		elif matrix[y][x+1] == ".":
			matrix[y][x+1] = "@"
			if target_found == True:
				matrix[y][x] = "."
			else:
				matrix[y][x] = "_"
			target_found = True

	elif direction == "D":
		print (" Moving Down ")

		# if is space
		if matrix[y+1][x] == "_":
			matrix[y+1][x] = "@"
			if target_found == True:
				matrix[y][x] = "."
				target_found = False
			else:
				matrix[y][x] = "_"
		
		# if is box
		elif matrix[y+1][x] == "$":
			if matrix[y+2][x] == "_":
				matrix[y+2][x] = "$"
				matrix[y+1][x] = "@"
				if target_found == True:
					matrix[y][x] = "."
					target_found = False
				else:
					matrix[y][x] = "_"
			
			elif matrix[y+2][x] == ".":
				matrix[y+2][x] = "*"
				matrix[y+1][x] = "@"
				if target_found == True:
					matrix[y][x] = "."
					target_found = False
				else:
					matrix[y][x] = "_"
		
		# if is box_on_target
		elif matrix[y+1][x] == "*":
			if matrix[y+2][x] == "_":
				matrix[y+2][x] = "$"
				matrix[y+1][x] = "@"
				if target_found == True:
					matrix[y][x] = "."
				else:
					matrix[y][x] = "_"
				target_found = True
				
			elif matrix[y+2][x] == ".":
				matrix[y+2][x] = "*"
				matrix[y+1][x] = "@"
				if target_found == True:
					matrix[y][x] = "."
				else:
					matrix[y][x] = "_"
				target_found = True
		
		# if is target
		elif matrix[y+1][x] == ".":
			matrix[y+1][x] = "@"
			if target_found == True:
				matrix[y][x] = "."
			else:
				matrix[y][x] = "_"
			target_found = True

	elif direction == "U":
		print (" Moving Up ")

		# if is space
		if matrix[y-1][x] == "_":
			matrix[y-1][x] = "@"
			if target_found == True:
				matrix[y][x] = "."
				target_found = False
			else:
				matrix[y][x] = "_"
		
		# if is box
		elif matrix[y-1][x] == "$":
			if matrix[y-2][x] == "_":
				matrix[y-2][x] = "$"
				matrix[y-1][x] = "@"
				if target_found == True:
					matrix[y][x] = "."
					target_found = False
				else:
					matrix[y][x] = "_"

			elif matrix[y-2][x] == ".":
				matrix[y-2][x] = "*"
				matrix[y-1][x] = "@"
				if target_found == True:
					matrix[y][x] = "."
					target_found = False
				else:
					matrix[y][x] = "_"					
					
		# if is box_on_target
		elif matrix[y-1][x] == "*":
			if matrix[y-2][x] == "_":
				matrix[y-2][x] = "$"
				matrix[y-1][x] = "@"
				if target_found == True:
					matrix[y][x] = "."
				else:
					matrix[y][x] = "_"
				target_found = True
				
			elif matrix[y-2][x] == ".":
				matrix[y-2][x] = "*"
				matrix[y-1][x] = "@"
				if target_found == True:
					matrix[y][x] = "."
				else:
					matrix[y][x] = "_"
				target_found = True
					
		# if is target
		elif matrix[y-1][x] == ".":
			matrix[y-1][x] = "@"
			if target_found == True:
				matrix[y][x] = "."
			else:
				matrix[y][x] = "_"
			target_found = True		
				
	drawLevel(matrix)
	
	if len(myLevel.getBoxes()) == 0:	
		global current_level
		current_level += 1
		initLevel(level_set,current_level)	
		
def initLevel(level_set,level):
	# screen.fill((0, 0, 0))
	floor=pygame.image.load('themes/Capture.PNG').convert()
	screen.blit(floor, (0, 0))

	#hiển thị mức level trên màn hình
	font = pygame.font.SysFont('consolas', 35)
	textSurface = font.render('Level:'+str(level), True, (200,100,100),(250,250,250))
	screen.blit(textSurface, (600,530))

	# Create an instance of this Level
	global myLevel
	myLevel = Level(level_set,level)
	# Draw this level
	drawLevel(myLevel.getMatrix())
	global target_found
	target_found = False

	

	

# Create the environment
myEnvironment = Environment(screen)
# Choose a level set
level_set = "test"
# Set the start Level
current_level = 1
target_found = False
run = False


while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and run == False:
				initLevel(level_set,current_level)
				run = True
			elif event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
			if run:
				if event.key == pygame.K_LEFT:
					movePlayer("L",myLevel)
				elif event.key == pygame.K_RIGHT:
					movePlayer("R",myLevel)
				elif event.key == pygame.K_DOWN:
					movePlayer("D",myLevel)
				elif event.key == pygame.K_UP:
					movePlayer("U",myLevel)
				elif event.key == pygame.K_u:
					dem = len(myLevel.getTarget())
					drawLevel(myLevel.getLastMatrix())
					if len(myLevel.getTarget()) >dem :
						target_found=False
					elif dem> len(myLevel.getTarget()):
						target_found=True
				elif event.key == pygame.K_r:
					initLevel(level_set,current_level)
		elif event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
