import pygame

pygame.init() 
size = (400, 400)
pygame.display.set_mode(size) 
pygame.display.set_icon

pygame.display.set_caption("jeu")

programIcon = pygame.image.load('Userbox_creeper.ico')
pygame.display.set_icon(programIcon)



state = True 
while state: 
	pygame.display.update() 