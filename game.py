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

player = pygame.transform.scale(player,(50, 50))




#rafraichissement
win.blit(bg, (0, 0))
state = True 

state = 1 
x = 0
y = 0 
hey = 1
cordonner = True

while state: 

	if hey == 9: 
		x +=5
		#y +=1

	if x == 725: 
		hey = 2
		if hey == 2:
			x -= 5 


	if x in [390,380,370,360,350,340,330,320,310,300,290,280,270,260,250,240,230,220,210,200,190,180,170,160,150,]:
		if y in [180,190]:  
			print("REDIRIGER EN BAS sur l'orizontal")
			y +=10
	if x in [140,150,160,170,180,190,200,210,220,230,240,250,260,270,400,410,420,430,440,450,460,470,480,490,500]:
		if y in [260,240]:  
			print("CAS special ")
			y +=10
	if x in [490,480,470]:
		if y in [150]:  
			print("38ème cas spéciale")
			y -=10 
	if x in [120,130,140,150,160,170,180,190,200,210]:
		if y in [60]:  
			print("2ème cas spésial ")
			y -=10
	if x in [400,140,150,160,170,180,190,200,210,220,230,240,250,260,270,290]:
		if y in [210]:  
			print("REDIRIGER EN HAUT sur l'orizontal")
			y -=10
	if x in [460,460]:
		if y in [230,220,210,200,190,180,170,160,150,140,130,120,110,100,90,80]:  
			print("rediriger VER la gauche sur la vertical ")
			x +=10
	if x in [110,220]:
		if y in [230,220,210,200,190,180,170,160,150,140,130,120,110,100,90,80,70,60]:  
			print("rediriger vers la droite sur la vertical")
			x -=10

    


	win.blit(player, (x, y))
	pygame.display.update() 
	pygame.time.Clock().tick(30)
	win.blit(bg, (0, 0))


	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			state = False
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_LEFT: 
				#print("gauche")
				x -=10
			if event.key == pygame.K_RIGHT: 
				#print("droite")
				x +=10
			if event.key == pygame.K_UP: 
				#print("HAUT")
				y -=10
			if event.key == pygame.K_DOWN: 
				#print("BAS")
				y +=10
			if event.key == pygame.K_SPACE: 
				print(x)
				print(y)
			
	
	


pygame.quit()


