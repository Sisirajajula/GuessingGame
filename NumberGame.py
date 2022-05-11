from tkinter import *
import random
def difficulty(Choice):
    if Choice == 'easy':
        return 10
    elif Choice == 'hard':
        return 5 
    else:
        return 0
def attempt(System_number,attempts):
    while attempts > 0:
        print(f'You have {attempts} attempts remaining to guess the number.')
        guess_number = int(input('Make a guess: '))
        if System_number > guess_number:
            print('Too low')
            print('Guess again.')
        elif System_number < guess_number:
            print('Too High')
            print('Guess again.')
        elif System_number == guess_number:
            print(f'You got it.The answer was {System_number}')
            break
        attempts -= 1
    if guess_number != System_number:
        print('You lost.Not guessed the number.')

print("Welcome to the Number Guessing Game!")
System_number = random.randint(1,100)
print("I'm thinking of a number between 1 and 100.")
Difficulty_Choice = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
attempts = difficulty(Difficulty_Choice.lower())
    
