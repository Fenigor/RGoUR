'''
DOCSTRING The Royal Game of UR Consol Version
'''
import random

class Player():

    mid_path = [i for i in range(4, 12)]
    finished = []

    def __init__(self, color, path, symbol):
        self.color = color
        self.path = [i for i in range(0, 5)]
        self.path.append(12)
        self.path.append(13)
        self.path[4] = path
        self.symbol = symbol
        self.pawns = [symbol for _ in range(7)]
'''
DEPRICATED
def create_board():
    ''''''
    DOCSTRING creates a board for "The Royal Game of UR"
    Input: None
    Output: 2 lists one for each player + 1 more representing the shared fields
    Return: None
    ''''''
    global MID_PATH
    global RED_PATH
    global BLUE_PATH
    MID_PATH = [i for i in range(4, 12)]
    #MID_PATH[MID_PATH.index(7)] = "R"
    RED_PATH = [i for i in range(0, 4)]
    RED_PATH.insert(4, MID_PATH)
    RED_PATH.append(12)
    RED_PATH.append(13)
    #RED_PATH[RED_PATH.index(3)] = "R"
    #RED_PATH[RED_PATH.index(13)] = "R"
    BLUE_PATH = RED_PATH.copy()
'''
def dice_roll():
    '''
    DOCSTRING simulates 4 4d dices being rolled
    Input: None
    Output: says if you rolled a move
    Return: number of moves you got by the roll
    '''
    num_moves = 0
    for _ in range(4):
        roll = random.randint(1, 4)
        if roll > 2:
            num_moves += 1
    print("You rolled {} moves".format(num_moves))
    return num_moves

def move(player, from_pos, moves):
    '''
    DOCSTRING moves a piece
    '''
    path = player.path
    symbol = player.symbol
    
    to_ = from_pos + moves
    if to_ > 14:
        print("Can't move!")
        return from_pos
    elif to_ == 14:
        if from_pos < 12:
            path[4][from_pos - 4] = from_pos
        else:
            path[from_pos - 7] = from_pos
        #FINISHED.append(symbol)
        print("Scored!")
        return 14
    elif to_ > 11:
        if from_pos < 12:
            path[4][from_pos - 4] = from_pos
        else:
            path[from_pos - 7] = from_pos
        path[to_-7] = symbol
    elif to_ > 3 and to_ < 12:
        if from_pos < 4:
            path[from_pos] = from_pos
        else:
            path[4][from_pos - 4] = from_pos
        path[4][to_-4] = symbol
    else:
        if from_pos != -1:
            path[from_pos] = from_pos
        path[path.index(to_)] = symbol
    return to_

def main():
    '''
    DOCSTRING Main Function
    '''

    red = Player("Red", Player.mid_path, "x")
    blue = Player("Blue", Player.mid_path, "o")
    pair = (red, blue)
    game_on = True
    i = 0
    while game_on:
        i = i%2
        num = Player.finished.count(pair[i].symbol)
        print("It's {}".format(pair[i].color))
        if num == 7:
            game_on = False
            break
        else:
            y = input("do you want to add a new piece (y for yes) ")
            if y == "y":
                move(pair[i], -1, dice_roll())
                print(pair[i].path)
            else:
                x = input("pick a position ")
                if pair[i].path[int(x)] == "x":
                    move(pair[i], int(x), dice_roll())
                print(pair[i].path)
        i += 1
    '''for _ in range(20):
        moves = dice_roll()
        if moves != 0:
            prev_pos = start
            start = move(RED_PATH, start, moves)
            if start > 14:
                start = prev_pos
            elif start in (3, 7, 13):
                pass
            elif start == 14:
                print(RED_PATH)
                break
        print(RED_PATH)
    print(RED_PAWS)'''
#main()

#from ipywidgets import interact, interactive, fixed
#import ipywidgets as widgets
#from IPython.display import display

def f(x):
    return x
  

#w = interact(f, x=10);  
#display(w)
