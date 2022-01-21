import pygame
from pygame import Color, draw, display, time

pygame.init()
clock = time.Clock()
gameDisplay = display.set_mode((600, 400))

#Print question
print('What colors do you want the circles to be? (name three in lowercase)')
#give inputed colors a variable
color1 = input()
color2 = input()
color3 = input()


#Ask how fast the person wants the code to go
print("How fast how you like your code to go?(the smaller the number the slower it goes)")
speed = int(input())

x = 50
y = 50


#Create infinte loop with other loops inside
while 0 == 0:
 for i in range(240):
    # Make white background
   gameDisplay.fill(Color('white'))

    # Draw a ball with chosen colors
   draw.circle(gameDisplay, Color(color1), (x, y), 30)

    # Show graphics on screen
   display.flip()
  
    # change location of center a little bit!!!
   x = x + 1
   y = y + 1

    # Control the refresh speed in frames per second
   clock.tick(speed)
  #Create loop 240 times
 for i in range(240):
    # Make white background   
    gameDisplay.fill(Color('white'))

    # Draw a ball with chosen colors
    draw.circle(gameDisplay, Color(color2), (x, y), 30)

    # Show graphics on screen
    display.flip()
  
    # change location of center a little bit!!!
    x = x + 1
    y = y - 1

    # Control the refresh speed in frames per second
    clock.tick(speed)
  #Create loop 480 times
 for i in range(480):
    # Make white background
    gameDisplay.fill(Color('white'))

    # Draw a ball with chosen colors
    draw.circle(gameDisplay, Color(color3), (x, y), 30)

    # Show graphics on screen
    display.flip()
  
    # change location of center a little bit!!!
    x = x - 1

    # Control the refresh speed in frames per second
    clock.tick(speed)