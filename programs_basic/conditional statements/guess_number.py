'''this program is to implement a game to guess a number between 1-10'''
import random
guess=0
num = random.randint(1,10)
while guess != num:
    guess=int(input("Guess the number until you get it correct"))
print("your guess was correct")