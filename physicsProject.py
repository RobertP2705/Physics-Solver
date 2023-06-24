# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
import math
import numpy

pygame.init()
icon = pygame.image.load("graphics/physicsIcon.jpg")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Physics')
clock = pygame.time.Clock()
title_font = pygame.font.Font('fonts/Queensides.ttf', 50)
boatProblem_font = pygame.font.Font('fonts/Queensides.ttf', 75)
boatProblem_velocity_font = pygame.font.Font('fonts/Queensides.ttf', 15)
boatProblem_decimals_font = pygame.font.Font('fonts/Queensides.ttf', 30)

physics_solver_text = pygame.image.load("graphics/physicsSolverText.png")
physics_solver_text_rect = physics_solver_text.get_rect(center = (400,200))

back_arrow = pygame.image.load('graphics/backArrow.png').convert_alpha()
back_arrow_rect = back_arrow.get_rect(topleft = (0,0))

def make_button(button_text, text_rect, color,x,y,width,length,border):
    button = pygame.draw.rect(screen, color, pygame.Rect(x, y, width, length), border)
    screen.blit(button_text, text_rect)
    return button
#boat
boatFrame1 = pygame.image.load('graphics/boatImage1.png').convert_alpha()
boatFrame2 = pygame.image.load('graphics/boatImage2.png').convert_alpha()
boatImage = boatFrame1

boatImage_rect = boatImage.get_rect(center = (200,670))

#playButton
playButton = pygame.image.load('graphics/playButton.png').convert_alpha()
playButton_rect = playButton.get_rect(center = (750,550))

#stopButton
stopButton = pygame.image.load('graphics/stopButton.png').convert_alpha()
stopButton_rect = stopButton.get_rect(center = (750,550))

#settings button
settings_frame1 = pygame.image.load('graphics/settingsIconFrame1.png')
settings_frame2 = pygame.image.load('graphics/settingsIconFrame2.png')
settings_button = settings_frame1
settings_button_rect = settings_button.get_rect(topleft = (700,700))


physics1_button_x = 290
physics1_button_y = 340
physics1_button_frame1 = pygame.image.load('graphics/physics1FirstFrame.png')
physics1_button_frame2 = pygame.image.load('graphics/physics1SecondFrame.png')
physics1_button = physics1_button_frame1
physics1_button_rect = physics1_button.get_rect(center = (425,physics1_button_y-10))

physics1_boatProblem_x = 180
physics1_boatProblem_y = 180
physics1_boatProblem_frame1 = pygame.image.load('graphics/boatProblemFirstFrame (2).png')
physics1_boatProblem_frame2 = pygame.image.load('graphics/boatProblemSecondFrame (2).png')
physics1_boatProblem = physics1_boatProblem_frame1
physics1_boatProblem_rect = physics1_boatProblem.get_rect(center = (400,300))


#pulley problem
physics1_pulleyProblem_frame1 = pygame.image.load('graphics/pulleyProblemFirstFrame (2).png')
physics1_pulleyProblem_frame2 = pygame.image.load('graphics/pulleyProblemSecondFrame (2).png')
physics1_pulleyProblem = physics1_boatProblem_frame1
physics1_pulleyProblem_rect = physics1_boatProblem.get_rect(center = (400,500))

#velocity variables
physics1_boatProblem_velocity_x = 550
physics1_boatProblem_velocity_y = 180
physics1_boatProblem_velocity_textBox = boatProblem_velocity_font.render("", False, ("Black"))
physics1_boatProblem_velocity_rectBox = physics1_boatProblem_velocity_textBox.get_rect(topleft = (physics1_boatProblem_velocity_x+5,physics1_boatProblem_velocity_y))
velocityNumber = ""

physics1_boatProblem_velocity_text = boatProblem_velocity_font.render("Boat Velocity:", False, ("Black"))
physics1_boatProblem_velocity_rect = physics1_boatProblem_velocity_textBox.get_rect(topleft = (physics1_boatProblem_velocity_x-100,physics1_boatProblem_velocity_y))
velocityTextLength = 15
boatVelocity = 0





#boat width variables
boatOffset = 25
physics1_boatProblem_boatWidth_textBox = boatProblem_velocity_font.render("", False, ("Black"))
physics1_boatProblem_boatWidth_rectBox = physics1_boatProblem_velocity_textBox.get_rect(topleft = (physics1_boatProblem_velocity_x+5,physics1_boatProblem_velocity_y-boatOffset))

physics1_boatProblem_boatWidth_text = boatProblem_velocity_font.render("River Width:", False, ("Black"))
physics1_boatProblem_boatWidth_rect = physics1_boatProblem_velocity_textBox.get_rect(topleft = (physics1_boatProblem_velocity_x-100,physics1_boatProblem_velocity_y-boatOffset))
boatWidthTextLength = 15
boatProblemboatWidth_button = make_button(physics1_boatProblem_boatWidth_textBox, physics1_boatProblem_boatWidth_rectBox, "#FFFFFF",physics1_boatProblem_velocity_x, physics1_boatProblem_y - boatOffset, boatWidthTextLength, 20,0)
boatWidthNumber = ""

physics_mode = 0
button_focus = 0

#river current
riverOffset = 50
physics1_boatProblem_riverCurrent_textBox = boatProblem_velocity_font.render("", False, ("Black"))
physics1_boatProblem_riverCurrent_rectBox = physics1_boatProblem_velocity_textBox.get_rect(topleft = (physics1_boatProblem_velocity_x+5,physics1_boatProblem_velocity_y-riverOffset))

physics1_boatProblem_riverCurrent_text = boatProblem_velocity_font.render("River Current:", False, ("Black"))
physics1_boatProblem_riverCurrent_rect = physics1_boatProblem_velocity_textBox.get_rect(topleft = (physics1_boatProblem_velocity_x-100,physics1_boatProblem_velocity_y-riverOffset))
riverCurrentTextLength = 15
boatProblemriverCurrent_button = make_button(physics1_boatProblem_riverCurrent_textBox, physics1_boatProblem_riverCurrent_rectBox, "#A9A9A9",physics1_boatProblem_velocity_x, physics1_boatProblem_y - riverOffset, riverCurrentTextLength, 20,0)
riverCurrentNumber = ""




#items to solve for
#angle variables
angleOffset = -50
physics1_boatProblem_angle_textBox = boatProblem_velocity_font.render("", False, ("Black"))
physics1_boatProblem_angle_rectBox = physics1_boatProblem_velocity_textBox.get_rect(topleft = (physics1_boatProblem_velocity_x+5,physics1_boatProblem_velocity_y-angleOffset))

physics1_boatProblem_angle_text = boatProblem_velocity_font.render("Boat Angle:", False, ("Black"))
physics1_boatProblem_angle_rect = physics1_boatProblem_velocity_textBox.get_rect(topleft = (physics1_boatProblem_velocity_x-100,physics1_boatProblem_velocity_y-angleOffset))
angleTextLength = 15
boatProblemAngle_button = make_button(physics1_boatProblem_angle_textBox, physics1_boatProblem_angle_rectBox, "Yellow",physics1_boatProblem_velocity_x, physics1_boatProblem_y - angleOffset, angleTextLength, 20,0)
angleNumber = ""


#magnitude of boat's velocity
velocityMagnitudeOffset = -75
velocityMagnitudeTextLength = 15
physics1_boatProblem_velocityMagnitude_textBox = boatProblem_velocity_font.render("", False, ("Black"))
physics1_boatProblem_velocityMagnitude_rectBox = physics1_boatProblem_velocity_textBox.get_rect(topleft = (physics1_boatProblem_velocity_x+5,physics1_boatProblem_velocity_y-velocityMagnitudeOffset))

physics1_boatProblem_velocityMagnitude_text = boatProblem_velocity_font.render("Magnitude of boat velocity:", False, ("Black"))
physics1_boatProblem_velocityMagnitude_rect = physics1_boatProblem_velocity_textBox.get_rect(topleft = (physics1_boatProblem_velocity_x-200,physics1_boatProblem_velocity_y-velocityMagnitudeOffset))
velocityMagnitudeTextLength = 15
boatProblemvelocityMagnitude_button = make_button(physics1_boatProblem_velocityMagnitude_textBox, physics1_boatProblem_velocityMagnitude_rectBox, "#A9A9A9",physics1_boatProblem_velocity_x, physics1_boatProblem_y - velocityMagnitudeOffset, velocityMagnitudeTextLength, 20,0)
velocityMagnitudeNumber = ""

#time for the boat to reach the opposite shore-line
boatTimeOffset = -100
boatTimeTextLength = 15
physics1_boatProblem_boatTime_textBox = boatProblem_velocity_font.render("", False, ("Black"))
physics1_boatProblem_boatTime_rectBox = physics1_boatProblem_velocity_textBox.get_rect(topleft = (physics1_boatProblem_velocity_x+5,physics1_boatProblem_velocity_y-boatTimeOffset))

physics1_boatProblem_boatTime_text = boatProblem_velocity_font.render("Time for the boat to reach the end:", False, ("Black"))
physics1_boatProblem_boatTime_rect = physics1_boatProblem_velocity_textBox.get_rect(topleft = (physics1_boatProblem_velocity_x-250,physics1_boatProblem_velocity_y-boatTimeOffset))
boatProblemboatTime_button = make_button(physics1_boatProblem_boatTime_textBox, physics1_boatProblem_boatTime_rectBox, "#A9A9A9",physics1_boatProblem_velocity_x, physics1_boatProblem_y - boatTimeOffset, boatTimeTextLength, 20,0)
boatTimeNumber = ""

#distance the boat travels dowsntream
distanceTravelledOffset = -125
distanceTravelledTextLength = 15
physics1_boatProblem_distanceTravelled_textBox = boatProblem_velocity_font.render("", False, ("Black"))
physics1_boatProblem_distanceTravelled_rectBox = physics1_boatProblem_velocity_textBox.get_rect(topleft = (physics1_boatProblem_velocity_x+5,physics1_boatProblem_velocity_y-distanceTravelledOffset))

physics1_boatProblem_distanceTravelled_text = boatProblem_velocity_font.render("Distance travelled downstream:", False, ("Black"))
physics1_boatProblem_distanceTravelled_rect = physics1_boatProblem_velocity_textBox.get_rect(topleft = (physics1_boatProblem_velocity_x-225,physics1_boatProblem_velocity_y-distanceTravelledOffset))
boatProblemdistanceTravelled_button = make_button(physics1_boatProblem_distanceTravelled_textBox, physics1_boatProblem_distanceTravelled_rectBox, "#A9A9A9",physics1_boatProblem_velocity_x, physics1_boatProblem_y - distanceTravelledOffset, distanceTravelledTextLength, 20,0)
distanceTravelledNumber = ""

#distance the boat travels dowsntream
timeElapsed = "0"
timeElapsedOffset = -225
timeElapsedTextLength = 330
physics1_boatProblem_timeElapsed_textBox = boatProblem_decimals_font.render("Time Elapsed: " + timeElapsed + " seconds", False, ("Black"))
physics1_boatProblem_timeElapsed_rectBox = physics1_boatProblem_velocity_textBox.get_rect(topleft = (physics1_boatProblem_velocity_x-100,physics1_boatProblem_velocity_y-timeElapsedOffset))


boatProblemtimeElapsed_button = make_button(physics1_boatProblem_timeElapsed_textBox, physics1_boatProblem_timeElapsed_rectBox, "White",physics1_boatProblem_velocity_x, physics1_boatProblem_y - timeElapsedOffset, timeElapsedTextLength, 40,0)

#decimals
decimals = False
decimalsOffset = -150
decimalsTextLength = 50
physics1_boatProblem_decimals_textBox = boatProblem_decimals_font.render("", False, ("Black"))
physics1_boatProblem_decimals_rectBox = physics1_boatProblem_velocity_textBox.get_rect(topleft = (physics1_boatProblem_velocity_x+4,physics1_boatProblem_velocity_y-decimalsOffset))

physics1_boatProblem_decimals_text = boatProblem_velocity_font.render("Decimals:", False, ("Black"))
physics1_boatProblem_decimals_rect = physics1_boatProblem_velocity_textBox.get_rect(topleft = (physics1_boatProblem_velocity_x-75,physics1_boatProblem_velocity_y-decimalsOffset+10))
boatProblemdecimals_button = make_button(physics1_boatProblem_decimals_textBox, physics1_boatProblem_decimals_rectBox, "Red",physics1_boatProblem_velocity_x, physics1_boatProblem_y - decimalsOffset, decimalsTextLength, 40,0)


#arrow timers
arrow_timer = pygame.USEREVENT + 1
wait_for_arrow = False
pygame.time.set_timer(arrow_timer, 1400)
typing = False
angleNumber = ""

boatProblemVelocity_button = make_button(physics1_boatProblem_velocity_textBox, physics1_boatProblem_velocity_rectBox,
                                         "#FFFFFF", physics1_boatProblem_velocity_x, physics1_boatProblem_y,
                                         velocityTextLength, 20, 0)

timeClock = pygame.time.Clock()
clockTick = 0
start_time = 0
real_start_time = 0
#variables for animation
runAnimation = False
boatFollowMouse = False

#Pulley Problem
#mass1
mass1x = 335
mass1y = 415
mass1TextLength = 15
physics1_pulleyProblem_mass1_textBox = boatProblem_velocity_font.render("", False, ("Black"))
physics1_pulleyProblem_mass1_rectBox = physics1_pulleyProblem_mass1_textBox.get_rect(topleft = (mass1x,mass1y))

pulleyProblemmass1_button = make_button(physics1_pulleyProblem_mass1_textBox, physics1_pulleyProblem_mass1_rectBox, "#FFFFFF",mass1x, mass1y, mass1TextLength, 20,0)
mass1Number = ""
mass1IntNumber = 0

#mass 2
mass2x = 440
mass2y = 415
mass2TextLength = 15
physics1_pulleyProblem_mass2_textBox = boatProblem_velocity_font.render("", False, ("Black"))
physics1_pulleyProblem_mass2_rectBox = physics1_pulleyProblem_mass2_textBox.get_rect(topleft = (mass2x,mass2y))

pulleyProblemmass2_button = make_button(physics1_pulleyProblem_mass2_textBox, physics1_pulleyProblem_mass2_rectBox, "#FFFFFF",mass2x, mass2y, mass2TextLength, 20,0)
mass2Number = ""
mass2IntNumber = 0
boatFrameCount = 0


#acceleration
accelerationNumber = ""
accelerationTextLength = 10
physics1_pulleyProblem_acceleration_textBox = boatProblem_velocity_font.render(accelerationNumber, False, ("Black"))
physics1_boatProblem_acceleration_rectBox = physics1_boatProblem_velocity_textBox.get_rect(center = (200,100))

physics1_pulleyProblem_acceleration_text = boatProblem_velocity_font.render("acceleration of blocks:", False, ("Black"))
physics1_pulleyProblem_acceleration_rect = physics1_boatProblem_velocity_textBox.get_rect(center = (500,100))

pulleyProblemacceleration_button = make_button(physics1_pulleyProblem_acceleration_textBox, physics1_boatProblem_acceleration_rectBox, "#A9A9A9", 450,200 , accelerationTextLength, 40,0)

#tension
tensionNumber = ""
tensionTextLength = 10
physics1_pulleyProblem_tension_textBox = boatProblem_velocity_font.render(tensionNumber, False, ("Black"))
physics1_boatProblem_tension_rectBox = physics1_boatProblem_velocity_textBox.get_rect(center = (200,150))

physics1_pulleyProblem_tension_text = boatProblem_velocity_font.render("tension of blocks:", False, ("Black"))
physics1_pulleyProblem_tension_rect = physics1_boatProblem_velocity_textBox.get_rect(center = (530,150))

pulleyProblemtension_button = make_button(physics1_pulleyProblem_tension_textBox, physics1_boatProblem_tension_rectBox, "#A9A9A9", 450,200 , tensionTextLength, 40,0)



#settings screen
screenColor = "Purple"
redOutlineBoxCoordinate = 250
screenColorText = boatProblem_decimals_font.render("Screen Color:", False, ("Black"))
screenColorText_rect = screenColorText.get_rect(center = (150,200))
screenColorPurple_rect = pygame.draw.rect(screen, "Purple", (250, 185, 0, 0))
screenColorGrey_rect = pygame.draw.rect(screen, "Grey", (300, 185, 0, 0))
screenColorOrange_rect = pygame.draw.rect(screen, "#601E51", (350, 185, 0, 0))
screenColorLightPurp_rect = pygame.draw.rect(screen, "#CBC3E3", (400, 185, 0, 0))
screenColorBlue_rect = pygame.draw.rect(screen, "#601EAE", (450, 185, 0, 0))
screenColorGreen_rect = pygame.draw.rect(screen, "#7C587D", (500, 185, 0, 0))


redOutlineBox2Coordinate = 1000
changeMusicText = boatProblem_decimals_font.render("Music:",False,("Black"))
changeMusicText_rect = changeMusicText.get_rect(center = (150, 300))
musicIcon1 = pygame.image.load('graphics/piano1.png')
musicIcon1Rect = musicIcon1.get_rect(center = (270,310))

musicIcon2 = pygame.image.load('graphics/piano2.png')
musicIcon2Rect = musicIcon2.get_rect(center = (330,310))

musicIcon3 = pygame.image.load('graphics/sun.png')
musicIcon3Rect = musicIcon3.get_rect(center = (390,310))

musicIcon4 = pygame.image.load('graphics/moon.png')
musicIcon4Rect = musicIcon4.get_rect(center = (450,310))

musicIcon5 = pygame.image.load('graphics/roblox.png')
musicIcon5Rect = musicIcon5.get_rect(center = (510,310))


funnySoundsText = boatProblem_decimals_font.render("funny sounds:",False,("Black"))
funnySoundsText_rect = changeMusicText.get_rect(center = (150, 300))

#whiteboard
redCircleOutlineCoordinates = (100,1000)
whiteCircleOutlineCoordinates = (1000,1000)
redCirclOutline = pygame.draw.circle(screen, ("Red"), (redCircleOutlineCoordinates), 20, 3)
whiteBoard = pygame.image.load('graphics/whiteboard.png')
whiteBoard_rect = whiteBoard.get_rect(center = (50,740))
pencil = pygame.image.load('graphics/pencil.png')
pencil_rect = pencil.get_rect(center = (100,600))
eraser = pygame.image.load('graphics/eraser.png')
eraser_rect = eraser.get_rect(center = (200,600))
whiteBoardBoard = pygame.image.load('graphics/whiteBoardBoard.png')
whiteBoardBoard_rect = whiteBoardBoard.get_rect(center = (400,400))
loadCount = 0
pencilEraser = 0
def playBoatAnimation(downstream, time, start_time):
    if downstream > 800:
        downstream = 800
    if (pygame.time.get_ticks() - start_time) >= 250:

            pixelPerHeight = ((river.height-60) / time) * .25
            pixelPerLength = (downstream / time) * .25
            boatImage_rect.x += pixelPerLength
            boatImage_rect.y -= pixelPerHeight
            if boatImage_rect.y < river.y-75:
                boatImage_rect.y = river.y-75
            return 250
    return 0
def getInfo(textLength, mode):
    number = ""
    numberKg = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    number += "1"
                    textLength += 3
                if event.key == pygame.K_2:
                    number += "2"
                    textLength += 7
                if event.key == pygame.K_3:
                    number += "3"
                    textLength += 8
                if event.key == pygame.K_4:
                    number += "4"
                    textLength += 7
                if event.key == pygame.K_5:
                    number += "5"
                    textLength += 9
                if event.key == pygame.K_6:
                    number += "6"
                    textLength += 8
                if event.key == pygame.K_7:
                    number += "7"
                    textLength += 7
                if event.key == pygame.K_8:
                    number += "8"
                    textLength += 8
                if event.key == pygame.K_9:
                    number += "9"
                    textLength += 8
                if event.key == pygame.K_0:
                    number += "0"
                    textLength += 10
                if event.key == pygame.K_RETURN and mode == 0:
                    returnArray = [number,textLength+4]
                    return returnArray
                elif event.key == pygame.K_RETURN and mode == 1:
                    numberKg += number + " kg"
                    returnArray = [numberKg, textLength + 13, number]
                    return returnArray
def getTextLength(stringValue):
    textAmount = 5
    for element in stringValue:
        if element == '1':
            textAmount += 3
        if element == '2':
            textAmount += 7
        if element == '3':
            textAmount += 8
        if element == '4':
            textAmount += 7
        if element == '5':
            textAmount += 9
        if element == '6':
            textAmount += 8
        if element == '7':
            textAmount += 7
        if element == '8':
            textAmount += 8
        if element == '9':
            textAmount += 8
        if element == '0':
            textAmount += 10
        if element == '.':
            textAmount += 5
    return textAmount + 5



pulleyGravity = 0
runPulleyAnimation = False
startingPulley = True
pulleyRuncount = 0
showButtons = [False,False]

Line1Set = (348, 400)
Line2Set =(450, 400)

button1Color = "Black"





#SOUNDS
button_sound = pygame.mixer.Sound("sounds/buttonClick.wav")
buttonClicked_sound = pygame.mixer.Sound("sounds/buttonClicked.mp3")
water_sound = pygame.mixer.Sound("sounds/water.wav")
pulley_sound = pygame.mixer.Sound("sounds/pulley.mp3")
playButtonArray = [False,False,False,False,False,False,False,False,False]




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == arrow_timer:
            wait_for_arrow = False

        if physics1_boatProblem_rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 1:
            physics1_boatProblem = physics1_boatProblem_frame2
            if playButtonArray[0] == False:
                pygame.mixer.Sound.play(button_sound)
            playButtonArray[0] = True
        else:
            playButtonArray[0] = False
            physics1_boatProblem = physics1_boatProblem_frame1
        if physics1_pulleyProblem_rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 1:
            physics1_pulleyProblem = physics1_pulleyProblem_frame2
            if playButtonArray[1] == False:
                pygame.mixer.Sound.play(button_sound)
            playButtonArray[1] = True
        else:
            playButtonArray[1] = False
            physics1_pulleyProblem = physics1_pulleyProblem_frame1

        if back_arrow_rect.collidepoint(pygame.mouse.get_pos()) and (physics_mode == 2) and wait_for_arrow == False:
            if playButtonArray[2] == False:
                pygame.mixer.Sound.play(button_sound)
            playButtonArray[2] = True
        else:
            playButtonArray[2] = False
        if back_arrow_rect.collidepoint(pygame.mouse.get_pos()) and (physics_mode == 3) and wait_for_arrow == False:
            if playButtonArray[3] == False:
                pygame.mixer.Sound.play(button_sound)
            playButtonArray[3] = True
        else:
            playButtonArray[3] = False
        if physics1_button_rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 0:
            physics1_button = physics1_button_frame2
            if playButtonArray[4] == False:
                pygame.mixer.Sound.play(button_sound)
            playButtonArray[4] = True
        else:
            button1Color = "Black"
            playButtonArray[4] = False
            physics1_button = physics1_button_frame1

        if back_arrow_rect.collidepoint(pygame.mouse.get_pos()) and (physics_mode == 1) and wait_for_arrow == False:
            if playButtonArray[5] == False:
                pygame.mixer.Sound.play(button_sound)
            playButtonArray[5] = True
        else:
            playButtonArray[5] = False
        if settings_button_rect.collidepoint(pygame.mouse.get_pos()):
            settings_button = settings_frame2
            if playButtonArray[6] == False:
                pygame.mixer.Sound.play(button_sound)
            playButtonArray[6] = True
        else:
            playButtonArray[6] = False
            settings_button = settings_frame1
        if back_arrow_rect.collidepoint(pygame.mouse.get_pos()) and (physics_mode == 4) and wait_for_arrow == False:
            if playButtonArray[7] == False:
                pygame.mixer.Sound.play(button_sound)
            playButtonArray[7] = True
        else:
            playButtonArray[7] = False
        if back_arrow_rect.collidepoint(pygame.mouse.get_pos()) and (physics_mode == 5) and wait_for_arrow == False:
            if playButtonArray[8] == False:
                pygame.mixer.Sound.play(button_sound)
            playButtonArray[8] = True
        else:
            playButtonArray[8] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if physics1_boatProblem_rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 1:
                physics_mode = 2
                pygame.mixer.Sound.play(buttonClicked_sound)
            if settings_button_rect.collidepoint(pygame.mouse.get_pos()):
                physics_mode = 4
                pygame.mixer.Sound.play(buttonClicked_sound)


            #setting color buttons
            if musicIcon1Rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 4 and redOutlineBox2Coordinate == 243:
                themeMusic = pygame.mixer.music.load("sounds/ChopinNocturne.wav")
                redOutlineBox2Coordinate = 1000
            elif musicIcon1Rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 4:
                themeMusic = pygame.mixer.music.load("sounds/ChopinNocturne.wav")
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play(-1)
                redOutlineBox2Coordinate = 243
            if musicIcon2Rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 4 and redOutlineBox2Coordinate == 303:
                themeMusic = pygame.mixer.music.load("sounds/ChopinNocturne.wav")
                redOutlineBox2Coordinate = 1000
            elif musicIcon2Rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 4:
                themeMusic = pygame.mixer.music.load("sounds/ChopinBalladeNo1.wav")
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play(-1)
                redOutlineBox2Coordinate = 303
            if musicIcon3Rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 4 and redOutlineBox2Coordinate == 363:
                themeMusic = pygame.mixer.music.load("sounds/ChopinNocturne.wav")
                redOutlineBox2Coordinate = 1000
            elif musicIcon3Rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 4:
                themeMusic = pygame.mixer.music.load("sounds/sunMusic.mp3")
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play(-1)
                redOutlineBox2Coordinate = 363
            if musicIcon4Rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 4 and redOutlineBox2Coordinate == 423:
                themeMusic = pygame.mixer.music.load("sounds/ChopinNocturne.wav")
                redOutlineBox2Coordinate = 1000
            elif musicIcon4Rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 4:
                themeMusic = pygame.mixer.music.load("sounds/moonMusic.mp3")
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play(-1)
                redOutlineBox2Coordinate = 423
            if musicIcon5Rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 4 and redOutlineBox2Coordinate == 483:
                themeMusic = pygame.mixer.music.load("sounds/ChopinNocturne.wav")
                redOutlineBox2Coordinate = 1000
            elif musicIcon5Rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 4:
                themeMusic = pygame.mixer.music.load("sounds/robloxMusic.mp3")
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play(-1)
                redOutlineBox2Coordinate = 483
            if screenColorPurple_rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 4:
                screenColor = "Purple"
                redOutlineBoxCoordinate = 250
            if screenColorGrey_rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 4:
                screenColor = "Grey"
                redOutlineBoxCoordinate = 300
            if screenColorOrange_rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 4:
                screenColor = "#601E51"
                redOutlineBoxCoordinate = 350
            if screenColorLightPurp_rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 4:
                screenColor = "#CBC3E3"
                redOutlineBoxCoordinate = 400
            if screenColorBlue_rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 4:
                screenColor = "#601EAE"
                redOutlineBoxCoordinate = 450
            if screenColorGreen_rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 4:
                screenColor = "#7C587D"
                redOutlineBoxCoordinate = 500
            if physics1_pulleyProblem_rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 1:
                physics_mode = 3
                pygame.mixer.Sound.play(buttonClicked_sound)
            if back_arrow_rect.collidepoint(pygame.mouse.get_pos()) and (physics_mode == 2) and wait_for_arrow == False:
                physics_mode = 1
                wait_for_arrow = True
                pygame.mixer.Sound.play(buttonClicked_sound)
            if back_arrow_rect.collidepoint(pygame.mouse.get_pos()) and (physics_mode == 4) and wait_for_arrow == False:
                physics_mode = 0
                wait_for_arrow = True
                pygame.mixer.Sound.play(buttonClicked_sound)
            if back_arrow_rect.collidepoint(pygame.mouse.get_pos()) and (physics_mode == 3) and wait_for_arrow == False:
                physics_mode = 1
                wait_for_arrow = True
                pygame.mixer.Sound.play(buttonClicked_sound)
            if back_arrow_rect.collidepoint(pygame.mouse.get_pos()) and (physics_mode == 5) and wait_for_arrow == False:
                physics_mode = 0
                wait_for_arrow = True
                pygame.mixer.Sound.play(buttonClicked_sound)
            if physics1_button_rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 0:
                physics_mode = 1
                pygame.mixer.Sound.play(buttonClicked_sound)
            if back_arrow_rect.collidepoint(pygame.mouse.get_pos()) and (physics_mode == 1) and wait_for_arrow == False:
                physics_mode = 0
                wait_for_arrow = True
                pygame.mixer.Sound.play(buttonClicked_sound)
            if boatProblemVelocity_button.collidepoint(pygame.mouse.get_pos()) and physics_mode == 2:
                velocityNumber = ""
                velocityTextLength = 5
                velocityOutput = getInfo(velocityTextLength, 0)
                velocityTextLength = velocityOutput[1]
                velocityNumber = velocityOutput[0]
            if boatProblemboatWidth_button.collidepoint(pygame.mouse.get_pos()) and physics_mode == 2:
                boatWidthNumber = ""
                boatWidthTextLength = 5
                boatWidthOutput = getInfo(boatWidthTextLength, 0)
                boatWidthNumber = boatWidthOutput[0]
                boatWidthTextLength = boatWidthOutput[1]
            if boatProblemriverCurrent_button.collidepoint(pygame.mouse.get_pos()) and physics_mode == 2:
                riverCurrentNumber = ""
                riverCurrentTextLength = 5
                riverCurrentOutput = getInfo(riverCurrentTextLength, 0)
                riverCurrentNumber = riverCurrentOutput[0]
                riverCurrentTextLength = riverCurrentOutput[1]
            if pencil_rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 5:
                pencilEraser = 1
                redCircleOutlineCoordinates = (100,600)
                whiteCircleOutlineCoordinates = (200,600)
            if eraser_rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 5:
                pencilEraser = 2
                redCircleOutlineCoordinates = (200,600)
                whiteCircleOutlineCoordinates = (100, 600)
            #pulley problem detection
            if pulleyProblemmass1_button.collidepoint(pygame.mouse.get_pos()) and physics_mode == 3:
                mass1Number = ""
                mass1TextLength = 5
                mass1Output = getInfo(mass1TextLength,1)
                mass1Number = mass1Output[0]
                mass1TextLength = mass1Output[1]
                mass1IntNumber = int(mass1Output[2])
                showButtons[0] = True
            if pulleyProblemmass2_button.collidepoint(pygame.mouse.get_pos()) and physics_mode == 3:

                mass2Number = ""
                mass2TextLength = 5
                mass2Output = getInfo(mass2TextLength,1)
                mass2Number = mass2Output[0]
                mass2TextLength = mass2Output[1]
                mass2IntNumber = int(mass2Output[2])
                showButtons[1] = True
            #other things
            if boatProblemdecimals_button.collidepoint(pygame.mouse.get_pos()) and decimals == False and physics_mode == 2:
                decimals = True
            elif boatProblemdecimals_button.collidepoint(pygame.mouse.get_pos()) and decimals == True and physics_mode == 2:
                decimals = False
            if boatProblemdecimals_button.collidepoint(pygame.mouse.get_pos()) and decimals == False and physics_mode == 3:
                decimals = True
            elif boatProblemdecimals_button.collidepoint(pygame.mouse.get_pos()) and decimals == True and physics_mode == 3:
                decimals = False
            if playButton_rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 2 and runAnimation == False:
                runAnimation = True
            elif stopButton_rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 2 and runAnimation == True:
                runAnimation = False
                start_time = pygame.time.get_ticks()
                real_start_time = pygame.time.get_ticks()
                clockTick = 0
            if whiteBoard_rect.collidepoint(pygame.mouse.get_pos()):
                physics_mode = 5
                wait_for_arrow = True
            if playButton_rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 3 and runPulleyAnimation == False:
                runPulleyAnimation = True
                pygame.mixer.Sound.play(pulley_sound)
            elif stopButton_rect.collidepoint(pygame.mouse.get_pos()) and physics_mode == 3 and runPulleyAnimation == True:
                runPulleyAnimation = False
                Line1Set = (348, 400)
                Line2Set = (450, 400)
                mass2y = 415
                mass1y = 415
                physics1_pulleyProblem_mass2_rectBox = physics1_pulleyProblem_mass2_textBox.get_rect(topleft=(mass2x, mass2y))
                physics1_pulleyProblem_mass1_rectBox = physics1_pulleyProblem_mass2_textBox.get_rect(topleft=(mass1x, mass1y))
                pulleyGravity = 0

            if boatImage_rect.collidepoint(pygame.mouse.get_pos()) and runAnimation == False and physics_mode == 2 and boatFollowMouse == True:
                boatFollowMouse = False
            elif boatImage_rect.collidepoint(pygame.mouse.get_pos()) and runAnimation == False and physics_mode == 2 and boatFollowMouse == False:
                boatFollowMouse = True

    if physics_mode == 0:
        loadCount = 0
        screen.fill((screenColor))
        screen.blit(whiteBoard, whiteBoard_rect)
        screen.blit(physics_solver_text, physics_solver_text_rect)
        screen.blit(settings_button,settings_button_rect)
        screen.blit(physics1_button, physics1_button_rect)
    elif physics_mode == 5:
        screen.blit(settings_button, settings_button_rect)
        redCirclOutline = pygame.draw.circle(screen, ("Red"), (redCircleOutlineCoordinates), 30, 3)
        whiteCircleOutline = pygame.draw.circle(screen, ("White"), (whiteCircleOutlineCoordinates), 30, 3)
        screen.blit(pencil, pencil_rect)
        screen.blit(eraser, eraser_rect)
        x1, y1, z1 = pygame.mouse.get_pressed(num_buttons=3)
        x, y = pygame.mouse.get_pos()
        if loadCount == 0:
            screen.fill("White")
            screen.blit(whiteBoardBoard, whiteBoardBoard_rect)
            screen.blit(back_arrow, back_arrow_rect)
            screen.blit(pencil, pencil_rect)
            screen.blit(eraser, eraser_rect)
            loadCount += 1
        elif x1 and wait_for_arrow == False and x>20 and x<770 and y >60 and y < 550 and pencilEraser == 1:
            pygame.draw.rect(screen, "Black", (x,y, 10, 10))
        elif x1 and wait_for_arrow == False and x>20 and x<740 and y >68 and y < 490 and pencilEraser == 2:
            pygame.draw.rect(screen, "White", (x, y, 50, 50))

    elif physics_mode == 4:
        loadCount = 0
        screen.fill((screenColor))
        screen.blit(settings_button, settings_button_rect)
        screen.blit(whiteBoard, whiteBoard_rect)
        screen.blit(screenColorText,screenColorText_rect)
        screen.blit(changeMusicText,changeMusicText_rect)
        screen.blit(back_arrow,back_arrow_rect)
        screen.blit(musicIcon1,musicIcon1Rect)
        screen.blit(musicIcon2, musicIcon2Rect)
        screen.blit(musicIcon3, musicIcon3Rect)
        screen.blit(musicIcon4, musicIcon4Rect)
        screen.blit(musicIcon5, musicIcon5Rect)
        screenColorPurple_rect = pygame.draw.rect(screen, "Purple", (250, 185, 40, 40))
        screenColorGrey_rect = pygame.draw.rect(screen, "Grey", (300, 185, 40, 40))
        screenColorOrange_rect = pygame.draw.rect(screen, "#601E51", (350, 185, 40, 40))
        screenColorLightPurp_rect = pygame.draw.rect(screen, "#CBC3E3", (400, 185, 40, 40))
        screenColorBlue_rect = pygame.draw.rect(screen, "#601EAE", (450, 185, 40, 40))
        screenColorGreen_rect = pygame.draw.rect(screen, "#7C587D", (500, 185, 40, 40))
        redOutlineBox = pygame.draw.rect(screen,"Red", (redOutlineBoxCoordinate,185,40,40),2)
        redOutlineBox2 = pygame.draw.rect(screen, "Red", (redOutlineBox2Coordinate, 283, 53, 49), 2)

    elif physics_mode == 1:
        loadCount = 0
        screen.fill(screenColor)
        screen.blit(whiteBoard, whiteBoard_rect)
        screen.blit(settings_button, settings_button_rect)
        screen.blit(back_arrow,back_arrow_rect)
        screen.blit(physics1_boatProblem,physics1_boatProblem_rect)
        screen.blit(physics1_pulleyProblem,physics1_pulleyProblem_rect)
    elif physics_mode == 2:
        loadCount = 0
        screen.fill(screenColor)
        screen.blit(whiteBoard, whiteBoard_rect)
        screen.blit(settings_button, settings_button_rect)
        screen.blit(back_arrow, back_arrow_rect)
        screen.blit(physics1_boatProblem_velocity_text, physics1_boatProblem_velocity_rect)
        river = pygame.draw.rect(screen, ("#ADD8E6"), pygame.Rect(0,400,800,300))
        screen.blit(physics1_boatProblem_angle_text, physics1_boatProblem_angle_rect)

        #playbutton


        #screen blits
        screen.blit(physics1_boatProblem_velocity_text, physics1_boatProblem_velocity_rect)
        screen.blit(physics1_boatProblem_angle_text, physics1_boatProblem_angle_rect)
        screen.blit(physics1_boatProblem_boatWidth_text, physics1_boatProblem_boatWidth_rect)
        screen.blit(physics1_boatProblem_riverCurrent_text, physics1_boatProblem_riverCurrent_rect)
        screen.blit(physics1_boatProblem_velocityMagnitude_text, physics1_boatProblem_velocityMagnitude_rect)
        screen.blit(physics1_boatProblem_boatTime_text, physics1_boatProblem_boatTime_rect)
        screen.blit(physics1_boatProblem_distanceTravelled_text, physics1_boatProblem_distanceTravelled_rect)
        screen.blit(physics1_boatProblem_decimals_text, physics1_boatProblem_decimals_rect)

        #boat Mouse thing
        if boatFollowMouse == True:
            boatImage_rect.center = pygame.mouse.get_pos()
        if boatImage_rect.y < river.y -75:
          boatImage_rect.y = river.y -75
        if boatImage_rect.y > river.y+200:
          boatImage_rect.y = river.y+200
        #velocity text box
        physics1_boatProblem_velocity_textBox = boatProblem_velocity_font.render(velocityNumber, False, ("Black"))
        #angle text box
        physics1_boatProblem_angle_textBox = boatProblem_velocity_font.render(angleNumber, False, ("Black"))
        #river width box
        physics1_boatProblem_boatWidth_textBox = boatProblem_velocity_font.render(boatWidthNumber, False, ("Black"))
        #river current box
        physics1_boatProblem_riverCurrent_textBox = boatProblem_velocity_font.render(riverCurrentNumber, False, ("Black"))
        #velocity magnitude
        physics1_boatProblem_velocityMagnitude_textBox = boatProblem_velocity_font.render(velocityMagnitudeNumber, False, ("Black"))
        #boat time
        physics1_boatProblem_boatTime_textBox = boatProblem_velocity_font.render(boatTimeNumber, False, ("Black"))
        #distance travelled
        physics1_boatProblem_distanceTravelled_textBox = boatProblem_velocity_font.render(distanceTravelledNumber, False, ("Black"))

        physics1_boatProblem_decimals_textBox = boatProblem_decimals_font.render("Off", False, ("Black"))
        physics1_boatProblem_decimals_rectBox = physics1_boatProblem_velocity_textBox.get_rect(
            topleft=(physics1_boatProblem_velocity_x + 4, physics1_boatProblem_velocity_y - decimalsOffset))

        physics1_boatProblem_decimals_text = boatProblem_velocity_font.render("Decimals:", False, ("Black"))
        physics1_boatProblem_decimals_rect = physics1_boatProblem_velocity_textBox.get_rect(
            topleft=(physics1_boatProblem_velocity_x - 75, physics1_boatProblem_velocity_y - decimalsOffset + 10))
        boatProblemdecimals_button = make_button(physics1_boatProblem_decimals_textBox,
                                                 physics1_boatProblem_decimals_rectBox, "Red",
                                                 physics1_boatProblem_velocity_x,
                                                 physics1_boatProblem_y - decimalsOffset, decimalsTextLength, 40, 0)

        #decimals
        if decimals == False:
            physics1_boatProblem_decimals_textBox = boatProblem_decimals_font.render("Off", False, ("Black"))
        elif decimals == True:
            physics1_boatProblem_decimals_textBox = boatProblem_decimals_font.render("On", False, ("Black"))




        if velocityNumber and boatWidthNumber and riverCurrentNumber and decimals == False:
            screen.blit(playButton, playButton_rect)
            velocityMagnitudeNumber = str(int(math.sqrt(math.pow(int(velocityNumber),2) + math.pow(int(riverCurrentNumber),2))))
            boatTimeNumber = str(int(int(boatWidthNumber)/int(velocityNumber)))
            distanceTravelledNumber = str(int((int(boatWidthNumber)/int(velocityNumber)) * int(riverCurrentNumber)))
            if (int(riverCurrentNumber) / int(velocityNumber)) > 1:
                angleNumber = "NaN"
                angleTextLength = 40
            else:
                angleNumber = str(int(numpy.arcsin((int(riverCurrentNumber) / int(velocityNumber))) * 180 / math.pi))
                angleTextLength = getTextLength(angleNumber)

            velocityMagnitudeTextLength = getTextLength(velocityMagnitudeNumber)
            boatTimeTextLength = getTextLength(boatTimeNumber)
            distanceTravelledTextLength = getTextLength(distanceTravelledNumber)

        if velocityNumber and boatWidthNumber and riverCurrentNumber and decimals == True:
            screen.blit(playButton, playButton_rect)
            velocityMagnitudeNumber = str(math.sqrt(math.pow(int(velocityNumber), 2) + math.pow(int(riverCurrentNumber), 2)))
            boatTimeNumber = str(int(boatWidthNumber) / int(velocityNumber))
            distanceTravelledNumber = str((int(boatWidthNumber) / int(velocityNumber)) * int(riverCurrentNumber))
            if (int(riverCurrentNumber) / int(velocityNumber)) > 1:
                angleNumber = "NaN"
                angleTextLength = 40

            else:
                angleNumber = str(numpy.arcsin((int(riverCurrentNumber) / int(velocityNumber))) * 180 / math.pi)
                angleTextLength = getTextLength(angleNumber)

            velocityMagnitudeTextLength = getTextLength(velocityMagnitudeNumber)
            boatTimeTextLength = getTextLength(boatTimeNumber)
            distanceTravelledTextLength = getTextLength(distanceTravelledNumber)



        #ANIMATION
        if runAnimation == True:

            screen.blit(stopButton, stopButton_rect)

            if clockTick == 0:
                pygame.mixer.Sound.play(water_sound)
                start_time = pygame.time.get_ticks()
                real_start_time = pygame.time.get_ticks()
                clockTick += 1
            if start_time <= real_start_time + 1000 * int(int(boatWidthNumber) / int(velocityNumber)):
                print("hello")
                timeElapsed = str(int((pygame.time.get_ticks() - real_start_time) / 1000))
                start_time += playBoatAnimation((int(boatWidthNumber) / int(velocityNumber)) * int(riverCurrentNumber),int(int(boatWidthNumber) / int(velocityNumber)), start_time)
            else:
                start_time = pygame.time.get_ticks()
                real_start_time = pygame.time.get_ticks()
                clockTick = 0
                runAnimation = False
            # Time Elapsed:
            physics1_boatProblem_timeElapsed_textBox = boatProblem_decimals_font.render("Time Elapsed: " + timeElapsed + " seconds", False, ("Black"))
            boatProblemtimeElapsed_button = make_button(physics1_boatProblem_timeElapsed_textBox,physics1_boatProblem_timeElapsed_rectBox, "White",physics1_boatProblem_velocity_x+4000,physics1_boatProblem_y - timeElapsedOffset,timeElapsedTextLength, 40, 0)

        #making buttons
        boatProblemVelocity_button = make_button(physics1_boatProblem_velocity_textBox, physics1_boatProblem_velocity_rectBox, "#FFFFFF", physics1_boatProblem_velocity_x, physics1_boatProblem_y, velocityTextLength,20, 0)
        boatProblemAngle_button = make_button(physics1_boatProblem_angle_textBox,physics1_boatProblem_angle_rectBox, "#A9A9A9",physics1_boatProblem_velocity_x, physics1_boatProblem_y-angleOffset,angleTextLength, 20, 0)
        boatProblemboatWidth_button = make_button(physics1_boatProblem_boatWidth_textBox, physics1_boatProblem_boatWidth_rectBox,"#FFFFFF", physics1_boatProblem_velocity_x, physics1_boatProblem_y-boatOffset,boatWidthTextLength, 20, 0)
        boatProblemriverCurrent_button = make_button(physics1_boatProblem_riverCurrent_textBox,physics1_boatProblem_riverCurrent_rectBox, "#FFFFFF",physics1_boatProblem_velocity_x, physics1_boatProblem_y - riverOffset,riverCurrentTextLength, 20, 0)
        boatProblemvelocityMagnitude_button = make_button(physics1_boatProblem_velocityMagnitude_textBox,physics1_boatProblem_velocityMagnitude_rectBox, "#A9A9A9",physics1_boatProblem_velocity_x,physics1_boatProblem_y - velocityMagnitudeOffset,velocityMagnitudeTextLength, 20,0)
        boatProblemboatTime_button = make_button(physics1_boatProblem_boatTime_textBox,physics1_boatProblem_boatTime_rectBox, "#A9A9A9",physics1_boatProblem_velocity_x,physics1_boatProblem_y - boatTimeOffset,boatTimeTextLength, 20, 0)
        boatProblemdistanceTravelled_button = make_button(physics1_boatProblem_distanceTravelled_textBox,physics1_boatProblem_distanceTravelled_rectBox, "#A9A9A9",physics1_boatProblem_velocity_x,physics1_boatProblem_y - distanceTravelledOffset, distanceTravelledTextLength, 20, 0)
        if decimals == False:
            boatProblemdecimals_button = make_button(physics1_boatProblem_decimals_textBox,physics1_boatProblem_decimals_rectBox, "Red",physics1_boatProblem_velocity_x,physics1_boatProblem_y - decimalsOffset, decimalsTextLength, 40, 0)
        elif decimals == True:
            boatProblemdecimals_button = make_button(physics1_boatProblem_decimals_textBox,physics1_boatProblem_decimals_rectBox, "Green",physics1_boatProblem_velocity_x,physics1_boatProblem_y - decimalsOffset, decimalsTextLength, 40, 0)
        if runAnimation:
            if boatFrameCount < 20 :
                boatImage = boatFrame2
                boatFrameCount += 1
            elif boatFrameCount >= 20 and boatFrameCount <= 40:
                boatImage = boatFrame1
                boatFrameCount += 1
            else:
                boatFrameCount = 0

        screen.blit(boatImage, boatImage_rect)
        #create a button focus that allows user to type in 1234567890 or . or x or - if you press enter you end the button focus
        #variables used in boat problem: angle of boat, speed of boat, speed of river, downstream distance, length of river, time it takes for boat to cross river, magnitude of the distance it moves
        #dont let boat get past river
        #move button to bottom right
        #move time elapsed under river
    elif physics_mode == 3:
        #making pulley

        screen.fill(screenColor)
        screen.blit(settings_button, settings_button_rect)
        screen.blit(whiteBoard, whiteBoard_rect)
        screen.blit(back_arrow, back_arrow_rect)
        screen.blit(physics1_pulleyProblem_acceleration_textBox, physics1_boatProblem_acceleration_rectBox)
        screen.blit(physics1_pulleyProblem_acceleration_text, physics1_pulleyProblem_acceleration_rect)
        screen.blit(physics1_boatProblem_decimals_text, physics1_boatProblem_decimals_rect)

        screen.blit(physics1_pulleyProblem_tension_textBox, physics1_boatProblem_tension_rectBox)
        screen.blit(physics1_pulleyProblem_tension_text, physics1_pulleyProblem_tension_rect)

        if mass2IntNumber != 0 and mass1IntNumber != 0 and decimals == True:
            if mass2IntNumber > mass1IntNumber:
                accelerationNumber = str(((mass2IntNumber - mass1IntNumber) * 10) / (mass2IntNumber + mass1IntNumber))
                accelerationTextLength = getTextLength(accelerationNumber)
                tensionNumber = str((mass2IntNumber*10) - (mass2IntNumber*(((mass2IntNumber - mass1IntNumber) * 10) / (mass2IntNumber + mass1IntNumber))))
                tensionTextLength = getTextLength(tensionNumber)
            if mass1IntNumber > mass2IntNumber:
                accelerationNumber = str(((mass1IntNumber - mass2IntNumber) * 10) / (mass2IntNumber + mass1IntNumber))
                accelerationTextLength = getTextLength(accelerationNumber)
                tensionNumber = str((mass1IntNumber*10) - (mass1IntNumber*(((mass1IntNumber - mass2IntNumber) * 10) / (mass2IntNumber + mass1IntNumber))))
                tensionTextLength = getTextLength(tensionNumber)
            if mass1IntNumber == mass2IntNumber:
                accelerationNumber = "0"
                accelerationTextLength = getTextLength(accelerationNumber)
                tensionNumber = "yo mama"
                tensionTextLength = getTextLength(tensionNumber)
        if mass2IntNumber != 0 and mass1IntNumber != 0 and decimals == False:
            if mass2IntNumber > mass1IntNumber:
                accelerationNumber = str(int(((mass2IntNumber - mass1IntNumber) * 10) / (mass2IntNumber + mass1IntNumber)))
                accelerationTextLength = getTextLength(accelerationNumber)
                tensionNumber = str(int((mass2IntNumber*10) - (mass2IntNumber*(((mass2IntNumber - mass1IntNumber) * 10) / (mass2IntNumber + mass1IntNumber)))))
                tensionTextLength = getTextLength(tensionNumber)
            if mass1IntNumber > mass2IntNumber:
                accelerationNumber = str(int(((mass1IntNumber - mass2IntNumber) * 10) / (mass2IntNumber + mass1IntNumber)))
                accelerationTextLength = getTextLength(accelerationNumber)
                tensionNumber = str(int((mass1IntNumber*10) - (mass1IntNumber*(((mass1IntNumber - mass2IntNumber) * 10) / (mass2IntNumber + mass1IntNumber)))))
                tensionTextLength = getTextLength(tensionNumber)
            if mass1IntNumber == mass2IntNumber:
                accelerationNumber = "0"
                accelerationTextLength = getTextLength(accelerationNumber)
                tensionNumber = "yo mama"
                tensionTextLength = getTextLength(tensionNumber)

        physics1_pulleyProblem_acceleration_textBox = boatProblem_velocity_font.render(accelerationNumber, False,("Black"))
        physics1_boatProblem_acceleration_rectBox = physics1_pulleyProblem_acceleration_textBox.get_rect(center=(655 + (accelerationTextLength/2), 100))
        pulleyProblemacceleration_button = make_button(physics1_pulleyProblem_acceleration_textBox,physics1_boatProblem_acceleration_rectBox, "#A9A9A9", 652, 93,accelerationTextLength, 20, 0)


        physics1_pulleyProblem_tension_textBox = boatProblem_velocity_font.render(tensionNumber, False,("Black"))
        physics1_boatProblem_tension_rectBox = physics1_pulleyProblem_tension_textBox.get_rect(center=(655 + (accelerationTextLength/2), 150))
        pulleyProblemtension_button = make_button(physics1_pulleyProblem_tension_textBox,physics1_boatProblem_tension_rectBox, "#A9A9A9", 652, 143,tensionTextLength, 20, 0)

        pulleyCircle = pygame.draw.circle(screen, (0,0,0), (400,200), 50)
        pulleyLine1 = pygame.draw.line(screen, "Black", (348, 200), Line1Set, 4)
        pulleyLine2 = pygame.draw.line(screen, "Black", (450, 200), Line2Set, 4)
        if pulleyRuncount == 0:
            pulleySquare1Rect = pygame.Rect(0, 0, 50, 50)
            pulleySquare1Rect.center = (348, 425)
            pulleySquare2Rect = pygame.Rect(0, 0, 50, 50)
            pulleySquare2Rect.center = (450, 425)
        if mass2IntNumber > mass1IntNumber and mass2IntNumber != 0 and mass1IntNumber != 0 and pulleyRuncount == 0 and runPulleyAnimation == True:
            print("hi")
            pulleyLine2 = pygame.draw.line(screen, "Black", (450, 200), (450, 400 + pulleyGravity), 4)
            pulleySquare2Rect.center = (450, 425+pulleyGravity)
            pulleyLine1 = pygame.draw.line(screen, "Black", (348,200),(348,400 - pulleyGravity),4)
            mass2y = 415 + pulleyGravity
            physics1_pulleyProblem_mass2_rectBox = physics1_pulleyProblem_mass2_textBox.get_rect(topleft=(mass2x, mass2y))
            pulleySquare1Rect.center = (348, 425-pulleyGravity)
            mass1y = 415 - pulleyGravity
            physics1_pulleyProblem_mass1_rectBox = physics1_pulleyProblem_mass1_textBox.get_rect(topleft=(mass1x, mass1y))

            Line1Set = (348,400 - pulleyGravity)
            Line2Set = (450, 400 + pulleyGravity)
        elif mass2IntNumber < mass1IntNumber and mass2IntNumber != 0 and mass1IntNumber != 0 and pulleyRuncount == 0 and runPulleyAnimation == True:
            pulleyLine2 = pygame.draw.line(screen, "Black", (450, 200), (450, 400 - pulleyGravity), 4)
            pulleySquare2Rect.center = (450, 425 - pulleyGravity)
            pulleyLine1 = pygame.draw.line(screen, "Black", (348, 200), (348, 400 + pulleyGravity), 4)
            mass2y = 415 - pulleyGravity
            physics1_pulleyProblem_mass2_rectBox = physics1_pulleyProblem_mass2_textBox.get_rect(
                topleft=(mass2x, mass2y))
            pulleySquare1Rect.center = (348, 425 + pulleyGravity)
            mass1y = 415 + pulleyGravity
            physics1_pulleyProblem_mass1_rectBox = physics1_pulleyProblem_mass1_textBox.get_rect(
                topleft=(mass1x, mass1y))
            Line1Set = (348, 400 + pulleyGravity)
            Line2Set = (450, 400 - pulleyGravity)
        elif mass2IntNumber > mass1IntNumber and mass2IntNumber != 0 and mass1IntNumber != 0 and pulleyRuncount == 1 and runPulleyAnimation == True:
            pulleyDoubleGravity = pulleyGravity*2
            print(pulleyDoubleGravity)
            pulleyLine2 = pygame.draw.line(screen, "Black", (450, 200), (450, 350 + pulleyDoubleGravity), 4)
            pulleySquare2Rect.center = (450, 375+pulleyDoubleGravity)
            pulleyLine1 = pygame.draw.line(screen, "Black", (348,200),(348,450 - pulleyDoubleGravity),4)
            mass2y = 365 + pulleyDoubleGravity
            physics1_pulleyProblem_mass2_rectBox = physics1_pulleyProblem_mass2_textBox.get_rect(topleft=(mass2x, mass2y))
            pulleySquare1Rect.center = (348, 475-pulleyDoubleGravity)
            mass1y = 465 - pulleyDoubleGravity
            physics1_pulleyProblem_mass1_rectBox = physics1_pulleyProblem_mass1_textBox.get_rect(topleft=(mass1x, mass1y))

            Line1Set = (348,450 - pulleyDoubleGravity)
            Line2Set = (450, 350 + pulleyDoubleGravity)
        elif mass2IntNumber < mass1IntNumber and mass2IntNumber != 0 and mass1IntNumber != 0 and pulleyRuncount == 1 and runPulleyAnimation == True:
            pulleyDoubleGravity = pulleyGravity*2
            pulleyLine2 = pygame.draw.line(screen, "Black", (450, 200), (450, 450 - pulleyDoubleGravity), 4)
            pulleySquare2Rect.center = (450, 475-pulleyDoubleGravity)
            pulleyLine1 = pygame.draw.line(screen, "Black", (348,200),(348,350 + pulleyDoubleGravity),4)
            mass2y = 465 - pulleyDoubleGravity
            physics1_pulleyProblem_mass2_rectBox = physics1_pulleyProblem_mass2_textBox.get_rect(topleft=(mass2x, mass2y))
            pulleySquare1Rect.center = (348, 375+pulleyDoubleGravity)
            mass1y = 365 + pulleyDoubleGravity
            physics1_pulleyProblem_mass1_rectBox = physics1_pulleyProblem_mass1_textBox.get_rect(topleft=(mass1x, mass1y))

            Line1Set = (348,350 + pulleyDoubleGravity)
            Line2Set = (450, 450 - pulleyDoubleGravity)
        if mass2IntNumber == mass1IntNumber:
            Line1Set = (348, 400)
            Line2Set = (450, 400)
            pulleySquare1Rect.center = (348, 425)
            pulleySquare2Rect.center = (450, 425)
            mass2y = 415
            mass1y = 415
            physics1_pulleyProblem_mass2_rectBox = physics1_pulleyProblem_mass2_textBox.get_rect(topleft=(mass2x, mass2y))
            physics1_pulleyProblem_mass1_rectBox = physics1_pulleyProblem_mass1_textBox.get_rect(topleft=(mass1x, mass1y))
        if runPulleyAnimation == True and pulleyGravity < 50:
            pulleyGravity += .1
        elif pulleyGravity >= 50:
            pulleyRuncount = 1
            pulleyGravity = 0
            runPulleyAnimation = False
        if showButtons[0] == True and showButtons[1] == True:
            if runPulleyAnimation == False:
                screen.blit(playButton, playButton_rect)

            if runPulleyAnimation == True:
                screen.blit(stopButton,stopButton_rect)
        physics1_boatProblem_decimals_textBox = boatProblem_decimals_font.render("", False, ("Black"))
        physics1_boatProblem_decimals_rectBox = physics1_boatProblem_velocity_textBox.get_rect(topleft=(650, 200))

        physics1_boatProblem_decimals_text = boatProblem_velocity_font.render("Decimals:", False, ("Black"))
        physics1_boatProblem_decimals_rect = physics1_boatProblem_velocity_textBox.get_rect(topleft=(550, 210))
        boatProblemdecimals_button = make_button(physics1_boatProblem_decimals_textBox,physics1_boatProblem_decimals_rectBox, "Red",650,200, decimalsTextLength, 40, 0)

        if decimals == False:
            physics1_boatProblem_decimals_textBox = boatProblem_decimals_font.render("Off", False, ("Black"))
            boatProblemdecimals_button = make_button(physics1_boatProblem_decimals_textBox,physics1_boatProblem_decimals_rectBox, "Red",650,200, decimalsTextLength, 40, 0)
        elif decimals == True:
            physics1_boatProblem_decimals_textBox = boatProblem_decimals_font.render("On", False, ("Black"))
            boatProblemdecimals_button = make_button(physics1_boatProblem_decimals_textBox,physics1_boatProblem_decimals_rectBox, "Green",650,200, decimalsTextLength, 40, 0)
        pulleySquare1 = pygame.draw.rect(screen, "Orange", pulleySquare1Rect)
        pulleySquare2 = pygame.draw.rect(screen, "Orange", pulleySquare2Rect)

        physics1_pulleyProblem_mass1_textBox = boatProblem_velocity_font.render(mass1Number,False, ("Black"))
        pulleyProblemmass1_button = make_button(physics1_pulleyProblem_mass1_textBox,physics1_pulleyProblem_mass1_rectBox, "#FFFFFF",mass1x, mass1y, mass1TextLength, 20,0)

        physics1_pulleyProblem_mass2_textBox = boatProblem_velocity_font.render(mass2Number, False, ("Black"))
        pulleyProblemmass2_button = make_button(physics1_pulleyProblem_mass2_textBox,
                                                physics1_pulleyProblem_mass2_rectBox, "#FFFFFF", mass2x, mass2y,
                                                mass2TextLength, 20, 0)

    pygame.display.update()
    clock.tick(60)





#Whiteboard
#Points system
#Talk to mr hwang or mr swanson