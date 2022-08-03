import random


def print_moves():
    print("""
Commands are as follows :
'W' or 'w' : Move Up
'S' or 's' : Move Down
'A' or 'a' : Move Left
'D' or 'd' : Move Right
""")


def print_grid(grid):
    for i in grid:
        for j in i:
            print(j, end=" ")
        print()


def generate_random_cell(grid):
    random_row = random.randint(0, 3)
    random_column = random.randint(0, 3)
    if grid[random_row][random_column] != 0:
        generate_random_cell()
    else:
        grid[random_row][random_column] = 2


def move(direction, grid):
    if direction == 'w':
        # TODO
        pass
    elif direction == 's':
        # TODO
        pass
    elif direction == 'a':
        # TODO
        pass
    elif direction == 'd':
        # TODO
        pass
    else:
        print("Wrong input.")


def main():
    grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    print_moves()

    generate_random_cell(grid)
    print_grid(grid)
    print()

    on = True
    while on:
        direction = input("Press the command : ").lower()
        move(direction, grid)
        print_grid(grid)
        print()


main()
