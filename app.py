# Rock Paper Scissor

import random

def userinput():
    user = input("Your Choice (rock, paper, scissor): ").strip().lower()
    return user

def computerinput():
    options = ['rock', 'paper', 'scissor']
    computer = random.choice(options)
    return computer

def rockpaperscissor(user, computer):
    if user == 'rock' or user == 'paper' or user == 'scissor':
        print("Computer input: ", computer)
        if (computer == user):
            print("Chutiya ho kya bc 😊....")
        elif (computer == 'rock'):
            if user == 'paper':
                print('User wins...')
            else:
                print('Computer wins...')
        elif (computer == 'paper'):
            if user == 'scissor':
                print('User wins...')
            else:
                print('Computer wins...')
        elif (computer == 'scissor'):
            if user == 'rock':
                print('User wins...')
            else:
                print('Computer wins...')
    else:
        print('bahggg makade😊...!')

def exitgame():
    print("""press 0 to exit and press any to continue.""", end=" ")
    if (input() == '0'):
        print("kyuu snake smell kr gyaa hai kyaaa...🐍")
        exit(0)

while True:
    user = userinput()
    computer = computerinput()
    rockpaperscissor(user,computer)
    exitgame()

