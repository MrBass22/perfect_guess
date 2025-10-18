
# PERFECT GUESS #

import random

def greet():
    print('''Welcome user. We are going to play "PERFECT GUESS".''')
    def starting():
        option = input('Would you like to start the game? [YES or NO]: ')
        l_option = option.lower()
        if(l_option == 'yes'):
            instructions()
        elif(l_option == 'no'):
            print("Thank You. Let's play again later then.")
            exit()
        else:
            print('Enter a valid reply.')
            starting()
    starting()
        
def instructions():
    print('''Here are the instructions to the game:
          The computer will choose one number between 1 and 100 (both inclusive).
          Then you have to guess that number.
          Upon guessing, you will be told whether the correct number is higher or lower than your guess.
          Likewise, you can continue the game until you guessed the correct number.
          So let's start the game!
          Best of Luck!!''')
    MAIN()

def MAIN():
    user = int(input('Enter your guess: '))
    if(user>G_number):
        print('Your pre-eminent speculation about the faultless integer needs to be lowered')
        MAIN()
    elif(user<G_number):
        print('Your pre-eminent speculation about the faultless integer needs to be highered')
        MAIN()
    else:
        print('Bravo! Noble, your dredgrey of investigating and yielding a positive probability of the faultless integer has paid off!')
        again()

def again():
    restart = input('Would you like to play again? [YES or NO]: ')
    l_restart = restart.lower()
    if(l_restart == 'yes'):
        MAIN()
    elif(l_restart == 'no'):
        print('Thank You for playing.')
        exit()
    else:
        print('Enter a valid reply.')
        again()

G_number = random.randint(1,100)
greet()