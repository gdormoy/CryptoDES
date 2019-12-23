from Extract_ConstantesDES import *
from ConvAlphaBin import *
from utils import *
import pprint

if __name__ == "__main__":
    Constantes = recupConstantesDES()
    f=open("../Messages/test.txt", "r")
    txt=f.read()
    f.close()
    newtxt = FiltreTXT(txt)

    f=open("../Messages/Clef_de_1.txt", "r")
    key=f.read()
    f.close()
    key56bit = convert_64bit_to_56bit_key(key)
    cp1 = Constantes['CP_1'][0]
    PI = Constantes['PI'][0]
    print(cp1)
    test = "0101111001011011010100100111111101010001000110101011110010010001"

    keyPermutation0 = permutation(cp1,test)
    print(f'Key:\n{test}')
    print(f'KeyPermutation:\n{keyPermutation0}')
    cutingKey = cutKey(keyPermutation0)
    print(cutingKey)
    cutingKey[0] = leftShift(cutingKey[0])
    print(cutingKey)
    bintxt = conv_bin(newtxt)

    cuttedBinTxt = cutBinText(bintxt)
