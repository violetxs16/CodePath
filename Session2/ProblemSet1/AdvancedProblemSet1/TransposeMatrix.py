#Write a function transpose() that accepts a 2D integer array matrix and returns the transpose of matrix. 
# The transpose of a matrix is the matrix flipped over its main diagonal, swapping the rows and columns.

#3x3 matrix before and after being transposed

def transpose(matrix1):
    matrix = matrix1.copy()
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            
            if row != col:
                print("in conditoin")
                temp = matrix[row][col]
                matrix[row][col] = matrix[row][col]
                matrix[row][col] = temp

    return matrix
        
#Example Usage

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))
    #[1, 4, 7],
   # [2, 5, 8],
   # [3, 6, 9]
#]
#Understand, we are dealing with a 2d array and returning the transpose of it. We swap the rows and columns to get the transpose
#       col 1 | col 2
#row 1     1    2       -> 1 3 
#row 3      3   4       -> 2 4

#plan: We use two for loops. The inner one access the cols while the outer access the rows. We will acess 1 2 3 first. 
#Outer[o] == row 1
#We keep col stationary so we get row[i][o] and swap with row[0][i]
#index = 0
#for row in range(len(matrix))
#   for col in range(len(row)):
#       temp = matrix[row][index]
#       matrix[row][index]   = matrix[index][col]
#       matrix[index][col] = temp