from Extract_ConstantesDES import *
from ConvAlphaBin import *

def convert_64bit_to_56bit_key(Key) :
    tmp = ' ' + Key
    newKey = ''
    for x in range(len(tmp)):
        if x % 8 != 0:
            newKey += tmp[x]

    return newKey

def cutBinText(txt) :
    index = (len(txt) // 64) + 1
    tab = MatZero(index,64)
    count = 0
    for x in range(len(tab)):
        for y in range(len(tab[x])):
            if count < len(txt):
                tab[x][y] = txt[count]
                count += 1

    return tab

def aligneMat(mat) :
    txt = ''
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            txt += str(mat[x][y])
    return txt

def swap(c, i, j):
    c = list(c)
    c[i], c[j] = c[j], c[i]
    return ''.join(c)

# TODO search how make the permutation
def permutation(mat1, mat2) :
    for x in range(len(mat1)):
        position = mat1[x] % (len(mat2) - 1)
        print(f'permut {mat2[position]} with {mat2[x]} old position: {position} new position: {x}')
        mat2 = swap(mat2, position, x)
    return mat2
