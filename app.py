# Rock Paper Scissor

import random

while True:
    options = ['rock', 'paper', 'scissor']
    computer = random.choice(options)
    user = input("Your Choice (rock, paper, scissor): ").strip().lower()
    print("Computer input: ", computer)
    if user == 'rock' or user == 'paper' or user == 'scissor':
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
    print("""press 0 to exit and press any to continue.""", end=" ")
    if(input() == '0'):
        print("kyuu snake smell kr gyaa hai kyaaa...🐍")
        break

