def print_board(cell):
    print('---------')
    print('|', cell[0], cell[1], cell[2], '|')
    print('|', cell[3], cell[4], cell[5], '|')
    print('|', cell[6], cell[7], cell[8], '|')
    print('---------')


def go_push(cell, symbol):
    coord_x, coord_y = input("Enter the coordinates:").split()
    if coord_x.isalpha() == True or coord_y.isalpha() == True:
        print("You should enter numbers!")
        go_push(cell, symbol)
    else:
        k = (int(coord_x) - 1) * 3 + int(coord_y) - 1

        if int(coord_x) > 3 or int(coord_y) > 3:
            print("Coordinates should be from 1 to 3!")
            go_push(cell, symbol)
        elif cell[k] == 'X' or cell[k] == 'O':
            print("This cell is occupied! Choose another one!")
            go_push(cell, symbol)
        else:
            cell[k] = symbol
            print_board(cell)
            return cell


def check(cell):
    def check_amount(cell):
        X = 0
        Y = 0
        for i in cell:
            if i == 'X':
                X += 1
            elif i == 'O':
                Y += 1
        return X, Y

    X, Y = check_amount(cell)
    if X > Y:
        go_push(cell, "O")
    else:
        go_push(cell, "X")

    x = 0
    y = 0
    if cell[0] == cell[1] == cell[2] == 'X' or \
            cell[3] == cell[4] == cell[5] == 'X' or cell[6] == cell[7] == cell[8] == 'X':
        x = 1
    elif cell[0] == cell[3] == cell[6] == 'X' or \
            cell[1] == cell[4] == cell[7] == 'X' or cell[2] == cell[5] == cell[8] == 'X':
        x = 1
    elif cell[0] == cell[4] == cell[8] == 'X' or cell[2] == cell[4] == cell[6] == 'X':
        x = 1

    if cell[0] == cell[1] == cell[2] == 'O' or \
            cell[3] == cell[4] == cell[5] == 'O' or cell[6] == cell[7] == cell[8] == 'O':
        y = 1
    elif cell[0] == cell[3] == cell[6] == 'O' or \
            cell[1] == cell[4] == cell[7] == 'O' or cell[2] == cell[5] == cell[8] == 'O':
        y = 1
    elif cell[0] == cell[4] == cell[8] == 'O' or cell[2] == cell[4] == cell[6] == 'O':
        y = 1

    X, Y = check_amount(cell)
    if x == 0 and y == 0 and X + Y == 9:
        print("Draw")
    elif x == 1 and y == 0:
        print("X wins")
    elif x == 0 and y == 1:
        print("O wins")
    else:
        check(cell)


cell = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
print_board(cell)
check(cell)
