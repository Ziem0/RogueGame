import sys, tty, termios, os, datetime, time, csv, random
from riddles import ask_riddles, question_1, question_2, question_3
from create_board import create_board, print_board
from update_inventory import print_table, add_item_to_inventory, inventory, added_items
from characters import insert_player
from screens import introduce_screen, you_lost, you_won
from hot_cold import run_game, game_over


def delay_print(s):
    '''Print letter by letter'''

    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.08)


def open_doors(board, inventory, sign, y_current_position, y_direction, x_current_position, x_direction):
    '''If hero has key and his position is next to door, remove door'''

    if  board[y_current_position + y_direction][x_current_position + x_direction] == sign:
        if inventory['keys'] > 0:
            board[y_current_position + y_direction][x_current_position + x_direction] = " "
            delay_print('Now you can go inside')
        else:
            delay_print('You do not have any keys!')


def getch():

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch



def take_next_step(y, x, y_next_step, x_next_step):
    '''Move main character'''

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

    time.sleep(3)
    os.system("clear")
    time_start = time.time()
    

    x_current_position = 1
    y_current_position = 1

    board = create_board('level_0.csv')
    print_board(board)
    print_table(inventory)
    last_hero_position = board[y_current_position][x_current_position]
    barriers = ['X','⌂','🚪']

    key_direction = getch()  #control

    while key_direction != "q":

        key_direction = getch()
        x_direction, y_direction = set_direction(key_direction)
        board[y_current_position][x_current_position] = last_hero_position

        if check_next_step(y_current_position + y_direction, x_current_position + x_direction, barriers, board):
            y_current_position, x_current_position = take_next_step(y_current_position, x_current_position, y_direction, x_direction)

        if inventory['dollars'] == 50:
            board[11][49] = "∃"

        if inventory['stamina'] <= 0:                
            game_over()
            sys.exit()

        if board[y_current_position][x_current_position] == '∃':
            ask_riddles(question_1, delay_print, handle_first_level, handle_first_level)

        elif key_direction == "q":
            sys.exit()


        open_doors(board, inventory, '🚪', y_current_position, y_direction, x_current_position, x_direction)
        add_item_to_inventory(board, inventory, y_current_position, x_current_position)
        last_hero_position = board[y_current_position][x_current_position]
        insert_player(board, y_current_position, x_current_position)

        print_board(board)
        print_table(inventory)


def handle_first_level():

    os.system("clear")
    time_start = time.time()

    x_current_position = 1
    y_current_position = 1

    board = create_board('level_1.csv')
    print_board(board)
    print_table(inventory)
    last_hero_position = board[y_current_position][x_current_position]
    barriers = ['X','⌂','🚪']

    key_direction = getch()  #control

    while key_direction != "q":

        key_direction = getch()
        x_direction, y_direction = set_direction(key_direction)
        board[y_current_position][x_current_position] = last_hero_position

        if check_next_step(y_current_position + y_direction, x_current_position + x_direction, barriers, board):
            y_current_position, x_current_position = take_next_step(y_current_position, x_current_position, y_direction, x_direction)

        if inventory['dollars'] == 170:
            board[8][60] = "∃"

        if inventory['stamina'] <= 0:                
            game_over()
            sys.exit()

        if board[y_current_position][x_current_position] == '∃':
            ask_riddles(question_2, delay_print, handle_first_level, handle_second_level)

        elif key_direction == "q":
            sys.exit()


        open_doors(board, inventory, '🚪', y_current_position, y_direction, x_current_position, x_direction)
        add_item_to_inventory(board, inventory, y_current_position, x_current_position)
        last_hero_position = board[y_current_position][x_current_position]
        insert_player(board, y_current_position, x_current_position)

        print_board(board)
        print_table(inventory)


def handle_second_level():
    
    os.system("clear")
    time_start = time.time()

    x_current_position = 1
    y_current_position = 1

    board = create_board('level_2.csv')
    print_board(board)
    print_table(inventory)
    last_hero_position = board[y_current_position][x_current_position]
    barriers = ['X','⌂','🚪', '🚛', '🚒', '🚙', '🚐', '🚲', '🚶', '🚸']

    key_direction = getch()  #control

    while key_direction != "q":

        key_direction = getch()
        x_direction, y_direction = set_direction(key_direction)
        board[y_current_position][x_current_position] = last_hero_position

        if check_next_step(y_current_position + y_direction, x_current_position + x_direction, barriers, board):
            y_current_position, x_current_position = take_next_step(y_current_position, x_current_position, y_direction, x_direction)

        if inventory['dollars'] == 250:
            board[1][49] = "∃"

        if inventory['stamina'] <= 0:                
            game_over()
            sys.exit()

        if board[y_current_position][x_current_position] == '∃':
            if inventory['revolver'] == 1 : 
                ask_riddles(question_3, delay_print, handle_first_level, handle_third_level)
        if board[y_current_position][x_current_position] == '∃':
            if inventory['revolver'] == 0 :
                delay_print('You need a gun to go to the next level!')  

        elif key_direction == "q":
            sys.exit()


        open_doors(board, inventory, '🚪', y_current_position, y_direction, x_current_position, x_direction)
        add_item_to_inventory(board, inventory, y_current_position, x_current_position)
        last_hero_position = board[y_current_position][x_current_position]
        insert_player(board, y_current_position, x_current_position)

        print_board(board)
        print_table(inventory)



def handle_third_level(): 

    os.system("clear")
    time_start = time.time()


    board = create_board('level_3.csv')
    print_board(board)
    print_table(inventory)
    bullets = inventory['bullets']
    delay_print('If you wanna cash, you will first have to shoot me. You have '+ str(bullets) +' bullets. Pull the trigger.')
    run_game()
    
    key_direction = getch()  #control

    while key_direction != "q":
                                               
        if key_direction == "q":
            sys.exit()

def main():
    
    introduce_screen()
    handle_zero_level()




if __name__ == '__main__':
    main()
