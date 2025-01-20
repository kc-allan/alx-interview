#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise
    :param matrix: 2D matrix
    :return: None
    """
    left, right = 0, len(matrix) - 1  # 0, 3

    while left < right:  # 0,1,2,3 < 3
        for i in range(right - left):  # 0, 1, 2
            top, bottom = left, right

            top_left = matrix[top][left + i]

            # Move bottom left to top left
            matrix[top][left + i] = matrix[bottom - i][left]

            # Move bottom right to bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # Move top right to bottom right
            matrix[bottom][right - i] = matrix[top + i][right]

            # move temp to top right
            matrix[top + i][right] = top_left
        left += 1
        right -= 1
