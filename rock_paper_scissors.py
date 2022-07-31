import random


def main():
    user = input(
        "What's your choice? 'r' for rock, 'p' for paper and 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print("It's a tie")
    elif is_win(user, computer):
        print("You won!")

    print("You lost!")

    play_again = input("Do you want to play again? [Y/N] ").lower()

    if play_again == "y":
        print()
        main()
    elif play_again == "n":
        quit()
    else:
        print("Invalid input")

# return true if user wins


def is_win(player, opponent):
    # returns true if user wins
    # r > s, s> p, p> r
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p")\
            or (player == "p" and opponent == "r"):
        return True


main()
