import random

fruits = ['Apples', 'Jambolan', 'Grapefruit', 'Kumquat', 'Huckleberry', 'Loquat', 'Oranges', 'Grapes', 'Guava',
          'Raspberries', 'Mango', 'Imbe', 'Rambutan', 'Clementine', 'Olive', 'Tamarind', 'Quince', 'Farkleberry', 'Cantaloupe', 'Kiwi', 'Wolfberry', 'Boysenberries', 'Persimmon', 'Voavanga', 'Watermelon', 'Hackberry',
          'Blueberries', 'Bananas', 'Cucumbers', 'Jackfruit', 'Cherries', 'Dates', 'Evergreen', 'Tomato', 'Avocados',
          'Strawberries', 'Longan']


def main():
    print("Guess the word! HINT: Word is a name of  a fruit")

    random_fruit = random.choice(fruits).lower()

    attempts = len(random_fruit) + 2

    blanks = []

    # add "_" to blanks list to replace letters in random_fruit
    for letter in random_fruit:
        blanks.append("_")

    # keep asking for a character from the user until attempts run out
    while attempts >= 1:
        character = input("Enter a letter to guess: ")

        if len(character) > 1:
            continue

        # if character in random_fruit and the blanks[index] is "_". then fill the blank with the character
        letter_index = 0
        if character in random_fruit:
            for letter in random_fruit:
                if letter == character and blanks[letter_index] == "_":
                    blanks[letter_index] = character
                    break
                letter_index += 1

        # print the word with filled blanks
        for letter in blanks:
            print(letter, end=" ")
        print()

        # if all blanks are filled then break the loop and print "winner" message
        if "_" not in blanks:
            print("Congratulations, You won!")
            break

        attempts -= 1

    if attempts == 0:
        print("Your attempts are over. Try again")


main()
