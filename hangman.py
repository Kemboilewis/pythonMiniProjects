from random import choice


# declaring variables
words = ["tree", "basket", 'chair', 'paper', 'python']
word = choice(words)
guessed, lives, game_over = [], 7, False

guesses = ['_'] * len(word)

while not game_over:
    hidden_word = "".join(guesses)
    print("Word to guess: {}".format(hidden_word))
    print("Lives: {}".format(lives))
    ans = input("Type quit or guess a letter: ").lower()

    if ans == 'quit':
        print("Thank you for playing")
        game_over = True
    elif ans in word:
        print("you guessed correctly")
        for i in range(len(word)):
            if word[i] == ans:
                guesses[i] = ans
                print(guesses)
    else:
        lives -= 1
        print("Incorrect, you lost a life")
        if lives <= 0:
            print("you lost all your lifes, you lost")
            game_over = True
