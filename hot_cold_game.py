import random, os

def run_game(bullets):
    num = str(random.randint(100,1000))
    print (num)
    while bullets > 0  :
        user_guess = input("Type a 3 digit number: ")

        guess_number = []
        for digit in num:
            guess_number.append(digit)

        user_number = []
        for digit in user_guess:
            user_number.append(digit)

        clues_list = []
        for i in range(3):
            if user_number[i] == guess_number[i]:
                clues_list.insert(0,"Hot")
            elif user_number[i] != guess_number[i] and user_number[i] in guess_number :
                clues_list.append("Warm")
        print(*clues_list)

        if not any(digit in guess_number for digit in user_number):
            print('Cold')
            bullets -= 1
        

            