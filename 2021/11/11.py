fichier=open('input.txt','r')
texte=fichier.read()
fichier.close()

t=[]
nombre=[]
for i in texte:
	if i!=' ' and i!='\n':
		nombre.append(int(i))
	if i=='\n':
		t.append(nombre)
		nombre=[]


def clignotement(t,i,j,DC):
	if t[i][j]>9 and (i,j) not in DC:
		DC.append((i,j))
		if i==0:
			if j==0:
				t[i][j+1]+=1
				clignotement(t,i,j+1,DC)
				t[i+1][j]+=1
				clignotement(t,i+1,j,DC)
				t[i+1][j+1]+=1
				clignotement(t,i+1,j+1,DC)

			elif j==9:
				t[i][j-1]+=1
				clignotement(t,i,j-1,DC)
				t[i+1][j-1]+=1
				clignotement(t,i+1,j-1,DC)
				t[i+1][j]+=1
				clignotement(t,i+1,j,DC)

			else:
				t[i][j-1]+=1
				clignotement(t,i,j-1,DC)
				t[i][j+1]+=1
				clignotement(t,i,j+1,DC)
				t[i+1][j-1]+=1
				clignotement(t,i+1,j-1,DC)
				t[i+1][j]+=1
				clignotement(t,i+1,j,DC)
				t[i+1][j+1]+=1
				clignotement(t,i+1,j+1,DC)

		elif i==9:
			if j==0:
				t[i-1][j]+=1
				clignotement(t,i-1,j,DC)
				t[i-1][j+1]+=1
				clignotement(t,i-1,j+1,DC)
				t[i][j+1]+=1
				clignotement(t,i,j+1,DC)

			elif j==9:
				t[i-1][j-1]+=1
				clignotement(t,i-1,j-1,DC)
				t[i-1][j]+=1
				clignotement(t,i-1,j,DC)
				t[i][j-1]+=1
				clignotement(t,i,j-1,DC)

			else:
				t[i-1][j-1]+=1
				clignotement(t,i-1,j-1,DC)
				t[i-1][j]+=1
				clignotement(t,i-1,j,DC)
				t[i-1][j+1]+=1
				clignotement(t,i-1,j+1,DC)
				t[i][j-1]+=1
				clignotement(t,i,j-1,DC)
				t[i][j+1]+=1
				clignotement(t,i,j+1,DC)

		else:
			if j==0:
				t[i-1][j]+=1
				clignotement(t,i-1,j,DC)
				t[i-1][j+1]+=1
				clignotement(t,i-1,j+1,DC)
				t[i][j+1]+=1
				clignotement(t,i,j+1,DC)
				t[i+1][j]+=1
				clignotement(t,i+1,j,DC)
				t[i+1][j+1]+=1
				clignotement(t,i+1,j+1,DC)

			elif j==9:
				t[i-1][j-1]+=1
				clignotement(t,i-1,j-1,DC)
				t[i-1][j]+=1
				clignotement(t,i-1,j,DC)
				t[i][j-1]+=1
				clignotement(t,i,j-1,DC)
				t[i+1][j-1]+=1
				clignotement(t,i+1,j-1,DC)
				t[i+1][j]+=1
				clignotement(t,i+1,j,DC)

			else:
				t[i-1][j-1]+=1
				clignotement(t,i-1,j-1,DC)
				t[i-1][j]+=1
				clignotement(t,i-1,j,DC)
				t[i-1][j+1]+=1
				clignotement(t,i-1,j+1,DC)
				t[i][j-1]+=1
				clignotement(t,i,j-1,DC)
				t[i][j+1]+=1
				clignotement(t,i,j+1,DC)
				t[i+1][j-1]+=1
				clignotement(t,i+1,j-1,DC)
				t[i+1][j]+=1
				clignotement(t,i+1,j,DC)
				t[i+1][j+1]+=1
				clignotement(t,i+1,j+1,DC)

flash=0
for tour in range(100):
	DC=[]

	for i in range(len(t)):
		for j in range(len(t[i])):
			t[i][j]+=1

	
	for i in range(len(t)):
		for j in range(len(t[i])):
			if t[i][j]>9:
				clignotement(t,i,j,DC)
	
	for i in range(len(t)):
		for j in range(len(t[i])):
			if t[i][j]>9:
				t[i][j]=0
				flash+=1

print(flash)

# Partie 2

L=[]
tour=0
while L==[]:

	DC=[]
	compteur=0

	for i in range(len(t)):
		for j in range(len(t[i])):
			t[i][j]+=1

	
	for i in range(len(t)):
		for j in range(len(t[i])):
			if t[i][j]>9:
				clignotement(t,i,j,DC)
	
	for i in range(len(t)):
		for j in range(len(t[i])):
			if t[i][j]>9:
				t[i][j]=0
				compteur+=1

	tour+=1

	if compteur==100:
		L.append(100+tour)		# car on a déjà fait 100 tour dans la partie 1
print(L[0])
