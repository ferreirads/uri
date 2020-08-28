x = list(map(int, input().split()))

a = 1
b = 0

while x[a] <= 0:
    if x[a] <= 0:
        a = a + 1
    elif x[a] > 0:
        break

for i in range(0, x[a]):
    b = b + x[0] + i

print(b)
