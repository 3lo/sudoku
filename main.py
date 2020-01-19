import numpy as np
import cv2 as cv
from PIL import ImageGrab
import pytesseract
print("sudoku")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
cv.namedWindow('image', cv.WINDOW_NORMAL)  # creates GUI window named Image.
cv.waitKey(0)  # waits for any keyboard event. 0 means indefinitely


def displayIMG():
    # cv.imshow()  # image of sudoku board with program input answers into appropriate blank boxes
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


def grabImg():
    img = ImageGrab.grab(bbox=(362, 240, 862, 740))  # captures screen - bbox captures portion [x, y, width, height]
    img_np = np.array(img)  # converting img to array format so cv can read
    frame = cv.cvtColor(img_np, cv.COLOR_BGR2GRAY)  # greyscale
    cv.imshow("frame", frame)
    cv.waitKey(0)
    cv.destroyAllWindows()
    print(pytesseract.image_to_string(img))  # Returns the result of a Tesseract OCR run on the image to string


if cv.waitKey(0) == ord('f'):
    grabImg()  # function screen captures sudoku.com and is cropped in on the sudoku board
    solve()

cv.destroyAllWindows()  # destroys the window we created
