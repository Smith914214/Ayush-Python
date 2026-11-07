n = 6
for i in range(n):
    for j in range(2*n-1):
        if((i==0 and (j % (n-1) != 0)) or (i==1 and (j % (n-1) == 0)) or (i-j == n//2) or (i+j == (2*n-2) +n//2)):
           print("*", end=" ")
        else:
            print(" ", end=" ")
    print()