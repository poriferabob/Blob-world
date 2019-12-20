import pygame
import random
from Class_Blob import Blob
from Class_FastBlob import FastBlob
import numpy as np

WIDTH = 1000
HEIGHT = 600
WHITE = (255,255,255)
BLUE = (0,0,180)
RED = (180,0,0)

pygame.init()
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blob world')
clock = pygame.time.Clock()

def is_touching(b1,b2):
    return np.linalg.norm(np.array([b1.x,b1.y])-np.array([b2.x,b2.y])) < (b1.size + b2.size)

def handle_collisions(blob_list):
    blues, reds, slow_reds = blob_list
    for first_blobs in blues, reds, slow_reds:
        for first_blob_id, first_blob in first_blobs.copy().items():
            for other_blobs in blues, reds, slow_reds:
                for other_blob_id, other_blob in other_blobs.copy().items():
                    if first_blob == other_blob:
                        pass
                    else:
                        if is_touching(first_blob, other_blob):
                            first_blob + other_blob
                            if other_blob.size <= 0:
                                del other_blobs[other_blob_id]
                            if first_blob.size <= 0:
                                del first_blobs[first_blob_id]
    return blues, reds, slow_reds

def draw_environment(blob_list):
    game_display.fill((0,0,0))
    blues, reds, slow_reds = handle_collisions(blob_list)
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.colour, [blob.x, blob.y], blob.size)
            blob.move()
            blob.limits()
    pygame.display.update()
    return blues, reds, slow_reds

def main():
    blue_blobs = dict(enumerate([FastBlob(BLUE, WIDTH, HEIGHT, random.randrange(10,20)) for i in range(15)]))
    red_blobs = dict(enumerate([FastBlob(RED, WIDTH, HEIGHT, random.randrange(10,20)) for i in range(3)]))
    slow_red_blobs = dict(enumerate([Blob(RED, WIDTH, HEIGHT, random.randrange(40,50)) for i in range(3)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        blue_blobs, red_blobs, slow_red_blobs = draw_environment([blue_blobs, red_blobs, slow_red_blobs])
        clock.tick(7)

if __name__ == '__main__':
    main()
