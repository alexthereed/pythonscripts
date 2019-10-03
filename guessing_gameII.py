#second attempt at a guessing game

#modules needed for this script
#random module needed to generate a random number

import random

num = random.randint(1,100)


#list to contain guesses
user_guesses = []




print("Welcome to guess the number! \n the computer has selected a random number between 0 and 100.")
print("You have an unlimited number of guesses \n After your first guess if you are given a response of \"COLD\" you are "
      "more than 10 numbers away from the correct number")
print("If you are given \"WARM\" on your first guess you are within 10 numbers of the correct number.")
print("After your first guess you will be given either a \"WARMER\" or \"COLDER\" based on if you are moving closer to or"
      "Further away from the correct number \n\n")
print("Good Luck!")

#boolean variable to continue or finish the game
game_status = True


while game_status == True:
    user_try = int(input("Please enter your guess: "))
    user_guesses.append(user_try)

    if user_try > 100 or user_try < 1:
        print("OUT OF BOUNDS!")
    else:
        if user_try == num:
            print(f"You WIN! it took you {len(user_guesses)} tires")
            game_status = False
        elif len(user_guesses) <= 1:
            if abs(user_try - num) > 10:
                print("COLD")
            if abs(user_try - num) <= 10:
                print("WARM")
        elif len(user_guesses) > 1:
            if abs(user_try - num) > abs(num - user_guesses[-2]):
                print('COLDER')
            if abs(user_try - num) < abs(num - user_guesses[-2]):
                print('WARMER')