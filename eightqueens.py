import random

# FUNCTIONS

# print the board nicely
def printBoard(board):

    for row in range(0,8):
        for col in range(0,8):
            if board[row][col] == 0:
                print(" _ ", end="")
            if board[row][col] != 0:
                print(" %d " % board[row][col], end="")
        print("")
    print("")
    

# return True if this space is legal
def isLegal (board, possRow, possCol):

    # check this row
    for counter in range(0,8):
        if board[possRow][counter] >= 1:
            return False
                    
    # check this column
    for counter in range(0,8):
        if board[counter][possCol] >= 1:
            return False

    # check the diagonals from here, up left
    colCounter = possCol
    for rowCounter in range(possRow, 0, -1):
        if colCounter-1 >= 0:
            if board[rowCounter-1][colCounter-1] >= 1:
                return False
        colCounter = colCounter - 1
        
    # check the diagonal from here, up right
    colCounter = possCol
    for rowCounter in range(possRow, 0, -1):
        if colCounter+1 <= 7:
            if board[rowCounter-1][colCounter+1] >= 1:
                return False
        colCounter = colCounter + 1

    # check the diagonal from here, down left
    colCounter = possCol
    for rowCounter in range(possRow, 7):
        if colCounter-1 >= 0:
            if board[rowCounter+1][colCounter-1] >= 1:
                return False
        colCounter = colCounter-1
    
    # check the diagonal from here, down right
    colCounter = possCol
    for rowCounter in range(possRow, 7):
        if colCounter+1 <= 7:
            if board[rowCounter+1][colCounter+1] >= 1:
                return False
        colCounter = colCounter+1

    return True


def playRandomly (board):
# randomly place eight queens, and evaluate the board

    queensPlaced = 0
    success = True
    
    while queensPlaced < 8:

        randomCol = random.randint(0,7)
        randomRow = random.randint(0,7)

        if board[randomRow][randomCol] == 0:
            # found an empty space

            # test to see if placing a queen here causes a conflict
            if not isLegal(board, randomRow, randomCol):
                success = False

            # place the queen
            queensPlaced = queensPlaced + 1
            board[randomRow][randomCol] = queensPlaced
                
    printBoard(board)
    
    if success == True:
        print ("By sheer luck, I found a winning board!")
    else:
        print ("My random placement did not work out.")

    return


# main program






def placeQueen(board, col):
    # Use backtracking to find all 92 possible solutions to the eight queens game
    if col == 8:
        printBoard(board)
        return 1
    count = 0
    for row in range(8): # try each possible row 
        if isLegal(board, row, col):
            board[row][col] = col+1 # place the queen
            count += placeQueen(board, col+1) # now attempt to solve the next column, if succesful, adds one to count, if not count stays at 0
            board[row][col] = 0 # remove queen and try next row
    return count



                    






board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]

solutions = placeQueen(board, 0)
print(solutions)