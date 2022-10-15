import re


def print_board(cell):
    print('---------')
    print('|', cell[0][0], cell[0][1], cell[0][2], '|')
    print('|', cell[1][0], cell[1][1], cell[1][2], '|')
    print('|', cell[2][0], cell[2][1], cell[2][2], '|')
    print('---------')


def check_game_board(cell):
    amount_X = cell.count("X")
    amount_O = cell.count("O")
    board_is_full = amount_X + amount_O == 9

    winning_combinations = \
        [[cell[0], cell[1], cell[2]], [cell[3], cell[4], cell[5]],
         [cell[6], cell[7], cell[8]], [cell[0], cell[4], cell[8]],
         [cell[2], cell[4], cell[6]], [cell[2], cell[5], cell[8]],
         [cell[1], cell[4], cell[7]], [cell[0], cell[3], cell[6]]]

    wins_X = len([cell for cell in winning_combinations if cell.count("X") == 3])
    wins_O = len([cell for cell in winning_combinations if cell.count("O") == 3])

    if wins_X and wins_O or max(amount_X, amount_O) - min(amount_X, amount_O) >= 2:
        game = False
    else:
        game = True

    if game:
        if not wins_X and not wins_O and board_is_full:
            result = "Draw"
        elif wins_X:
            result = "X wins"
        elif wins_O:
            result = "O wins"
        else:
            result = "Game not finished"
    else:
        result = "Impossible"

    print(result)


def go_push(push, cell, symbol):
    if not re.search(r'\d\s\d', push):
        print("You should enter numbers!")
        return True

    x = int(push[0])
    y = int(push[2])
    if x > 3 or x < 1 or y > 3 or y < 1:
        print("Coordinates should be from 1 to 3!")
        return True

    i = x - 1
    j = y - 1
    if cell[i][j] in ["X", "O"]:
        print("This cell is occupied! Choose another one!")
        return True

    cell[i][j] = symbol

    return False


initial_cell = input("Enter cells: ").replace("_", " ")
cell = [
    [initial_cell[0], initial_cell[1], initial_cell[2]],
    [initial_cell[3], initial_cell[4], initial_cell[5]],
    [initial_cell[6], initial_cell[7], initial_cell[8]]
]
print_board(cell)

play_game = True
while play_game:
    enter_coord = input("Enter the coordinates: ")
    play_game = go_push(enter_coord, cell, "X")
print_board(cell)
