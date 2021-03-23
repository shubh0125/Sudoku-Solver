board = [[3,4,1,0],
         [0,2,0,0],
         [0,0,2,0],
         [0,1,3,4], ]


def solve(b):
    find = find_empty(b)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 5):
        if valid(b, i, (row, col)):
            b[row][col] = i

            if solve(b):
                return True

            b[row][col] = 0

    return False


def valid(b, num, pos):
    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(b)):
        if b[i][pos[1]] == num and pos[0] != i:
            return False

    x0 = pos[1] // 2
    y0 = pos[0] // 2

    for i in range(y0 * 2, y0 * 2 + 1):
        for j in range(x0 * 2, x0 * 2 + 1):
            if b[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(b):
    for i in range(len(b)):
        if i % 2 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(b[0])):
            if j % 2 == 0 and j != 0:
                print(" | ", end="")

            if j == 3:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")


def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return i, j

    return None


print_board(board)
solve(board)
print("")
print("")
print_board(board)