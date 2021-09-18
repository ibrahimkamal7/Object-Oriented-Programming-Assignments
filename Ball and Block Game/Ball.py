#Ibrahim Kamal
#ik363
#Ball class to draw the ball

from Drawable import Drawable
import pygame

class Ball(Drawable):
    def __init__(self , location , color , radius , visibility):
        super().__init__(visibility) #visibility boolean of ball
        self.location = location #location of ball
        self.color = color #color of ball
        self.radius = radius #radius of ball
        
    def draw(self , surface):
        #drawing ball ball if visibility boolean is true
        if self.visibility:
            pygame.draw.circle(surface , self.color , (round(self.location[0]) , round(self.location[1])) , self.radius)
            
    def get_rect(self):
        #returning rect for the ball
        self.rect = pygame.Rect(self.location[0]-self.radius , self.location[1]-self.radius , self.radius*2 , self.radius*2)
        return self.rect