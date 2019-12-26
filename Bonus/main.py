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
    print(nib_vnoc(encryption))
    return encryption

def decryption(key,txt):
    print("DECRYPTION")
    return None

if __name__ == "__main__":
    command = sys.argv[1]
    text = sys.argv[2]
    key = sys.argv[3]

    Constantes = recupConstantesDES()
    f=open(text, "r")
    txt=f.read()
    f.close()
    newtxt = FiltreTXT(txt)

    f=open(key, "r")
    key=f.read()
    f.close()

    if command.upper() == "ENCRYPT":
        encryption(key,newtxt)
    elif command.upper() == "DECRYPT":
        decryption(key,txt)
