import sys
from Extract_ConstantesDES import *
from ConvAlphaBin import *
from utils import *
from pprint import pprint

def encryption(key,txt):
    newtxt = FiltreTXT(txt)
    bintxt = conv_bin(newtxt)
    k = createKeys(key,Constantes)
    m = permuteText(bintxt,Constantes)
    r = ronde(k,m,Constantes)
    res = nib_vnoc(r)
    print(r)
    return {'binary': encryption, 'text': res}

def decryption(key,txt):
    print("DECRYPTION")
    decrypt = ''
    res = ''
    bintxt = conv_bin(txt)
    # bintxt = '1000100000110110101000010001001111001011011000001001010010010000'
    k = createKeys(key,Constantes)
    m = permuteText(bintxt,Constantes)
    r = decryptRonde(k,m,Constantes)

    res = nib_vnoc(r)
    return {'binary': decrypt, 'text': res}



if __name__ == "__main__":
    command = sys.argv[1]
    pathToText = sys.argv[2]
    pathToKey = sys.argv[3]
    res = dict()

    Constantes = recupConstantesDES()
    with open(pathToText, 'r',encoding='utf-8', errors='ignore') as file:
        txt = file.read()
    txt = txt.rstrip("\r\n")
    txt = txt.rstrip("\n")
    txt = txt.rstrip()

    with open(pathToKey, 'r') as file:
        key = file.read()
    key = key.rstrip("\r\n")
    key = key.rstrip("\n")
    key = key.rstrip()

    if command.upper() == "ENCRYPT":
        res = encryption(key,txt)
    elif command.upper() == "DECRYPT":
        res = decryption(key,txt)

    print(res['text'])
