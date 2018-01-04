import random
import os
import sys
import time
from update_inventory import inventory
from screens import *

def run_game():
    
    random_digit = draw_digits()
    print(random_digit)

    random_digit_list = list(random_digit)
    tries = 1

    while True:
        count_hot = 0
        count_warm = 0
        count_cold = 0
        print('Guess #', tries)

        digit_input = guess_digit()
        digit_input_list = check_digit(digit_input, random_digit_list)

        tries += 1

        if inventory['bullets'] == 0:
            os.system('clear')
            game_over()
            sys.exit()
            
        if digit_input_list == random_digit_list:
            os.system('clear')
            win_game()
            


def draw_digits():
    
    random_digit = range(100, 1000)
    random_digit = str(random.choice(random_digit))
    return random_digit


def guess_digit():

    digit_input = 0
    while True:
        try:
            digit_input = int(input("Guess digit: "))
        except ValueError:
            print("Try again. Enter 3 digits.")
            continue

        if len(str(digit_input)) != 3:
            print("Try again. Enter 3 digits.")
            continue
        else:
            break
    return str(digit_input)


def check_digit(digit_input, random_digit_list):

    count_hot = 0
    count_warm = 0
    count_cold = 0

    digit_input_list = list(digit_input)
    index_of_hot = []
    for item in range(len(digit_input_list)):
        if digit_input_list[item] == random_digit_list[item]:
            count_hot += 1
            index_of_hot.append(item)

    list_to_check_warm = [0, 1, 2]
    for i in range(len(index_of_hot)):
        list_to_check_warm.remove(index_of_hot[i])

    for i in list_to_check_warm:
        if digit_input_list[i] in random_digit_list:
            count_warm += 1
        else:
            count_cold += 1
    if count_cold == 3:
        print("Cold")
        inventory['bullets'] -= 1
    else:
        print("Hot " * count_hot, " Warm " * count_warm)
        inventory['bullets'] -= 1
    print("bullets: {}".format(inventory['bullets']))

    return digit_input_list

def game_over():
    '''Print last highscores and game over'''

    os.system('clear')
    you_lost()
    print ("\n\n\n\n\n\nLast highscores:\n")
    highscores = open('score.txt').read()
    print (highscores)


def win_game():
    '''Save the winner score to txt file, print last highscores and print you are the master of thieves'''

    os.system('clear')
    you_won()
    highscores = open('score.txt').read()
    print ("\n\n\n\n\nLast highscores:\n" + highscores)
    name = input('\n\n\nWhat is your name? ')
    fh = open('score.txt', 'a')
    fh.write('Name: ' + name + "  ")
    fh.write("Dollars: " + str(inventory['dollars']) + " \n")
    fh.close()
    print ('Your score has been added')
    sys.exit()
