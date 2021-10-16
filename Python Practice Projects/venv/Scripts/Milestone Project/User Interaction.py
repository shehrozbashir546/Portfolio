#Displays the game list
def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)

#Choose the position
def position_choice():
    choice = 'wrong'
    
    while choice not in ['0','1','2']:
        choice = input("Pick a position 0,1,2: ")
        if choice not in ['0','1','2']:
            clear_output()
            print("Sorry invalid choice! ")
    return int(choice)

#in case you want to replace your value
def replace_choice(game_list,position):

    user_place = input("Type to place at the position: ")
    game_list[position] = user_place
    return(game_list)


def gameOn():
    choice = 'wrong'

    while choice not in ['Y', 'N']:
        choice = input("Another Try? Y or N?: ")
        if choice not in ['Y', 'N']:
            print("Sorry invalid choice! ")
    if choice == 'Y':
        return True
    else:
        return False

#Intialize the Game
game_on = True
game_list = [0,1,2]
while game_on == True:
    display_game(game_list)
    position = position_choice()
    game_list = replace_choice(game_list,position)
    display_game(game_list)
    game_on = gameOn()
