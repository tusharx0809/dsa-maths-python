"""Below program is to check  if a number exists in sorted 2d-matrix using binary search"""

def search_matrix(matrix, target):
    if not matrix:
        return False
    
    m = len(matrix)
    n = len(matrix[0])

    l = 0
    r = m * n - 1

    while l <= r:
        mid = (l + r) // 2
        mid_val = matrix[mid // n][mid % n]

        if mid_val == target:
            return True
        elif mid_val < target:
            l = mid + 1
        else:
            r = mid - 1
    return False

matrix = [
          [1, 3, 5, 7],
          [10,11,16,20],
          [23,30,34,60]
        ]

print(search_matrix(matrix, 30)) # will return True
print(search_matrix(matrix, 2)) # will return False