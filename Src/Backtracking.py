import numpy as np
from itertools import combinations

def is_valid(board, row, col, num):
    """
    Vérifie si l'ajout de `num` dans la cellule (row, col) est valide selon les règles du sudoku.
    """
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or board[row//3*3 + i//3][col//3*3 + i%3] == num:
            return False
    return True

def solve_sudoku(board):
    """
    Utilise l'algorithme de backtracking pour résoudre la grille de sudoku.
    """
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def find_empty(board):
    """
    Trouve une cellule vide (valeur 0) dans la grille de sudoku.
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def check_irreducible_set(board, irreducible_set):
    """
    Vérifie si un ensemble donné est un ensemble inévitable pour la grille de sudoku.
    """
    original_board = np.copy(board)
    for r, c in irreducible_set:
        if board[r][c] == 0:
            return False
    for r, c in irreducible_set:
        board[r][c] = 0
    unique_solution = solve_sudoku(board)
    board = np.copy(original_board)
    return unique_solution

def find_irreducible_sets(board, size):
    """
    Trouve des ensembles inévitables de la taille spécifiée dans la grille de sudoku.
    """
    filled_positions = [(r, c) for r in range(9) for c in range(9) if board[r][c] != 0]
    for comb in combinations(filled_positions, size):
        if check_irreducible_set(board, comb):
            return comb
    return None


# Trouver des ensembles inévitables de taille 2 par exemple
size = 2
irreducible_set = find_irreducible_sets(sudoku_board, size)

print("Ensemble inévitable trouvé:", irreducible_set)

