import pygame

pygame.init() 
size = (400, 400)
pygame.display.set_mode(size) 
pygame.display.set_caption("jeu")


state = True 
while state: 
	pygame.display.update()