import math
import random


# calculate a random number according to the formula log2(upper_bound - lower_bound + 1)
def num_of_guesses(upper_bound, lower_bound):
    return round(math.log(upper_bound - lower_bound + 1, 2))


# generate a random number a return it
def generate_a_random_number(start, end):
    random_number = random.randint(start, end)
    return random_number


def main():
    try:
        start = int(input("Enter starting number: "))

        # if starting number is less than 0 call the main function again to ask for user input "This is Recursion"
        if start < 0:
            main()
        try:
            end = int(input("Enter ending number: "))

            # if ending number is less than 1 call the main function again
            if end < 1:
                main()

            total_guesses = num_of_guesses(end, start)
            print(f"You have {total_guesses} guesses to try")

            random_number = generate_a_random_number(start, end)
            tries = 0

            while total_guesses >= 1:
                guess = int(input("Guess: "))

                if guess == random_number:
                    print("Congratulations u guessed right!")
                    if tries == 1:
                        print(f"You tried {tries} time")
                    else:
                        print(f"You tried {tries} times")
                    break

                elif guess > random_number:
                    print("Try Again! Your guess is too high")
                    total_guesses -= 1
                    tries += 1

                elif guess < random_number:
                    print("Try Again! Your guess is too low")
                    total_guesses -= 1
                    tries += 1

                else:
                    print("Your tries are over, Better Luck Next time!")

        except ValueError:
            print("Wrong data type!")
            main()
    except ValueError:
        print("Wrong data type!")
        main()


main()
