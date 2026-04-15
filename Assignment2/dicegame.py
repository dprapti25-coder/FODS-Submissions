'''Dice guessing game with random values between 1-6'''
import random

dice = random.randint(1, 6)

guess = int(input("Guess the dice value (1 to 6): "))

print("\nDice value was:", dice)

if guess == dice:
    print("😊 Correct guess! Well done!")
elif abs(guess - dice) == 1:
    print("😐 Close guess! You were off by 1.")
else:
    print("❌ Wrong guess! Try again.")