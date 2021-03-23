board = [[1, 0, 0, 2, 3, 4, 0, 0, 12, 0, 6, 0, 0, 0, 7, 0],
         [0, 0, 8, 0, 0, 0, 7, 0, 0, 3, 0, 0, 9, 10, 6, 11],
         [0, 12, 0, 0, 10, 0, 0, 1, 0, 13, 0, 11, 0, 0, 14, 0],
         [3, 0, 0, 15, 2, 0, 0, 14, 0, 0, 0, 9, 0, 0, 12, 0],
         [13, 0, 0, 0, 8, 0, 0, 10, 0, 12, 2, 0, 1, 15, 0, 0],
         [0, 11, 7, 6, 0, 0, 0, 16, 0, 0, 0, 15, 0, 0, 5, 13],
         [0, 0, 0, 10, 0, 5, 15, 0, 0, 4, 0, 8, 0, 0, 11, 0],
         [16, 0, 0, 5, 9, 12, 0, 0, 1, 0, 0, 0, 0, 0, 8, 0],
         [0, 2, 0, 0, 0, 0, 0, 13, 0, 0, 12, 5, 8, 0, 0, 3],
         [0, 13, 0, 0, 15, 0, 3, 0, 0, 14, 8, 0, 16, 0, 0, 0],
         [5, 8, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 13, 9, 15, 0],
         [0, 0, 12, 4, 0, 6, 16, 0, 13, 0, 0, 7, 0, 0, 0, 5],
         [0, 3, 0, 0, 12, 0, 0, 0, 6, 0, 0, 4, 11, 0, 0, 16],
         [0, 7, 0, 0, 16, 0, 5, 0, 14, 0, 0, 1, 0, 0, 2, 0],
         [11, 1, 15, 9, 0, 0, 13, 0, 0, 2, 0, 0, 0, 14, 0, 0],
         [0, 14, 0, 0, 0, 11, 0, 2, 0, 0, 13, 3, 5, 0, 0, 12]
         ]


def solve(b):
    find = find_empty(b)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 17):
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

    x0 = pos[1] // 4
    y0 = pos[0] // 4

    for i in range(y0 * 4, y0 * 4 + 4):
        for j in range(x0 * 4, x0 * 4 + 4):
            if b[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(b):
    for i in range(len(b)):
        if i % 4 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  ")

        for j in range(len(b[0])):
            if j % 4 == 0 and j != 0:
                print(" | ", end="")

            if j == 15:
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
