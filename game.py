import pygame

pygame.init() 
size = (400, 400)
pygame.display.set_mode(size) 
pygame.display.set_icon

pygame.display.set_caption("jeu")

programIcon = pygame.image.load('Userbox_creeper.ico')
pygame.display.set_icon(programIcon)

bg = pygame.image.load("python.png")
pygame.display.blit(bg, (400, 400))



state = True 
while state: 
	pygame.display.update() 