
import pygame
import sys
import math
pygame.init()

display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def main(self, display):
        pygame.draw.rect(display, (255, 5, 5), (self.x, self.y, self.width, self.height))


class PlayerBullet:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y


player = Player(400, 300, 32, 32)

display_scroll = [0, 0]

while True:
    display.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT

    pygame.draw.rect(display, (255, 0, 0), (100-display_scroll[0], 100-display_scroll[1], 16, 16) )
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        display_scroll[0] -= 5
    
    if keys[pygame.K_a]:
        display_scroll[0] += 5

    if keys[pygame.K_s]:
        display_scroll[1] -= 5

    if keys[pygame.K_w]:
        display_scroll[1] += 5


    player.main(display)

