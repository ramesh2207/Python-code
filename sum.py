n=int(input("enter the value of n : "))
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(j,n-1):
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()
