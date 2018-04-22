"""
GUI version of "Whispers of War"
Framework : Pygame 
"""

import pygame
import game

def main():
  ##########Initialization##########
  thisGame = Game()
  # Initialize Pygame
  pygame.init()
  # Initialize Screen (Surface)
  screen = pygame.display.set_mode(thisGame.getScreenResolution())
  # Initialize Title
  pygame.display.set_caption('Whispers of War')
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
    global pause
    global pause_start
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


def playing_loop():
    global start_time
    start_time = pygame.time.get_ticks()

    playing = True
    screen.fill((0, 0, 0))
    print_text1(screen, 'Playing', 'resources/fonts/arial.ttf', 100,
                (255, 255, 255), screen_w / 2, 300)

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        botton('PAUSE', (0, 0, 0), screen_w / 2 - int(150 / 2), screen_h - 50,
               150, 50, (100, 255, 180), (0, 150, 0), 'pause')

        pygame.display.update()
        clock.tick(60)


menu_loop()