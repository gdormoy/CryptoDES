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
    k = dict()
    # k[0] = convert_64bit_to_56bit_key(key)

    # cp1 = Constantes['CP_1'][0]
    # PI = Constantes['PI'][0]
    test = "0101111001011011010100100111111101010001000110101011110010010001"
    k[0] = convert_64bit_to_56bit_key(test)

    keyPermutation0 = permutation(Constantes['CP_1'][0],test)
    cutingKey = cutKey(keyPermutation0)
    cutingKey[0] = leftShift(cutingKey[0])
    cutingKey[1] = leftShift(cutingKey[1])
    concatKey = concatenate(cutingKey[0],cutingKey[1])
    k[1] = permutation(Constantes['CP_2'][0], concatKey)
    print(k)

    bintxt = conv_bin(newtxt)

    cuttedBinTxt = cutBinText(bintxt)
