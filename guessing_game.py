#guessing game
#script picks a random number between 1 and 100


import random

guesses = []


guess_num = random.randint(1,100)

game_status = True



while game_status == True:
    player_guess = int(input('Please guess a number: '))
    print
    guesses.append(player_guess)
#This block makes sure the inputs are within 0 and 100
    if player_guess > 100 or player_guess < 1:
        print('OUT OF BOUNDS!')
    else:
        if player_guess == guess_num:
            print("you win")
            print("You got it in " + str(len(guesses)) + " guesses")
            game_status = False
        elif abs(player_guess - guess_num) >= 10 and len(guesses) == 1:
            print("COLD")
        elif abs(player_guess - guess_num) <= 10 and len(guesses) == 1:
            print("WARM")
        elif len(guesses) > 1 and abs(player_guess - guess_num) > abs(guess_num - guesses[-2]):
            print('COLDER')
        elif len(guesses) > 1 and abs(player_guess - guess_num) < abs(guess_num - guesses[-2]):
            print('WARMER')


