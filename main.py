import character
import card
import maps
import position
def print_welcome():
    print("Welcome to the random name game")

def number_players():
    number = int(input("Please enter the number of players(2-4)"))
    return number

def create_player():
    while (1):
        type = input("What kind of character do you want(archer, mage, knight, warrior)? Please enter the first character")
        if type.lower() == "a":
            cha = character.createAcher()
            return cha
        if type.lower() == 'm':
            cha = character.createMage()
            return cha
        if type.lower() == 'k':
            cha = character.createKnight()
            return cha
        if type.lower() == 'w':
            cha = character.createWarrior()
            return cha
        print("Invalid input, please try again.")


if __name__ == '__main__':
    number_random_card = 10
    map = maps.Maps()
    map.create_map()
    map.set_random_card(number_random_card)
    print_welcome()
    players_num = number_players()
    players = []
    for i in range(players_num):
        players.append(create_player())
        position = players[i].getPosition()
        x = position.getx()
        y = position.gety()
        map.coordinate[x][y].set_obj(players[i], "Player")
        map.picture[x] = map.picture[x][:y - 1] + "P" + map.picture[x][y:]
        map.coordinate[x][y].terrain.stepable = False
    while(1):
        for i in range(players_num):
            print("Player number " +  str(i + 1) + "'s turn")
            player = players[i]
            player.addCard(card.generateCard())
            player.buff = []
            print(len(player.hand))
            for j in range(len(player.hand)):
                print(str(j) + ". " + str(player.hand[j]))
            print(str(len(player.hand)) + ". " + "Quit turn.")
            choice = int(input("Please enter your move"))
            if choice == len(player.hand):
                continue
            user_card = player.hand.pop(choice)
            if user_card.getType() == "Spell Card":
                player.useSpellCard(user_card)
            elif user_card.getType() == "Move Card":
                player.useMoveCard(user_card, map)
            else:
                player.useAttackCard(user_card, map)
        break