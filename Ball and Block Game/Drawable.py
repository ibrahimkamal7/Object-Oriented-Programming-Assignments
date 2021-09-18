#Ibrahim Kamal
#ik363
#Drawable class(abstract)

#Modules required for creating abstract classes and methods
from abc import ABCMeta , abstractmethod

class Drawable(metaclass=ABCMeta):
    location = [0,0] #loation list
    def __init__(self , visibility):
        self.visibility = visibility #visibility bolean

    #Abstract methods
    @abstractmethod
    def draw(self , surface):
        pass

    @abstractmethod
    def get_rect(self):
        pass
