with open("input.txt") as f:
	texte = f.read().strip()

liste = [int(i) for i in texte.split(",")]

def part1(a,b):
	t = [i for i in liste]
	t[1] = a
	t[2] = b
	i = 0
	while t[i] != 99:
		if t[i] == 1:
			t[t[i+3]] = t[t[i+1]] + t[t[i+2]]
		elif t[i] == 2:
			t[t[i+3]] = t[t[i+1]] * t[t[i+2]]
		i += 4
	return t[0]

print("Partie 1 :",part1(12,2))

def part2():
	# a et b doivent être des indices valides de la liste
	for a in range(len(liste)):
		for b in range(len(liste)):
			if part1(a,b) == 19690720:
				return a*100+b

print("Partie 2 :",part2())