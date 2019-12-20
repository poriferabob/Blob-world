import random
from Class_Blob import Blob

class FastBlob(Blob):

    def __init__(self, colour, x_boundary, y_boundary, size):
        
        Blob.__init__(self, colour, x_boundary, y_boundary, size)

    def move(self):
        self.x += random.randrange(-20,21)
        self.y += random.randrange(-20,21)
