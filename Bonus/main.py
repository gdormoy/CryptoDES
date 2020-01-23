import sys
from Extract_ConstantesDES import *
from ConvAlphaBin import *
from utils import *
from pprint import pprint

def encryption(key,txt, constantes):
    #binaire = "1101110010111011110001001101010111100110111101111100001000110010100111010010101101101011111000110011101011011111"
    bintxt = conv_bin(txt)
    k = createKeys(key,constantes)
    m=cutBinText(bintxt)
    for x in range(0, len(m)):
        m[x] = permuteText(m[x],constantes)
    #print(f'm: {m}')
    r = ronde(k,m,constantes)
    res = nib_vnoc(r)
    return {'binary': r, 'text': res}

def decryption(key,txt,constantes):
    res = ''
    bintxt = conv_bin(txt)
    k = createKeys(key,constantes)
    m=cutBinText(bintxt)
    for x in range(0, len(m)):
        m[x] = permuteText(m[x],constantes)
    r = decryptRonde(k,m,constantes)
    res = nib_vnoc(r)
    return {'binary': r, 'text': res}



if __name__ == "__main__":
    command = sys.argv[1]
    pathToText = sys.argv[2]
    pathToKey = sys.argv[3]
    res = dict()

    Constantes = recupConstantesDES()
    # with open(pathToText, 'r',encoding='utf-8', errors='ignore') as file:
    #     txt = file.read()
    txtFile = open(pathToText,"r")
    txt = txtFile.read()


    # with open(pathToKey, 'r') as file:
    #     key = file.read()
    keyFile = open(pathToKey,"r")
    key = keyFile.read()

    if command.upper() == "ENCRYPT":
        res = encryption(key,txt,Constantes)
    elif command.upper() == "DECRYPT":
        res = decryption(key,txt,Constantes)
    elif command.upper() == "ALL":
        res['encrypt'] = encryption(key,txt,Constantes)
        res['decrypt'] = decryption(key,res['encrypt']['text'],Constantes)
    else:
        print('You must bo choose between encrypt, decrypt or all function!')

    print(res['text'])
