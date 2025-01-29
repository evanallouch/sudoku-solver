import numpy as np



def detectL(M,i,k) :
    for z in range (len(M)) :
        if M[i][z] == k :
            return False
    else :
        return True


def detectC(M,i,k) :
    for z in range (len(M)) :
        if M[z][i] == k :
            return False
    else :
        return True


def detectB(M,i,k) :










def gen() :
    nombres = np.random.shuffle([1,2,3,4,5,6,7,8,9])
    A = np.array([[0]*9 for i in range(9)])
    for i in range (len(A)) :
        for j in range(len(A)) :
            if A[i][j] == 0 :
                for elements in nombres :
                    if valide(A,i,j,elements) :
                        A[i][j] = elements
                        if gen() :
                            return True
                        A[i][j] = 0
                    return False
    return A


