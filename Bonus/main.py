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
    print(cp1)
    test = "01011110101101010100101111110101000000110110111101001000"

    keyPermutation0 = permutation(cp1,test)
    print(f'Key:\n{test}')
    print(f'KeyPermutation:\n{keyPermutation0}')
    # print()
    # print(key56bit)

    # for x in range(len(key56bit)):
    #     print(key56bit[x], end = "\t")
    #     if (x + 1) % 8 == 0:
    #         print()

    bintxt = conv_bin(newtxt)

    cuttedBinTxt = cutBinText(bintxt)
    # print(f'cuttedBinTxt 0\n{cuttedBinTxt[0]}')

    # for x in range(len(cuttedBinTxt)):
    #     for y in range(len(cuttedBinTxt[x])):
    #         print(cuttedBinTxt[x][y], end = '\t')
    #     print()
    # print()

    PI = Constantes['PI'][0]

    # print(f'PI\n{PI}')
    p0 = []
    # for x in range(len(cuttedBinTxt)):
    #     p0.append(permutation(PI,cuttedBinTxt[x]))
    #
    # for x in range(len(p0)):
    #     print(f'p0 {x}\n{p0[x]}')

    # for x in range(len(PI)):
    #     print(PI[x], end = '\t')
    # print()


    # print("\nPI:")
    # count = 1
    # for value in range(len(Constantes['PI'][0])):
    #     print(Constantes['PI'][0][value], end = "\t")
    #     if (value + 1) % 8 == 0:
    #         print()

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(Constantes)
