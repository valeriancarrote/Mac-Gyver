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
while state: 
	x +=5
	#y +=1
	if x == 725: 
		x -= 50 

	
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
			if event.key == pygame.K_RIGHT: 
				print("droite")
			if event.key == pygame.K_UP: 
				print("HAUT")
			if event.key == pygame.K_DOWN: 
				print("BAS")
	pygame.display.flip()



pygame.quit()


