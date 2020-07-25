#Ibrahim Kamal
#ik363
#Block Class to draw the blocks

from Drawable import Drawable 
import pygame

class Block(Drawable):
    size = [20 , 20]
    def __init__(self , location , visibility):
        super().__init__(visibility)#visibility boolean of block
        self.location = location #position of block
        self.color = (0,0,255)#color of block
        self.rect = pygame.Rect(self.location, self.size)
        
    def draw(self, surface):
        #draw block if visibility boolean is true
        if self.visibility:
            pygame.draw.rect(surface , self.color , self.rect)#drawing the block
            pygame.draw.rect(surface , (0,0,0) , self.rect , 1)#drawing outline of block

    def get_rect(self):
        return self.rect #return the rect for the block
