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
    # cp1 = Constantes['CP_1'][0]
    # PI = Constantes['PI'][0]
    test = "0101111001011011010100100111111101010001000110101011110010010001"
    k = createKeys(test,Constantes)
    pprint(k)

    bintxt = conv_bin(newtxt)

    cuttedBinTxt = cutBinText(bintxt)
