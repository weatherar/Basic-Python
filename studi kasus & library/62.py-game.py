import pygame

# init
pygame.init()

# variable running game 
isRun = True 

#membuat dsiplay surface object 
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang))

# object game
# posisi
x = 250
y = 250

# ukuran
panjang = 20
lebar = 20

# kecepatan
speed = 10


while isRun:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
            
    #ambil semua keyboard press
    keys = pygame.key.get_pressed()
    
    # ambil ke kiri 

    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
        
    if keys[pygame.K_RIGHT] and x < window_lebar-lebar:
        x += speed
        
    if keys[pygame.K_DOWN] and y < window_panjang-panjang:
        y += speed
        
    if keys[pygame.K_UP] and y > 0:
        y -= speed
        

    # game dynamic 
    

    #update asset
    window.fill((255,255,255))
    pygame.draw.rect(window,(255,120,0),(x,y,lebar,panjang))
    #render ke display
    pygame.display.update()
    
pygame.quit()


# user input, database input
# update asset
# render ke display

