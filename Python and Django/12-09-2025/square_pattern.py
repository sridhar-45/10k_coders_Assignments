#   1.WAP to print square pattern using nested loop.
# n = int(input())
n = 5
for i in range(n):
    for j in range(n):
        if  i == 0 or i == n-1 or j ==0 or j == n-1:
            print("*",end = " ")
        else:
            print(" ",end =" ")
    print()       
