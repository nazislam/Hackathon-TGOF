"""
GUI version of "Whispers of War"
Framework : Pygame 
"""

import pygame
import random

import game

pygame.init()

# resolution
screen_w = 1280
screen_h = 720

# Surface
screen = pygame.display.set_mode((screen_w, screen_h))

# Title
pygame.display.set_caption('Hangman')

# The game's clock
clock = pygame.time.Clock()


def unpause():
    global pause
    global start_time
    global pause_start
    pause = False
    pause_end = pygame.time.get_ticks()
    start_time = start_time + pause_end - pause_start


# Pause the Game with another screen
def paused():
    global pause_start
    global pause
    pause = True
    pause_start = pygame.time.get_ticks()
    screen.fill((0, 0, 0))
    print_text1(screen, 'PAUSED', 'resources/fonts/arial.ttf', 150,
                (255, 255, 255), screen_w / 2, 300)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        botton('RESUME', (0, 0, 0), (screen_w / 2 - 75),
               (screen_h * 1 / 2 + 50), 150, 50, (100, 255, 180), (0, 150, 0),
               'unpause')
        botton('QUIT', (0, 0, 0), screen_w / 2 - 75, screen_h * 1 / 2 + 100,
               150, 50, (100, 255, 180), (0, 150, 0), 'quit')

        pygame.display.update()
        clock.tick(60)


def botton(smg, smgc, x, y, w, h, ic, ac, action="None"):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(screen, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            if action == 'start':
                #reset()
                playing_loop()

            elif action == 'pause':
                paused()

            elif action == 'unpause':
                unpause()

            elif action == 'menu':
                menu_loop()

            elif action == 'quit':
                pygame.quit()
                quit()

    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
    print_text1(screen, smg, 'freesansbold.ttf', int(h * 0.4), smgc,
                (2 * (x) + w) / 2, (2 * (y) + h) / 2)


# Print text position by center coor
def print_text1(surface, text, font, size, color, centerx, centery):
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = ((centerx), (centery))
    surface.blit(text_surface, text_rect)


# Print text position by top left corner
def print_text2(surface, text, font, size, color, x, y):
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.x, text_rect.y = x, y
    surface.blit(text_surface, text_rect)


def menu_loop():
    intro = True
    screen.fill((0, 0, 0))
    print_text1(screen, 'Whispers of War', 'resources/fonts/arial.ttf', 100,
                (255, 255, 255), screen_w / 2, 300)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        botton('START', (0, 0, 0), (screen_w / 2 - 75),
               (screen_h * 1 / 2 + 50), 150, 50, (100, 255, 180), (0, 150, 0),
               'start')

        pygame.display.update()
        clock.tick(60)


def selecting_loop():
    pass


def renderMapTerrain():
    grass = pygame.image.load('resources/terrain/grass.png')
    grass = pygame.transform.scale(grass, (40, 40))
    mountain = pygame.image.load('resources/terrain/mountain.png')
    mountain = pygame.transform.scale(mountain, (40, 40))
    river = pygame.image.load('resources/terrain/river.png')
    river = pygame.transform.scale(river, (40, 40))
    swamp = pygame.image.load('resources/terrain/swamp.png')
    swamp = pygame.transform.scale(swamp, (40, 40))
    terrainDict = {".": grass, "^": mountain, "*": river, "-": swamp}

    startPos = 235
    file = open("map3/map.txt", "r")
    char = file.read(1)

    for i in range(14):
        for k in range(27):
            if char == "\n":
                char = file.read(1)
                continue
            terrain = terrainDict[char]
            screen.blit(terrain, (235 + 40 * k, 5 + i * 40))
            char = file.read(1)

    file.close()


def playing_loop():
    global start_time
    start_time = pygame.time.get_ticks()

    renderMapTerrain()

    while True:
        # Show Prgress
        #screen.fill((0, 0, 0))
        screen.fill((255, 255, 255))
        background = pygame.image.load('resources/interfaces/border.png')
        screen.blit(background, (0, 0))
        renderMapTerrain()

        for event in pygame.event.get():
            # Handle non-keyboard input
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # UI Bottons
        botton('PAUSE', (0, 0, 0), 5, screen_h - 55, 112, 50, (100, 255, 180),
               (0, 150, 0), 'pause')
        botton('PAUSE', (0, 0, 0), 5 + 112 + 1, screen_h - 55, 112, 50,
               (100, 255, 180), (0, 150, 0), 'pause')
        """
        terrain = pygame.image.load('resources/terrain/grass.png')
        terrain = pygame.transform.scale(terrain, (40, 40))
        screen.blit(terrain, (235, 5))
        """

        #botton('O', (0, 0, 0), 235, 5, 40, 40, (100, 255, 180), (0, 150, 0), 'pause')

        # Keep track of frames
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    menu_loop()
