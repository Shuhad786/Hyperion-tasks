import pygame 
import random
pygame.init() 

screen_width = 800 #resolution X
screen_height = 600 #resolution Y
screen = pygame.display.set_mode((screen_width,screen_height),pygame.FULLSCREEN) #screen made to fit monitor
pygame.display.set_caption("spiderman in action") #name of the game
screen_borderX = screen_width - 100 #stops the player from going off screen
screen_borderY = screen_height - 100 #stops the player from going off screen

music = pygame.mixer.music.load("song.mp3") #background song
pygame.mixer.music.play(-1) #loop for the background song

spiderman = pygame.image.load("spider.png") #images for the game
villain = pygame.image.load("venom.png")
lazer = pygame.image.load("hadoken.png")
prize = pygame.image.load("gold.jpg")
throw_object = pygame.image.load("rock.png")
background = pygame.image.load("wall.jpg")

spidey_height = spiderman.get_height() #dimensions for characters
spidey_width = spiderman.get_width()
venom_height = villain.get_height()
venom_width = villain.get_width()
hadoken_height = lazer.get_height()
hadoken_width = lazer.get_width()
gold_height = prize.get_height()
gold_width = prize.get_width()
rock_height = throw_object.get_height()
rock_width = throw_object.get_width()



print("This is the height of the player image: " +str(spidey_height))
print("This is the width of the player image: " +str(spidey_width))

spidermanXPosition = 50 #position of player X
spidermanYPosition = 50 #position of player Y
vel = 5 #speed at which player moves

villainXPosition =  screen_width + 50 #position of enemies and prize
villainYPosition =  random.randint(0, screen_height - venom_height)
lazerXPosition =  screen_width + 300
lazerYPosition =  random.randint(0, screen_height - hadoken_height)
prizeXPosition =  screen_width + 400
prizeYPosition =  random.randint(0, screen_height - gold_height)
throw_objectXPosition =  screen_width + 100
throw_objectYPosition =  random.randint(0, screen_height - rock_height)

while 1: 

    screen.fill((0,0,0)) # Clears the screen.
    screen.blit(background, (0, 0))
    screen.blit(spiderman, (spidermanXPosition, spidermanYPosition)) # This draws characters images to the screen at the position specified
    screen.blit(villain, (villainXPosition, villainYPosition))
    screen.blit(lazer, (lazerXPosition, lazerYPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    screen.blit(throw_object, (throw_objectXPosition, throw_objectYPosition))
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    keys = pygame.key.get_pressed() #keys are listed for ease

    if keys[pygame.K_UP] and spidermanYPosition > vel:
       spidermanYPosition -= vel 
        
    if keys[pygame.K_DOWN] and spidermanYPosition < screen_borderY - vel:
       spidermanYPosition += vel 

    if keys[pygame.K_LEFT] and spidermanXPosition > vel:
        spidermanXPosition -= vel

    if keys[pygame.K_RIGHT] and spidermanXPosition < screen_borderX - vel:
        spidermanXPosition += vel

    #Bounding box for player

    spidermanBox = pygame.Rect(spiderman.get_rect())
    spidermanBox.top = spidermanYPosition
    spidermanBox.left = spidermanXPosition

    # Bounding box for the enemies and prize:

    villainBox = pygame.Rect(villain.get_rect())
    villainBox.top = villainYPosition
    villainBox.left = villainXPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    lazerBox = pygame.Rect(lazer.get_rect())
    lazerBox.top = lazerYPosition
    lazerBox.left = lazerXPosition

    throw_objectBox = pygame.Rect(throw_object.get_rect())
    throw_objectBox.top = throw_objectYPosition
    throw_objectBox.left = throw_objectXPosition
    
   
    # Test collision of the boxes:
    
    if spidermanBox.colliderect(villainBox):
        print("You died!")
        pygame.quit()
        exit(0)

    elif spidermanBox.colliderect(lazerBox):
        print("You died!")
        pygame.quit()
        exit(0)

    elif spidermanBox.colliderect(throw_objectBox):
        print("You died!")
        pygame.quit()
        exit(0)

    if spidermanBox.colliderect(prizeBox):
        print("You got the gold!")
        pygame.quit()
        exit(0)
        
    # If the prize is off the screen the user loses the game:
    if prizeXPosition < 0 - gold_width:
        print("you lost!")
        pygame.quit()
        exit(0) 
        
    
    
    # Make enemy approach the player.
    
    villainXPosition -= 0.70
    prizeXPosition -= 0.50
    lazerXPosition -= 0.60
    throw_objectXPosition -= 0.90
    # ================The game loop logic ends here. =============
  

 
