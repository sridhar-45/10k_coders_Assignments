def rotate_matrix(mat):
    n = len(mat)
    m = len(mat[0])
    res = [[0]*m for _ in range(n)]
    for c in range(m):
        for r in range(n):
            res[r][c] = mat[c][r]
    
    return res

# n = int(input("enter number :"))    
# arr = []
# for _ in range(n):
#     arr = list(map(int, input().split()))
n = 4
arr = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
print("before matrix rotate :")
for i in range(n):
    for j in range(n):
        print(arr[i][j] , end = " ")
    print()   
    
print()    
ans = rotate_matrix(arr)
print("after rotated array :")
for i in range(n):
    for j in range(n):
        print(ans[i][j] , end = " ")
    print()    
    
            
            
