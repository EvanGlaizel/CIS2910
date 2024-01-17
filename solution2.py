##########################################
# DO NOT LEAVE ANY CODE OUTSIDE ROUTINES #
# IT CAN CAUSE THE AUTOGRADER TO CRASH   #
##########################################

# function getBinaryStrings
# Input n: integer
# constraints: n > 0
# Output: returns a list of binary numbers of length n, in numerical order
#         represent each binary number as a list of n 1s and 0s
#         ex:
#            101 would be [1, 0, 1]
#            0001 would be [0, 0, 0, 1]

# Examples:
# |---------|----------------------------------------------------------|
# |  Input  |                         Output                           |
# |---------|----------------------------------------------------------|
# |    1    | [[0], [1]]                                               |
# |---------|----------------------------------------------------------|
# |    2    | [[0, 0], [0, 1], [1, 0], [1, 1]]                         |
# |---------|----------------------------------------------------------|
# |    4    | [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], |
# |         |  [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], |
# |         |  [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], | 
# |         |  [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]] |
# |---------|----------------------------------------------------------|
def getBinaryStrings( n ):
    outList = []

    for x in n * n:
        print("A")
    
    # Hint: you may want to write additional helper routines
    return outList

##########################################
# DO NOT LEAVE ANY CODE OUTSIDE ROUTINES #
# IT CAN CAUSE THE AUTOGRADER TO CRASH   #
##########################################
