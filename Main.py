import pygame ,random
from duck import Duck, cursor
from dog import Dog
from tkinter import messagebox, Tk

started = False
numclicks = 0 
thing = 0
thing2 = 0
check = False

pygame.init()
pygame.display.set_caption('Duck Hunt \u00a9 Nintendo 1985')
imgicon = pygame.image.load('images/duckhunticon.png')
imgicon = pygame.transform.smoothscale(imgicon, (imgicon.get_width() // 2, imgicon.get_height() // 2))
pygame.display.set_icon(imgicon)
pygame.mouse.set_visible(False)
surface = pygame.display.set_mode((640, 480))

# Initilalizng classes
crosshair = cursor()
dog = Dog(surface)
duck1 = Duck(surface) 
duck2 = Duck(surface)

# Fonts
start_font = pygame.font.Font('neuropol.ttf', 24)
game_font = pygame.font.Font('neuropol.ttf',20)
start_output = start_font.render('CLICK SPACEBAR TO BEGIN', True, '#80d010')

# Gameplay values 
score = 0 
hits = 0 
accuracy = 0
game_output1 = game_font.render("SCORE:    " + str(score), True,'#80d010')
game_output2 = game_font.render("HITS:    " + str(hits), True, '#80d010')
game_output3 = game_font.render("ACCURACY:    " + str(accuracy) + "%", True, '#80d010')

# Background images
imgBackground = pygame.image.load('images/background.png')
imgForeground = pygame.image.load('images/foreground.png')

# Initializing mixer, music, soundeffects
pygame.mixer.init()
pygame.mixer.music.load('intro.mp3')
pygame.mixer.music.play(-1)
soundeffects = [pygame.mixer.Sound('gunshot.mp3')]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
# Account for crosshair movement
        if event.type == pygame.MOUSEMOTION:
            crosshair.setX(event.pos[0] - (crosshair.getWidth() // 2))
            crosshair.setY(event.pos[1])
# Account for dog movement
        if event.type == pygame.USEREVENT:
            dog.move()
            if dog.getX() + dog.getWidth() >= surface.get_width():
                dog.setDirection("left")
            elif dog.getX() <= 0:
                dog.setDirection("right")
# Accoutn for duck movement
        if event.type == pygame.USEREVENT + 1:
            duck1.move()
            if duck1.getY() <=0:
                duck1.setDirectionY("down")
            elif duck1.getY() >=250:
                duck1.setDirectionY("up")
            if duck1.getX() >= surface.get_width():
                duck1.setDirectionX("left")
            elif duck1.getX() + duck1.getWidth() <= 0:
                duck1.setDirectionX("right")
        if event.type == pygame.USEREVENT + 2:
            duck2.move()
            if duck2.getY() <=0:
                duck2.setDirectionY("down") 
            elif duck2.getY() >=250:
                duck2.setDirectionY("up")
            if duck2.getX() >= surface.get_width():
                duck2.setDirectionX("left")
            elif duck2.getX() + duck2.getWidth() <= 0:
                duck2.setDirectionX("right")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and started == False:
                pygame.time.set_timer(pygame.USEREVENT, 70)
                pygame.time.set_timer(pygame.USEREVENT + 1,random.randint(30,40))
                pygame.time.set_timer(pygame.USEREVENT + 2,random.randint(30,40))
                started = True
        if event.type == pygame.MOUSEBUTTONDOWN and started == True:
            if event.button == pygame.BUTTON_LEFT:
                if dog.isHit() == False:
                    pygame.mixer.Sound.play(soundeffects[0])
                    numclicks += 1
                    if crosshair.getBounds().colliderect(duck1.getBounds()) and duck1.isDead() == False:
                        check = True
                        duck1.killDuck()
                        score += 10
                        hits += 1 
                        game_output1 = game_font.render("SCORE:    " + str(score), True,'#80d010')
                        game_output2 = game_font.render("HITS:    " + str(hits), True, '#80d010')
                    if crosshair.getBounds().colliderect(duck2.getBounds()) and duck2.isDead() == False and check == False:
                        duck2.killDuck()
                        score += 10 
                        hits += 1
                        game_output1 = game_font.render("SCORE:    " + str(score), True,'#80d010')
                        game_output2 = game_font.render("HITS:    " + str(hits), True, '#80d010')
                    if crosshair.getBounds().colliderect(dog.getBounds()):
                        dog.shootDog()
                    check = False
            accuracy = (f'{(hits/numclicks)*100:.0f}')
            game_output3 = game_font.render("ACCURACY:  " + str(accuracy) + "%", True, '#80d010')
# End game if player's accuracy is less than 65% and have clicked more than 5 times
            if int(accuracy) < 65 and numclicks > 5:
                pygame.mixer.music.stop()
                Tk().withdraw()
                box = messagebox.askyesno('Duck Hunt', 'GAME OVER\nYour final score is ' + str(score) + '\nWould you like to play again? ')
                if box == True:
                    pygame.mixer.music.play(-1)
                    started = False
                    hits = 0 
                    score = 0 
                    accuracy = 0 
                    numclicks = 0 
                    dog.reset()
                    duck1.reset()
                    duck2.reset()
                    game_output1 = game_font.render("SCORE:    " + str(score), True,'#80d010')
                    game_output2 = game_font.render("HITS:    " + str(hits), True, '#80d010')
                    game_output3 = game_font.render("ACCURACY:  " + str(accuracy) + "%", True, '#80d010')
                elif box == False:
                    pygame.quit()

# Blit the background on the surface
    surface.blit(imgBackground, (0, 0))
    if started == False:
        surface.blit(start_output, ((surface.get_width() - start_output.get_width()) // 2, surface.get_height() - 50))
    if started == True:
        surface.blit(duck1.getImage(),duck1.getLocation())
        surface.blit(duck2.getImage(),duck2.getLocation())
# Account for the dog being shot
        if dog.isHit() == True:
            surface.blit(dog.getImage(),dog.getLocation())
        surface.blit(imgForeground,(0,0))
        surface.blit(game_output1, (game_output1.get_width() - 140, surface.get_height() - 50))
        surface.blit(game_output2, (game_output2.get_width() + 110, surface.get_height() - 50))
        surface.blit(game_output3, (game_output3.get_width() + 140, surface.get_height() - 50))
        if dog.isHit() == False:
            surface.blit(dog.getImage(),dog.getLocation())
    surface.blit(crosshair.getcrosshairimg(), (crosshair.getDirections()))
# Update the surface
    pygame.display.update()
    
    