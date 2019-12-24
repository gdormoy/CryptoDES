from Extract_ConstantesDES import *
from ConvAlphaBin import *
from utils import *
from pprint import pprint

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
    m = dict()
    # cp1 = Constantes['CP_1'][0]
    # PI = Constantes['PI'][0]
    test = "0101111001011011010100100111111101010001000110101011110010010001"
    testbintxt= '1101110010111011110001001101010111100110111101111100001000110010100111010010101101101011111000110011101011011111'
    k = createKeys(test,Constantes)
    bintxt = conv_bin(newtxt)
    cuttedBinTxt = cutBinText(testbintxt)
    pprint(cuttedBinTxt)

    for x in range(len(cuttedBinTxt)):
        m[x] = permutation(Constantes['PI'][0], cuttedBinTxt[x])

    pprint(m)

    cuttingKey = cutKey(m[0])
    print(cuttingKey)
    # cuttingKey[0] = leftShift(cutingKey[0])
    # cuttingKey[1] = leftShift(cutingKey[1])
