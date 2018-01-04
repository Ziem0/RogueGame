import sys, tty, termios, os, time, random, datetime, time, csv, random
from riddles import ask_riddles, question_1, question_2, question_3
from create_board import create_board, print_board
from update_inventory import print_table, add_item_to_inventory, inventory, added_items #add_to_inventory
from start_screen import *  
from characters import insert_player



def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.08)



def open_door(board, inventory, sign, y_current_position, y_direction, x_current_position, x_direction):
    if  board[y_current_position + y_direction][x_current_position + x_direction] == sign:
        if inventory['keys'] > 0:
            board[y_current_position + y_direction][x_current_position + x_direction] = " "
            delay_print('Now you can go inside')
        else:
            delay_print('You do not have any keys!')



def getch():
    '''Launches the keys'''
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch



def makes_good_step(y, x, y_next_step, x_next_step):
    '''Moves main character''' 

    y += y_next_step
    x += x_next_step
    
    return y, x



def check_next_step(y, x, barriers, board):
    '''Check the correctness of the next step'''

    return board[y][x] not in barriers



def set_direction(key_direction):
    '''Determines the value and direction of the hero's movement'''

    if key_direction == "w":
        x_direction = 0
        y_direction = -1
        inventory['stamina'] -= 1

    elif key_direction == "s":
        x_direction = 0
        y_direction = 1
        inventory['stamina'] -= 1

    elif key_direction == "a":
        x_direction = -1
        y_direction = 0
        inventory['stamina'] -= 1

    elif key_direction == "d":
        x_direction = 1
        y_direction = 0
        inventory['stamina'] -= 1

    else:
        x_direction = 0
        y_direction = 0


    return x_direction, y_direction


def handle_zero_level():
    # time.sleep(3)
    os.system("clear")
    time_start = time.time()

    x_current_position = 1
    y_current_position = 1

    board = create_board('level_0.csv')
    last_hero_position = board[y_current_position][x_current_position]
    barriers = ['X','⌂','🚪']

    key_direction = getch()  #control

    while key_direction != "q":

        key_direction = getch()
        x_direction, y_direction = set_direction(key_direction)
        board[y_current_position][x_current_position] = last_hero_position

        if check_next_step(y_current_position + y_direction, x_current_position + x_direction, barriers, board):
            y_current_position, x_current_position = makes_good_step(y_current_position, x_current_position, y_direction, x_direction)

        if inventory['dollars'] == 30:
            board[11][49] = "∃"

        if inventory['stamina'] <= 0:                #Gdy stamina spadnie ponizej 0 wyskakuje game over i highscores.
            game_over()
            sys.exit()

        if inventory['dollars'] > 150:                #W przypadku wygranej zapisuje wynik do pliku
            time_end = time.time() - time_start
            roundtime = round(time_end)
            win_game(roundtime)
            sys.exit()

        if board[y_current_position][x_current_position] == '∃':
            ask_riddles(question_1, delay_print, handles_first_level, handles_second_level)
            handles_first_level()

        elif key_direction == "q":
            sys.exit()


        open_doors(board, inventory, '🚪', y_current_position, y_direction, x_current_position, x_direction)
        add_item_to_inventory(board, inventory, y_current_position, x_current_position)
        last_hero_position = board[y_current_position][x_current_position]
        insert_player(board, y_current_position, x_current_position)

        print_board(board)
        print_table(inventory)



def handles_first_level():
    
    os.system("clear")
    x_current_position = 1  
    y_current_position = 1
    
    board = create_board('level_1.csv')
    last_hero_position = board[y_current_position][x_current_position]
    barriers = ['X','⌂','🚪']

    key_direction = getch()  #control

    while key_direction != "q":

        key_direction = getch()
        x_direction, y_direction = set_direction(key_direction)
        board[y_current_position][x_current_position] = last_hero_position

        if check_next_step(y_current_position + y_direction, x_current_position + x_direction, barriers, board):
            y_current_position, x_current_position = makes_good_step(y_current_position, x_current_position, y_direction, x_direction)
        
        if inventory['dollars'] == 40:
            board[8][60] = "∃"            
        
        if board[y_current_position][x_current_position] == '∃':
            ask_riddles(question_1, delay_print, handles_first_level, handles_second_level)
            # handles_second_level()   

         

        elif key_direction == "q":
            sys.exit()
        
        open_door(board, inventory, '🚪', y_current_position, y_direction, x_current_position, x_direction)
        add_item_to_inventory(board, inventory, y_current_position, x_current_position)
        last_hero_position = board[y_current_position][x_current_position]
        insert_player(board, y_current_position, x_current_position)        
                 
        print_board(board)
        print_table(inventory)
        



def handles_second_level():
    """Handle game's second level game."""

    os.system("clear")
    x_current_position = 1  #starting position of player
    y_current_position = 1
    board = create_board("level_1.csv")
    last_hero_position = board[y_current_position][x_current_position]

    barriers = ['X','⌂','🚪']
    added_items = []

    key_direction = getch()  #control

    while key_direction != "q":
        x_direction = 0
        y_direction = 0

        key_direction = getch()
        x_direction, y_direction = set_direction(key_direction)
        board[y_current_position][x_current_position] = last_hero_position

        if check_next_step(y_current_position + y_direction, x_current_position + x_direction, barriers, board):
            y_current_position, x_current_position = makes_good_step(y_current_position, x_current_position, y_direction, x_direction)

        add_item_to_inventory(board, inventory, y_current_position, x_current_position)
        last_hero_position = board[y_current_position][x_current_position]
        insert_player(board, y_current_position, x_current_position)
        print_board(board)
        print_table(inventory)

# def main():
#     kdfghkdjhfgkjdhfg(handles_first_level)
#     handles_first_level()    

if __name__ == '__main__':
    handles_first_level()
