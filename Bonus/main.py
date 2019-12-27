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
    encryption = ''.join(r.values())
    res = nib_vnoc(encryption)
    return {'binary': encryption, 'text': res}

def decryption(key,txt):
    print("DECRYPTION")
    decrypt = ''
    res = ''
    return {'binary': decrypt, 'text': res}

if __name__ == "__main__":
    command = sys.argv[1]
    pathToText = sys.argv[2]
    pathToKey = sys.argv[3]
    res = dict()

    Constantes = recupConstantesDES()
    f=open(pathToText, "r")
    txt=f.read()
    f.close()
    newtxt = FiltreTXT(txt)

    f=open(pathToKey, "r")
    key=f.read()
    f.close()

    if command.upper() == "ENCRYPT":
        res = encryption(key,newtxt)
    elif command.upper() == "DECRYPT":
        res = decryption(key,txt)

    print(res['text'])
