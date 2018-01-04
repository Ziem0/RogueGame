import sys, tty, termios, os, csv

def create_board(level):
    
    board = []
    with open(level, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            row = list(row[0])
            board.append(row)

    return board



def print_board(board):
    """Prints board"""
    
    os. system("clear")
    for row in board:
        line = ''.join(row)
        print(line)



        







