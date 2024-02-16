
# takes in nAggressive, nPassive >= 0
# returns the number of possible arrangements of dogs
# Examples:
# |  Input  |  Output  |
# |---------|----------|
# |   0,0   |     1    |
# |---------|----------|
# |   1,1   |     2    |
# |---------|----------|
# |   0,2   |     0    |
# |---------|----------|
# |   2,2   |    12    |
# |---------|----------|
def dogArrangements( nPassive, nAggressive ): # The agressives split passives up into groups. Each group must have at least one passive
    totalFact = 1
    kFact = 1
    nFact = 1

    for i in range(1, nPassive + nAggressive + 1):
        totalFact *= i

    for i in range(1, nPassive + 1):
        kFact *= i

    for i in range(1, nAggressive + 1):
        nFact *= i        
        
    print(totalFact, kFact, nFact)
    return totalFact // (kFact * nFact)

# Testing code provided in main():
def main():
    testArgs = [[0,0,1],[1,1,2],[0,2,0],[2,2,12]]
    for arg in testArgs:
        passive, aggressive, answer = arg
        result = dogArrangements(passive,aggressive)
        if result != answer:
            print(f"Failed dogArrangements test with args nPassive={passive} nAggressive={aggressive}.\nExpected: {answer}, Got: {result}")
        else:
            print(f"Passed dogArrangements test with args nPassive={passive} nAggressive={aggressive}.")
    return 0

if __name__ == '__main__':
    main()
