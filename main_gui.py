"""
GUI version of "Whispers of War"
Framework : Pygame 
"""

import pygame
import random
import character
import card
import mapsGUI
import position

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

# Player's ID
global player_id
global player_img
player_id = [0, 1]
player_img = []

#Jobs Avatar
archer = pygame.image.load('resources/characters/archer.png')
archer = pygame.transform.scale(archer, (40, 40))
knight = pygame.image.load('resources/characters/knight.png')
knight = pygame.transform.scale(knight, (40, 40))
mage = pygame.image.load('resources/characters/mage.png')
mage = pygame.transform.scale(mage, (40, 40))
warrior = pygame.image.load('resources/characters/warrior.png')
warrior = pygame.transform.scale(warrior, (40, 40))

# Map's Property
global map
global players_num
global number_random_card
global players
global cur_player
number_random_card = 10
players_num = 2
players = []
cur_player = "" 
map = mapsGUI.Maps()
map.create_map()
map.set_random_card(number_random_card)
map.set_random_box(number_random_card)

##############################################################################
archer = pygame.image.load('resources/interfaces/character_button/archer.png')
archer = pygame.transform.scale(archer, (200, 200))

knight = pygame.image.load('resources/interfaces/character_button/knight.png')
knight = pygame.transform.scale(knight, (200, 200))

mage = pygame.image.load('resources/interfaces/character_button/mage.png')
mage = pygame.transform.scale(mage, (200, 200))

warrior = pygame.image.load(
    'resources/interfaces/character_button/warrior.png')
warrior = pygame.transform.scale(warrior, (200, 200))

##

archer2 = pygame.image.load(
    'resources/interfaces/character_button/archer2.png')
archer2 = pygame.transform.scale(archer2, (200, 200))

knight2 = pygame.image.load(
    'resources/interfaces/character_button/knight2.png')
knight2 = pygame.transform.scale(knight2, (200, 200))

mage2 = pygame.image.load('resources/interfaces/character_button/mage2.png')
mage2 = pygame.transform.scale(mage2, (200, 200))

warrior2 = pygame.image.load(
    'resources/interfaces/character_button/warrior2.png')
warrior2 = pygame.transform.scale(warrior2, (200, 200))

##############################################################################


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

            elif action == 'selecting':
                selecting_loop(0)
                selecting_loop(1)

            elif action == 'quit':
                pygame.quit()
                quit()

    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
    print_text1(screen, smg, 'freesansbold.ttf', int(h * 0.4), smgc,
                (2 * (x) + w) / 2, (2 * (y) + h) / 2)


#def botton2(smg, smgc, x, y, w, h, ic, ac, action="None"):


def botton2(img, img2, x, y, action="None"):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #center_x = x + 100
    #center_y = y + 100

    #distance = ((mouse[0]-center_x)**2 + (mouse[1]-center_y)**2)**0.5
    #distance > 50**2
    if x < mouse[0] < x + 200 and y < mouse[1] < y + 200:
        screen.blit(img, (x, y))

        if click[0] == 1 and action != None:
            
            if action == 'start':
                #reset()
                playing_loop()

            elif action == 'pause':
                paused()

            elif action == 'unpause':
                unpause()
            
            elif action == 'selecting':
                selecting_loop(0)
                selecting_loop(1)

            elif action == 'menu':
                menu_loop()

            elif action == "1":
                targets = cur_player.check_attack_range(map)
                user_card = cur_player.hand.pop(choice)
                if user_card.getType() == "Spell Card":
                    cur_player.useSpellCard(user_card)
                elif user_card.getType() == "Move Card":
                    cur_player.useMoveCard(user_card, map)
                    map.print_map()
                    #print("Your position is: " + str(cur_player.getPosition()))
                else:
                    if targets == 0:
                        cur_player.hand.append(user_card)
                        print("Invalid move, there is no target in range")
                        #continue
                    x, y = cur_player.useAttackCard(user_card, map)
                    if x == -1:
                        pass
                        #continue
                    obj = map.coordinate[x][y].get_obj()
                    #print("Successful hit. Enermy's Hp is " + str(obj.getHp()))
                    if obj.getHp() <= 0:
                        map.delete(x, y)
                        players.remove(obj)

            elif action in [0, 1]:
                archerImg = pygame.image.load('resources/characters/archer.png')
                archerImg = pygame.transform.scale(archerImg, (40, 40))
                knightImg = pygame.image.load('resources/characters/knight.png')
                knightImg = pygame.transform.scale(knightImg, (40, 40))
                mageImg = pygame.image.load('resources/characters/mage.png')
                mageImg = pygame.transform.scale(mageImg, (40, 40))
                warriorImg = pygame.image.load('resources/characters/warrior.png')
                warriorImg = pygame.transform.scale(warriorImg, (40, 40))
                
                if img is archer:
                    char = character.createAcher(player_id[action])
                    player_img.append(archerImg)
                elif img is mage:
                    char = character.createMage(player_id[action])
                    player_img.append(mageImg)
                elif img is knight:
                    char = character.createKnight(player_id[action])
                    player_img.append(knightImg)
                else:
                    char = character.createWarrior(player_id[action])
                    player_img.append(warriorImg)

                players.append(char)
                position = players[action].getPosition()
                x = position.getx()
                y = position.gety()
                map.coordinate[x][y].set_obj(players[action], "Player")
                map.picture[
                    x] = map.picture[x][:y - 1] + "P" + map.picture[x][y:]
                map.print_map()
                map.coordinate[x][y].terrain.stepable = False

                if action == 0:
                    selecting_loop(1)
                if action == 1:
                    playing_loop()

            elif action == 'quit':
                pygame.quit()
                quit()

    else:
        screen.blit(img2, (x, y))


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

def renderHand(player_hand):
    count = 0
    for card in player_hand:
        card_name = card.getName()
        cur_card = pygame.image.load('resources/cards/' + card_name + '.png')
        cur_card = pygame.transform.scale(cur_card, (84, 140))
        screen.blit(cur_card, (370 + 84 * count + 10 * count, 573))
        botton2(cur_card, cur_card,370 + 84 * count + 10 * count, 573, str(count))


        count += 1

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

def renderMapUpdate():
    box = pygame.image.load('resources/boxes/armor_box.png')
    box = pygame.transform.scale(box, (40, 40))
    card = pygame.image.load('resources/cards/card.png')
    card = pygame.transform.scale(card, (40, 40))


    objectDict = {"Card" : card,
                   "Box" : box,
                   "Player0" : player_img[0],
                   "Player1": player_img[1]}

    startPos = 235

    for m in range(14):
        for n in range(26):
            card_type = map.coordinate[m][n].get_type()
            if card_type != "nothing":
                objectImg = objectDict[card_type]
                
                screen.blit(objectImg, (235 + 40 * n, 5 + m * 40))
                #screen.blit(screen, terrain, (235 + 40 * k, 5 + i * 40))


def menu_loop():
    intro = True
    screen.fill((0, 0, 0))
    #print_text1(screen, 'Whispers of War', 'resources/fonts/arial.ttf', 100,(255, 255, 255), screen_w / 2, 300)
    switch = False

    background = pygame.image.load('resources/interfaces/interface_start_logo.png')
    screen.blit(background, (0, 0))

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        if switch == True:
            background = pygame.image.load('resources/interfaces/black.png')
            screen.blit(background, (0, 0))
            botton('START', (0, 0, 0), (screen_w / 2 - 75),(screen_h * 1 / 2 + 400), 150, 50, (100, 255, 180), (0, 150, 0),'selecting')
            logo = pygame.image.load('resources/interfaces/interface_title.png')
            logo = pygame.transform.scale(logo, (540, 160))
            botton2(logo, logo, screen_w/2 - 265, screen_h/2 - 250, action="selecting")

            start = pygame.image.load('resources/interfaces/buttons/start.png')
            start_on_click = pygame.image.load('resources/interfaces/buttons/start_on_click.png')
            exit = pygame.image.load('resources/interfaces/buttons/exit.png')
            exit_on_click = pygame.image.load('resources/interfaces/buttons/exit_on_click.png')
            #logo = pygame.transform.scale(logo, (540, 160))
            botton2(start, start_on_click, screen_w/2 - 135, screen_h/2 , action = "selecting")
            botton2(exit, exit_on_click, screen_w/2 - 135, screen_h/2 + 200 , action = "quit")

            

            #botton('START', (0,0,0), (screen_w/2-75), (screen_h*1/2+50), 150, 50, (100, 255, 180), (0, 150, 0),'start')

        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            switch = True
            

        pygame.display.update()
        clock.tick(60)


def selecting_loop(player_number):
    intro = True
    screen.fill((0, 0, 0))
    background = pygame.image.load(
        'resources/interfaces/background/interface_selection' +
        str(player_number+1) + '.png')
    screen.blit(background, (0, 0))

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        botton2(archer, archer2, 55, 210, player_number)
        botton2(mage, mage2, 350, 210, player_number)
        botton2(knight, knight2, 700, 210, player_number)
        botton2(warrior, warrior2, 1010, 210, player_number)

        pygame.display.update()
        clock.tick(60)


def playing_loop():
    global start_time
    start_time = pygame.time.get_ticks()
    turn = 0

    while True:
        # Show Prgress
        #screen.fill((0, 0, 0))
        screen.fill((255, 255, 255))
        background = pygame.image.load('resources/interfaces/border.png')
        screen.blit(background, (0, 0))
        renderMapTerrain()
        renderMapUpdate()
        command = ""

        exit_in_interface = pygame.image.load('resources/interfaces/buttons/exit_in_interface.png')
        exit_in_interface_on_click = pygame.image.load('resources/interfaces/buttons/exit_in_interface_on_click.png')

        pause_in_interface = pygame.image.load('resources/interfaces/buttons/pause_in_interface.png')
        pause_in_interface_on_click = pygame.image.load('resources/interfaces/buttons/pause_in_interface_on_click.png')
        
        botton2(exit_in_interface, exit_in_interface_on_click,  5 + 110 + 5, screen_h - 55, action="quit")
        botton2(pause_in_interface, pause_in_interface_on_click, 5, screen_h - 55, action="pause")

        warrior_icon_property = pygame.image.load('resources/interfaces/character_button/warrior_icon_property.png')
        botton2(warrior_icon_property, warrior_icon_property,  5, 5, action="quit")

        back_card = pygame.image.load('resources/interfaces/card.png')
        back_card = pygame.transform.scale(back_card, (225 , 525))
        botton2(back_card, back_card,  5, 155)


        """botton(smg, smgc, x, y, w, h, ic, ac, action="None")
        botton2(img, img2, x, y, action="None"):

        botton('PAUSE', (0, 0, 0), 5 + 110 + 5, screen_h - 55, 110, 50,(100, 255, 180), (0, 150, 0), 'pause')
        botton('PAUSE', (0, 0, 0), 5, screen_h - 55, 110, 50, (100, 255, 180), (0, 150, 0), 'pause')"""


        if turn == 0:
            cur_player = players[turn]
            if len(cur_player.hand) < 8:
                cur_player.addCard(card.generateCard())
            cur_player.buff = []

            for event in pygame.event.get():
                # Handle non-keyboard input
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            """
            command += "Player number " + str(turn + 1) + "'s turn\n"
            targets = player.check_attack_range(map)
            command += "Your current Hp is" + str(cur_player.getHp()) + "\n"
            command += "Your location is " + str(cur_player.getPosition()) + "\n"
            for j in range(len(cur_player.hand)):
                command += str(j) + ". " + str(cur_player.hand[j]) + "\n"
                command += str(len(cur_player.hand)) + ". " + "Quit turn.\n"
            command += "Please enter your move: \n"
            """

            renderHand(cur_player.hand)
            #smg, smgc, x, y, w, h, ic, ac, action="None"
            #botton(command, (0, 0, 0), 5, screen_h - 55, 225, 50, (100, 255, 180),(0, 150, 0))
            

            
            # UI Bottons
            """botton('PAUSE', (0, 0, 0), 5, screen_h - 55, 110, 50, (100, 255, 180),
                (0, 150, 0), 'pause')
            botton('PAUSE', (0, 0, 0), 5 + 110 + 5, screen_h - 55, 110, 50,
                (100, 255, 180), (0, 150, 0), 'pause')
        """
        else:
            cur_player = players[turn]
            cur_player.addCard(card.generateCard())
            cur_player.buff = []

            for event in pygame.event.get():
                # Handle non-keyboard input
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # UI Bottons
            botton('PAUSE', (0, 0, 0), 5, screen_h - 55, 110, 50, (100, 255, 180),
                (0, 150, 0), 'pause')
            botton('PAUSE', (0, 0, 0), 5 + 110 + 5, screen_h - 55, 110, 50,
                (100, 255, 180), (0, 150, 0), 'pause')

            

        #botton('O', (0, 0, 0), 235, 5, 40, 40, (100, 255, 180), (0, 150, 0), 'pause')

        # Keep track of frames
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    menu_loop()
