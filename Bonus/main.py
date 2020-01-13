import sys
from Extract_ConstantesDES import *
from ConvAlphaBin import *
from utils import *
from pprint import pprint

def encryption(key,txt, constantes):
    newtxt = FiltreTXT(txt)
    bintxt = conv_bin(newtxt)
    k = createKeys(key,constantes)
    m = permuteText(bintxt,constantes)
    r = ronde(k,m,constantes)
    res = nib_vnoc(r)
    return {'binary': r, 'text': res}

def decryption(key,txt,constantes):
    decrypt = ''
    res = ''
    bintxt = conv_bin(txt)
    # bintxt = '1000100000110110101000010001001111001011011000001001010010010000'
    k = createKeys(key,constantes)
    m = permuteText(bintxt,constantes)
    r = decryptRonde(k,m,constantes)

    res = nib_vnoc(r)
    return {'binary': r, 'text': res}



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
        res = encryption(key,txt,Constantes)
    elif command.upper() == "DECRYPT":
        res = decryption(key,txt,Constantes)
    else:
        print('You must bo choose between encrypt or decrypt function!')

    print(res['text'])
