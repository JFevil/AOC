from itertools import product

def nombre(temp):
	if temp[0]=='-':
		return -nombre(temp[1:])
	if temp.isdigit():
		return int(temp)
	return temp

with open('input.txt','r') as f:
	texte=f.read()
	
data = []
for ligne in texte.splitlines():
	state, temp = ligne.split(" ")
	x_temp, y_temp, z_temp = temp.split(",")
	x0, x1 = map(int, x_temp[2:].split(".."))
	y0, y1 = map(int, y_temp[2:].split(".."))
	z0, z1 = map(int, z_temp[2:].split(".."))
	data.append((state=="on", x0, x1, y0, y1, z0, z1))

d=dict()
for cuboid in data:
	if abs(cuboid[1]) <= 50:
		x=[i for i in range(cuboid[1],cuboid[2]+1)]
		y=[i for i in range(cuboid[3],cuboid[4]+1)]
		z=[i for i in range(cuboid[5],cuboid[6]+1)]
		if cuboid[0]:
			for i in product(x,y,z):
				d[i]=1
		else:
			for i in product(x,y,z):
				d[i]=0
				
res=0
for i in d:
	if d[i]==1:
		res+=1

print("Partie 1 :",res)

def intersection(a, b):
	x0 = max(a[1], b[1])
	x1 = min(a[2], b[2])
	y0 = max(a[3], b[3])
	y1 = min(a[4], b[4])
	z0 = max(a[5], b[5])
	z1 = min(a[6], b[6])
	if x0 <= x1 and y0 <= y1 and z0 <= z1:
		return (x0, x1, y0, y1, z0, z1)

def volume(cuboid):
	state, x0, x1, y0, y1, z0, z1 = cuboid
	signe = 1 if state else -1
	return signe * (x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1)

cuboids = []
for new in data:
	update = []
	for cuboid in cuboids:
		inter = intersection(cuboid, new)
		if inter:
			update.append((not cuboid[0],) + inter)

	if new[0]:
		update.append(new)

	cuboids.extend(update)

res = 0
for i in cuboids:
	res += volume(i)

print("Partie 2 :",res)