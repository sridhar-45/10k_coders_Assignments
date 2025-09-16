# n_r = int(input())
# n_c = int(input())

no_rows = 5
no_cols = 10

for i in range(no_rows):
    for j in range(no_cols):
        if i == 0 or i == no_rows-1 or j == 0 or j == no_cols-1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
            
