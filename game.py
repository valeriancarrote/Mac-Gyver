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

player = pygame.image.load("image/Steve.gif").convert()

#rafraichissement
win.blit(player, (0, 0))
win.blit(bg, (0, 0))
state = True 
while state: 

	pygame.display.update() 

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			state = False



pygame.quit()


