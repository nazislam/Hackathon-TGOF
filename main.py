import character
def print_welcome():
    print("Welcome to the random name game")

def number_players():
    number = int(input("Please enter the number of players(2-4)"))
    return number

def create_player():
    while (1):
        type = input("What kind of character do you want(archer, mage, knight, warrior)? Please enter the first character")
        if type == "a":
            cha = character.archer
            return cha
        if type == 'm':
            cha = character.mage
            return cha
        if type == 'k':
            cha = character.knight
            return cha
        if type == 'w':
            cha = character.warrior
            return cha
        print("Invalid input, please try again. (Try to input lower case character)")


if __name__ == '__main__':
    print_welcome()
    players_num = number_players()
    players = []
    for i in range(players_num):
        players.append(create_player())