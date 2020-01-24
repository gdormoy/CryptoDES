import sys
from Extract_ConstantesDES import *
from ConvAlphaBin import *
from utils import *
from pprint import pprint

def encryption(key,txt, constantes):
    bintxt = conv_bin(txt)
    k = createKeys(key,constantes)
    if k == "error":
        res = "Votre clef est incorrecte"
        return {'binary': bintxt, 'text': res}

    m=cutBinText(bintxt)
    for x in range(0, len(m)):
        m[x] = permuteText(m[x],constantes)
    r = ronde(k,m,constantes)
    res = nib_vnoc(r)
    return {'binary': r, 'text': res}

def decryption(key,txt,constantes):
    res = ''
    bintxt = conv_bin(txt)
    k = createKeys(key,constantes)
    if k == "error":
        res = "Votre clef est incorrecte"
        return {'binary': bintxt, 'text': res}
        
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

    #Load constantes
    Constantes = recupConstantesDES()

    #Reading file
    txtFile = open(pathToText,"r")
    txt = txtFile.read()
    keyFile = open(pathToKey,"r")
    key = keyFile.read()

    # Check Command
    if command.upper() == "ENCRYPT":
        res = encryption(key,txt,Constantes)
    elif command.upper() == "DECRYPT":
        res = decryption(key,txt,Constantes)
    elif command.upper() == "ALL":
        res['encrypt'] = encryption(key,txt,Constantes)
        res['decrypt'] = decryption(key,res['encrypt']['text'],Constantes)
    else:
        print('You must bo choose between encrypt, decrypt or all function!')

    txtFile.close()
    keyFile.close()

    print(res['text'])
