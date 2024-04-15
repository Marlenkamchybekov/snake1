import pygame

clock = pygame.time.Clock()


pygame.init()
screen = pygame.display.set_mode((627,480))
pygame.display.set_caption("pygame kamchybekov7 game")
# icon = pygame.image.load()
#pygame.display.set_icon(icon)
car = pygame.image.load('images/car2.png')
car_x = 600
brag_list =[

]
bg = pygame.image.load('images/fon2.jpg')
walk_left = [
    pygame.image.load('images/player r11.png'),
    pygame.image.load('images/player r12.png'),
    pygame.image.load('images/player r13.png'),
    pygame.image.load('images/player r14.png')
   
]
walk_right = [
    pygame.image.load('images/player f11.png'),
    pygame.image.load('images/player f12.png'),
    pygame.image.load('images/player f13.png'),
    pygame.image.load('images/player f14.png')

]
player_anim_count = 0
bg_x = 0
player_x = 120
player_y = 330

player_speed = 10 

is_jump = False
jum_count = 10

pul = pygame.image.load('images/pulya1.png')
puls =[]
puls_left = 10


bg_sound = pygame.mixer.Sound('music/mus.mp3')
bg_sound.play()



brag_timer = pygame.USEREVENT + 1
pygame.time.set_timer(brag_timer,3000)
# square = pygame.Surface((100,10))
# square.fill('Black')

# line_start = (50,50)
# line_end = (400,50)
# line_color = ('White')
gameplay = True

logica = False

label =pygame.font.Font(None,40)
lose_label = label.render ('GAME OVER!',logica,(193,196,199))
restart_label = label.render('Restart',logica,(115,132,148))
restart_label_rect =restart_label.get_rect(topleft =(180,200))



                             #SIKL




dis =True
while dis:
    
    
    screen.blit(bg,(bg_x, 0))
    screen.blit(bg,(bg_x + 620, 0))
    

    
    if gameplay:


        player_rect = walk_left[0].get_rect(topleft = (player_x,player_y))
        if brag_list:
            for (el,i) in enumerate(brag_list):
                screen.blit (car,i)
                i.x -=10
                if player_rect.colliderect(i):
                    gameplay = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player_x > 50:
            screen.blit(walk_left[player_anim_count],(player_x,player_y))
        else:
            screen.blit(walk_right[player_anim_count],(player_x,player_y))
        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 700:
            player_x += player_speed


        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jum_count > -11:
                if jum_count > 0:
                    player_y -= (jum_count **2)/2
                else :
                    player_y += (jum_count **2)/2
                jum_count -= 1
            else:
                is_jump=False
                jum_count = 10

        

        if player_anim_count == 3:
            player_anim_count = 0
        else :
            player_anim_count += 1
            
        bg_x -= 2
        if bg_x == -620:
            bg_x = 0
        
        if puls:
            for (i , el) in enumerate(puls):
                screen.blit(pul,(el.x,el.y))
                el.x +=4
                
                if el.x > 630:
                    puls.pop(i)
                
                if brag_list:
                    for (index,brag_el)in enumerate(brag_list):
                        if el.colliderect(brag_el):
                            brag_list.pop(index)
                            puls.pop(i)
    else:
        screen.fill((72,0,120))
        screen.blit(lose_label,(180,100))
        screen.blit(restart_label,restart_label_rect)
        
        mouse = pygame.mouse.get_pos()

        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            brag_list.clear()
            puls.clear()
            
            puls_left = 10
        
    


        
        car_x -= 10

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dis == False
            pygame.quit()
        if event.type == brag_timer:
            brag_list.append(car.get_rect(topleft =(600,350)))
            
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_UP\
            and puls_left > 0:
            puls.append(pul.get_rect(topleft = (player_x + 10,player_y+4)))
            puls_left -=1
            
                



    clock.tick(20)
