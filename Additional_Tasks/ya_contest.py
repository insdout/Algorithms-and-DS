inp = []
for _ in range(4):
	inp.append(int(input()))
if inp[0] == inp[1] == 0:
	print("INF")
else:
	if inp[0] == 0:
		print("NO")
	else:
		sol = -inp[1]/inp[0]
		if (sol*10) % 10 != 0:
			print("NO")
		elif int(sol)* inp[2] +  inp[3] != 0:
			print(int(sol))
		else:
			print("NO")