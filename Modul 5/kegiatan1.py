A = [[2,1,-1],
     [1,1,1],
     [1,-2,1]]
B = [[1,6,0]]

def transpose(function):
    def wrapper(*args):
        return [[row[i] for row in function(*args)] for i in range(len(function(*args)[0]))]
    return wrapper

@transpose
def adjoint_3x3(matrix):
    cofactor = [[matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1], matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0], matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0]],
                [matrix[0][1]*matrix[2][2] - matrix[0][2]*matrix[2][1], matrix[0][0]*matrix[2][2] - matrix[0][2]*matrix[2][0], matrix[0][0]*matrix[2][1] - matrix[0][1]*matrix[2][0]],
                [matrix[0][1]*matrix[1][2] - matrix[0][2]*matrix[1][1], matrix[0][0]*matrix[1][2] - matrix[0][2]*matrix[1][0], matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]]]
    adjoint = []
    for i in range(len(cofactor)):
        adjoint.append([])
        for j in range(len(cofactor[i])):
            if (i+j)%2 == 0: adjoint[i].append(cofactor[i][j])
            else: adjoint[i].append(-cofactor[i][j])
    return adjoint

def det_3x3(matrix):
    return  matrix[0][0]*matrix[1][1]*matrix[2][2] + \
            matrix[0][1]*matrix[1][2]*matrix[2][0] + \
            matrix[0][2]*matrix[1][0]*matrix[2][1] - \
            matrix[0][2]*matrix[1][1]*matrix[2][0] - \
            matrix[0][1]*matrix[1][0]*matrix[2][2] - \
            matrix[0][0]*matrix[1][2]*matrix[2][1]
        
def inverse(amatrix):
    try:
        perkalian = [[1/det_3x3(amatrix)*adjoint_3x3(amatrix)[i][j] for j in range(len(adjoint_3x3(amatrix)[i]))] for i in range(len(adjoint_3x3(amatrix)))]
    except ZeroDivisionError:
        raise ValueError("Determinan matriks tidak boleh nol")
    return perkalian

def matrices_multiply(matrix_3x3, matrix_3x1):
    result = []
    for i in range(3):
        result.append(matrix_3x3[i][0]*matrix_3x1[0][0] + matrix_3x3[i][1]*matrix_3x1[0][1] + matrix_3x3[i][2]*matrix_3x1[0][2])
    return [result]

def result(function):
    def wrapper(*args):
        hasil = function(*args)
        x = hasil[0][0]
        y = hasil[0][1]
        z = hasil[0][2]
        return f"Nilai x, y, dan z masing - masing adalah {int(x)}, {int(y)} dan {int(z)}" 
    return wrapper

@result
def get_result(matrixA, matrixB):
    return matrices_multiply(inverse(matrixA), matrixB)

X = get_result(A, B)

print(X)