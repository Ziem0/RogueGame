import os, sys

intro ='''
                                                    ███        ▄█    █▄     ▄█     ▄████████    ▄████████
                                                ▀█████████▄   ███    ███   ███    ███    ███   ███    ███
                                                   ▀███▀▀██   ███    ███   ███▌   ███    █▀    ███    █▀
                                                    ███   ▀  ▄███▄▄▄▄███▄▄ ███▌  ▄███▄▄▄      ▄███▄▄▄
                                                    ███     ▀▀███▀▀▀▀███▀  ███▌ ▀▀███▀▀▀     ▀▀███▀▀▀
                                                    ███       ███    ███   ███    ███    █▄    ███
                                                    ███       ███    ███   ███    ███    ███   ███
                                                   ▄████▀     ███    █▀    █▀     ██████████   ███
                                                   '''

story = '''            In this game we identify with the most wanted thief in Miami. Our goal is to steal money from different places and collect energy
            drinks to charge our stamina. First stage is quite easy and its rather warm up than a real robbery. Our hero is really hungry and
            his mission is to make a little robbery from the farm. When we complete first level we pass to the next levels: forest,bank and the
            final room. Stolen and found items will be added to our private backpack and displayed on the screen. You are able to open doors by
            picking keys hidden on the board. Apart from earning money it's very important to find weapon and pick up as many bullets as you can.
            It will be useful in the last room. We hope you will enjoy our game. Have fun!!!'''


tutorial = '''                                              Game is really simple. If you want to move just press:
                                                                    w - move up,
                                                                    s - move down,
                                                                    a - move left,
                                                                    d - move right.

            Try to avoid enemies and other obstacles. Your mission is to steal as many items as it possible and of course to survive.

                                                                PRESS "F" TO CONTINUE'''

how_to_play = '''
                                                 ▄ .▄      ▄▄▌ ▐ ▄▌    ▄▄▄▄▄           ▄▄▄·▄▄▌   ▄▄▄· ▄· ▄▌
                                                ██▪▐█▪     ██· █▌▐█    •██  ▪         ▐█ ▄███•  ▐█ ▀█▐█▪██▌
                                                ██▀▐█ ▄█▀▄ ██▪▐█▐▐▌     ▐█.▪ ▄█▀▄      ██▀·██▪  ▄█▀▀█▐█▌▐█▪
                                                ██▌▐▀▐█▌.▐▌▐█▌██▐█▌     ▐█▌·▐█▌.▐▌    ▐█▪·•▐█▌▐▌▐█ ▪▐▌▐█▀·.
                                                ▀▀▀ · ▀█▄▀▪ ▀▀▀▀ ▀▪     ▀▀▀  ▀█▄▀▪    .▀   .▀▀▀  ▀  ▀  ▀ •'''

lose = '''
.----------------. .----------------. .----------------. .----------------.   .----------------. .----------------. .----------------. .----------------.
| .--------------. | .--------------. | .--------------. | .--------------. | | .--------------. | .--------------. | .--------------. | .--------------. |
| |    ______    | | |      __      | | | ____    ____ | | |  _________   | | | |     ____     | | | ____   ____  | | |  _________   | | |  _______     | |
| |  .' ___  |   | | |     /  \     | | ||_   \  /   _|| | | |_   ___  |  | | | |   .'    `.   | | ||_  _| |_  _| | | | |_   ___  |  | | | |_   __ \    | |
| | / .'   \_|   | | |    / /\ \    | | |  |   \/   |  | | |   | |_  \_|  | | | |  /  .--.  \  | | |  \ \   / /   | | |   | |_  \_|  | | |   | |__) |   | |
| | | |    ____  | | |   / ____ \   | | |  | |\  /| |  | | |   |  _|  _   | | | |  | |    | |  | | |   \ \ / /    | | |   |  _|  _   | | |   |  __ /    | |
| | \ `.___]  _| | | | _/ /    \ \_ | | | _| |_\/_| |_ | | |  _| |___/ |  | | | |  \  `--'  /  | | |    \ ' /     | | |  _| |___/ |  | | |  _| |  \ \_  | |
| |  `._____.'   | | ||____|  |____|| | ||_____||_____|| | | |_________|  | | | |   `.____.'   | | |     \_/      | | | |_________|  | | | |____| |___| | |
| |              | | |              | | |              | | |              | | | |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' | | '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '----------------'   '----------------' '----------------' '----------------' '----------------' '''

win = '''
                                                                           _                     __   _   _     _                      _
                    /\_/\___  _   _    __ _ _ __ ___   _ __ ___   __ _ ___| |_ ___ _ __    ___  / _| | |_| |__ (_) _____   _____ ___  / \\
                    \_ _/ _ \| | | |  / _` | '__/ _ \ | '_ ` _ \ / _` / __| __/ _ | '__|  / _ \| |_  | __| '_ \| |/ _ \ \ / / _ / __|/  /
                     / | (_) | |_| | | (_| | | |  __/ | | | | | | (_| \__ | ||  __| |    | (_) |  _| | |_| | | | |  __/\ V |  __\__ /\_/
                     \_/\___/ \__,_|  \__,_|_|  \___| |_| |_| |_|\__,_|___/\__\___|_|     \___/|_|    \__|_| |_|_|\___| \_/ \___|___\/'''


hero = '''
                                       ____ _                                                     _
                                      / ___| |__   ___   ___  ___  ___   _   _  ___  _   _ _ __  | |__   ___ _ __ ___
                                     | |   | '_ \ / _ \ / _ \/ __|/ _ \ | | | |/ _ \| | | | '__| | '_ \ / _ | '__/ _ \\
                                     | |___| | | | (_) | (_) \__ |  __/ | |_| | (_) | |_| | |    | | | |  __| | | (_) _
                                      \____|_| |_|\___/ \___/|___/\___|  \__, |\___/ \__,_|_|    |_| |_|\___|_|  \___(_)
                                                                         |___/ \n'''


def introduce_screen():
    print (intro + 3*'\n')
    print (story + 1*'\n')
    print (how_to_play + 3*'\n')
    print (tutorial)
    cont = input('\n')
    if cont == 'f' or cont == 'F':
        os.system('clear')
        print(hero)
        #name = input('Enter your hero name: ')
        print ('\n👨 - European guy. Left jail few days ago. With no prospects. Purpose of his life is to fulfill basic living needs.')
        print ('👳 - Arabic guy. He is strange but ambitious. He can blow up.')
        print ('👲 - Chinese little guy. He likes rice and the rice is everything what he needs. He steals money for rice.\n')
        choose = input('Choose you nationality: \n1 - European guy,\n2 - Arabic guy,\n3 - Chinese guy\n')
        #while choose in ['1', '2', '3']:
        while choose != '1' or choose != '2' or choose != '3':
            if choose == '1':
                print ('\nYou have chosen the guy from Lithuania. Colour of your skin is white.')
                break
            elif choose == '2':
                print ('\nYou have chosen the guy from Turkey. Colour of your skin is mixed.')
                break
            elif choose == '3':
                print ('\nYou have chosen the guy from China. Colour of your skin is yellow.')
                break
            else:
                choose = input('Choose option from 1, 2 or 3. Try again: ')
    else:
        exit()


def you_lost():
    print(lose)


def you_won():
    print(win)
