import random
playing = True
number = str(random.randint(0,9))

print("I will generate a number from 0-9, try to guess it, one digit at a time.")
print("The game ends when you get 1 point")
while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
        print("You win the game")
        print("The number was", number)
        break
    else:
        print("Your guess is incorrect, please try again. \n")

