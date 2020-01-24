from Extract_ConstantesDES import *
from ConvAlphaBin import *

# Reduce a key with 64 bits to a new key with 56 bits
def convert_64bit_to_56bit_key(Key) :
    tmp = ' ' + Key
    newKey = ''
    count = 0
    for x in range(len(tmp)):
        if x % 8 != 0:
            newKey += tmp[x]
            if tmp[x] == '1':
                count += 1
        elif x % 8 == 0 and x != 0:
            if tmp[x] == '1':
                count += 1
            if count % 2 == 0:
                return "error"
            count = 0
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
    res1, res2 = "", ""
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

# Function to move the bits to the right
def rightShift(key):
    first = key[-1]
    key = first + key[:-1]
    return key

# Function to concatenate two keys and return one
def concatenate(key1,key2):
    key = key1 + key2
    return key

# Function to create the 16 keys for D.E.S encryption
def createKeys(key, constantes):
    k = dict()
    k[0] = convert_64bit_to_56bit_key(key)
    if k[0] == "error":
        return "error"

    keyPermutation = permutation(constantes['CP_1'][0],key)
    cutingKey = cutKey(keyPermutation)
    for x in range(1,17):
        cutingKey[0] = leftShift(cutingKey[0])
        cutingKey[1] = leftShift(cutingKey[1])
        concatKey = concatenate(cutingKey[0],cutingKey[1])
        k[x] = permutation(constantes['CP_2'][0], concatKey)
    return k

def permuteText(bintxt, constantes):
    m = permutation(constantes['PI'][0], bintxt)
    return m

def ronde(k,m,constantes):
    res = ''
    resTmp = dict()
    resCal = []
    EDK = dict()
    for x in range(0,len(m)):
        cutingKey = cutKey(m[x])
        for y in range(1,17):
            row = ""
            col = ""
            expension = permutation(constantes['E'][0],cutingKey[1])
            cal = bin(int(expension, 2) ^ int(k[y], 2))[2:]
            while len(cal) < len(expension):
                cal = '0' + cal
            resCal = [(cal[i:i+6]) for i in range(0, len(cal), 6)]
            for i in range(len(resCal)):
                row = resCal[i][0] + resCal[i][-1]
                col = resCal[i][1:-1]
                resCal[i] = bin(int(constantes['S'][i][int(row,2)][int(col,2)]))[2:]
                while len(resCal[i]) < 4:
                    resCal[i] = '0' + resCal[i]
            strResCal = ''.join(resCal)
            permutStrResCal = permutation(constantes['PERM'][0], strResCal)
            tmp = cutingKey[1]
            value = bin(int(permutStrResCal, 2) ^ int(cutingKey[0],2))[2:]
            while len(value) < len(tmp):
                value = '0' + value
            cutingKey[1] = value
            cutingKey[0] = tmp
        concat = cutingKey[0] + cutingKey[1]
        inverse = permutation(constantes['PI_I'][0], concat)
        resTmp[x] = inverse
    res = ''.join(resTmp.values())
    return res

def decryptRonde(k,m,constantes):
    res = ''
    resTmp = dict()
    resCal = []
    EDK = dict()
    for x in range(0,len(m)):
        cutingKey = cutKey(m[x])
        for y in range(16,0,-1):
            row = ""
            col = ""
            expension = permutation(constantes['E'][0],cutingKey[0])
            cal = bin(int(expension, 2) ^ int(k[y], 2))[2:]
            while len(cal) < len(expension):
                cal = '0' + cal
            resCal = [(cal[i:i+6]) for i in range(0, len(cal), 6)]
            for i in range(len(resCal)):
                row = resCal[i][0] + resCal[i][-1]
                col = resCal[i][1:-1]
                resCal[i] = bin(int(constantes['S'][i][int(row,2)][int(col,2)]))[2:]
                while len(resCal[i]) < 4:
                    resCal[i] = '0' + resCal[i]
            strResCal = ''.join(resCal)
            permutStrResCal = permutation(constantes['PERM'][0], strResCal)
            tmp = cutingKey[0]
            value = bin(int(permutStrResCal, 2) ^ int(cutingKey[1],2))[2:]
            while len(value) < len(tmp):
                value = '0' + value
            cutingKey[0] = value
            cutingKey[1] = tmp
        concat = cutingKey[0] + cutingKey[1]
        inverse = permutation(constantes['PI_I'][0], concat)
        resTmp[x] = inverse
    res = ''.join(resTmp.values())
    return res


    # res = ''
    # resTmp = dict()
    # for x in range(1,len(m)):
    #     cutingKey = cutBinText(m[x])
    #     # print(cutingKey)
    #     for y in range(16,0,-1):
    #         # print(f'transformation: {y}, cutingKey: {cutingKey}')
    #         row = ""
    #         col = ""
    #         expension = permutation(constantes['E'][0],cutingKey[0])
    #         cal = bin(int(expension, 2) ^ int(k[y], 2))[2:]
    #         while len(cal) < len(expension):
    #             cal = '0' + cal
    #         # print(f'Cal: {cal}')
    #         resCal = [(cal[i:i+6]) for i in range(0, len(cal), 6)]
    #         # print(f'resCal: {resCal}')
    #         for i in range(len(resCal)):
    #             row = resCal[i][0] + resCal[i][-1]
    #             col = resCal[i][1:-1]
    #             resCal[i] = bin(int(constantes['S'][i][int(row,2)][int(col,2)]))[2:]
    #             while len(resCal[i]) < 4:
    #                 resCal[i] = '0' + resCal[i]
    #         strResCal = ''.join(resCal)
    #         # print(f'strResCal: {strResCal}')
    #         permutStrResCal = permutation(constantes['PERM'][0], strResCal)
    #         # print(f'permutStrResCal: {permutStrResCal}')
    #         tmp = cutingKey[0]
    #         value = bin(int(permutStrResCal, 2) ^ int(cutingKey[1],2))[2:]
    #         while len(value) < len(tmp):
    #             value = '0' + value
    #         cutingKey[0] = value
    #         cutingKey[1] = tmp
    #
    #     concat = cutingKey[0] + cutingKey[1]
    #     resTmp[x] = permutation(constantes['PI_I'][0], concat)
    #
    # res = ''.join(resTmp.values())
    # return res
