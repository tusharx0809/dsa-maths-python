"""Below program is to find the transpose of a 2d-matrx"""
#Transpose of matrix where we switch all the diagonal elements, or we can say that rows and columns are interchanged

def transpose(matrix):
    transpose = [[0] * len(matrix) for _ in range(len(matrix[0]))] # create an empty matrix(all elements 0) equal to the size of matrix 
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            transpose[j][i] = matrix[i][j]
    return transpose

matrix = [               #result      #   [[1, 4, 7],  
          [1,2,3],                    #    [2, 5, 8],
          [4,5,6],                    #   [3, 6, 9]]
          [7,8,9]
    ]

print(transpose(matrix))
