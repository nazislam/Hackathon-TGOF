import character
import card
import maps
import os
import position
def print_welcome():
    print("Welcome to the Whispers of War")

def number_players():
    number = int(input("Please enter the number of players(2-4)"))
    return number

def create_player(i):
    while (1):
        type = input("What kind of character do you want(archer, mage, knight, warrior)? Please enter the first character: ")
        if type.lower() == "a":
            cha = character.createAcher(i)
            return cha
        if type.lower() == 'm':
            cha = character.createMage(i)
            return cha
        if type.lower() == 'k':
            cha = character.createKnight(i)
            return cha
        if type.lower() == 'w':
            cha = character.createWarrior(i)
            return cha
        print("Invalid input, please try again.")


if __name__ == '__main__':
    number_random_card = 10
    map = maps.Maps()
    map.create_map()
    map.set_random_card(number_random_card)
    map.set_random_box(number_random_card)
    print_welcome()
    players_num = number_players()
    players = []
    for i in range(players_num):
        players.append(create_player(i))
        position = players[i].getPosition()
        x = position.getx()
        y = position.gety()
        map.coordinate[x][y].set_obj(players[i], "Player")
        map.picture[x] = map.picture[x][:y - 1] + "P" + map.picture[x][y:]
        map.coordinate[x][y].terrain.stepable = False
    map.print_map()
    while(1):
        for i in range(players_num):
            player = players[i]
            player.addCard(card.generateCard())
            player.buff = []
            while (1):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Player number " + str(i + 1) + "'s turn")
                targets = player.check_attack_range(map)
                print("Your current Hp is", player.getHp())
                print("Your location is " + str(player.getPosition()))
                for j in range(len(player.hand)):
                    print(str(j) + ". " + str(player.hand[j]))
                print(str(len(player.hand)) + ". " + "Quit turn.")
                choice = int(input("Please enter your move"))
                if choice == len(player.hand):
                    break
                user_card = player.hand.pop(choice)
                if user_card.getType() == "Spell Card":
                    player.useSpellCard(user_card)
                elif user_card.getType() == "Move Card":
                    player.useMoveCard(user_card, map)
                    map.print_map()
                    print("Your position is: " + str(player.getPosition()))
                else:
                    if targets == 0:
                        player.hand.append(user_card)
                        print("Invalid move, there is no target in range")
                        continue
                    x, y = player.useAttackCard(user_card, map)
                    if x == -1:
                        print("Are you sure you don't need a new pair of glasses?")
                        input("Press enter to continue")
                        continue
                    obj = map.coordinate[x][y].get_obj()
                    print("Successful hit. Enermy's Hp is " + str(obj.getHp()))
                    input("Press enter to continue")
                    if obj.getHp() <= 0:
                        map.delete(x, y)
                        players.remove(obj)
                #if len(players) == 1:
                    #print("Player number " + str(i + 1) + " won")
                    #exit()
        #break