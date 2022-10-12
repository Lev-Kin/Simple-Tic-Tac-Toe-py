cell = list(input())

print('---------')
print('|', cell[0], cell[1], cell[2], '|')
print('|', cell[3], cell[4], cell[5], '|')
print('|', cell[6], cell[7], cell[8], '|')
print('---------')

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

game = False
result = ""
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
