import pygame 

pygame.init()

screen=pygame.display.set_mode((600,450))
pygame.display.set_caption("pygame SNAKE game")

white
blue =(0,0,255)
red =(255,0,0)

dis = True
while  dis:
    
    screen.fill

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dis == False
            
    pygame.draw.rect(screen,blue,(200,150,10,10))
    pygame.display.update()

pygame.quit()
quit()




