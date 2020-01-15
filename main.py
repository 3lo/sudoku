import cv2 as cv
print("sudoku")

cv.namedWindow('image', cv.WINDOW_NORMAL)  # creates GUI window named Image.
cv.waitKey(0)  # waits for any keyboard event. 0 means indefinitely


def displayIMG():
    # cv.imshow() image of sudoku board with program input answers into appropriate blank boxes
    pass


def solve():
    # solve sudoku board - can be found with backtracking - recursion
    # List of path - and List of numbers we visited but left to get rid of infinite loops
    displayIMG()
    pass


grid = [[0, 7, 0, 0, 0, 4, 1, 3, 0],
        [9, 4, 5, 6, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 7, 0, 0, 6],
        [0, 5, 0, 0, 3, 0, 0, 0, 4],
        [6, 9, 3, 0, 4, 0, 0, 0, 2],
        [4, 8, 2, 1, 0, 6, 0, 5, 7],
        [5, 0, 0, 3, 7, 0, 0, 6, 0],
        [0, 6, 0, 0, 0, 0, 0, 8, 1],
        [8, 0, 9, 5, 0, 0, 0, 7, 0]]

for i in range(9):  # printing grid
    print(grid[i])

if cv.waitKey(0) == ord('f'):
    # Screen capture sudoku.com board
    # Crop image to only the board
    solve()
    print('f')

cv.destroyAllWindows()  # destroys the window we created
