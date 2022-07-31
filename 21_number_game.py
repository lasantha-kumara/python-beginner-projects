import random

input_numbers = []


def player_move():
    try:
        numbers = int(input("How many number do you wish to enter? "))

        # if input_numbers size is not 0 then check if remaining numbers user going to add is equal to or greater then 21.
        # if it is then print message and quit
        if len(input_numbers) != 0:
            if input_numbers[-1] + numbers >= 21:
                print("You lose, Try again")
                quit()

        # get last number from input_numbers if there is none assign 0 as last_number
        if len(input_numbers) == 0:
            last_number = 0
        else:
            last_number = input_numbers[-1]

        # ask x number of numbers from user
        for i in range(numbers):
            new_number = last_number + 1
            n = int(input("> "))

            # add it to input_numbers if it is in order else show message and quit
            if n == new_number:
                input_numbers.append(n)
            else:
                print("You are disqualified")
                quit()

            last_number += 1

    except ValueError:
        print("Invalid input")
        player_move()


def computer_move():
    random_range = random.randint(1, 5)

    # if input_numbers size is not 0 then check if remaining numbers user going to add is equal to or greater then 21.
    # if it is then print message and quit
    if len(input_numbers) != 0:
        if input_numbers[-1] + random_range >= 21:
            print("You Won, Congratulations!")
            quit()

    # get last number from input_numbers if there is none assign 0 as last_numbers
    if len(input_numbers) == 0:
        last_number = 0
    else:
        last_number = input_numbers[-1]

    # get a radom amount of range and put numbers to input_numbers in order
    for i in range(random_range):
        new_number = last_number + 1

        input_numbers.append(new_number)

        last_number += 1


def main():
    print("Player 2 is computer")

    print("Do you want to start the game? (Yes/No)")
    start = input("> ").lower()

    if start == "yes" or "y":
        print("Enter 'F' to take the first chance.")
        print("Enter 'S' to take the second chance.")
        chance = input("> ").lower()
        # if user choose to play first
        if chance == "f":
            player_move()
            computer_move()
        # if user choose to play second
        elif chance == "s":
            computer_move()
        else:
            print("Wrong input.")
            quit()

        on = True
        # while user or computer meet 21 this is going to run
        while on:
            print("Order of inputs after computer's turn is: ")
            print(input_numbers, "\n")
            print("Your turn.\n")

            player_move()
            computer_move()

    elif start == "no" or "n":
        quit()
    else:
        print("Wrong input.")


main()
