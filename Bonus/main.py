import sys
from Extract_ConstantesDES import *
from ConvAlphaBin import *
from utils import *
from pprint import pprint

def encryption(key,txt):
    bintxt = conv_bin(txt)
    k = createKeys(key,Constantes)
    m = permuteText(bintxt,Constantes)
    r = ronde(k,m,Constantes)
    # encryption = ''.join(r.values())
    res = nib_vnoc(r)
    print(r)
    return {'binary': encryption, 'text': res}

def decryption(key,txt):
    print("DECRYPTION")
    decrypt = ''
    res = ''
    # bintxt = conv_bin(txt)
    bintxt = '1000100000110110101000010001001111001011011000001001010010010000'
    # print(txt)
    # print(bintxt)
    k = createKeys(key,Constantes)
    r = decryptRonde(k,bintxt,Constantes)
    # m = permuteText(bintxt,Constantes)
    decrypt = ''.join(r.values())
    res = nib_vnoc(decrypt)
    print(decrypt)
    print(res)
    return {'binary': decrypt, 'text': res}



if __name__ == "__main__":
    command = sys.argv[1]
    pathToText = sys.argv[2]
    pathToKey = sys.argv[3]
    res = dict()

    Constantes = recupConstantesDES()
    with open(pathToText, 'r') as file:
        txt = file.read()
    txt = txt.rstrip()
    newtxt = FiltreTXT(txt)

    with open(pathToKey, 'r') as file:
        key = file.read()
    key = key.rstrip('\n')

    if command.upper() == "ENCRYPT":
        res = encryption(key,newtxt)
    elif command.upper() == "DECRYPT":
        res = decryption(key,txt)

    print(res['text'])
