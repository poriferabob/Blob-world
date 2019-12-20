import random

class Blob:

    def __init__(self, colour, x_boundary, y_boundary, size):
        self.colour = colour
        self.size = size
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)

    def move(self):

        self.move_x = random.randrange(-6,7)
        self.move_y = random.randrange(-6,7)

        self.x += self.move_x
        self.y += self.move_y

    def limits(self):
        if self.x < 0:
            self.x = 0
        elif self.x > self.x_boundary:
            self.x = self.x_boundary

        if self.y < 0:
            self.y = 0
        elif self.y > self.y_boundary:
            self.y = self.y_boundary

    def __add__(self, other_blob):
        if other_blob.size > self.size:
                other_blob.size += self.size
                self.size = 0
