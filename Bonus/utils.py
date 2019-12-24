from Extract_ConstantesDES import *
from ConvAlphaBin import *

# Reduce a key with 64 bits to a new key with 56 bits
def convert_64bit_to_56bit_key(Key) :
    tmp = ' ' + Key
    newKey = ''
    for x in range(len(tmp)):
        if x % 8 != 0:
            newKey += tmp[x]

    return newKey

# Convert a binary string to a 64 bits binary string list
def cutBinText(txt) :
    index = (len(txt) // 64) + 1
    res = [''] * index
    tab = MatZero(index,64)
    count = 0

    for x in range(len(tab)):
        for y in range(len(tab[x])):
            if count < len(txt):
                tab[x][y] = txt[count]
                count += 1

    for x in range(len(tab)):
        for y in range(len(tab[x])):
            res[x] += str(tab[x][y])

    return res

# Function to permut elements in array with array keys
def permutation(mat1, mat2) :
    res = ''
    if type(mat2) != type(list()):
        mat2 = list(mat2)
    for x in (mat1):
        res += mat2[x]
    return res

# Function to cut the key in the middle and return two keys
def cutKey(key):
    res1, res2 = '', ""
    if type(key) != type(list()):
        key = list(key)
    for x in range(len(key)):
        if x < len(key)//2:
            res1 += key[x]
        else:
            res2 += key[x]
    return [res1, res2]

# Function to move the bits to the left
def leftShift(key):
    last = key[0]
    key = key[1:] + last
    return key

# Function to concatenate two keys and return one
def concatenate(key1,key2):
    key = key1 + key2
    return key

# Function to create the 16 keys for D.E.S encryption
def createKeys(key, constantes):
    k = dict()
    k[0] = convert_64bit_to_56bit_key(key)
    keyPermutation = permutation(constantes['CP_1'][0],key)
    cutingKey = cutKey(keyPermutation)
    for x in range(1,17):
        cutingKey[0] = leftShift(cutingKey[0])
        cutingKey[1] = leftShift(cutingKey[1])
        concatKey = concatenate(cutingKey[0],cutingKey[1])
        k[x] = permutation(constantes['CP_2'][0], concatKey)
    return k
