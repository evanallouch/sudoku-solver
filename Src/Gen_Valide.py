import numpy as np

def valideL(A, i, k):
    return k not in A[i]

def valideC(A, j, k):
    return k not in A[:, j]

def valideB(A, i, j, k):
    row_start, col_start = (i // 3) * 3, (j // 3) * 3
    return k not in A[row_start:row_start+3, col_start:col_start+3]

def valide(A, i, j, k):
    return valideL(A, i, k) and valideC(A, j, k) and valideB(A, i, j, k)

def gen():
    nombres = list(range(1, 10))
    A = np.zeros((9, 9), dtype=int)
    def solver():
        for i in range(9):
            for j in range(9):
                if A[i][j] == 0:
                    np.random.shuffle(nombres)
                    for num in nombres:
                        if valide(A, i, j, num):
                            A[i][j] = num
                            if solver():
                                return True
                            A[i][j] = 0
                    return False
        return True

    solver()
    return A

sudoku_board = gen()
print(sudoku_board)
