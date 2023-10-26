import pygame
import sys
import math
import subprocess
import random
import time
pygame.init()

# Konstante verdier
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900
PLAYER_SPEED = 3
BULLET_SPEED = 10
PLAYER_COLOR = (5, 255, 5)
PLAYER2_COLOR = (5, 5, 255)
BULLET_COLOR = (255, 255, 255)
pygame.mouse.set_visible(False)

# Klokke
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

#Spiller
class Player:

    # Definerer Player posisjon og størrelse
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # Lager bevegelse
    def move(self, keys):
        if keys[pygame.K_d]:
            self.x += PLAYER_SPEED
        if keys[pygame.K_a]:
            self.x -= PLAYER_SPEED
        if keys[pygame.K_s]:
            self.y += PLAYER_SPEED
        if keys[pygame.K_w]:
            self.y -= PLAYER_SPEED

    # Tegner en firkant som er lik player med størrelse og posisjon
    def draw(self, display):
        pygame.draw.rect(display, PLAYER_COLOR, (self.x, self.y, self.width, self.height))

#  Spiller 2
class Player2:

    # Definerer Player posisjon og størrelse
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # Lager bevegelse
    def move(self, keys):
        if keys[pygame.K_RIGHT]:
            self.x += PLAYER_SPEED
        if keys[pygame.K_LEFT]:
            self.x -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.y += PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.y -= PLAYER_SPEED

    # Tegner en firkant som er lik player med størrelse og posisjon
    def draw(self, display):
        pygame.draw.rect(display, PLAYER2_COLOR, (self.x, self.y, self.width, self.height))


# Lager en PlayerBullet class
class PlayerBullet:

    # lager hoved funksjonen som bestemmer alt
    def __init__(self, x, y, mouse_x, mouse_y):

        # X og Y posisjoner
        self.x = x
        self.y = y

        self.angle = random.uniform(0, 2 * math.pi)

        # Calculate velocity based on the random angle
        self.speed = BULLET_SPEED
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

    def move(self):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

    def draw(self, display):
        pygame.draw.circle(display, BULLET_COLOR, (self.x, self.y), 5)




# Lager mainloopen i gamet som alltid er aktiv
def main():

    # Gjør Player class til player i main loopen så du kan kalle på den her
    player = Player(400, 300, 32, 32)
    player2 = Player2(400, 330, 32, 32)

    # Lager en liste som bullets posisjonene og annen info blir lagret
    player_bullets = []

    last_shot_time = 0

    initial_player1_x, initial_player1_y = 400, 300
    initial_player2_x, initial_player2_y = 400, 330

    # Lager mainloopen som lager skjermen
    while True:
        display.fill((0, 0, 0))

        # Finner museposisjonen og leter etter key pressed
        mouse_x, mouse_y = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        # Lar deg lukke gamet
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Sjekker tiden, om det har gått ett sekund skyter den
        current_time = pygame.time.get_ticks()
        if current_time - last_shot_time >= 1000:  # 1000 milliseconds = 1 second
            player_bullets.append(PlayerBullet(player.x, player.y, mouse_x, mouse_y))
            last_shot_time = current_time
            player_bullets.append(PlayerBullet(player2.x, player2.y, mouse_x, mouse_y))


        # Calculate the distance between the players
        dx = player2.x - player.x
        dy = player2.y - player.y
        distance = math.sqrt(dx * dx + dy * dy)

        # Define a maximum distance threshold
        max_distance = 120
        rope_strength = 2
        # If the distance exceeds the threshold, move players closer together
        if distance > max_distance:
            rope_strength = distance * 2
            ratio = max_distance / distance
            player2.x -= (dx * ratio)*(rope_strength / max_distance)/55
            player2.y -= (dy * ratio)*(rope_strength / max_distance)/55

        # Ensure that players stay within the screen boundaries
        player.x = max(0, min(player.x, SCREEN_WIDTH - player.width))
        player.y = max(0, min(player.y, SCREEN_HEIGHT - player.height))
        player2.x = max(0, min(player2.x, SCREEN_WIDTH - player2.width))
        player2.y = max(0, min(player2.y, SCREEN_HEIGHT - player2.height))

        # Oppdaterer posisjonen ettersom hvilke knapper er blitt trykket på
        player.move(keys)
        player.draw(display)

        player2.move(keys)
        player2.draw(display)

        # Tegner bullets på skjermen
        for bullet in player_bullets:
            bullet.move()
            bullet.draw(display)

        # Oppdaterer skjermen 60 ganger i sekundet
        clock.tick(60)
        pygame.display.update()

# Starter programmet ved å sjekke om dette programmet er hoved programmet og starter opp main funksjonen
if __name__ == "__main__":
    main()


