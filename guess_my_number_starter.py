import random


def guess():
    
    secret = random.randrange(1, 99)

    guess_number = input("I am thinking of a number between 1 and 20, enter any number to play: ")
    
    if guess_number.isdigit():
        print("Let's play")
        guess_number = int(guess_number)
    else:
        print("Invalid input! learn to follow instructions haha")
        
    guess_number = int(input("Guess the secret number: "))
    for i in range(1, 7):
        print("Try", i)
        if guess_number < secret:
            print("Oops try again too low")
            guess_number = int(input("Guess the secret number again: "))
        elif guess_number > secret:
            print("Ahh, your guess was too high")
            guess_number = int(input("Guess the secret number again: "))
        else:
            break
    if guess_number == secret:
        print("Yay, Congrats! you got the guess", guess_number, "right")
    else:
        print("You have exhausted your chances.")

    retry = input("If you want to take it again, enter Y/N: ")
    
    if retry == "y" or retry == "Y":
        guess()
    elif retry == "n" or retry == "N":
        print("Game over, honour your pillow's appointment!! have a good night haha")
    else:
        print("Invalid input, try to follow instructions! \n")
        retry = input("If you'd want to take it again, enter Y/N: ")
        if retry == "y" or retry == "Y":
            guess()
        elif retry == "n" or retry == "N":
            print("Game over, honour your pillow's appointment!! have a good night haha ")
    
    
guess()
