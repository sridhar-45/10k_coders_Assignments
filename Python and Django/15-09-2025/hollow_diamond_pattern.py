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
    



##### hallow butterfly...
n = 5
print("* " + " " * 2 * (n-1) + "*")
for i in range(n, 0, -1):
    s =" " * (n-i)
    if i == 1:
        print("*" + s + "*"+ s + "*")
    else:
        print("*" + s + "* " + "  "*(i-2) + "*" + s + "*")
        
for i in range(2, n+1):
    s = " " * (n-i)
    # if i == 1:
    #     print(s + "* ")
    # else:
    print("*" + s + "* " + "  "*(i-2) + "*"+ s + "*")
print("* " + " "* 2*(n-1) + "*")


    
