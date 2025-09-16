def left_half_diamond(n):
    # Upper half (ascending)
    for i in range(1, n + 1):
        spaces = " " * (n-i)
        stars = "*" * i
        print(spaces + stars)
        
     # Lower half (descending)
    for i in range(n - 1, 0, -1):
        spaces = " " * (n-i)
        stars = "*" * i
        print(spaces + stars)    
    
   
left_half_diamond(5)        
