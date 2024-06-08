def affichage(carte):
	for i in carte:
		for j in i:
			print(j, end="")
		print()

def est_accessible(carte, l1, c1, l2, c2):
	if carte[l2][c2] != ".":
		return 0
	Q = [(l1,c1,0)]
	cache = set()
	while Q:
		l, c, cost = Q.pop()
		if (l,c) == (l2,c2):
			return cost
		cache.add((l,c))
		for nl, nc in [(l-1,c), (l+1,c), (l,c-1), (l,c+1)]:
			if (nl,nc) not in cache and carte[nl][nc] == ".":
				Q.append((nl,nc,cost+1))
	return 0

def chambre_accesible(carte, l, c):
	colonneChambre = {'A':3, 'B':5, 'C':7, 'D':9}
	espece = carte[l][c]
	c2 = colonneChambre[espece]
	for i in range(len(carte)-2, 1, -1):
		if carte[i][c2] == '.':
			return i, c2, est_accessible(carte, l, c, i, c2)
		if carte[i][c2] != espece:
			return i, c2, 0
	return i, c2, 0

def en_position(carte, l, c):
	espece = carte[l][c]
	colonneChambre = {'A':3, 'B':5, 'C':7, 'D':9}
	if espece not in colonneChambre:
		return False
	if c != colonneChambre[espece]:
		return False
	for i in range(l+1, len(carte)-1):
		if carte[i][c] != espece:
			return False
	return True

def fini(carte):
	for i in range(len(carte)):
		for j in range(len(carte[i])):
			if carte[i][j] in "ABCD" and not en_position(carte, i, j):
				return False
	return True

def algo(carte, chambre_accesible):
	position = set()
	for l in range(len(carte)):
		for c in range(len(carte[l])):
			if carte[l][c] in "ABCD" and not en_position(carte, l, c):
				position.add((l,c))
	Q = [(carte, position, 0)]
	cout = {'A':1, 'B':10, 'C':100, 'D':1000}
	cache = dict()
	res = -1
	while Q:
		carte, position, energy = Q.pop()
		temp = tuple(map(tuple, carte))
		if temp in cache and energy >= cache[temp]:
			continue
		if fini(carte):
			res = energy if res == -1 else min(res, energy)
			continue
		cache[temp] = energy
		for (l,c) in position:
			if en_position(carte, l, c):
				continue
			d,e,f = chambre_accesible(carte, l, c)
			if f == 0:
				if l in range(2, len(carte)-1):
					for nl, nc in ((1, 1), (1, 2), (1, 4), (1, 6), (1, 8), (1, 10), (1, 11)):
						x = est_accessible(carte, l, c, nl, nc)
						if x != 0:
							new_energy = energy + cout[carte[l][c]]*x
							new_carte = [[j for j in i] for i in carte]
							new_carte[l][c], new_carte[nl][nc] = new_carte[nl][nc], new_carte[l][c]
							new_position = position - {(l,c)} | {(nl,nc)}
							Q.append((new_carte, new_position, new_energy))
			else:
				new_energy = energy + cout[carte[l][c]]*f
				new_carte = [[j for j in i] for i in carte]
				new_carte[l][c], new_carte[d][e] = new_carte[d][e], new_carte[l][c]
				new_position = position - {(l,c)}
				Q.append((new_carte, new_position, new_energy))
	return res

def cartes():
	with open("input.txt") as f:
		texte = f.read().strip()

	# texte = """#############
	# #...........#
	# ###B#C#B#D###
	#   #A#D#C#A#
	#   #########"""

	carte1 = [[i for i in ligne] for ligne in texte.splitlines()]
	carte1[-2] += 2*[' ']
	carte1[-1] += 2*[' ']

	rajout1 = "  #D#C#B#A#"
	rajout2 = "  #D#B#A#C#"
	carte2 = [[i for i in ligne] for ligne in texte.splitlines()]
	carte2.insert(3, [i for i in rajout1])
	carte2.insert(4, [i for i in rajout2])
	carte2[-4] += 2*[' ']
	carte2[-3] += 2*[' ']
	carte2[-2] += 2*[' ']
	carte2[-1] += 2*[' ']

	return carte1, carte2

carte1, carte2 = cartes()
print("Partie 1 :",algo(carte1, chambre_accesible))
print("Partie 2 :",algo(carte2, chambre_accesible))