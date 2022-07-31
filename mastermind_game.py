import random

# get to numbers and compare digits in it. and return correct amount if digits


def count_correct_digits(random_number, guess):
    correct_digits = 0

    for num1, num2 in zip(str(random_number), str(guess)):
        if num1 == num2:
            correct_digits += 1
        else:
            pass

    return correct_digits

# get to numbers and compare digits in it. and print correct amount if digits


def print_correct_digits(random_number, guess):

    for num1, num2 in zip(str(random_number), str(guess)):
        if num1 == num2:
            print(num1, end=" ")
        else:
            print("_", end=" ")


def main():
    random_number = random.randint(1000, 10000)
    print(random_number)

    tries = 1

    on = True
    while on:
        if tries == 1:
            try:
                guess1 = int(input("Guess the 4 digit number: "))

                if random_number == guess1:
                    print(
                        "Great! You guessed the number in just 1 try! You're a Mastermind!")
                    return

                else:
                    correct_digits = count_correct_digits(
                        random_number, guess1)
                    print(
                        f"Not quite the number. But you did get {correct_digits} digit(s) correct!")
                    print("Also these numbers in your input were correct.")
                    print_correct_digits(random_number, guess1)
                    print("\n")

            except ValueError:
                print("Invalid input.")
                continue

        else:
            try:
                guess2 = int(input("Enter your next choice of numbers: "))

                if random_number == guess2:
                    print("You've become a Mastermind.")
                    print(f"It took you only {tries} tries.")
                    return

                else:
                    correct_digits = count_correct_digits(
                        random_number, guess2)
                    print(
                        f"Not quite the number. But you did get {correct_digits} digit(s) correct!")
                    print("Also these numbers in your input were correct.")
                    print_correct_digits(random_number, guess2)
                    print("\n")

            except ValueError:
                print("Invalid input.")
                continue

        tries += 1


main()
