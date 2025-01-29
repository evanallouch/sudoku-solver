def candidats_lignes(sudoku, i):
    L_dans = []
    L_candidats = []
    for j in range(9):
        if sudoku[i][j] != 0:
            L_dans.append(sudoku[i][j])
    for k in range(1, 10):
        if k not in L_dans:
            L_candidats.append(k)
    return L_candidats


def candidats_colonnes(sudoku, j):
    L_dans = []
    L_candidats = []
    for i in range(9):
        if sudoku[i][j] != 0:
            L_dans.append(sudoku[i][j])
    for k in range(1, 10):
        if k not in L_dans:
            L_candidats.append(k)
    return L_candidats


def candidats_blocs(sudoku, i, j):
    L_dans = []
    L_candidats = []
    bloc_i = i // 3
    bloc_j = j // 3
    for x in range(bloc_i * 3, (bloc_i * 3) + 3):
        for y in range(bloc_j * 3, (bloc_j * 3) + 3):
            if sudoku[x][y] != 0:
                L_dans.append(sudoku[x][y])
    for k in range(1, 10):
        if k not in L_dans:
            L_candidats.append(k)
    return L_candidats


def candidats(sudoku, i, j):
    L1 = candidats_lignes(sudoku, i)
    L2 = candidats_colonnes(sudoku, j)
    L3 = candidats_blocs(sudoku, i, j)
    L4 = []
    if sudoku [i][j] == 0 :
        for k in range(1, 10):
            if k in L1 and k in L2 and k in L3:
                L4.append(k)
        return L4
    else :
        return []



def paires_isolées_lignes (sudoku,i) :
    occurence = [0]*10
    for j in range(9) :
        if sudoku[i][j] != 0 :
            occurence [sudoku[i][j]] +=1
        else :
            L = candidats(sudoku,i,j)
            for elements in L :
                occurence[elements] +=1
    for n in range (len(occurence)) :
        if occurence(n) >= 2 :
            case_vide = []
            for j in range (9) :
                if sudoku[i][j] == 0 and n in candidats(sudoku,i,j) :
                    case_vide.append(n)


L = [[4,0,0,0,0,0,0,0,5],[0,3,2,0,4,5,9,1,0],[0,0,5,0,7,0,6,0,0],[0,0,0,5,1,9,0,0,0],
    [0,0,7,2,6,4,8,0,0],[2,0,0,0,8,0,0,0,0],[0,0,9,0,0,0,7,0,0],[0,4,6,0,0,0,1,8,0],
    [0,0,0,0,3,0,0,0,0]]
