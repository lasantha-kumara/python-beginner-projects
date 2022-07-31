import random

words = ['cobweb', 'rough', 'narrow', 'red', 'substantial', 'sock', 'seemly', 'silly', 'outstanding', 'self',
         'thought', 'curve', 'history', 'fence', 'ground', 'pies', 'depressed', 'plot', 'decide', 'enchanted']


def main():
    name = input("Enter your name: ")
    print("Good Luck,", name)

    blanks = []

    random_word = random.choice(words)

    attempts = len(random_word) + 2

    # add '_' to to blanks list
    for letter in random_word:
        blanks.append("_")

    print("Guess the characters")

    # print blanks before starting
    for letter in blanks:
        print(letter)

    while attempts >= 1:
        character = input("Guess a character: ")

        # if input is not character ask again by skip all line below this
        if len(character) > 1:
            continue

        # if character in random word and the letter is already not in blanks then add it to fill the blanks
        letter_index = 0
        for letter in random_word:
            if letter == character and blanks[letter_index] == "_":
                blanks[letter_index] = character
                break
            letter_index += 1

        # print remaining blanks after filling a letter
        for letter in blanks:
            print(letter)

        # if all blanks are filled the end the game and print the below message
        if "_" not in blanks:
            print("You Won!")
            print("The word is:", random_word)
            return 0

        attempts -= 1

    if attempts == 0:
        print("Better Luck next time!")
        return 0


main()
