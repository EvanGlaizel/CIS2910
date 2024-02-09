
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
def dogArrangements( nPassive, nAggressive ):
    nFact = 1
    kFact = 1

    for i in range(1, nPassive + nAggressive + 1):
        nFact *= i

    for i in range(1, nAggressive + 1):
        kFact *= i
        
    print(nFact, kFact)
    return nFact // kFact

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
