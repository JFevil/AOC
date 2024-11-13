with open("input.txt") as f:
	texte = f.read().strip()

def algo(s):
	i = 0
	openBrackets = 0
	res1 = res2 = 0
	garbage = False
	while i < len(s):
		if not garbage:
			if s[i] == '{':
				openBrackets += 1
			elif s[i] == '}':
				res1 += openBrackets
				openBrackets -= 1
			elif s[i] == '<':
				garbage = True
			elif s[i] == '!':
				i += 1
		else:
			if s[i] == '!':
				i += 1
			elif s[i] == '>':
				garbage = False
			else:
				res2 += 1
		i += 1
	return res1, res2

res1, res2 = algo(texte)

print(f"Partie 1 :", res1)
print(f"Partie 2 :", res2)