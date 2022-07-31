# add 2 names to 2 different letters and remove common letter and return remaining letters
def remove_common_letters(name1, name2):
    name1_letters = []
    name2_letters = []

    for x in name1:
        name1_letters.append(x)

    for y in name2:
        name2_letters.append(y)

    for letter in name1_letters[:]:
        if letter in name2_letters:
            name1_letters.remove(letter)
            name2_letters.remove(letter)

    remaining_letters = name1_letters + name2_letters

    return remaining_letters


def main():
    name1 = input("Player1 name: ")
    name2 = input("Player2 name: ")

    remaining_letters = remove_common_letters(name1, name2)

    letter_count = len(remaining_letters)

    relationship = ['Friends', 'Lovers', 'Admirers',
                    'Marriage', 'Enemies', 'Secret Lovers']
    on = True
    n = 1

    # loop through relationship list while n == letter count
    while on:
        for i in relationship:
            current_relationship = i

            if n == letter_count:
                on = False
                break

            n += 1

    # when n == letter count print relationship
    print("Relationship status :", current_relationship)


main()
