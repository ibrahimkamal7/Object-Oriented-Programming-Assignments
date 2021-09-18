#Ibrahim Kamal
#ik363
#Main Script to run the game

import pygame
from Drawable import Drawable
from Ball import Ball
from Block import Block
from Text import Text
import time

class Line(Drawable): #Line Class which will draw the ground plane
    color = 0,0,0 #color of line
    width = 1 #width of line

    def __init__(self , startPosition , endPosition , visibility):
        
        super().__init__(visibility) #boolean for line visibility 
        self.startPosition = startPosition #starting point of line
        self.endPosition = endPosition #ending point of line
        #Calculating the rectangle of the line
        #pygame.Rect(x, y, width, height)
        self.rect = pygame.Rect(*self.location ,
                                self.endPosition[0] - self.startPosition[0] ,
                                self.endPosition[1] - self.endPosition[0])

    def draw(self , surface):
        #draw the line if visibibility boolean is true
        if self.visibility:
            self.rect = pygame.draw.line(surface , self.color , self.startPosition , self.endPosition , self.width)

    def get_rect(self):
        return self.rect #return the line's rect


#returns True if the given two object collides
def intersect(rect1 , rect2):
    if (rect1.x < rect2.x + rect2.width
        and rect1.x + rect1.width > rect2 .x
        and rect1.y < rect2.y + rect2.height
        and rect1.height + rect1.y > rect2.y):
        return True
    return False

print("\nWelcome to the \"Blocks and Ball\" game.\nThe rules of the game are as follows:\n1. You have to drag the ball to hit the blocks.\n2. Everytime you hit a block, you will score 1 point.\n3. If the ball goes out of the window frame, it will return to its initial position.\n4. There is no chance limit. You can hit the blocks as many times as you want.\nEnjoy!!")
#Initializing the PyGame modules
pygame.init()

window = 500 , 500 #setting the window size
canvas = pygame.display.set_mode(window) #creating window
clock = pygame.time.Clock() #Clock module to keep 60fps during the game

#creating score, game completion text
displayScore = Text([0 , 0] , (0 , 0 , 0) , True , "Your Score: 0") #player score text
completeText = Text([80 , 200] , (0 , 0 , 0) , False , "Congratuations! You completed the game.") #game completion text

line = Line((0 , 400) , (500 ,400) , True) #creating a Line class object
ball = Ball([20 , 400] , (255 , 0 , 0) , 8 , True) #creating a Ball class object


blocks = [] #list to store Block objects

#creating 9 blocks with size 20
#starting x and y co-ordinates are 400 and 300 respectively
blocks = [Block([400 , 340] , True) , Block([420 , 340] , True) , Block([440 , 340] , True) , Block([400 , 360] , True), Block([420 , 360] , True) , Block([440 , 360] , True), Block([400 , 380] , True) , Block([420 , 380] , True), Block([440 , 380] , True)]

start = None #tuple to store cursor position when a player clicks
#Constants
dt = .1 #delta time constant
g = 6.67 #gravity constant
R = 0.7 #rebound constant
eta = 0.5 #friction constant

xv = 0 #to change the horizontal velocity of ball 
yv = 0 #to change the vertical velocity of ball

score = 0 #stores the score of the player

#Game loop
while True:
    
    canvas.fill((255 , 255 , 255))
    #drawing ground plane and the ball
    line.draw(canvas)
    ball.draw(canvas)
    
    MousePos = pygame.mouse.get_pos() #storing mouse position
    for event in pygame.event.get():

        #Quitting the game when the window closes
        if event.type == pygame.QUIT:
            False
            exit()
        #storing the position of mouse on mouse button down event
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start = MousePos
        #Mouse button up event
        #calculating the new velocity on mouse button up event after storing the mouse position
        elif event.type == pygame.MOUSEBUTTONUP:
            end = MousePos
            xv = end[0] - start[0] #changing horizontal velocity
            yv = start[1] - end[1] #changing vertical velocity
    
    #changing the vertical velocity keeping in the mind the effect of gravity when ball is above the ground            
    if ball.location[1] < line.startPosition[1]:
        yv = yv - g * dt
    
    #setting the new location of the ball
    ball.location[0] = ball.location[0] + dt * xv
    ball.location[1] = ball.location[1] - dt * yv
            
    #changing the horizontal and vertical velocities when the ball hits the ground
    if ball.location[1] >= line.startPosition[1] and yv < 0:
        yv = yv * (-1) * R
        xv = xv * eta
       
    #changing the ball position to initial position if the ball goes out of the screen
    if ball.location[0] > line.endPosition[0] or ball.location[0] < line.startPosition[0] or ball.location[1] < 0:
        ball.location[0] = 20
        ball.location[1] = 400
        xv = 0
        yv = 0
        
    #run function for every block in the blocks list
    i = 0
    while i < len(blocks):
        
       #checking whether ball collides with the block/s
        if blocks[i].visibility and intersect(blocks[i].get_rect(), ball.get_rect()):
            blocks[i].visibility = False #setting visibility to false if the ball and block collide
            score = score + 1 #increasing the score when ball hit the block
            displayScore.text = "Your Score: "+str(score) #resetting the score text
            if score == len(blocks):
                completeText.visibility = True
                ball.visibility = False
                line.visibility = False
                displayScore.location = (200 , 220)
        blocks[i].draw(canvas)
        i = i + 1
        
    displayScore.draw(canvas)
    completeText.draw(canvas)
    #updating the screen and delay to keep 60 frames per second
    pygame.display.update()
    clock.tick(60)

pygame.display.quit() #uninitializing the display module first for closing the window faster
pygame.quit() #ending pygame
