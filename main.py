import cv2 as cv
print("sudoku")

cv.namedWindow('image', cv.WINDOW_NORMAL)  # creates GUI window named Image.
cv.waitKey(0)  # waits for any keyboard event. 0 means indefinitely


def displayIMG():
    # cv.imshow() image of sudoku board with program input answers into appropriate blank boxes
    pass


def solve():
    # solve sudoku board
    # solution can be find with backtracking - recursion
    displayIMG()
    pass


if cv.waitKey(0) == ord('f'):
    # Screen capture sudoku.com board
    # Crop image to only the board
    solve()
    print('f')

cv.destroyAllWindows()  # destroys the window we created
