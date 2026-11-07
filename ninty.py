n =5
num = 1
for i in range(1
               n+1):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()
    
n = 5
for i in range(n):
    ch = 65
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()
    
n = 5
for i in range(1, n+1):
    for j in range(1,i+1):
        print((i + j) %2, end=" ")
    print()