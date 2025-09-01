def solve(name):
    if name[-1] in "ia":
        return (name, "female")
        
    return (name, "male")    


ip=['sravani','sravan','kumar','kumari','lalitha','lalith','arjun','lakshmi','nandini']
op = tuple(solve(name) for name in ip)
print(op)
