import random
import sys
sys.path.append('C:/Users/allou/Desktop/Travail/prépa/2ème année/TIPE')
from Backtracking import Backtracking


def creation_sudoku():
    sudoku = [[0]*9 for a in range(9)]
    cases_devoilees = random.randint(17, 35)
    k = 0
    while k < cases_devoilees:
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        if sudoku[i][j] == 0:
            sudoku[i][j] = random.randint(1, 9)
            k += 1
    if Backtracking.solution_sudoku(sudoku) :
        return Backtracking.solution_sudoku1(sudoku)
    else :
        return creation_sudoku()

