def printBoard(board):

    for row in range(0,4):
        for col in range(0,4):
            if board[row][col] == 0:
                print(" _ ", end="")
            if board[row][col] != 0:
                print(" %s " % board[row][col], end="")
        print("")
    print("")

def isLegal(board, poss_row, poss_col):
    if board[poss_row][poss_col] != 0:
        return False

    for square in board[poss_row]: # search row to see if rook already in row, return False if there is
        if square == "R":
            return False

    return True


def place_rook(board, col):
    if col == 4:
        printBoard(board)
        return 1
    count = 0
    for row in range(len(board)):
        if isLegal(board, row, col):
            board[row][col] = "R"
            count += place_rook(board, col+1) # only adds if rook is sucessfully placed
            board[row][col] = 0
    return count

board = [ [0, "X", 0, 0],
    [0, 0, 0, "X"],
    ["X", 0, 0, 0],
    [0, 0, "X", 0]]


place_rook(board, 0)