def right_half_diamond(n):
    # Upper half (ascending)
    for i in range(1, n + 1):
        print("*" * i)
    
    # Lower half (descending)
    for i in range(n - 1, 0, -1):
        print("*" * i)
basic_half_diamond(5)        
