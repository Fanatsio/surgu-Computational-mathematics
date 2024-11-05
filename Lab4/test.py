import numpy as np
from typing import Tuple, Union

def read_matrix_from_file(filename: str) -> Union[Tuple[np.ndarray, int], None]:
    try:
        with open(filename, 'r') as file:
            n = int(file.readline().strip())
            A = [list(map(float, line.split()[:-1])) for line in file]
        return np.array(A), n
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
    except ValueError:
        print("Ошибка: файл содержит некорректные данные.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    return None

def to_upper_triangular(A: np.ndarray, n: int) -> Tuple[np.ndarray, int, bool]:
    swap_count = 0
    
    for i in range(n):
        max_row = i + np.argmax(np.abs(A[i:, i]))
        if i != max_row:
            A[[i, max_row]] = A[[max_row, i]]
            swap_count += 1
            print(f"Перестановка строк {i + 1} и {max_row + 1}:\n{A}\n")
        
        if np.isclose(A[i, i], 0):
            print("Элемент на главной диагонали равен 0, матрица вырожденная.")
            return A, swap_count, True

        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            print(f"Обнуление элемента в строке {j + 1}, столбце {i + 1}:\n{A}\n")

    return A, swap_count, False

def gauss_determinant(A: np.ndarray, n: int) -> float:
    A, swap_count, singular = to_upper_triangular(A, n)

    if singular:
        return 0.0

    det = (-1) ** swap_count * np.prod(np.diag(A))
    print("Матрица после приведения к треугольному виду:\n", A, "\n")
    return det

filename = 'matrix_data.txt'
matrix_data = read_matrix_from_file(filename)

if matrix_data:
    A, n = matrix_data
    print("Исходная матрица A:\n", A)
    det = gauss_determinant(A.copy(), n)
    print("\nОпределитель матрицы A:", det)
