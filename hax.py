i = 1
print("i = 1")
print("while True:")
while True:
	print("\t", end = "")
	if i % 2 == 0:
		print(f"if i == {i}: \n\tprint('Parillinen')")
	elif i % 2 != 0:
		print(f"if i == {i}: \n\tprint('Pariton')")
	if i == 100000:
		break

