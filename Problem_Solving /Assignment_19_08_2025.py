# Task:1
# I/p:-
# l1=[Sravan,harish,aravind,akhil]
# l2=[24,17,20,18]

# o/p:- sravan-24-Eligible
#       harish-17-not eligible
#       aravind-20-eligible
#       akhil-18-eligible

names = ["sravan", "harish", " aravind", "akhil"]
ages = [24, 17, 20, 18]

for name, age in zip(names, ages):
    if age >= 18:
        print(f"{name}-{age}-Elgible")
    else:
        print(f"{name}-{age}-not eligble")





# 2. sum of digits
# I/p:- n=123          n=120
# o/p:- 6   #1+2+3     3     #1+2+0

n = 120
res = 0
while n:
    res += n%10
    n //= 10
    
print(res)    




# 3. highest digit in an integer:-
# I/p:- n=123498
# o/p:- 9
n = 123498
max_digit = float("-inf")

while n:
    max_digit = max(max_digit, n%10)
    n //= 10

print(max_digit)    




# 4. choc_price=1/-
# 3 wrappers= 1 
# choc_amount=21     21+7+2+1==31
# how many chocs I can eat==?? 

chocolates = 21
wrappers = chocolates
res = chocolates

while wrappers >= 3:  
    new_choco = wrappers // 3   
    res += new_choco           
    wrappers = new_choco + (wrappers % 3)  

print(res)

        
