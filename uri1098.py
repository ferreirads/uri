v = 0
for i in range(11):
    for j in range(3):
        k = (j + 1) + (0.2 * i)
        if(i == 0) or (i == 5) or (i == 10):
            print("I=%d J=%d"%(v + 0.2, k))
        else:
            print("I=%.1f J=%.1f"%(v, k))
    v = v + 0.2
