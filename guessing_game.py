from random import randint
from IPython.display import clear_output

guessed = False
number = randint(0, 9)
guesses = 0
while not guessed:
    ans = input("Try to guess the number I am thinkin of: ")
    guesses += 1

    clear_output()
    if int(ans) == number:
        print("congratulations you have guessed it correctly")
        print(f'It took you {guesses} guesses!')
    elif int(ans) > number:
        print("Number is lower than what you guessed")
    elif int(ans) < number:
        print("number is greater than what you guessed")
