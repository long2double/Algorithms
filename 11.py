a = 1
b = set()
for i in range(2, 1025):
    a ^= i
    b.add(a)
print(b)