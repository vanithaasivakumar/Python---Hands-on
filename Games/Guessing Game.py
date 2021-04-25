'''The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!'''

from random import randint
num=randint(1,100)
num_of_guesses=0
print('''The player has to guess a number between 1 and 100.
        The rules are:
        On a player's first turn, if their guess is within 10 of the number, return "WARM!"
        further than 10 away from the number, return "COLD!"
        On all subsequent turns, if a guess is closer to the number than the previous guess return "WARMER!"
        farther from the number than the previous guess, return "COLDER"''')
while TRUE:
    guess=input("Guess the number between 0 and 100: ")
    if guess not in range(0,101):
        print("OUT OF BOUNDS")
        num_of_guesses+=1
        continue
    elif guess in range(num-10,num+10)
        print("WARM")
    elif guess not in range(num-10,num+10)
        print("COLD")



