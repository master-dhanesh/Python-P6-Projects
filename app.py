from random import randint

number_range = input("Enter Number range seperated by space: ").split()
if  len(number_range) == 2:
    start = int(number_range[0])
    end = int(number_range[1])
    random_number = randint(start, end)
    chances = 5

    while chances > 0:
        user_input = int(input("Guess the number: "))
        if user_input > end or user_input < start:
            print("Chutiya hai kya...")
            continue
        else:
            if user_input > random_number:
                print("Number is smaller...better luck next time💗")
            elif user_input < random_number:
                print("Number is greater...better luck next time💗")
            else:
                print("Gotcha...Purus-kaar milega tumhe...")
                break
            chances = chances - 1
            if chances == 0:
                print("Tumse na ho paaega...💩")
else:
    print("Dekh kr likh bhadwe...😊")