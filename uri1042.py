v1, v2, v3 = input().split()
v1 = int(v1)
v2 = int(v2)
v3 = int(v3)

if v1 < v2 < v3:
    print(v1)
    print(v2)
    print(v3)
    print()

elif v3 < v2 < v1:
    print(v3)
    print(v2)
    print(v1)
    print()

elif v1 < v3 < v2:
    print(v1)
    print(v3)
    print(v2)
    print()

elif v2 < v3 < v1:
    print(v2)
    print(v3)
    print(v1)
    print()

elif v2 < v1 < v3:
    print(v2)
    print(v1)
    print(v3)
    print()

elif v3 < v1 < v2:
    print(v3)
    print(v1)
    print(v2)
    print()

print(v1)
print(v2)
print(v3)
