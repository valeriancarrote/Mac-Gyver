import pygame



pygame.init() 
size = (800, 400)
win = pygame.display.set_mode(size) 
pygame.display.set_icon



pygame.display.set_caption("jeu")

programIcon = pygame.image.load('Userbox_creeper.ico')
pygame.display.set_icon(programIcon)

bg = pygame.image.load("image/python.png")
bg = pygame.transform.scale(bg,(800, 400))


player = pygame.image.load("image/Player.png").convert_alpha()

player = pygame.transform.scale(player,(100, 100))




#rafraichissement
win.blit(bg, (0, 0))
state = True 

state = 1 
x = 0
y = 0 
hey = 1

while state: 

	if hey == 9: 
		x +=5
		#y +=1

	if x == 725: 
		hey = 2
		if hey == 2:
			x -= 5 



	win.blit(player, (x, y))
	pygame.display.update() 
	pygame.time.Clock().tick(30)
	win.blit(bg, (0, 0))

	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			state = False
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_LEFT: 
				print("gauche")
				x -=10
			if event.key == pygame.K_RIGHT: 
				print("droite")
				x +=10
			if event.key == pygame.K_UP: 
				print("HAUT")
				y -=10
			if event.key == pygame.K_DOWN: 
				print("BAS")
				y +=10
	
	
	pygame.display.flip()



pygame.quit()


