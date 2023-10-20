import pygame
import sys
import math
pygame.init()

# Konstante verdier
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 3
BULLET_SPEED = 10
PLAYER_COLOR = (255, 5, 5)
BULLET_COLOR = (255, 255, 255)

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

# Lager en PlayerBullet class
class PlayerBullet:

    # lager hoved funksjonen som bestemmer alt
    def __init__(self, x, y, mouse_x, mouse_y):

        # X og Y posisjoner
        self.x = x
        self.y = y

        # Bestemmer muse posisjonen
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y

        # Regner ut vinkelen mellom Player og musen
        self.angle = math.atan2(y - mouse_y, x - mouse_x)
        self.x_vel = math.cos(self.angle) * BULLET_SPEED
        self.y_vel = math.sin(self.angle) * BULLET_SPEED

    def move(self):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

    def draw(self, display):
        pygame.draw.circle(display, BULLET_COLOR, (self.x, self.y), 5)

# Lager mainloopen i gamet som alltid er aktiv
def main():

    # Gjør Player class til player i main loopen så du kan kalle på den her
    player = Player(400, 300, 32, 32)

    # Lager en liste som bullets posisjonene og annen info blir lagret
    player_bullets = []

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
            
            # Sjekker om du trykker ned venstre klikk og så appender enn bullet i listen
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player_bullets.append(PlayerBullet(player.x, player.y, mouse_x, mouse_y))

        # Oppdaterer posisjonen ettersom hvilke knapper er blitt trykket på
        player.move(keys)

        # Oppdaterer spriten etter posisjonen
        player.draw(display)

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
