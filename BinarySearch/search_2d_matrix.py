"""
I was so excruciatingly close, but ultimately couldn't think of the
if statements for the first binary search. I'll still give it to myself,
but man it was close.
"""

def searchMatrix(matrix: list, target: int) -> bool:
    left, right = 0, len(matrix) - 1
    target_not_found = True

    while left <= right and target_not_found:
        midpoint = (left + right) // 2

        if target > matrix[midpoint][-1]:
            left = midpoint + 1

        elif target < matrix[midpoint][0]:
            right = midpoint - 1

        else:
            target_row = midpoint
            target_not_found = False

    if target_not_found:
        return False

    left, right = 0, len(matrix[0]) - 1

    while left <= right:
        midpoint = (left + right) // 2

        if matrix[target_row][midpoint] < target:
            left = midpoint + 1

        elif matrix[target_row][midpoint] > target:
            right = midpoint - 1

        else:
            return True

    return False