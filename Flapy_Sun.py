import pygame 
import random
import os

pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((700, 700))#(800 → X),(800 ↓ Y) 380, 380 300 300
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Flapy Sun")
screen.fill((69,179,255))
#Default Values
y_bird = 330
speed = 2

velosity = 3.0
acselitarion = 0.15

Reset_Count = 0

x_pipe = 700
x_pipe2 = 1000
x_pipe3 = 1300
all_pipe_Y = 480
score = 0
ground_speed = 2
ground_x_1 = 0
ground_x_2 = 700
ground_x_3 = 1400
Game_Over = False

Cload_Speed = .3
Cload_X = random.randint(0, 200)
Random_Cloud_Y = random.randint(10, 300)

Cload_Speed_2 = .3
Cload_X_2 = random.randint(200, 400)
Random_Cloud_Y_2 = random.randint(10, 300)

Cload_Speed_3 = .3
Cload_X_3 = random.randint(400, 600)
Random_Cloud_Y_3 = random.randint(10, 300)

def image_path(image):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(BASE_DIR, "Sprites", image)
    return image_path

Pipe_Top = pygame.image.load(image_path("Pipe_Top.png")).convert_alpha()
Pipe_Bottom = pygame.image.load(image_path('Pipe_Bottom.png')).convert_alpha()
FlapySun = pygame.image.load(image_path('Flapy_Sun.png')).convert_alpha()

#Grounds
Ground_1 = pygame.image.load(image_path('Ground_1.png')).convert_alpha()
Ground_2 = pygame.image.load(image_path('Ground_2.png')).convert_alpha()
Ground_3 = pygame.image.load(image_path('Ground_3.png')).convert_alpha()
#Back Ground 
Back_Ground = pygame.image.load(image_path('Back_Ground.png'))
#Buttons
Button_Ligth = pygame.image.load(image_path('Button_Light.png')).convert_alpha()
Buttom_Dark = pygame.image.load(image_path('Button_Dark.png')).convert_alpha()
#Clouds
Cloud_1 = pygame.image.load(image_path('Cloud_1.png')).convert_alpha()
Cloud_2 = pygame.image.load(image_path('Cloud_2.png')).convert_alpha()
Cloud_3 = pygame.image.load(image_path('Cloud_3.png')).convert_alpha()
#Game_Over
Game_OverV2 = pygame.image.load(image_path('Game_OverV2.png')).convert_alpha()
#Press_Any_Buttom
Press_Any_Buttom = pygame.image.load(image_path('Press_Any_Button_To_Reset.png')).convert_alpha()
#Flap Sound
Flap_Sound = pygame.mixer.Sound(image_path('Flap_SoundV1.wav'))
#Icon
icon_image = pygame.image.load(image_path('A_Sun_Yey.png'))
pygame.display.set_icon(icon_image)

screen.blit(FlapySun, (100, y_bird))

random_pipe_higth = random.randint(-80, 80)
random_pipe_higth2 = random.randint(-80, 80)
random_pipe_higth3 = random.randint(-80, 80)
while running:
    #Resets The Pipe Position 
    all_pipe_Y = 430
    all_pipe_Y_test = -530

    #Gravity of a bird
    if Game_Over == False:
        y_bird = y_bird + velosity
        velosity = velosity + acselitarion

    #Makes a sky color and fill the screan
    screen.fill((69,179,255))
    #Cloads
    Cload_X += Cload_Speed
    screen.blit(Cloud_1, (Cload_X, Random_Cloud_Y))
    if Cload_X >= 700:
        Cload_X = -100 - random.randint(0, 30)
        Random_Cloud_Y = random.randint(10, 300)    

    Cload_X_2 += Cload_Speed_2
    screen.blit(Cloud_2, (Cload_X_2, Random_Cloud_Y_2))
    if Cload_X_2 >= 700:
        Cload_X_2 = -100 - random.randint(0, 30)
        Random_Cloud_Y_2 = random.randint(10, 300)    

    Cload_X_3 += Cload_Speed_3
    screen.blit(Cloud_3, (Cload_X_3, Random_Cloud_Y_3))
    if Cload_X_3 >= 700:
        Cload_X_3 = -100 - random.randint(0, 30)
        Random_Cloud_Y_3 = random.randint(10, 300)

    #Adds a bird to the screen
    screen.blit(FlapySun, (100, y_bird))#Bird

    if x_pipe <= 1300:
        x_pipe = x_pipe - speed
        screen.blit(Pipe_Top, (x_pipe, all_pipe_Y_test + random_pipe_higth))
        screen.blit(Pipe_Bottom, (x_pipe, all_pipe_Y + random_pipe_higth)) 
    #Check if the pipe leves the screan
    if x_pipe == -120:
        #Moves it back to the start
        x_pipe = 800
        #Random mizes the pipe Y position
        random_pipe_higth = random.randint(-80, 80)   

    if x_pipe2 <= 1300:
        x_pipe2 = x_pipe2 - speed
        screen.blit(Pipe_Top, (x_pipe2, all_pipe_Y_test + random_pipe_higth2))
        screen.blit(Pipe_Bottom, (x_pipe2, all_pipe_Y + random_pipe_higth2)) 
    if x_pipe2 == -120:
        x_pipe2 = 800
        random_pipe_higth2 = random.randint(-80, 80)


    if x_pipe3 <= 1300:
        x_pipe3 = x_pipe3 - speed
        screen.blit(Pipe_Top, (x_pipe3, all_pipe_Y_test + random_pipe_higth3))
        screen.blit(Pipe_Bottom, (x_pipe3, all_pipe_Y+random_pipe_higth3)) 
    if x_pipe3 == -120:
        x_pipe3 = 800
        random_pipe_higth3 = random.randint(-80, 80)

    #Checks is the touches the top the the map and end the game
    if y_bird <= 0:
        Game_Over = True 
    #Get the info if the the bird hit box has been coved by a pipe == thouched the pipe
    if Game_Over == False:
        pixel_color_TOP_LEFT = screen.get_at((100, int(y_bird)))
        pixel_color_BOTTOM_LEFT = screen.get_at((100, int(y_bird+35)))

        pixel_color_TOP_RIGHT = screen.get_at((100+35, int(y_bird)))
        pixel_color_BOTTOM_RIGHT = screen.get_at((100+35, int(y_bird+35)))

    #If the pixel is green end the game 
    if (pixel_color_TOP_LEFT == (41,212,91) or  pixel_color_BOTTOM_LEFT == (41,212,91)) or (pixel_color_TOP_LEFT == (57,107,22) or  pixel_color_BOTTOM_LEFT == (57,107,22)) or (pixel_color_TOP_LEFT == (90,168,35) or  pixel_color_BOTTOM_LEFT == (90,168,35)):
            Game_Over == True
    if (pixel_color_TOP_RIGHT == (41,212,91) or  pixel_color_BOTTOM_RIGHT == (41,212,91)) or (pixel_color_TOP_LEFT == (57,107,22) or  pixel_color_BOTTOM_LEFT == (57,107,22)) or (pixel_color_TOP_LEFT == (90,168,35) or  pixel_color_BOTTOM_LEFT == (90,168,35)):  
            Game_Over = True
    #End the game if the bird touches the ground
    if y_bird >= 615:
         Game_Over = True

    #Ground movent
    ground_x_1 = ground_x_1 - ground_speed
    ground_x_2 = ground_x_2 - ground_speed
    ground_x_3 = ground_x_3 - ground_speed
    #Checks if the ground leaves the screen 
    if ground_x_1 == -700:
        #Moves the ground to the start
        ground_x_1 = 1400
    if ground_x_2 == -700:
        ground_x_2 = 1400
    if ground_x_3 == -700:
        ground_x_3 = 1400
    #And dravv the ground
    screen.blit(Ground_1, (ground_x_1, 650))
    screen.blit(Ground_2, (ground_x_2, 650))
    screen.blit(Ground_2, (ground_x_3, 650))

    if Game_Over == True:
        #Game_Over Text
        y_bird = 330
        Reset_Count += 1
        screen.blit(Game_OverV2, (249, 319)) 
        screen.blit(Press_Any_Buttom, (410,370))

    #Checks if the pipe leaves the screan
    #vvith out ending the game
    if Game_Over == False:
        if x_pipe == 0 or x_pipe2 == 0 or x_pipe3 == 0:
            #inceases the score
            score = score + 1
    #Dravv the score to the screen 
    score_text = str(score)
    Score_Text = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface3 = Score_Text.render(score_text, False, (255, 255, 255))
    #Checks the legth of the text and moves is to make it fit
    screen.blit(text_surface3, (670 - (5 * len(score_text)), 5))
    #Chekcs for events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Vhen vvindovv is close end the game
            running = False
        if Game_Over == False:
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                #Flaps a brid
                if keys[pygame.K_SPACE]:
                    velosity = -4
                    Flap_Sound.play()
        if event.type == pygame.KEYDOWN:
            if Game_Over == True:
                Reset_Count += 1
                if Reset_Count >= 30:
                    Flap_Sound.play()
                    y_bird = 330
                    speed = 2
                    velosity = -4
                    x_pipe = 700
                    x_pipe2 = 1000
                    x_pipe3 = 1300
                    all_pipe_Y = 480
                    score = 0
                    ground_x_1 = 0
                    ground_x_2 = 700
                    ground_x_3 = 1400
                    Game_Over = False
                    Reset_Count = 0
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
#End the game
pygame.quit()