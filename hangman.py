from random import choice
from string import ascii_lowercase

print("H A N G M A N")

def hangman_game():
    words = ["python", "java", "kotlin", "javascript"]
    secret_word = choice(words)
    secret_word_char = list(secret_word)

    displayed_letters = list(len(secret_word) * "-")
    user_letters = []
    lives = 8

    while lives > 0:
        print("")
        print("".join(displayed_letters))
        user_letter = input("Input a letter: > ")
        if len(user_letter) == 1:
            if user_letter in ascii_lowercase:
                if user_letter in secret_word and user_letter not in displayed_letters:
                    position = 0
                    for char in secret_word:
                        if char == user_letter:
                            displayed_letters[position] = user_letter
                        position += 1
                elif user_letter in user_letters:
                    print("You already typed this letter")
                else:
                    print("No such letter in the word")
                    lives -= 1
                if "-" not in displayed_letters:
                    print("You guessed the word!")
                    print("You survived!\n")
                    break
                user_letters.append(user_letter)
            else:
                print("It is not an ASCII lowercase letter")
        else:
            print("You should input a single letter")
    else:
        print("You are hanged!\n")

while True:
    menu_selection = input("Type \"play\" to play the game, \"exit\" to quit: ")
    if menu_selection == "play":
        hangman_game()
    if menu_selection == "exit":
        exit()