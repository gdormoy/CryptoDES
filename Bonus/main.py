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
    # print(newtxt)
    bintxt = conv_bin(newtxt)
    print(bintxt)
    # debintxt = nib_vnoc(bintxt)
    # print(debintxt)

    foo = cutBinText(bintxt)
    print("foo")
    for x in range(len(foo)):
        for y in range(len(foo[x])):
            print(foo[x][y], end = '')
        print()

    bar = aligneMat(foo)
    print()
    print(bar)
    print()
    print(nib_vnoc(bar))

    f=open("../Messages/Clef_de_1.txt", "r")
    key=f.read()
    f.close()
    key56bit = convert_64bit_to_56bit_key(key)
    print()
    print(key56bit)
    print("\nKey56bit:")

    for x in range(len(key56bit)):
        print(key56bit[x], end = "\t")
        if (x + 1) % 8 == 0:
            print()

    print("\nPI:")
    count = 1
    for value in range(len(Constantes['PI'][0])):
        print(Constantes['PI'][0][value], end = "\t")
        if (value + 1) % 8 == 0:
            print()

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(Constantes)
