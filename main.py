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
            cha = character.archer
            return cha
        if type.lower() == 'm':
            cha = character.mage
            return cha
        if type.lower() == 'k':
            cha = character.knight
            return cha
        if type.lower() == 'w':
            cha = character.warrior
            return cha
        print("Invalid input, please try again.")


if __name__ == '__main__':
    map = maps.Maps()
    map.create_map()
    print_welcome()
    players_num = number_players()
    players = []
    for i in range(players_num):
        players.append(create_player())
        position = players[i].getPosition()
        x = position.getx()
        y = position.gety()
        map.coordinate[x][y].set_obj(players[i])
    ach = players[0]
    x, y, atk = ach.useAttackCard(card.AttackCard("abc", "abc", 20))
    ach.useSpellCard(card.SpellCard("abc", "abc", 0, 10, 0, 0, 0, 0))
    obj = map.coordinate[x][y].get_obj()
    obj.setHp(obj.getHp() - atk)
    map.coordinate[x][y].set_obj(obj)
    print(map.coordinate[x][y].get_obj().getHp())
    mag = players[1]

