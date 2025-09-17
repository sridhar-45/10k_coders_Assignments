for i in range(1, n+1):
    s = " " * (n-i)
    if i == 1:
        print(s + "* ")
    else:
        print(s + "* " + "  "*(i-2) + "*")

for i in range(n, 0, -1):
    s =" " * (n-i)
    if i == 1:
        print(s + "* ")
    else:
        print(s + "* " + "  "*(i-2) + "*")
    
