fichier=open('input.txt','r')
texte=fichier.read()
fichier.close()

instruction="""fold along x=655
fold along y=447
fold along x=327
fold along y=223
fold along x=163
fold along y=111
fold along x=81
fold along y=55
fold along x=40
fold along y=27
fold along y=13
fold along y=6
"""

alphabet="abcdefghijklmnopqrstuvwxyz"
instructions=[]
ligne=[]
temp=''
for i in instruction:
    if i=='\n':
        ligne.append(int(temp))
        temp=''
        instructions.append(ligne)
        ligne=[]
    if i=='x' or i=='y':
        ligne.append(i)
    if i not in alphabet and i!=' ' and i!='=':
        temp+=i
    


t=[]
ligne=[]
valeur=''
for i in texte:
    if i=='\n':
        ligne.append(int(valeur))
        valeur=''
        t.append(ligne)
        ligne=[]
    elif i==',':
        ligne.append(int(valeur))
        valeur=''
    else:
        valeur+=i

dim_x=655*2
dim_y=447*2


grille=[]
for y in range(dim_y+1):
    grille.append([])
    for x in range(dim_x+1):
        grille[y].append('.')

for ligne in t:
    grille[ligne[1]][ligne[0]]='#'

def coupe_x(grille,X):
    g1=[]
    g2=[]

    for y in range(len(grille)):
        g1.append([])
        g2.append([])
        for x in range(X):
            g1[y].append('.')
            g2[y].append('.')

    for y in range(len(g1)):
        for x in range(X):
            g1[y][x]=grille[y][x]
            g2[y][x]=grille[y][x+X+1]

    for y in range(len(g2)):
        g2[y]=g2[y][::-1]

    return g1,g2

def coupe_y(grille,Y):
    return (grille[:Y],grille[:Y:-1])


def fusion(g1,g2):
    g=[]
    for y in range(len(g1)):
        g.append([])
        for x in range(len(g1[y])):
            if g1[y][x]=='#' or g2[y][x]=='#':
                g[y].append('#')
            else:
                g[y].append('.')
    return g

def count(g):
    count=0
    for i in g:
        for j in i:
            if j=='#':
                count+=1

    return count


g1,g2=coupe_x(grille,655)
print("Partie 1 : "+str(count(fusion(g1,g2))))


# Partie 2

for instruction in instructions:
    if instruction[0]=='x':
        g1,g2=coupe_x(grille,instruction[1])
        grille=fusion(g1,g2)
    if instruction[0]=='y':
        g1,g2=coupe_y(grille,instruction[1])
        grille=fusion(g1,g2)

for i in grille:
    for j in i:
        print(j,end='')
    print()
