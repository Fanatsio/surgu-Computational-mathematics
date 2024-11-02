import numpy as np

def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        _ = int(file.readline().strip())
        A = []
        b = []
        
        for line in file:
            *row, bi = map(float, line.split())
            A.append(row)
            b.append(bi)
        
        A = np.array(A)
        b = np.array(b)
        
    return A, b

def gauss_determinant(A):
    n = A.shape[0]
    det = 1
    for i in range(n):
        max_row = i + np.argmax(np.abs(A[i:, i]))
        if i != max_row:
            A[[i, max_row]] = A[[max_row, i]]
            det *= -1

        if A[i, i] == 0:
            return 0

        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]

    for i in range(n):
        det *= A[i, i]
        
    return det

filename = 'matrix_data.txt'
A, b = read_matrix_from_file(filename)

print("Исходная матрица A:")
print(A)
print("\nВектор свободных членов b:")
print(b)

det = gauss_determinant(A.copy()) 

print("\nОпределитель матрицы A:", det)
