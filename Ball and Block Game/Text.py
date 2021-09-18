#Ibrahim Kamal
#ik363
#Text Class to draw the text areas and display the score and the winning text

from Drawable import Drawable
import pygame

class Text(Drawable):
    def __init__(self , location , color , visibility , text=""):
        super().__init__(visibility) #visibility boolean of ball
        self.location = location #position of text
        self.text = text #text to be displayed
        self.color = color #color of text
        self.font = pygame.font.SysFont("Arial", 25) #setting font size and font
        self.rect = pygame.Rect(self.location,self.font.size(self.text))
        
    def draw(self, surface):
        #displaying text if visibility boolean is true
        if self.visibility:
            render = self.font.render(self.text , True , self.color)
            surface.blit(render , self.location)

    def get_rect(self):
        #return rect for the text
        return self.rect
