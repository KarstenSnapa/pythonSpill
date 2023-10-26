import pygame
import sys
import subprocess
import os

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_COLOR = (0, 255, 0)
BUTTON_HOVER_COLOR = (0, 200, 0)
MENU_COLOR = (0, 0, 0)

# Finne filer for å kunne bla til andre filer
current_directory = os.path.dirname(__file__)

# Initialize the display
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Define button class
class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.hovered = False

    def draw(self, display):
        color = BUTTON_HOVER_COLOR if self.hovered else BUTTON_COLOR
        pygame.draw.rect(display, color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.rect.center)
        display.blit(text, text_rect)

# Lager knappene på skjermen
play_button = Button(300, 200, BUTTON_WIDTH, BUTTON_HEIGHT, "Play", "play")
exit_button = Button(300, 300, BUTTON_WIDTH, BUTTON_HEIGHT, "Exit", "exit")

buttons = [play_button, exit_button]

# Menu loop
while True:
    display.fill(MENU_COLOR)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button in buttons:
                if button.rect.collidepoint(mouse_x, mouse_y):
                    if button.action == "play":
                        print("Play button clicked")
                        # Add code for starting the game here
                        script_path = os.path.join(current_directory, "Spill.py")
                        subprocess.Popen(["python3", script_path])
                    elif button.action == "exit":
                        sys.exit()


    # Sjekker om du har musen over en knapp og så viser det
    for button in buttons:
        button.hovered = button.rect.collidepoint(mouse_x, mouse_y)
        button.draw(display)

    # Oppdaterer spillet med 60 fps
    pygame.display.update()
    clock.tick(60)
