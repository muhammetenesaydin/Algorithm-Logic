"""
Kendisine parametre olarak gelen n  ile n*n lik spiral matrisi yazınız 

Örnek :
1 2 3
8 9 4
7 6 5

"""


def spiral_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    

    value = 1
    
    start_row, end_row = 0, n - 1
    start_col, end_col = 0, n - 1
    
    while start_row <= end_row and start_col <= end_col:
        
        for i in range(start_col, end_col + 1):
            matrix[start_row][i] = value
            value += 1
        start_row += 1
        
        
        for i in range(start_row, end_row + 1):
            matrix[i][end_col] = value
            value += 1
        end_col -= 1
        
        if start_row <= end_row:
            for i in range(end_col, start_col - 1, -1):
                matrix[end_row][i] = value
                value += 1
            end_row -= 1
        
        if start_col <= end_col:
            for i in range(end_row, start_row - 1, -1):
                matrix[i][start_col] = value
                value += 1
            start_col += 1
    
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

n = 3
spiral = spiral_matrix(n)
print_matrix(spiral)