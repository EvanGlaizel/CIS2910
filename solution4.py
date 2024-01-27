# Inputs:
#     board: 8 by 8 array of strings representing a chessboard state
# constraints:
#     each string in the board is one of 'K','Q','N','B','R','-':
#           'K' => King
#           'Q' => Queen
#           'N' => Knight
#           'B' => Bishop
#           'R' => Rook
#           '-' => Empty square
# Output: returns the number of moves that can be taken from this board state

# Other things to note:
#       All the pieces follow the rules of movement that apply to a standard chess game
#       All the pieces are on the same team so do not worry about any other rules of chess 
#         beyond standard movement (no taking pieces, castling, checks, etc)
#       There may be multiples of any piece on the board, such as 7 Kings or 10 Knights
def countValidChessMoves( board ):
    moves = 0

    lastFound = 0

    for i in range(len(board)):
        for j in range(len(board[i])):

            if (board[i][j] == 'K'):
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if (k >= 0 and k < len(board) and l >= 0 and l < len(board[i])):
                            if (board[k][l] == '-'):
                                moves += 1
                
            elif (board[i][j] == 'Q'):

                for k in range(i - 1,-1,-1):
                    if (board[k][j] == '-'):
                        moves += 1
                    else:
                        break
                for k in range(i+1,len(board)):
                    if (board[k][j] == '-'):
                        moves += 1
                    else:
                        break
                for k in range(j - 1,-1,-1):
                    if (board[i][k] == '-'):
                        moves += 1
                    else:
                        break
                for k in range(j+1,len(board[i])):
                    if (board[i][k] == '-'):
                        moves += 1
                    else:
                       break

                for k in range(min(i,j) + 1):
                    if (board[i-k][j-k] == '-'):
                        moves += 1
                    elif (k != 0):
                        break
                for k in range(min(i,7-j) + 1):
                    if (board[i-k][j+k] == '-'):
                        moves += 1
                    elif (k != 0):
                        break
                for k in range(min(7 - i, j) + 1):
                    if (board[i+k][j-k] == '-'):
                        moves += 1
                    elif (k != 0):
                        break
                for k in range(min(7 - i, 7 - j) + 1):
                    if (board[i+k][j+k] == '-'):
                        moves += 1
                    elif (k != 0):
                        break

            elif (board[i][j] == 'N'): 
                for k in range(len(board)):
                    for l in range(len(board[i])):
                        if (abs(i - k) == 1 and abs(j - l) == 2 and board[k][l] == '-'):
                            moves += 1
                        elif (abs(i - k) == 2 and abs(j - l) == 1 and board[k][l] == '-'):
                            moves += 1

            elif (board[i][j] == 'B'):
                for k in range(min(i,j) + 1):
                    if (board[i-k][j-k] == '-'):
                        moves += 1
                    elif (k != 0):
                        break
                for k in range(min(i,7-j) + 1):
                    if (board[i-k][j+k] == '-'):
                        moves += 1
                    elif (k != 0):
                        break
                for k in range(min(7 - i, j) + 1):
                    if (board[i+k][j-k] == '-'):
                        moves += 1
                    elif (k != 0):
                        break
                for k in range(min(7 - i, 7 - j) + 1):
                    if (board[i+k][j+k] == '-'):
                        moves += 1
                    elif (k != 0):
                        break

            elif (board[i][j] == 'R'):
                for k in range(i - 1,-1,-1):
                    if (board[k][j] == '-'):
                        moves += 1
                    else:
                        break
                for k in range(i+1,len(board)):
                    if (board[k][j] == '-'):
                        moves += 1
                    else:
                        break
                for k in range(j - 1,-1,-1):
                    if (board[i][k] == '-'):
                        moves += 1
                    else:
                        break
                for k in range(j+1,len(board[i])):
                    if (board[i][k] == '-'):
                        moves += 1
                    else:
                       break
    return moves

# Testing code provided in main():
def main():
    # update this path with the path to your tests directory!
    testDir = "tests/"
    for i in range(1,9): #iterates over test files
        board=[]
        numMoves=0
        with open(f"{testDir}/board{i}.txt") as idFile:
            for idx, line in enumerate(idFile.readlines()):
                if idx == 8:
                    numMoves = int(line)
                    break
                row=[]
                for char in str(line).split()[0]:
                    row.append(char)
                board.append(row)
        print(board)
        calculatedMoves = countValidChessMoves(board)
        if numMoves == calculatedMoves:
            print("Passed")
        else:
            print(f"Failed, Expected: {numMoves}, Got: {calculatedMoves}")
    return 0

if __name__ == '__main__':
    main()