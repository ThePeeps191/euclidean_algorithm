a, b = int(input("Enter number 1: ")), int(input("Enter number 2: "))
r = a % b
i = 0
while r != 0:
	a = b
	b = r
	i = a // b
	r = a - i * b
print(b)
