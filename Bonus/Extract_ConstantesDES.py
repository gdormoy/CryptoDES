#Récupère un tableau associatif avec les constantes du chiffrement DES
def recupConstantesDES() :
	f=open("ConstantesDES.txt", "r")
	txt=f.read()
	f.close()

	sdl='\n'

	X=dict()

	#Permutation initiale
	clef="PI"
	X[clef]=MatZero(1, 64)
	deb=txt.find(clef+' =')
	fin=txt.find('FIN '+clef)
	col=0
	while(txt[deb]!=sdl and deb<fin) : deb+=1
	deb+=1
	while(deb<fin) :
		X[clef][0][col]=0
		while(ord('0')<=ord(txt[deb])<=ord('9') and deb<fin) :
			X[clef][0][col]=10*X[clef][0][col]+int(txt[deb])
			deb+=1
		X[clef][0][col]-=1#Car les entiers sont entre 1 et 64
		while(not(ord('0')<=ord(txt[deb])<=ord('9')) and deb<fin) : deb+=1

		col+=1

	#Permutation initiale inverse
	clef="PI_I"
	X[clef]=MatZero(1, 64)
	deb=txt.find(clef+' =')
	fin=txt.find('FIN '+clef)
	col=0
	while(txt[deb]!=sdl and deb<fin) : deb+=1
	deb+=1
	while(deb<fin) :
		X[clef][0][col]=0
		while(ord('0')<=ord(txt[deb])<=ord('9') and deb<fin) :
			X[clef][0][col]=10*X[clef][0][col]+int(txt[deb])
			deb+=1
		X[clef][0][col]-=1#Car les entiers sont entre 1 et 64
		while(not(ord('0')<=ord(txt[deb])<=ord('9')) and deb<fin) : deb+=1

		col+=1

	#Fonction d'expantion
	clef="E"
	X[clef]=MatZero(1, 48)
	deb=txt.find(clef+' =')
	fin=txt.find('FIN '+clef)
	col=0
	while(txt[deb]!=sdl and deb<fin) : deb+=1
	deb+=1
	while(deb<fin) :
		X[clef][0][col]=0
		while(ord('0')<=ord(txt[deb])<=ord('9') and deb<fin) :
			X[clef][0][col]=10*X[clef][0][col]+int(txt[deb])
			deb+=1
		X[clef][0][col]-=1#Car les entiers sont entre 1 et 48
		while(not(ord('0')<=ord(txt[deb])<=ord('9')) and deb<fin) : deb+=1

		col+=1

	#Permutation
	clef="PERM"
	X[clef]=MatZero(1, 32)
	deb=txt.find(clef+' =')
	fin=txt.find('FIN '+clef)
	col=0
	while(txt[deb]!=sdl and deb<fin) : deb+=1
	deb+=1
	while(deb<fin) :
		X[clef][0][col]=0
		while(ord('0')<=ord(txt[deb])<=ord('9') and deb<fin) :
			X[clef][0][col]=10*X[clef][0][col]+int(txt[deb])
			deb+=1
		X[clef][0][col]-=1#Car les entiers sont entre 1 et 32
		while(not(ord('0')<=ord(txt[deb])<=ord('9')) and deb<fin) : deb+=1

		col+=1

	#Première permutation des clefs
	clef="CP_1"
	X[clef]=MatZero(1, 56)
	deb=txt.find(clef+' =')
	fin=txt.find('FIN '+clef)
	col=0
	while(txt[deb]!=sdl and deb<fin) : deb+=1
	deb+=1
	while(deb<fin) :
		X[clef][0][col]=0
		while(ord('0')<=ord(txt[deb])<=ord('9') and deb<fin) :
			X[clef][0][col]=10*X[clef][0][col]+int(txt[deb])
			deb+=1
		X[clef][0][col]-=1#Car les entiers sont entre 1 et 56
		while(not(ord('0')<=ord(txt[deb])<=ord('9')) and deb<fin) : deb+=1

		col+=1


	#Seconde permutation des clefs
	clef="CP_2"
	X[clef]=MatZero(1, 48)
	deb=txt.find(clef+' =')
	fin=txt.find('FIN '+clef)
	col=0
	while(txt[deb]!=sdl and deb<fin) : deb+=1
	deb+=1
	while(deb<fin) :
		X[clef][0][col]=0
		while(ord('0')<=ord(txt[deb])<=ord('9') and deb<fin) :
			X[clef][0][col]=10*X[clef][0][col]+int(txt[deb])
			deb+=1
		X[clef][0][col]-=1#Car les entiers sont entre 1 et 48
		while(not(ord('0')<=ord(txt[deb])<=ord('9')) and deb<fin) : deb+=1

		col+=1

	#Les 8 fonctions de substitution (numéroté de 0 à 7)
	clef="S"
	X[clef]=dict()
	for i in range(0,8) :
		X[clef][i]=MatZero(4, 16)
		deb=txt.find(clef+str(i+1)+' =')
		fin=txt.find('FIN '+clef+str(i+1))
		col=0
		lig=0
		while(txt[deb]!=sdl and deb<fin) : deb+=1
		deb+=1
		while(deb<fin) :
			X[clef][i][lig][col]=0
			while(ord('0')<=ord(txt[deb])<=ord('9') and deb<fin) :
				X[clef][i][lig][col]=10*X[clef][i][lig][col]+int(txt[deb])
				deb+=1

			while(not(ord('0')<=ord(txt[deb])<=ord('9')) and deb<fin) :
				if(txt[deb]==sdl and col>=0) :
					lig+=1
					col=-1
				deb+=1

			col+=1

	return X

def MatZero(a,b):
	tab = [[0 for x in range(b)] for y in range(a)]
	return tab
