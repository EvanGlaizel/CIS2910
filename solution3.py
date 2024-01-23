import numpy as np
from PIL import Image

# Inputs:
#     img: m by n by 3 array of integers representing the color values of a photo
#     rGroups: integer representing the number of groups of red color values
#     gGroups: integer representing the number of groups of green color values
#     bGroups: integer representing the number of groups of blue color values
# constraints: 
#     1 <= rGroups, gGroups, bGroups <= 256
#     0 <= all integers in img <= 255
# Output: returns an array with the same dimensions as img, 
#         with its color values quantized according to the specified groups
def colorQuantize( img, rGroups, gGroups, bGroups ):
    red = 0
    green = 0
    blue = 0

    rDivisor = 0
    gDivisor = 0
    bDivisor = 0

    for m in range(len(img)):
        for n in range(len(img[m])):
            rDivisor = 256/rGroups

            for r in rGroups:
                if (n / rDivisor == r):
                    red = rDivisor * (r + 1) / 2

            for g in gGroups:
                if (n / gDivisor == g):
                    green = gDivisor * (g + 1) / 2

            for b in bGroups:
                if (n / bDivisor == b):
                    blue = bDivisor * (b + 1) / 2

            img[m][n] = [red, green, blue]

    return img

# Testing and starter code provided in main(): 
def main():
    # Change the path in .open() to the file that you want to read in
    img = Image.open('tests/3by3.png').convert('RGB')
    arr = np.array(img)
    outArr = colorQuantize( arr, 256, 256, 256 )
    
    # Change testing to be True to test against a specified file
    testing = False
    if testing:
        # Change the path in .open() to the file that you want to test against
        testImg = Image.open('tests/3by3_256_256_256.png').convert('RGB')
        testArr = np.array(testImg)
        for row in range(len(testArr)):
            for col in range(len(testArr[0])):
                if outArr[row][col][0] != testArr[row][col][0]:
                    print("red color mismatch at row: " + str(row) + " col: " + str(col))
                    return
                if outArr[row][col][1] != testArr[row][col][1]:
                    print("green color mismatch at row: " + str(row) + " col: " + str(col))
                    return
                if outArr[row][col][2] != testArr[row][col][2]:
                    print("blue color mismatch at row: " + str(row) + " col: " + str(col))
                    return

    # Set saveFile to save your image,
    # e.g. saveFile = "myIMG.png" would save the image as the file "myIMG.png" in the directory where this code runs
    saveFile = "img.png"
    if saveFile != "img.png":
        outIMG = Image.fromarray(outArr)
        outIMG.save(saveFile)
    return 0

if __name__ == '__main__':
    main()

##########################################
# DO NOT LEAVE ANY CODE OUTSIDE ROUTINES #
# IT CAN CAUSE THE AUTOGRADER TO CRASH   #
##########################################


