i = 1
print("i = 1")
print("while True:")
while True:
	print("\t", end = "")
	if i % 2 == 0:
		print(f"if i == {i}: \n\t\tprint('Even/Parillinen')")
		i += 1
	elif i % 2 != 0:
		print(f"if i == {i}: \n\t\tprint('Odd/Pariton')")
		i += 1
	if i == 100000:
		break

