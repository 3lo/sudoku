import cv2 as cv
print("sudoku")

cv.namedWindow('image', cv.WINDOW_NORMAL)  # creates GUI window named Image.
cv.waitKey(0)  # waits for any keyboard event. 0 means indefinitely
# key f = 102
# cv.destroyAllWindows()  # destroys the window we created

# Goal: Snippet function to capture sudoku board
# Then solve sudoku board
# cv.imshow() image of sudoku board with program input answers into appropriate boxes

# sudoku solution has to deal with backtracking ?
