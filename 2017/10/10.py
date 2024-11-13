with open("input.txt") as f:
	texte = f.read().strip()

def reverse(liste, i, length):
	for k in range(length//2):
		a = (i+k)%256
		b = (i+length-k-1)%256
		liste[a], liste[b] = liste[b], liste[a]

def algo(lengths):
	liste = list(range(256))
	i = 0
	skip = 0
	for length in lengths:
		# print(f"{liste} {i=} {skip=} {length=}")
		reverse(liste, i, length)
		i = (i + length + skip)%256
		skip += 1
	return liste[0]*liste[1]

lengths = list(map(int, texte.split(',')))
print("Partie 1 :", algo(lengths))

def algo2(s):
	lengths = []
	for i in s:
		lengths.append(ord(i))
	lengths += [17, 31, 73, 47, 23]
	liste = list(range(256))
	i = 0
	skip = 0
	for _ in range(64):
		for length in lengths:
			reverse(liste, i, length)
			i = (i + length + skip)%256
			skip += 1
	res = ""
	for i in range(16):
		temp = 0
		for j in range(16):
			temp ^= liste[16*i+j]
		temp = str(hex(temp))[2:]
		res += ('0' if len(temp) < 2 else '') + temp
	return res

print("Partie 2 :", algo2(texte))