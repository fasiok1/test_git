def determinant(matrix):

    i = len(matrix)
    j = len(matrix[0])

    if i != j: return 'Введите матрицу квадратного вида'
    
    elif i == 1 and j == 1: return matrix[0][0]

    elif i == 2 and j == 2 : 
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        su_m = 0
        for i_1 in range(i):
            minor = []
            for x in range(i):
                ad = []
                for y in range(i):
                    if x != 0 and y != i_1:
                        ad += [matrix[x][y]]
                if ad != []:
                    minor += [ad]
            su_m += matrix[0][i_1]*determinant(minor)*(-1)**i_1
        return su_m

matrix = [
    [1,2,5,8,555],
    [3,4,6,1,232],
    [7,8,9,6,88],
    [3,-3,6,4,7],
    [3,5,2,5,42]
]

print(determinant(matrix))